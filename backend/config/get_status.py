import os
import yaml
import psutil
import pandas as pd 
from backend.optimization.optimization_manager import OtimizationManager
from backend.config.yaml_manager import YamlManager
from frontend.aux_files.get_outputs_to_analyse import GetOutputs

class GetStatus():
    def verify_gui_stage(self):
        """
        Verify the current stage in the GUI and proceed accordingly (e.g., load optimization data or start optimization).
        """
        if not self.error_tracking and hasattr(self, 'yaml_computer_files') and os.path.isfile(self.yaml_computer_files):
            data = YamlManager.load_yaml(self, self.yaml_computer_files)

            for _, value in data.items():
                if isinstance(value, str) and (value.strip().startswith("True") or value.strip().startswith("Running")):
                    self.iteration_in_progress = True
        

        if not self.error_tracking and hasattr(self, 'yaml_project_info'):
            data = YamlManager.load_yaml(self, self.yaml_project_info)

            last_opt_data = data.get("12. Last Otimization Datas", None)
            it_datas = data.get("09. PSO and Simulation", None) 
            
            if last_opt_data:
                self.reload = True

                if last_opt_data.get("Remaining Iterations") == 0:
                    self.process_finished = True

                    ####################
                    
                    path = os.path.join(self.graph_folder, "forces_result.xlsx")
                    datas = pd.ExcelFile(path)
                    sheet_names = datas.sheet_names
                    [self.ui.combobox_file.addItems([f"sim_{name}"]) for name in sheet_names]
                    self.ui.combobox_file.setCurrentIndex(1)
                    GetOutputs.atualize_ui(self)
                    
                    self.ui.button_result_back.hide()
                    self.ui.pages.setCurrentIndex(12)
                    ####################

                elif last_opt_data.get("Remaining Iterations") == it_datas.get("Iterations"):
                    file_paths = [self.yaml_computer_files, self.yaml_materials_properties, self.yaml_parameters, os.path.join(self.excel_files, "datas.xlsx")]
                    for file in file_paths:
                        if os.path.exists(file):
                            os.remove(file)
                            print(f"File {file} removed.")

                    if "10. Current Optimization" in data:
                        del data["10. Current Optimization"]

                    with open(self.yaml_project_info, "w", encoding="utf-8") as f:
                        yaml.safe_dump(data, f, allow_unicode=True)

                    self.reload = False
                        
                elif last_opt_data.get("Remaining Iterations") >= 0:
                    for key, info in data["11. Best Otimization Datas"].items():
                        if info in (None, "", "null"):
                            self.reload = None

                    # Starting otimization from previous point
                    if self.reload:
                        OtimizationManager(self)
                        path = os.path.join(self.graph_folder, "forces_result.xlsx")
                        datas = pd.ExcelFile(path)
                        sheet_names = datas.sheet_names
                        [self.ui.combobox_file.addItems([f"sim_{name}"]) for name in sheet_names]
                        self.ui.combobox_file.setCurrentIndex(1)
                        GetOutputs.atualize_ui(self)
                        self.ui.pages.setCurrentIndex(11)
                        



    def load_info_to_ui(self):
        data_ui = YamlManager.load_yaml(self, self.yaml_project_info)
        output_data = data_ui.get("03. Outputs", None)
        cond_data = data_ui.get("05. Conditions", None)
        param_data = data_ui.get("07. Parameters to Iterate", None)
        param_limits_data = data_ui.get("08. Parameters Limits", None)
        pso_simulation_data = data_ui.get("09. PSO and Simulation", None)

        if output_data:
            GetStatus.set_output_analysis(self, output_data)

        if cond_data:
            GetStatus.set_condition_to_ui(self, cond_data)

        if param_data:
            GetStatus.set_param_to_ui(self, param_data, param_limits_data)
        
        if pso_simulation_data:
            GetStatus.set_pso_simulation_to_ui(self, pso_simulation_data)

        if hasattr(self, 'yaml_materials_properties'):
            if os.path.isfile(self.yaml_materials_properties):
                data_mat = YamlManager.load_yaml(self, self.yaml_materials_properties)
                GetStatus.set_material_values_to_ui(self, data_mat)


    def set_output_analysis(self, outputs_data):
        self.forces = outputs_data.get("Forces", False)
        self.temp = outputs_data.get("Temperature", False)
        self.chip = outputs_data.get("Chip", False)

        self.ui.forces.setChecked(self.forces)
        self.ui.temperature.setChecked(self.temp)
        self.ui.chip.setChecked(self.chip)

        weights_raw = outputs_data.get("Weights", ['0', '0', '0', '0', '0'])
        self.weights = []
        for w in weights_raw:
            self.weights.append(float(w))

        self.ui.wfc.setText(str(weights_raw[0]))
        self.ui.wfn.setText(str(weights_raw[1]))
        self.ui.wt.setText(str(weights_raw[2]))
        self.ui.wccr.setText(str(weights_raw[3]))
        self.ui.wcsr.setText(str(weights_raw[4]))


    def set_condition_to_ui(self, conditions):
        self.ui.comboBox_condition.clear()
        
        for condition_name in sorted(conditions.keys()):
            if condition_name[:4] == "Cond":
                self.ui.comboBox_condition.addItem(condition_name)

        self.ui.comboBox_condition.addItem("Condition 01") if self.ui.comboBox_condition.findText("Condition 01") == -1 else None
        self.ui.comboBox_condition.setCurrentIndex(self.ui.comboBox_condition.findText("Condition 01"))

        
    def set_param_to_ui(self, parameters, parameters_limits):
        self.ui.frame_105.show()

        for param, value in parameters.items():
            checkbox = getattr(self.ui, f"checkBox_param_{param}", None)
            frame = getattr(self.ui, f"frame_limits_param_{param}", None)
            min = getattr(self.ui, f"lineEdit_min_param_{param}", None)
            max = getattr(self.ui, f"lineEdit_max_param_{param}", None)

            frame.show()
            if checkbox and value:
                checkbox.setChecked(True)
            else:
                frame.hide()

            if parameters_limits:
                if param in parameters_limits:
                    min.setText(parameters_limits[param]["min"])
                    max.setText(parameters_limits[param]["max"])
            else:
                min.setText("")
                max.setText("")

    def set_pso_simulation_to_ui(self, pso_simulation_data):
        self.number_of_particles = int(pso_simulation_data["Particles"])
        self.ui.label_number_conditions.setText(pso_simulation_data["Cutting Conditions"])
        self.ui.lineEdit_number_iteration.setText(str(pso_simulation_data["Iterations"]))
        self.ui.lineEdit_number_particles.setText(str(pso_simulation_data["Particles"]))
        self.ui.lineEdit_var1.setText(str(pso_simulation_data["fig"]))
        self.ui.lineEdit_var2.setText(str(pso_simulation_data["w"]))
        self.ui.lineEdit_var3.setText(str(pso_simulation_data["fip"]))
        self.ui.combobox_core_by_simulation.setCurrentText(pso_simulation_data["Cores by Simulation"])
        self.ui.combobox_number_computer.setCurrentText(pso_simulation_data["Computers"])
        self.ui.combobox_main_computer.setCurrentText(pso_simulation_data["Main Computer"])

        # Calculando os cores disponiveis
        threshold = 8
        cpu_percentages = psutil.cpu_percent(percpu=True)
        num_physical_cores = psutil.cpu_count(logical=False)
        self.availableCores = sum(1 for i, usage in enumerate(cpu_percentages) if usage < threshold and i < num_physical_cores)
        self.ui.label_cores.setText(str(self.availableCores))
    

    def set_material_values_to_ui(self, data):
        """
        Displays the material properties on the user interface.

        This method shows the values for the material properties based on
        the selected material.
        """
        self.ui.frame_material_model.hide()
        self.ui.frame_damage_model.hide()

        # Display the values of material properties on the UI
        for material, info in data.items():
            self.ui.comboBox_material.addItem(material)
            self.ui.comboBox_material.setCurrentIndex(0)
            self.ui.comboBox_material_limits.addItem(material)
            self.ui.comboBox_material_limits.setCurrentIndex(0)

            for prop, values in info.items():
                if prop == "Plastic" and len(values) > 0:
                    self.ui.frame_material_model.show()
                    self.ui.label_param_A.setText("{:0.4g}".format(values["A"]))
                    self.ui.label_param_B.setText("{:0.4g}".format(values["B"]))
                    self.ui.label_param_n.setText("{:0.4g}".format(values["n"]))
                    self.ui.label_param_C1.setText("{:0.4g}".format(values["C1"]))
                    self.ui.label_param_C2.setText("{:0.4g}".format(values["C2"]))
                    self.ui.label_param_C3.setText("{:0.4g}".format(values["C3"]))
                    self.ui.label_param_e.setText("{:0.4g}".format(values["e"]))
                    self.ui.label_param_k.setText("{:0.4g}".format(values["k"]))
                    self.ui.label_param_Ts.setText("{:0.4g}".format(values["Ts"]))
                elif prop == "Damage Initiation" and len(values) > 0:
                    self.ui.frame_damage_model.show()
                    self.ui.label_param_D1.setText("{:0.4g}".format(values["D1"]))
                    self.ui.label_param_D2.setText("{:0.4g}".format(values["D2"]))
                    self.ui.label_param_D3.setText("{:0.4g}".format(values["D3"]))
                    self.ui.label_param_D4.setText("{:0.4g}".format(values["D4"]))
                    self.ui.label_param_D5.setText("{:0.4g}".format(values["D5"]))
                    self.ui.label_param_Tm.setText("{:0.4g}".format(values["Tm"]))
                    self.ui.label_param_Tt.setText("{:0.4g}".format(values["Tt"]))
                    self.ui.label_param_e_damage.setText("{:0.4g}".format(values["e"]))
                    self.ui.label_param_p.setText("{:0.4g}".format(values["p"]))
