import json
import yaml
import os
from PySide6.QtCore import QTimer
from backend.config.yaml_manager import YamlManager

class AuxFunctions():
    def save_create_setup_option(self, geometry):        
        data = YamlManager.load_yaml(self, self.yaml_project_info)
        data.setdefault("3. Conditions", {})
        data["3. Conditions"]["Import Geometry (.inp)"] = geometry == "import"

        if geometry == "import":
            self.ui.pages.setCurrentIndex(6)
            self.ui.frame_15.show()
            self.ui.frame_20.show()

        else:
            self.ui.frame_95.show()
            self.ui.pages.setCurrentIndex(5)
            self.ui.frame_15.hide()
            self.ui.frame_20.hide()

        YamlManager.save_yaml_info(self, self.yaml_project_info, "3. Conditions", data["3. Conditions"])



    # Display a warning message in the provided label
    def warning(self, label_warning=None, message=None):
        if label_warning:
            label_warning.show()
            label_warning.setText(message)
            QTimer.singleShot(3000, lambda: label_warning.setText(""))
            self.ui.button_create_geometry_next.setEnabled(False)

