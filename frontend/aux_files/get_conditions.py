import os 
import yaml
import shutil
from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QTimer
from frontend.aux_files.yaml_generator import YamlClass
from frontend.aux_files.aux_layout import SetLayout
from backend.inp_configuration import InpManager

class GetCondition:
    def set_conditions(self):
        with open(self.project_infos_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        for key, value in data.items():
            if key[:9] == "Condition":
                self.ui.comboBox_condition.addItem(key)
                GetCondition.change_combobox_info(self)

        if self.ui.comboBox_condition.findText("Condition 01") == -1:
            self.ui.comboBox_condition.addItem("Condition 01")
        self.ui.comboBox_condition.setCurrentIndex(self.ui.comboBox_condition.findText("Condition 01"))


    def get_input_path(self):
        inputFile, _ = QFileDialog.getOpenFileName(self)
        self.ui.label_input.setText(inputFile)


    def check_values(self, value):
        try:
            float(value)
            return value
        except:
            return None


    def get_defaut_user_conditions(self, call=None):
        velocity = GetCondition.check_values(self, self.ui.lineEdit_velocity.text().replace(',', '.'))
        deepCuth = GetCondition.check_values(self, self.ui.lineEdit_deepCuth.text().replace(',', '.'))
        rakeAngle = GetCondition.check_values(self, self.ui.lineEdit_rakeAngle.text().replace(',', '.').replace('+', ''))
        tempPath = self.ui.lineEdit_tempPath.text()
        inputFile = self.ui.label_input.text()

        if velocity and deepCuth and rakeAngle and tempPath and inputFile:
            condition = self.ui.comboBox_condition.currentText()
            data = {"velocity": velocity, "deepCuth": deepCuth, "rakeAngle": rakeAngle, "tempPath": tempPath, "inputFile": inputFile}
            YamlClass.save_yaml_info(self, self.project_infos_path, condition, data)
            
            if call == "new":
                new_condition = f"Condition 0{self.ui.comboBox_condition.count() + 1}"
                self.ui.comboBox_condition.addItem(new_condition)
                self.ui.comboBox_condition.setCurrentIndex(self.ui.comboBox_condition.findText(new_condition))
            

    def change_combobox_info(self):
        if os.path.exists(self.project_infos_path):
            with open(self.project_infos_path, "r", encoding="utf-8") as file:
                data = yaml.safe_load(file) or {}

            if self.ui.comboBox_condition.currentText() in data:
                self.ui.lineEdit_velocity.setText(data[self.ui.comboBox_condition.currentText()]["velocity"])
                self.ui.lineEdit_deepCuth.setText(data[self.ui.comboBox_condition.currentText()]["deepCuth"])
                self.ui.lineEdit_rakeAngle.setText(data[self.ui.comboBox_condition.currentText()]["rakeAngle"])
                self.ui.lineEdit_tempPath.setText(data[self.ui.comboBox_condition.currentText()]["tempPath"])
                self.ui.label_input.setText(data[self.ui.comboBox_condition.currentText()]["inputFile"])
            else:
                self.ui.lineEdit_velocity.setText("")
                self.ui.lineEdit_deepCuth.setText("")
                self.ui.lineEdit_rakeAngle.setText("")
                self.ui.lineEdit_tempPath.setText("")
                self.ui.label_input.setText("")


    def move_inp_files(self):
        if os.path.exists(self.project_infos_path):
            SetLayout.change_page(self, 4)
            QTimer.singleShot(0.005, lambda: GetCondition.move_files(self))



    def move_files(self):
        with open(self.project_infos_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file) or {}

        for key , condition_data in data.items():
            if key[:9] == "Condition":
                v = condition_data["velocity"]
                h = condition_data["deepCuth"]
                gam = condition_data["rakeAngle"]
                input_file_path = condition_data["inputFile"]

                if os.path.exists(input_file_path):
                    new_input_file_path = os.path.join(self.inp_path, f"sim_v{v}_h{h}_gam{gam}.inp")
                    shutil.copy(input_file_path, new_input_file_path)
        InpManager.get_available_parameters(self)
        InpManager.get_list_with_parameters_name(self)
