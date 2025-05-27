import os 
import yaml
import shutil
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QFileDialog
from frontend.aux_files.yaml_generator import YamlClass


class GetCondition:
    """
    Class that manages simulation conditions and interactions with
    the graphical user interface.
    """
        
    def set_conditions(self):
        """
        Sets simulation conditions from the project information file,
        populating the combobox with conditions.
        """

        with open(self.project_infos_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        self.ui.comboBox_condition.clear()
        for key, info in data.items():
            for condition, value in info.items():
                if condition[:9] == "Condition":
                    self.ui.comboBox_condition.addItem(condition)
                    GetCondition.change_combobox_info(self)

        if self.ui.comboBox_condition.findText("Condition 01") == -1:
            self.ui.comboBox_condition.addItem("Condition 01")
        self.ui.comboBox_condition.setCurrentIndex(self.ui.comboBox_condition.findText("Condition 01"))


    def get_input_path(self):
        """
        Opens a file dialog for the user to choose the input file path
        and updates the label in the graphical user interface.
        """
        inputFile, _ = QFileDialog.getOpenFileName(self)
        self.ui.label_input.setText(inputFile)


    def save_conditions(self):
        """
        Saves the current simulation conditions to the project information
        file and moves the input files to the appropriate location.
        """
        GetCondition.get_defaut_user_conditions(self)
        GetCondition.move_inp_files(self)


    def check_values(self, value):
        try:
            float(value)
            return value
        except:
            return None


    def get_defaut_user_conditions(self, call=None):
        """
        Gets the default user conditions from the graphical interface and
        saves them to the project information file.
        """
        self.error_tracking = False
        velocity = GetCondition.check_values(self, self.ui.lineEdit_velocity.text().replace(',', '.'))
        deep_cuth = GetCondition.check_values(self, self.ui.lineEdit_deepCuth.text().replace(',', '.'))
        rake_angle = GetCondition.check_values(self, self.ui.lineEdit_rakeAngle.text().replace(',', '.').replace('+', ''))
        temp_path = self.ui.lineEdit_tempPath.text() if self.ui.lineEdit_tempPath.text() else None
        inputFile = self.ui.label_input.text()

        cutting_force = GetCondition.check_values(self, self.ui.lineEdit_cutting_force.text().replace(',', '.'))
        normal_force = GetCondition.check_values(self, self.ui.lineEdit_normal_force.text().replace(',', '.'))
        chip_compression = GetCondition.check_values(self, self.ui.lineEdit_CCR.text().replace(',', '.'))
        chip_segmentation = GetCondition.check_values(self, self.ui.lineEdit_CSR.text().replace(',', '.'))

        if velocity and deep_cuth and rake_angle and inputFile:
            with open(self.project_infos_path, "r", encoding="utf-8") as file:
                data = yaml.safe_load(file) or {}

            if "3. Conditions" not in data:
                data["3. Conditions"] = {}

            condition = self.ui.comboBox_condition.currentText()

            # print(f"cond_{condition[-2:]}")
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
            
            YamlClass.save_yaml_info(self, self.project_infos_path, "3. Conditions", data["3. Conditions"])
            
            if call == "new":
                new_condition = f"Condition 0{self.ui.comboBox_condition.count() + 1}"
                self.ui.comboBox_condition.addItem(new_condition)
                self.ui.comboBox_condition.setCurrentIndex(self.ui.comboBox_condition.findText(new_condition))
        else:
            self.error_tracking = True


    def change_combobox_info(self):
        """
        Updates the values in the input fields based on the selected condition
        from the combobox.
        """

        if os.path.exists(self.project_infos_path):
            with open(self.project_infos_path, "r", encoding="utf-8") as file:
                data = yaml.safe_load(file) or {}

            if "3. Conditions" in data:
                if self.ui.comboBox_condition.currentText() in data["3. Conditions"]:
                    # Set values from the selected condition to the corresponding input fields
                    self.ui.lineEdit_velocity.setText(data["3. Conditions"][self.ui.comboBox_condition.currentText()]["Cutting Properties"]["velocity"])
                    self.ui.lineEdit_deepCuth.setText(data["3. Conditions"][self.ui.comboBox_condition.currentText()]["Cutting Properties"]["deepCuth"])
                    self.ui.lineEdit_rakeAngle.setText(data["3. Conditions"][self.ui.comboBox_condition.currentText()]["Cutting Properties"]["rakeAngle"])
                    self.ui.lineEdit_tempPath.setText(data["3. Conditions"][self.ui.comboBox_condition.currentText()]["Cutting Properties"]["tempPath"])
                    self.ui.label_input.setText(data["3. Conditions"][self.ui.comboBox_condition.currentText()]["Cutting Properties"]["inputFile"])
                    self.ui.lineEdit_cutting_force.setText(data["3. Conditions"][self.ui.comboBox_condition.currentText()]["Experimental Datas"]["cutting_force"])
                    self.ui.lineEdit_normal_force.setText(data["3. Conditions"][self.ui.comboBox_condition.currentText()]["Experimental Datas"]["normal_force"])
                    self.ui.lineEdit_CCR.setText(data["3. Conditions"][self.ui.comboBox_condition.currentText()]["Experimental Datas"]["chip_compression"])
                    self.ui.lineEdit_CSR.setText(data["3. Conditions"][self.ui.comboBox_condition.currentText()]["Experimental Datas"]["chip_segmentation"])
                else:
                    # Clear the fields if the selected condition does not exist
                    self.ui.lineEdit_velocity.setText("")
                    self.ui.lineEdit_deepCuth.setText("")
                    self.ui.lineEdit_rakeAngle.setText("")
                    self.ui.lineEdit_tempPath.setText("")
                    self.ui.label_input.setText("")
                    self.ui.lineEdit_cutting_force.setText("")
                    self.ui.lineEdit_normal_force.setText("")
                    self.ui.lineEdit_CCR.setText("")
                    self.ui.lineEdit_CSR.setText("")


    def move_inp_files(self):
        """ Moves the input files to the appropriate directory if no errors are found in the conditions. """
        if os.path.exists(self.project_infos_path) and not self.error_tracking:
            self.ui.pages.setCurrentIndex(4)
            GetCondition.move_files(self)
        else:
            self.ui.label_condition_warning.show()
            QTimer.singleShot(3000, lambda: self.ui.label_condition_warning.hide())


    def move_files(self):
        """ Moves the input files to the target directory, renaming them based on their conditions. """
        with open(self.project_infos_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file) or {}

        for info, value in data.items():
            for key, condition_data in value.items():
                if key[:9] == "Condition":
                    cond = condition_data["Cutting Properties"]["name"]
                    # v = condition_data["Cutting Properties"]["velocity"]
                    # h = condition_data["Cutting Properties"]["deepCuth"]
                    # gam = condition_data["Cutting Properties"]["rakeAngle"]
                    input_file_path = condition_data["Cutting Properties"]["inputFile"]

                    if os.path.exists(input_file_path):
                        new_input_file_path = os.path.join(self.inp_path, f"sim_{cond}.inp")
                        shutil.copy(input_file_path, new_input_file_path)


