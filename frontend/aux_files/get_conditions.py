import os 
import json
import yaml
import shutil
import subprocess
from typing import Optional

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QFileDialog, QMessageBox
from backend.config.yaml_manager import YamlManager


class GetCondition:
    """
    Manages simulation conditions and their interaction with the GUI.
    """ 

    def _check_values(self, value) -> Optional[str]:
        """
        Validates if a value is a valid float string.

        Args:
            value (str): Value to check.

        Returns:
            Optional[str]: Same value if valid, otherwise None.
        """
        try:
            float(value)
            return value
        except:
            return None


    def change_combobox_info(self) -> None:
        """
        Updates GUI fields based on the selected condition from the combobox.
        """
        data = YamlManager.load_yaml(self, self.yaml_project_info)
        conditions = data.get("3. Conditions", {})

        selected = self.ui.comboBox_condition.currentText()
        props = conditions.get(selected, {}).get("Cutting Properties", {})
        exp = conditions.get(selected, {}).get("Experimental Datas", {})

        self.ui.lineEdit_velocity.setText(props.get("velocity", ""))
        self.ui.lineEdit_deepCuth.setText(props.get("deepCuth", ""))
        self.ui.lineEdit_rakeAngle.setText(props.get("rakeAngle", ""))
        self.ui.lineEdit_tempPath.setText(props.get("tempPath", ""))
        self.ui.label_input.setText(props.get("inputFile", ""))
        self.ui.lineEdit_cutting_force.setText(exp.get("cutting_force", ""))
        self.ui.lineEdit_normal_force.setText(exp.get("normal_force", ""))
        self.ui.lineEdit_CCR.setText(exp.get("chip_compression", ""))
        self.ui.lineEdit_CSR.setText(exp.get("chip_segmentation", ""))


    def get_input_path(self) -> None:
        """
        Opens a file dialog for the user to select an input file.
        """
        input_file, _ = QFileDialog.getOpenFileName(self)
        self.ui.label_input.setText(input_file)


    def get_user_conditions(self, call: Optional[str] = None) -> None:
        """
        Captures user-entered simulation data from GUI and stores it in YAML.

        Args:
            call (str, optional): If "new", adds a new condition to the combo box.
        """
        velocity = GetCondition._check_values(self, self.ui.lineEdit_velocity.text().replace(',', '.'))
        deep_cuth = GetCondition._check_values(self, self.ui.lineEdit_deepCuth.text().replace(',', '.'))
        rake_angle = GetCondition._check_values(self, self.ui.lineEdit_rakeAngle.text().replace(',', '.').replace('+', ''))
        temp_path = self.ui.lineEdit_tempPath.text() if self.ui.lineEdit_tempPath.text() else "None"
        inputFile = self.ui.label_input.text() if self.ui.label_input.text() else "None"

        cutting_force = GetCondition._check_values(self, self.ui.lineEdit_cutting_force.text().replace(',', '.'))
        normal_force = GetCondition._check_values(self, self.ui.lineEdit_normal_force.text().replace(',', '.'))
        chip_compression = GetCondition._check_values(self, self.ui.lineEdit_CCR.text().replace(',', '.'))
        chip_segmentation = GetCondition._check_values(self, self.ui.lineEdit_CSR.text().replace(',', '.'))

        if all([velocity, deep_cuth, rake_angle, inputFile]): 
            data = YamlManager.load_yaml(self, self.yaml_project_info)

            if "3. Conditions" not in data:
                data["3. Conditions"] = {}
            condition = self.ui.comboBox_condition.currentText()

            data["3. Conditions"][condition] = {
                "Cutting Properties": {
                    "name": f"cond{condition[-2:]}",
                    "velocity": velocity, 
                    "deepCuth": deep_cuth, 
                    "rakeAngle": rake_angle, 
                    "tempPath": temp_path, 
                    "inputFile": inputFile
                }, 
                "Experimental Datas": {
                    "cutting_force": cutting_force, 
                    "normal_force": normal_force, 
                    "chip_compression": chip_compression, 
                    "chip_segmentation": chip_segmentation
                }}
            
            YamlManager.save_yaml_info(self, self.yaml_project_info, "3. Conditions", data["3. Conditions"])
            
            if call == "new":
                new_condition = f"Condition 0{self.ui.comboBox_condition.count() + 1}"
                self.ui.comboBox_condition.addItem(new_condition)
                self.ui.comboBox_condition.setCurrentIndex(self.ui.comboBox_condition.findText(new_condition))
        else:
            self.error_tracking = True

    
    def manage_inp_files(self) -> bool:
        """
        Saves simulation conditions and determines if geometry will be imported or created.
        
        Returns:
            bool: True if geometry is imported, False otherwise.
        """
        data = YamlManager.load_yaml(self, self.yaml_project_info)
        conditions = data.get("3. Conditions", {})
        import_geometry = conditions.get("Import Geometry (.inp)") 

        if import_geometry is True:
            GetCondition._handle_imported_geometry(self, data)
        elif import_geometry is False:
            GetCondition._handle_created_geometry(self, conditions)
        else:
            print("[Warning] 'Import Geometry (.inp)' is not defined.")
            GetCondition.error_tracking = True
        return import_geometry
        

    def _handle_imported_geometry(self, data) -> None:
        """
        Handles logic for when geometry is imported (.inp files).
        Copies each condition's input file to the appropriate directory.
        """
        if os.path.exists(self.yaml_project_info) and not self.error_tracking:
            self.ui.pages.setCurrentIndex(7)

            for _, value in data.items():
                for key, condition_data in value.items():
                    if key.startswith("Condition"):
                        cond = condition_data["Cutting Properties"]["name"]
                        input_file_path = condition_data["Cutting Properties"]["inputFile"]

                        if os.path.exists(input_file_path):
                            new_input_file_path = os.path.join(self.inp_path, f"sim_{cond}.inp")
                            shutil.copy(input_file_path, new_input_file_path)
        else:
            QMessageBox.warning(self, "Error", "There are one or more conditions with invalid values.")

    def _handle_created_geometry(self, conditions) -> None:
        """
        Handles logic for when geometry is created from user-defined parameters.

        Args:
            conditions (dict): The full "3. Conditions" section from the YAML.
        """
        self.ui.pages.setCurrentIndex(7)

        for condition, data_types in conditions.items():
            if condition.startswith("Condition"):
                cutting_props = data_types.get("Cutting Properties")
                if cutting_props:
                    cond = cutting_props["name"]
                    rakeAngle = cutting_props["rakeAngle"]
                    deepCuth = cutting_props["deepCuth"]
                    velocity = cutting_props["velocity"]

                    with open(os.path.join(self.defaut_geometry, "geometry_datas.json"), "r") as file:
                        geo_data = json.load(file)

                    new_input_file_path = os.path.join(self.defaut_geometry, f"sim_{cond}.json")
                    geo_data["generalInformation"]["modelName"] = cond
                    geo_data["assemblyAndSimulationData"]["toolPosition"]["Deep of Cuth"] = deepCuth
                    geo_data["toolData"]["createPartInformation"]["rakeAngle"] = rakeAngle
                    geo_data["assemblyAndSimulationData"]["stepsAndHistoryInformation"]["velocity"] = velocity

                    with open(new_input_file_path, "w") as file:
                        json.dump(geo_data, file, indent=4)

            abaqus_command = r'C:\SIMULIA\Commands\abq2021.bat cae noGUI="backend/create_geometry/main.py"'            
            try:
                result = subprocess.run(abaqus_command, shell=True, check=True, capture_output=True, text=True)
                print('=== STDOUT ===\n', result.stdout, '\n=== STDERR ===\n', result.stderr)
            except subprocess.CalledProcessError as e:
                print("=== ERRO NA EXECUÇÃO DO ABAQUS ===")
                print("Código de retorno:", e.returncode)   
                print('\n=== STDOUT ===\n', e.stdout, '\n=== STDERR ===\n', e.stderr)


