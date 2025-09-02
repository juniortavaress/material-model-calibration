# -*- coding: utf-8 -*-
import os 
import sys
from datetime import datetime
from PySide6.QtWidgets import QFileDialog, QMessageBox
from backend.config.get_status import GetStatus
from backend.config.yaml_manager import YamlManager

class SoftwareConfig():
    """
    Manages the configuration and initialization of the software environment,
    including folder structure setup, credential management, and project-specific data.
    """

    def software_setup(self) -> None:
        """
        Creates the root software directory and loads existing Abaqus configuration if available.
        """
        self.software_folder = os.path.join(os.getenv("SystemDrive", "C:") , "\MaterialOtimization")
        self.software_config_file = os.path.join(self.software_folder, "config", "config.yaml")
        
        if not os.path.exists(self.software_folder):
            os.makedirs(self.software_folder)

        base_path = getattr(sys, '_MEIPASS', os.getcwd())
        self.subrotine_dir = os.path.join(base_path, "backend", "abaqus_simulation_manager", "aux_files", "subrotine")

        if os.path.exists(self.software_config_file):
            data_abq = YamlManager.load_yaml(self, self.software_config_file)
            self.abaqus_path = data_abq["abaqus_path"]
            self.ui.label_abaqus.setText(self.abaqus_path)


    def project_setup(self) -> None:
        """
        Initializes the project by creating the project folder and validating user credentials.
        """
        self.showMaximized()

        if os.path.exists(self.software_folder) and self.ui.lineEdit_project_name.text():
            self.project_name = self.ui.lineEdit_project_name.text()
            self.project_folder = os.path.join(self.software_folder, self.project_name)
            self.yaml_project_info = os.path.join(self.project_folder, "info.yaml")
            
            if not os.path.exists(self.project_folder):
                os.makedirs(self.project_folder)
            SoftwareConfig.check_credentials(self)
        
        GetStatus.verify_gui_stage(self)

        
    def check_credentials(self) -> None:
        """
        Verifies if user credentials exist and are correct. 
        If not, creates new credentials and proceeds to the next interface page.
        """
        # If credentials alreary exist load them, else create the credentials
        if "info.yaml" in os.listdir(self.project_folder):
            project_data = YamlManager.load_yaml(self, self.yaml_project_info)

            if self.ui.lineEdit_password.text() == project_data["01. Info"]["Password"]:
                SoftwareConfig.load_saved_datas(self, project_data)
                GetStatus.load_info_to_ui(self)
                self.ui.pages.setCurrentIndex(1)
            else:
                QMessageBox.warning(self, "Error", "The project already exists and the password is wrong.")
        else:
            if self.ui.lineEdit_project_name.text() and self.ui.lineEdit_password.text():
                data = {"Date": datetime.today().strftime('%d-%m-%Y'), "Project Name": self.ui.lineEdit_project_name.text(), "Password": self.ui.lineEdit_password.text()}
                YamlManager.save_yaml_info(self, self.yaml_project_info, "01. Info", data)
                self.ui.pages.setCurrentIndex(1)


    def load_saved_datas(self, project_data: dict) -> None:
        """
        Loads previously saved data from the project configuration file.

        Args:
            project_data (dict): The dictionary loaded from the YAML configuration file.
        """
        if 'Result_path' in project_data.get("02. Result Path", {}):
            self.user_result_folder = project_data["02. Result Path"]["Result_path"]
            self.ui.label_result.setText(self.user_result_folder)
            self.ui.button_settings_next_page.setEnabled(True)
            SoftwareConfig.set_user_config_path(self)
            

    def get_results_and_abaqus_folders(self, type: str) -> None:
        """
        Opens a dialog for the user to select the Abaqus executable or result directory.

        Args:
            type (str): Determines the type of dialog. Use "abq" for Abaqus path selection.
        """

        if type == "abq":
            self.abaqus_path, _ = QFileDialog.getOpenFileName(self)

            if self.abaqus_path:
                self.ui.label_abaqus.setText(self.abaqus_path)
                YamlManager.save_yaml_info(self, self.software_config_file, "abaqus_path", self.abaqus_path)
                self.ui.button_result.setEnabled(True)
            else:
                self.ui.label_abaqus.setText(" ")
                QMessageBox.warning(self, "Error", "Select a valid path.")

        elif type == "result":
            result_path = QFileDialog.getExistingDirectory()
            if not result_path:
                self.ui.label_result.setText(" ")
                QMessageBox.warning(self, "Error", "Select a valid path.")
                return
            
            self.user_result_folder = os.path.join(result_path, self.project_name)
            self.ui.label_result.setText(self.user_result_folder)

            if os.path.exists(self.yaml_project_info):
                data = {"Result_path": self.user_result_folder}
                YamlManager.save_yaml_info(self, self.yaml_project_info, "02. Result Path", data)        
            SoftwareConfig.set_user_config_path(self)

        if type != "abq" and type != "result":
            if not self.ui.label_result.text().strip() or not self.ui.label_abaqus.text().strip():
                QMessageBox.warning(self, "Error", "Select a valid path.")
            else:
                self.ui.pages.setCurrentIndex(2)


    def set_user_config_path(self) -> None:
        """
        Creates all necessary subfolders in the project and result directories.
        Also defines the paths used throughout the project and saves them if needed.
        """
        if not os.path.exists(self.user_result_folder):
            os.makedirs(self.user_result_folder)

        # Paths in the code
        self.scripts_path = os.path.join(os.getcwd(), "backend", "abaqus_results_extractor", "extract_results_from_odb")   

        # Folders inside result folder
        self.excel_files = os.path.join(self.user_result_folder, "excel_files")
        self.chip_images = os.path.join(self.user_result_folder, "chip_images")
        self.odb_processing = os.path.join(self.user_result_folder, "auxiliary_files", "odb_processing")
        self.python_files = os.path.join(self.user_result_folder, "auxiliary_files", "python_files_to_computers")
        self.simulation_inp_files = os.path.join(self.user_result_folder, "auxiliary_files", "simulation_inp_files")

        folders_result = [self.excel_files, self.chip_images, self.simulation_inp_files, self.odb_processing, self.python_files]
        for folder in folders_result:
            if not os.path.exists(folder):
                os.makedirs(folder)

        # Folders inside project folder
        self.log_files = os.path.join(self.project_folder, "logs")
        self.user_config = os.path.join(self.project_folder, "config")
        self.graph_folder = os.path.join(self.project_folder, "graph_results")
        self.simulation_folder = os.path.join(self.project_folder, "simulation_folder")
        self.cae_path = os.path.join(self.project_folder, "defaut", "CAE")
        self.inp_path = os.path.join(self.project_folder, "defaut", "INPFiles")
        self.defaut_geometry = os.path.join(self.project_folder, "defaut", "geometry_datas")
        self.obj_path = os.path.join(self.project_folder, "json_and_obj_files", "objFiles")
        self.json_default_path = os.path.join(self.project_folder, "json_and_obj_files", "jsonFiles")
        
        folders_project = [self.log_files, self.user_config, self.graph_folder, self.simulation_folder, self.cae_path, self.inp_path, self.defaut_geometry, self.obj_path, self.json_default_path]
        for folder in folders_project:
            if not os.path.exists(folder):
                os.makedirs(folder)

        self.yaml_parameters = os.path.join(self.user_config, "parameters.yaml")
        self.yaml_materials_properties = os.path.join(self.user_config, "material_properties.yaml")
        self.yaml_computer_files = os.path.join(self.python_files, "computers_list.yaml")

        # Enable next step in UI
        self.ui.button_settings_next_page.setEnabled(True)








