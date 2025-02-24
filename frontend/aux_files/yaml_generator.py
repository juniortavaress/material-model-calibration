import os
import yaml
import shutil
from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QTimer
from datetime import datetime
from frontend.aux_files.aux_dict import *

class YamlClass:
    def create_login_credentials(self):
        self.software_path = os.path.join(os.getenv("SystemDrive", "C:") , "\MaterialOtimization")

        if os.path.exists(self.software_path) and self.ui.lineEdit_project_name.text():
            if f"{self.ui.lineEdit_project_name.text()}.yaml" in os.listdir(self.software_path):
                self.project_name = self.ui.lineEdit_project_name.text()
                self.project_infos_path = os.path.join(self.software_path, f"{self.project_name}.yaml")
                with open(self.project_infos_path, "r", encoding="utf-8") as file:
                    data = yaml.safe_load(file)

                if self.ui.lineEdit_password.text() == data["1. Info"]["Password"]:
                    if "Result_path" in data.get("1. Info", {}):
                        self.user_result_folder = data["1. Info"]["Result_path"]
                        self.ui.label_result.setText(self.user_result_folder)
                        self.ui.button_settings_next_page.setEnabled(True)
                        YamlClass.set_user_config_path(self, True)
                    self.ui.pages.setCurrentIndex(1)
                else:
                    self.ui.label_login_warning.show()
                    QTimer.singleShot(3000, lambda: self.ui.label_login_warning.hide())

            else:
                if self.ui.lineEdit_project_name.text() and self.ui.lineEdit_password.text():
                    self.project_name = self.ui.lineEdit_project_name.text()
                    self.project_infos_path = os.path.join(self.software_path, f"{self.project_name}.yaml")
                    data = {"Date": datetime.today().strftime('%d-%m-%Y'), "Password": self.ui.lineEdit_password.text()}
                    YamlClass.save_yaml_info(self, self.project_infos_path, "1. Info", data)
                    self.ui.pages.setCurrentIndex(1)


    def set_software_config_path(self, call=None):
        """
        Set the path for the software configuration file.

        If called with "start", it loads the existing configuration.
        Otherwise, it allows the user to select the Abaqus path.
        """
        self.software_config_path = os.path.join(os.getenv("SystemDrive", "C:") , "\MaterialOtimization", "config.yaml")

        if call == "start":
            if os.path.exists(self.software_config_path):
                with open(self.software_config_path, "r", encoding="utf-8") as file:
                    data_abq = yaml.safe_load(file)

                self.abaqus_path = data_abq["abaqus_path"]
                self.ui.label_abaqus.setText(self.abaqus_path)
                self.ui.button_result.setEnabled(True)

        else:
            self.abaqus_path, _ = QFileDialog.getOpenFileName(self)

            if self.abaqus_path:
                self.ui.label_abaqus.setText(self.abaqus_path)
                YamlClass.save_yaml_info(self, self.software_config_path, "abaqus_path", self.abaqus_path)
                self.ui.button_result.setEnabled(True)
            else:
                self.ui.label_abaqus.setText(" ")
                self.ui.label_path_warning.show()
                QTimer.singleShot(3000, lambda: self.ui.label_path_warning.hide())


    def set_user_config_path(self, call=None):
        """
        Set the user result folder path. If it does not exist, ask the user for a directory.
        Creates required subdirectories and saves paths in a YAML file.
        """
        if call != True or not hasattr(self, "user_result_folder"):
            self.result_path = QFileDialog.getExistingDirectory()

            if not self.result_path:
                self.ui.label_result.setText(" ")
                self.ui.label_path_warning.show()
                QTimer.singleShot(3000, lambda: self.ui.label_path_warning.hide())
                return
            
            self.user_result_folder = os.path.join(self.result_path, self.project_name)
            self.ui.label_result.setText(self.user_result_folder)

        if os.path.exists(self.user_result_folder):
            shutil.rmtree(self.user_result_folder)

        self.excel_files = os.path.join(self.user_result_folder, "excel_files")
        self.odb_files = os.path.join(self.user_result_folder, "obd_files")
        self.chip_images = os.path.join(self.user_result_folder, "chip_images")

        self.auxiliary_files = os.path.join(self.user_result_folder, "auxiliary_files")
        self.user_config = os.path.join(self.auxiliary_files, "config")
        self.python_files = os.path.join(self.auxiliary_files, "python_files_to_computers")
        self.simulation_inp_files = os.path.join(self.auxiliary_files, "simulation_inp_files")
        self.odb_processing = os.path.join(self.auxiliary_files, "odb_processing")
        self.cae_path = os.path.join(self.auxiliary_files, "defaut/CAE")
        self.inp_path = os.path.join(self.auxiliary_files, "defaut/INPFiles")
        self.json_defaut_path = os.path.join(self.auxiliary_files, "defaut/jsonFiles")
        self.obj_path = os.path.join(self.auxiliary_files, "defaut/objFiles")

        # Creating folders setup
        folders = [self.excel_files, self.odb_files, self.chip_images, self.user_config, self.python_files, self.simulation_inp_files, self.odb_processing, self.cae_path, self.inp_path, self.json_defaut_path, self.obj_path]
        for folder in folders:
            os.makedirs(folder)
        
        # Add path to project .yaml
        if self.project_infos_path:
            dict_with_folders = dict_folder_setup(self)
            YamlClass.save_yaml_info(self, self.project_infos_path, "2. Paths", dict_with_folders)

        # Allowing go to next page
        self.ui.button_settings_next_page.setEnabled(True)
        # Add result folder to the config.yaml
        if os.path.exists(self.project_infos_path):
            with open(self.project_infos_path, "r", encoding="utf-8") as file:
                existing_data = yaml.safe_load(file) or {}
            existing_data["1. Info"]["Result_path"] = self.user_result_folder
            with open(self.project_infos_path, "w", encoding="utf-8") as file:
                yaml.dump(existing_data, file, default_flow_style=False, allow_unicode=True, width=float("inf"))


    def save_yaml_info(self, yaml_path, condition, datas):
        """
        Save or update YAML files.
        """
        if os.path.exists(yaml_path):
            with open(yaml_path, "r", encoding="utf-8") as file:
                existing_data = yaml.safe_load(file) or {}
        else:
            existing_data = {}

        existing_data[condition] = datas
        
        os.makedirs(os.path.dirname(yaml_path), exist_ok=True)
        with open(yaml_path, "w", encoding="utf-8") as file:
            yaml.dump(existing_data, file, default_flow_style=False, allow_unicode=True, width=float("inf"))
