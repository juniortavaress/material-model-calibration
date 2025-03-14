# -*- coding: utf-8 -*-
import os 
import yaml
import shutil
import pandas as pd
from datetime import datetime

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QFileDialog

from backend.config.yaml_generator_backend import YamlClassBackEnd
from backend.pso.start_otimization import OtimizationManager


class SoftwareConfig():
    """
    Class to manage the configuration of the software, including setting up paths, loading configurations, 
    and saving data for project management.
    """
        
    def software_setup(self):
        """
        Set up the software by creating necessary folders and copying required files.
        """
        # Defining paths
        self.software_path = os.path.join(os.getenv("SystemDrive", "C:") , "\MaterialOtimization")
        source_results_dir = r"backend\aux_files\results"
        self.destination_results_dir = os.path.join(self.software_path, "extract_results")
        source_subrotine_dir = r"backend\aux_files\subrotine"
        destination_subrotine_dir = os.path.join(self.software_path, "compiled")
        folder_to_create = [self.software_path, self.destination_results_dir, destination_subrotine_dir]

        # Creating Server Folders
        for folder in folder_to_create:
            if not os.path.exists(folder):
                os.makedirs(folder)

        # Moving Auxiliar Results Python Files
        for file in os.listdir(source_results_dir):
            source_path = os.path.join(source_results_dir, file)
            destination_path = os.path.join(self.destination_results_dir, file)
            shutil.copy(source_path, destination_path)

        # Moving Subrotine files
        for file in os.listdir(source_subrotine_dir):
            source_path = os.path.join(source_subrotine_dir, file)
            destination_path = os.path.join(destination_subrotine_dir, file)
            shutil.copy(source_path, destination_path)
        
        # Loading Software Information
        SoftwareConfig.set_software_config_path(self, "start")


    def set_software_config_path(self, call=None):
        """
        Set the path for the software configuration file. If called with "start", it loads the existing configuration.
        Otherwise, it allows the user to select the Abaqus path.
        """
        self.software_config_path = os.path.join(os.getenv("SystemDrive", "C:") , "\MaterialOtimization", "config.yaml")

        if call == "start":
            if os.path.exists(self.software_config_path):
                with open(self.software_config_path, "r", encoding="utf-8") as file:
                    data_abq = yaml.safe_load(file)

                self.abaqus_path = data_abq["abaqus_path"]
                self.ui.label_abaqus.setText(self.abaqus_path)
        else:
            self.abaqus_path, _ = QFileDialog.getOpenFileName(self)

            if self.abaqus_path:
                self.ui.label_abaqus.setText(self.abaqus_path)
                YamlClassBackEnd.save_yaml_info(self, self.software_config_path, "abaqus_path", self.abaqus_path)
                self.ui.button_result.setEnabled(True)
            else:
                self.ui.label_abaqus.setText(" ")
                self.ui.label_path_warning.show()
                QTimer.singleShot(3000, lambda: self.ui.label_path_warning.hide())


    def verify_gui_stage(self):
        """
        Verify the current stage in the GUI and proceed accordingly (e.g., load optimization data or start optimization).
        """
        if not self.error_tracking and hasattr(self, 'project_infos_path'):
            load_datas = True

            with open(self.project_infos_path, "r", encoding="utf-8") as file:
                data = yaml.safe_load(file) or {}

            if "8. Otimization Datas" in data:
                # Loading results to show in the interface
                if data["8. Otimization Datas"]["Status"] == "Done":
                    path = os.path.join(self.graph_folder, "forces_result.xlsx")
                    datas = pd.ExcelFile(path)
                    sheet_names = datas.sheet_names
                    [self.ui.combobox_file.addItems([f"sim_{name}"]) for name in sheet_names]
                    self.ui.combobox_file.setCurrentIndex(1)
                    self.ui.button_result_back.hide()
                    self.ui.pages.setCurrentIndex(9)

                elif data["8. Otimization Datas"]["Status"] == "pending":
                    for _, info in data["8. Otimization Datas"]["Last Iteration Values"].items():
                        if info == None:
                            load_datas = None

                    # Starting otimization from previous point
                    if load_datas:
                        self.ui.pages.setCurrentIndex(8)
                        OtimizationManager.main(self)


    def project_setup(self):
        """
        Set up the project by creating necessary folders and checking login information.
        """
        if os.path.exists(self.software_path) and self.ui.lineEdit_project_name.text():
            self.project_name = self.ui.lineEdit_project_name.text()

            # Paths
            self.project_path = os.path.join(self.software_path, self.project_name)
            self.simulation_folder = os.path.join(self.project_path, "simulation_folder")
            self.graph_folder = os.path.join(self.project_path, "graph_results")
            folders_to_create = [self.project_path, self.simulation_folder, self.graph_folder]

            # Creating Server Folders
            for folder in folders_to_create:
                if not os.path.exists(folder):
                    os.makedirs(folder)

            # Checking login infos
            SoftwareConfig.check_credentials(self)
    

    def check_credentials(self):
        """
        Check if the credentials exist and if they are correct. If not, create new ones.
        """
        self.project_infos_path = os.path.join(self.project_path, "info.yaml")
        
        # If credentials alreary exist load them, else create the credentials
        if "info.yaml" in os.listdir(self.project_path):
            with open(self.project_infos_path, "r", encoding="utf-8") as file:
                project_data = yaml.safe_load(file)

            if self.ui.lineEdit_password.text() == project_data["1. Info"]["Password"]:
                SoftwareConfig.load_saved_datas(self, project_data)
                self.ui.pages.setCurrentIndex(1)
            else:
                self.ui.label_login_warning.show()
                QTimer.singleShot(3000, lambda: self.ui.label_login_warning.hide())
        else:
            if self.ui.lineEdit_project_name.text() and self.ui.lineEdit_password.text():
                SoftwareConfig.create_datas(self)


    def load_saved_datas(self, project_data):
        """
        Load saved data from the project file if it exists.
        """
        if "Result_path" in project_data.get("2. Result Path", {}):
            self.user_result_folder = project_data["2. Result Path"]["Result_path"]
            self.ui.label_result.setText(self.user_result_folder)
            self.ui.button_settings_next_page.setEnabled(True)
            SoftwareConfig.set_user_config_path(self)
    

    def create_datas(self):
        """
        Create a new project and save the initial data in a YAML file.
        """
        data = {"Date": datetime.today().strftime('%d-%m-%Y'), "Project Name": self.ui.lineEdit_project_name.text(), "Password": self.ui.lineEdit_password.text()}
        YamlClassBackEnd.save_yaml_info(self, self.project_infos_path, "1. Info", data)
        self.ui.pages.setCurrentIndex(1)


    def get_results_folders(self):
        """
        Open a file dialog to allow the user to select a results folder.
        """
        self.result_path = QFileDialog.getExistingDirectory()

        if not self.result_path:
            self.ui.label_result.setText(" ")
            self.ui.label_path_warning.show()
            QTimer.singleShot(3000, lambda: self.ui.label_path_warning.hide())
            return
        
        self.user_result_folder = os.path.join(self.result_path, self.project_name)
        self.ui.label_result.setText(self.user_result_folder)

        # Add result folder to the info.yaml
        if os.path.exists(self.project_infos_path):
            data = {"Result_path": self.user_result_folder}
            YamlClassBackEnd.save_yaml_info(self, self.project_infos_path, "2. Result Path", data)


    def set_user_config_path(self):
        """
        Set the user result folder path. If it does not exist, ask the user for a directory.
        Creates required subdirectories and saves paths in a YAML file.
        """
        if not os.path.exists(self.user_result_folder):
            os.makedirs(self.user_result_folder)

        self.excel_files = os.path.join(self.user_result_folder, "excel_files")
        self.chip_images = os.path.join(self.user_result_folder, "chip_images")
        self.simulation_inp_files = os.path.join(self.user_result_folder, "auxiliary_files/simulation_inp_files")
        self.odb_processing = os.path.join(self.user_result_folder, "auxiliary_files/odb_processing")
        self.python_files = os.path.join(self.user_result_folder, "auxiliary_files/python_files_to_computers")

        # Auxiliary Folders 
        self.user_config = os.path.join(self.project_path, "config")
        self.cae_path = os.path.join(self.project_path, "defaut/CAE")
        self.inp_path = os.path.join(self.project_path, "defaut/INPFiles")
        self.json_defaut_path = os.path.join(self.project_path, "json_and_obj_files/jsonFiles")
        self.obj_path = os.path.join(self.project_path, "json_and_obj_files/objFiles")

        if os.path.exists(self.project_infos_path):
            with open(self.project_infos_path, "r", encoding="utf-8") as file:
                existing_data = yaml.safe_load(file) or {}

        if "8. Otimization Datas" not in existing_data:
            # Creating folders setup
            folders = [self.excel_files, self.chip_images, self.simulation_inp_files, self.odb_processing, self.python_files, self.user_config, self.cae_path, self.inp_path, self.json_defaut_path, self.obj_path]
            for folder in folders:
                if os.path.exists(folder):
                    shutil.rmtree(folder)     
                os.makedirs(folder)

        # Allowing go to next page
        self.ui.button_settings_next_page.setEnabled(True)




