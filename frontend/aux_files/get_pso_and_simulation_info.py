import os
import sys
import shutil
import psutil
from PySide6.QtCore import QTimer
from backend.config.yaml_manager import YamlManager
from PySide6.QtWidgets import QMessageBox

class GetPsoAndSimulation:
    """
    Handles the process of saving Particle Swarm Optimization (PSO) 
    and simulation configurations, as well as generating Python scripts 
    for distributed simulation execution.
    """
    def show_pso_and_results_info(self):
        data = YamlManager.load_yaml(self, self.yaml_project_info)
        if "09. PSO and Simulation" not in data and "05. Conditions" in data:
            self.ui.label_number_conditions.setText(str(len(data["05. Conditions"])))

            threshold = 8
            cpu_percentages = psutil.cpu_percent(percpu=True)
            num_physical_cores = psutil.cpu_count(logical=False)
            self.availableCores = sum(1 for i, usage in enumerate(cpu_percentages) if usage < threshold and i < num_physical_cores)
            self.ui.label_cores.setText(str(self.availableCores))
        self.ui.pages.setCurrentIndex(10)

    def save_info(self) -> None:
        """
        Coordinates the saving of user input from the UI into the YAML file
        and generates the corresponding Python simulation scripts.
        """
        GetPsoAndSimulation.generate_yaml_info(self)
        GetPsoAndSimulation.create_python_files(self)


    def generate_yaml_info(self) -> None:
        """
        Extracts PSO and simulation parameters from the UI, validates inputs,
        and saves them into the YAML configuration file.

        If any invalid input is detected, an error flag is set and a 
        warning label is shown in the UI.
        """
        data = YamlManager.load_yaml(self, self.yaml_project_info)
        data.setdefault("09. PSO and Simulation", {})

        core_by_simulation = self.ui.combobox_core_by_simulation.currentText()
        number_computer = self.ui.combobox_number_computer.currentText()
        main_computer = self.ui.combobox_main_computer.currentText()
        number_conditions = self.ui.label_number_conditions.text()

        try:
            self.error_tracking = False
            iterations = int(self.ui.lineEdit_number_iteration.text())
            particles = int(self.ui.lineEdit_number_particles.text())
            var1 = float(self.ui.lineEdit_var1.text())
            var2 = float(self.ui.lineEdit_var2.text())
            var3 = float(self.ui.lineEdit_var3.text())

            if iterations <= 0 or particles <= 0:
                self.error_tracking = True
            elif core_by_simulation == "None" or number_computer == "None" or main_computer == "None":
                self.error_tracking = True

        except:
            self.error_tracking = True

        if not self.error_tracking:
            data["09. PSO and Simulation"] = {
                "Cutting Conditions": number_conditions,
                "Iterations": iterations,
                "Particles": particles,
                "w": var2,
                "fig": var1,
                "fip": var3,
                "Cores by Simulation": core_by_simulation,
                "Computers": number_computer,
                "Main Computer": main_computer}

            YamlManager.save_yaml_info(self, self.yaml_project_info, "09. PSO and Simulation", data["09. PSO and Simulation"])
            self.ui.pages.setCurrentIndex(11)
        else:
            QMessageBox.warning(self, "Error", "There are one or more parameters with invalid values.")


    def create_python_files(self) -> None:
        """
        Generates and writes the required Python simulation files for each
        computer based on the YAML configuration. This includes dynamic code
        generation for simulation execution and parallel management.
        """
        if getattr(sys, 'frozen', False):  
            base_path = sys._MEIPASS
        else:
            base_path = os.getcwd() 
    
        pararel_simulation_source = os.path.join(base_path, "backend", "abaqus_simulation_manager", "aux_scripts", "parallel_simulation.py")
        status_manager_source = os.path.join(base_path, "backend", "abaqus_simulation_manager", "aux_scripts", "status_manager.py")

        if not self.error_tracking:
            data = YamlManager.load_yaml(self, self.yaml_project_info)

            defaut_file = os.path.join(base_path, "backend", "abaqus_simulation_manager", "aux_files", "aux_simulation", "code_to_run_simulation.py")
            computers = data["09. PSO and Simulation"]["Computers"]
            cores_by_simulation = data["09. PSO and Simulation"]["Cores by Simulation"]
            main_activated = data["09. PSO and Simulation"]["Main Computer"]
            project_name = data["01. Info"]["Project Name"]

            i = 1 if main_activated == "Yes" else  2
            
            with open(defaut_file, 'r') as file:
                template_simulation_code  = file.read()

            for computer in range(i, int(computers) + 1):
                computer_file = os.path.join(self.python_files, f"computer_0{computer}.py")
                
                modified_code  = (
                    template_simulation_code
                    .replace("XX", f"0{computer}")
                    .replace("X", f"{computer}")
                    .replace("cores_by_simulation", cores_by_simulation)
                    .replace("project_name", project_name)
                    .replace("path_to_list_yaml", self.yaml_computer_files)
                    .replace("path_to_odb_processing", self.odb_processing)
                    .replace("path_to_abq_bat", self.abaqus_path)
                )

                with open(computer_file, 'w') as file:
                    file.write(modified_code)

            with open(pararel_simulation_source, 'r') as file:
                conteudo = file.read()
            conteudo_modificado_parallel = conteudo.replace("from backend.abaqus_simulation_manager.aux_scripts.status_manager import StatusManager", "from status_manager import StatusManager")
            with open(os.path.join(self.python_files, "parallel_simulation.py"), 'w') as file:
                file.write(conteudo_modificado_parallel)

            shutil.copy(status_manager_source, os.path.join(self.python_files, "status_manager.py"))

