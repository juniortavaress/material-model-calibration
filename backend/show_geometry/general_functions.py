import json
import yaml
import os
from PySide6.QtCore import QTimer
from frontend.aux_files.yaml_generator import YamlClass

class AuxFunctions():
    def __init__(self):
        super(AuxFunctions, self).__init__()


    # Display a warning message in the provided label
    def warning(self, label_warning=None, message=None):
        if label_warning:
            label_warning.show()
            label_warning.setText(message)
            QTimer.singleShot(3000, lambda: label_warning.setText(""))
            self.ui.button_create_geometry_next.setEnabled(False)


    # Clean the specified folder and create it if it doesn't exist
    def clean_and_create_folder(self, path):
        try:
            for file in os.listdir(path):
                pathFile = os.path.join(path, file)
                os.remove(pathFile)
        except FileNotFoundError:
            os.makedirs(path)
        except PermissionError as e:
            print(f"Permission error: {e}. (AuxFiles\general_functions.py -> clean_and_create_folder)")


    # Save data to a JSON file
    def save_dict(pathName, data):
        with open(pathName, 'w') as json_file:
            json.dump(data, json_file, indent=4)




    def save_create_setup_option(self, geometry):
        with open(self.project_infos_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file) or {}

        if "3. Setup Infos" not in data:
            data["3. Setup Infos"] = {}

        if geometry == "import":
            data["3. Setup Infos"] = {"Import Geometry (.inp)": True}
            self.ui.pages.setCurrentIndex(5)
            self.ui.button_import_inp.clicked.connect(lambda: self.ui.frame_15.show())
            self.ui.button_import_inp.clicked.connect(lambda: self.ui.frame_20.show())

        else:
            data["3. Setup Infos"] = {"Import Geometry (.inp)": False}
            self.ui.frame_95.show()
            self.ui.pages.setCurrentIndex(4)
            self.ui.button_create_geometry.clicked.connect(lambda: self.ui.frame_15.hide())
            self.ui.button_create_geometry.clicked.connect(lambda: self.ui.frame_20.hide())

        YamlClass.save_yaml_info(self, self.project_infos_path, "3. Setup Infos", data["3. Setup Infos"])

