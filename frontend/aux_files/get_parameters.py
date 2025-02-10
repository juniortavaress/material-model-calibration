import os
import yaml
from frontend.aux_files.yaml_generator import YamlClass

class GetParameters:
    def save_parameters(self, call=None):
        with open(self.project_infos_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        if call == "save":
            param_checkboxes = {
                "A": self.ui.checkBox_param_A,
                "B": self.ui.checkBox_param_B,
                "n": self.ui.checkBox_param_n,
                "C1": self.ui.checkBox_param_C1,
                "C2": self.ui.checkBox_param_C2,
                "C3": self.ui.checkBox_param_C3,
                "e": self.ui.checkBox_param_e,
                "k": self.ui.checkBox_param_k,
                "Ts": self.ui.checkBox_param_Ts,
                "D1": self.ui.checkBox_param_D1,
                "D2": self.ui.checkBox_param_D2,
                "D3": self.ui.checkBox_param_D3,
                "D4": self.ui.checkBox_param_D4,
                "D5": self.ui.checkBox_param_D5,
                "Tm": self.ui.checkBox_param_Tm,
                "Tt": self.ui.checkBox_param_Tt,
                "e_damage": self.ui.checkBox_param_e_damage,
                "p": self.ui.checkBox_param_p}

            checkbox_status = {}
            for param, checkbox in param_checkboxes.items():
                checkbox_status[param] = checkbox.isChecked()
            YamlClass.save_yaml_info(self, self.project_infos_path, "Parameters to Iterate", checkbox_status)

        elif call == "load":
            if "Parameters to Iterate" in data:
                for param, value in data["Parameters to Iterate"].items():
                    if value == True:
                        checkbox = getattr(self.ui, f"checkBox_param_{param}", None)
                        if checkbox:
                            checkbox.setChecked(True)
