# -*- coding: utf-8 -*-
import os
import sys
import platform
from datetime import datetime
from collections import defaultdict
from PySide6.QtWidgets import QFileDialog, QMessageBox

from frontend.aux_files.output_configuration_manager import OutputConfigurationManager
from frontend.aux_files.simulation_configuration_manager import SimulationConfiguratorManager
from backend.optimization.aux_files.thread_manager import WorkerThread
from backend.optimization.optimization_manager import OtimizationManager
from backend.abaqus_simulation_manager.parallel_simulation import ParallelSimulation


class SoftwareConfig():
    """
    Manages the configuration and initialization of the software environment.


    This includes project creation/loading, Abaqus path setup, optimization management,
    and handling of auxiliary computer synchronization.
    """

    def software_setup(self) -> None:
        """
        Initialize the software environment.
        - Creates references to essential backend directories.
        - Identifies the current computer by its hostname.
        - Loads Abaqus executable path if already registered in the database.
        """        
        self.pc_id = platform.node()
        print("Computer:", self.pc_id)
        # self.pc_id = "4TH-PRE3660-111"

        response = self.supabase.table("abaqus_paths").select("*").eq("pc_id", self.pc_id).execute()
        if response.data and len(response.data) > 0:
            self.abaqus_path = response.data[0]['abaqus_path']
            self.ui.label_abaqus.setText(self.abaqus_path)
        else:
            self.abaqus_path = None


    def _register_computer(self):
        """
        Register or update the current computer in the `computers` table.
        Each (project_id, computer_id) pair must be unique. If the computer is already
        registered, its status and timestamp are updated. Otherwise, a new record is created.
        """
        now = datetime.utcnow().isoformat()
        existing = self.supabase.table("computers") \
            .select("id, computer_number") \
            .eq("project_id", self.project_id) \
            .eq("computer_id", self.pc_id) \
            .execute()

        if existing.data:
            self.computer_number = existing.data[0]["computer_number"]
            self.supabase.table("computers").update({
                "status": True,
                "last_update": now
            }).eq("id", existing.data[0]["id"]).execute()
        else:
            all_computers = self.supabase.table("computers") \
                .select("computer_number") \
                .eq("project_id", self.project_id) \
                .execute()
            used_numbers = [entry["computer_number"] for entry in all_computers.data if "computer_number" in entry]
            self.computer_number  = max(used_numbers, default=0) + 1

            self.supabase.table("computers").insert({
                "project_id": self.project_id,
                "computer_id": self.pc_id,
                "status": True,
                "last_update": now,
                "computer_number": self.computer_number
            }).execute()


    def project_setup(self) -> None:
        """
        Create or load a project from user input.
        - Validates the provided project name and password.
        - If project exists and credentials match: loads saved configuration.
        - If project does not exist: creates a new one.
        """
        self.project_name = self.ui.lineEdit_project_name.text()
        project_password = self.ui.lineEdit_password.text()

        if not self.project_name or not project_password:
            QMessageBox.warning(self, "Error", "Please enter project name and password.")
            return
    
        response = self.supabase.table("projects").select("*").eq("project_name", self.project_name).execute()
        if response.data and len(response.data) > 0:
            self.project = response.data[0]
            if project_password == self.project["password"]:
                self.project_id = self.project["id"]
                
                if self.project["id_main_computer"] == self.pc_id:
                    self.main_cp = True
                    QMessageBox.information(self, "Success", "Project loaded successfully!\nRunning as MAIN computer")
                    SoftwareConfig._register_computer(self)
                    SoftwareConfig._load_saved_datas(self, self.project)     
                else:
                    QMessageBox.information(self, "Success", "Project loaded successfully!\nRunning as Auxiliary computer")
                    SoftwareConfig._register_computer(self)
                    SoftwareConfig._load_information_aux_computers(self)
                    if self.abaqus_path:
                        SoftwareConfig.start_aux_optimization(self)
                    else:
                        self.ui.pages.setCurrentIndex(1)
            else:
                QMessageBox.warning(self, "Error", "Password is wrong.")
        else:
            insert_response = self.supabase.table("projects").insert({
                "project_name": self.project_name,
                "password": project_password,
                "id_main_computer": self.pc_id,
                "created_at": datetime.now().isoformat()
            }).execute()
            
            if insert_response.data:
                self.project_id = insert_response.data[0]["id"]
                QMessageBox.information(self, "Success", "Project created successfully!")
                self.ui.pages.setCurrentIndex(1)


    def _load_information_aux_computers(self):
        """
        Load project data for auxiliary computers.
        - Loads outputs and graphs.
        - Retrieves simulation configuration from database.
        - Starts worker thread for distributed simulation management.
        """
        SoftwareConfig._load_outputs(self, self.project)
        SoftwareConfig.set_user_config_path(self)

        response = self.supabase.table("project_simulation").select("*").eq("project_id", self.project["id"]).execute()
        if response.data and len(response.data) > 0:
            self.cores_by_simulation = response.data[0].get("cores_by_simulation", 4)

        current_opt_datas = self.supabase.table("current_optimization_data").select("*").eq("project_id", self.project["id"]).execute()
        if current_opt_datas.data and len(current_opt_datas.data) > 0:
            self.current_opt = current_opt_datas.data[0].get("iteration", 1)
            
        SoftwareConfig._load_graphs(self, self.project)
        
        
    def start_aux_optimization(self):
        try:
            self.ui.pages.setCurrentIndex(10)
            self.thread = WorkerThread(lambda: SoftwareConfig.manage_simulation(self), name="PsoThread")
            self.thread.start()
        except Exception as e:
            print("Erro")
       

    def manage_simulation(self) -> None:
        """
        Run all simulations for the current optimization.
        Initializes the `ParallelSimulation` instance with proper CPU allocation and
        executes all Abaqus simulations for the project.
        """
        try:
            cp_id = f"cp{str(self.computer_number).zfill(2)}"
            self.sim_thread = ParallelSimulation(self, self.cores_by_simulation, cp_id)
            self.sim_thread.run_all_simulations()
        except Exception as e:
            print(f"Simulation management error: {e}")


    def _load_outputs(self, project) -> None:
        response = self.supabase.table("project_outputs").select("*").eq("project_id", project["id"]).execute()
        if response.data and len(response.data) > 0:
            output_data = response.data[0]

            self.forces = output_data.get("forces", False)
            self.chip = output_data.get("chip", False)

            self.wfc = float(output_data.get("weight_fc", 0.5))
            self.wfn = float(output_data.get("weight_fn", 0.1))
            self.wccr = float(output_data.get("weight_ccr", 0.2))
            self.wcsr = float(output_data.get("weight_csr", 0.2))

            self.ui.forces.setChecked(self.forces)
            self.ui.chip.setChecked(self.chip)
            self.ui.wfc.setText(str(self.wfc))
            self.ui.wfn.setText(str(self.wfn))
            self.ui.wccr.setText(str(self.wccr))
            self.ui.wcsr.setText(str(self.wcsr))
            OutputConfigurationManager.update_ui_visibility(self)


    def _load_conditions(self, project) -> None:
        cond_response = self.supabase.table("conditions").select("*").eq("project_id", project["id"]).execute()
        if cond_response.data and len(cond_response.data) > 0:
            first_condition = cond_response.data[0]  
            self.ui.comboBox_condition.clear()

            for cond in cond_response.data:
                name_display = "Condition " + cond["name"].replace("cond", "")
                self.ui.comboBox_condition.addItem(name_display)

            first_display_name = "Condition " + first_condition["name"].replace("cond", "")
            self.ui.comboBox_condition.setCurrentText(first_display_name)
            self.ui.lineEdit_velocity.setText(str(first_condition.get("velocity") or ""))
            self.ui.lineEdit_deepCuth.setText(str(first_condition.get("deepcuth") or ""))
            self.ui.lineEdit_rakeAngle.setText(str(first_condition.get("rakeangle") or ""))
            self.ui.label_input.setText(first_condition.get("inputfile") or "")
            self.ui.lineEdit_cutting_force.setText(str(first_condition.get("cutting_force") or ""))
            self.ui.lineEdit_normal_force.setText(str(first_condition.get("normal_force") or ""))
            self.ui.lineEdit_CCR.setText(str(first_condition.get("chip_compression") or ""))
            self.ui.lineEdit_CSR.setText(str(first_condition.get("chip_segmentation") or ""))
            self.ui.pages.setCurrentIndex(6)


    def _load_parameters(self, project) -> None:
        param_response = self.supabase.table("parameters").select("*").eq("project_id", project["id"]).execute()
        if param_response.data:
            for param_entry in param_response.data:
                name = param_entry["name"]  
                iterate = param_entry.get("iterate", False)
                min_value = param_entry.get("min_value", "")
                max_value = param_entry.get("max_value", "")
                
                checkbox = getattr(self.ui, f"checkBox_param_{name}", None)
                if checkbox:
                    checkbox.setChecked(iterate)

                frame = getattr(self.ui, f"frame_limits_param_{name}", None)
                if frame:
                    frame.hide()
                    parent = frame.parentWidget().parentWidget()
                    if iterate:
                        frame.show()
                        if parent and not parent.isVisible():
                            parent.show()

                min_field = getattr(self.ui, f"lineEdit_min_param_{name}", None)
                max_field = getattr(self.ui, f"lineEdit_max_param_{name}", None)
                if min_field and max_field:
                    if min_value != "":
                        min_field.setText(str(min_value))
                    if max_value != "":
                        max_field.setText(str(max_value))
            SimulationConfiguratorManager.update_simulation_info(self)


    def _load_simulation(self, project) -> None:
        sim_response = self.supabase.table("project_simulation").select("*").eq("project_id", project["id"]).execute()
        if sim_response.data and len(sim_response.data) > 0:
            sim_data = sim_response.data[0]
            self.total_iterations = sim_data.get("total_iterations", 0)
            self.ui.combobox_core_by_simulation.setCurrentText(str(sim_data.get("cores_by_simulation", "None")))
            self.ui.combobox_main_computer.setCurrentText(str(sim_data.get("main_computer", "None")))
            self.ui.label_number_conditions.setText(str(sim_data.get("cutting_conditions", 0)))
            self.ui.lineEdit_number_iteration.setText(str(self.total_iterations))
            self.ui.lineEdit_number_particles.setText(str(sim_data.get("particles", 0)))
            self.ui.lineEdit_fig.setText(str(sim_data.get("fig", 0)))
            self.ui.lineEdit_w.setText(str(sim_data.get("w", 0)))
            self.ui.lineEdit_fip.setText(str(sim_data.get("fip", 0)))
            # self.ui.pages.setCurrentIndex(9)


    def _load_graphs(self, project):
        graph_datas = self.supabase.table("simulation_forces_results").select("*").eq("project_id", project["id"]).execute()
        if graph_datas.data and len(graph_datas.data) > 0:
            [self.ui.combobox_file.addItems([item["filename"]]) for item in graph_datas.data]
            self.ui.combobox_file.setCurrentIndex(1)

        iterations = defaultdict(list)
        completed_iteration = self.supabase.table("results").select("iteration_number, error").eq("project_id", self.project_id).execute()
        for row in completed_iteration.data:
            iter_number = row.get("iteration_number")
            error = row.get("error")
            iterations[iter_number].append(error)

        valid_iterations = len([i for i, errors in iterations.items() if all(e is not None for e in errors)])
        if valid_iterations >= 2:
            self.ui.combobox_analysis_type.insertItem(0, "Convergence Analysis")
            self.ui.combobox_analysis_type.setCurrentIndex(0)
            self.ui.combobox_file.setCurrentIndex(0)


    def _check_optimization_status(self, project) -> None:
        current_opt_datas = self.supabase.table("current_optimization_data").select("*").eq("project_id", project["id"]).execute()
        if current_opt_datas.data and len(current_opt_datas.data) > 0:
            self.current_opt = current_opt_datas.data[0]["iteration"]
            
            if self.current_opt == self.total_iterations:
                print('Optimization already finished.')
                self.process_finished = True
                self.ui.button_result_back.setEnabled(False)
                self.ui.pages.setCurrentIndex(10)

            elif self.current_opt < self.total_iterations and self.current_opt > 1:
                print('Reloading last optimization state...')
                self.reload = True

                optimization_status = self.supabase.table("results").select("*").eq("project_id", project["id"]).eq("iteration_number", self.current_opt).execute()
                if optimization_status.data and len(optimization_status.data) > 0:
                    opt_data = optimization_status.data

                    all_errors_filled = all(item.get("error") is not None for item in opt_data)
                    self.iteration_in_progress = False if all_errors_filled else True

                    if self.iteration_in_progress:
                        print('Continuing Otimization Manager')
                        OtimizationManager(self)
                        self.ui.pages.setCurrentIndex(10)
                    else:
                        self.current_opt += 1
                        print('Restarting Otimization Manager')
                        OtimizationManager(self)
                        self.ui.pages.setCurrentIndex(10)

            print('Current Opt:', self.current_opt)
            print('self.reload:', self.reload)


    def _load_saved_datas(self, project) -> None:
        """
        Loads previously saved data from the project configuration file and updates the UI accordingly.
        """
        self.ui.pages.setCurrentIndex(1)
        SoftwareConfig.set_user_config_path(self)

        SoftwareConfig._load_outputs(self, project)
        SoftwareConfig._load_conditions(self, project)
        SoftwareConfig._load_parameters(self, project)
        SoftwareConfig._load_simulation(self, project)
        
        SoftwareConfig._load_graphs(self, project)
        SoftwareConfig._check_optimization_status(self, project)
        # self.ui.pages.setCurrentIndex(1)
        


    def get_results_and_abaqus_folders(self, type: str, call) -> None:
        """
        Opens a dialog for the user to select the Abaqus executable or result directory.

        Args:
            type (str): Determines the type of dialog. Use "abq" for Abaqus path selection.
        """
        if type == "abq":
            self.abaqus_path, _ = QFileDialog.getOpenFileName(self)
            if self.abaqus_path:
                self.ui.label_abaqus.setText(self.abaqus_path)
                existing = self.supabase.table("abaqus_paths").select("*").eq("pc_id", self.pc_id).execute().data
                if existing:
                    print('existe')
                    self.supabase.table("abaqus_paths").update({
                    "abaqus_path": self.abaqus_path
                }).eq("pc_id", self.pc_id).execute()
                else:
                    self.supabase.table("abaqus_paths").upsert({
                    "pc_id": self.pc_id,
                    "abaqus_path": self.abaqus_path
                }).execute()
                # self.ui.button_result.setEnabled(True)
            else:
                self.ui.label_abaqus.setText(" ")
                QMessageBox.warning(self, "Error", "Select a valid path.")
            
        if type != "abq":
            if not self.ui.label_abaqus.text().strip():
                QMessageBox.warning(self, "Error", "Select a valid path.")
            else:
                SoftwareConfig.set_user_config_path(self)
                self.ui.pages.setCurrentIndex(2)
                


    def set_user_config_path(self) -> None:
        """
        Creates all necessary subfolders in the project directories.
        Also defines the paths used throughout the project and saves them if needed.
        """
        self.scripts_path = os.path.join(os.getcwd(), "backend", "abaqus_results_extractor", "extract_results_from_odb")   
        drive = os.getenv("SystemDrive", "C:")
        if not drive.endswith("\\") and not drive.endswith("/"):
            drive += "/"
        self.project_folder = os.path.join(drive, "MaterialOtimization", self.project_name)

        dirs = [self.project_folder]
        for dir in dirs:
            if not os.path.exists(dir):
                os.makedirs(dir)

        self.log_files = os.path.join(self.project_folder, "logs")
        self.chip_images = os.path.join(self.project_folder, "chip_images")
        self.simulation_folder = os.path.join(self.project_folder, "simulation_folder")
        self.obj_path = os.path.join(self.project_folder, "raw_datas", "objFiles")
        self.json_default_path = os.path.join(self.project_folder, "raw_datas", "jsonFiles")
        
        folders_result = [self.chip_images, self.simulation_folder, self.json_default_path, self.obj_path, self.log_files]
        for folder in folders_result:
            if not os.path.exists(folder):
                os.makedirs(folder)









