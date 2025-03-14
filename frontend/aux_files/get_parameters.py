import os
import re
import yaml
from PySide6.QtCore import QTimer
from frontend.aux_files.yaml_generator import YamlClass


class GetParameters:
    """
    Class responsible for managing material properties and parameters.
    It handles reading, defining, saving, and displaying material data
    from YAML files and INP files.
    """
        
    def parameter_and_interface_manager(self):
        """
        Manages the parameters and interface by getting the material data,
        defining variables, and displaying the values.
        """
        if not self.error_tracking:
            material_info = GetParameters.get_available_parameters(self)
            GetParameters.define_variables_name(self, material_info)
            GetParameters.get_list_with_parameters_name(self)
            GetParameters.show_paramters_values(self)


    def get_available_parameters(self):
        """
        Reads the material parameters from the input file and returns the data
        in a structured dictionary format.

        Returns:
            dict: A dictionary with material names as keys and their properties as values.
        """
        material_info = {}
        valid_properties = {"Damage Initiation", "Damage Evolution", "Plastic"}

        # Check if project information exists and get path to input file
        if os.path.exists(self.project_infos_path):
            with open(self.project_infos_path, "r", encoding="utf-8") as file:
                data = yaml.safe_load(file) or {}

            for key, info in data.items():
                for condition, value in info.items():
                    if condition == "Condition 01":
                        path_to_inp = value["Cutting Properties"]["inputFile"]

            # Parse the input file for material data
            i = 0
            current_material = None
            current_property = None

            with open(path_to_inp, "r", encoding="utf-8") as inp_file:
                lines = inp_file.readlines()

            while i < len(lines):
                line = lines[i].strip()

                # Get Material Name
                match_material = re.match(r"\*Material, name=\"?([^\"]+)\"?", line)
                if match_material:
                    current_material = match_material.group(1).strip()
                    material_info[current_material] = {}
                    current_property = None  
                    i += 1
                    continue

                # Get Properties Name
                match_property = re.match(r"\*([A-Za-z\s\-]+)", line)
                if match_property:
                    property_name = match_property.group(1).strip()
                    if property_name in valid_properties:
                        current_property = match_property.group(1).strip()
                        material_info[current_material][current_property] = []
                    else:
                        current_property = None
                    i += 1
                    continue

                # Get Properties Values
                if current_material and current_property:
                    if re.match(r"^[\d\.\-eE\s,]+$", line):
                        values = [float(v) for v in re.split(r"[,\s]+", line) if v]

                        if current_property == "Damage Initiation" or current_property == "Plastic":
                            material_info[current_material][current_property].extend(values)
                        else:
                            material_info[current_material][current_property].append(values)
                    else:
                        current_property = None

                if re.match(r"\** INTERACTION PROPERTIES", line):
                    break
                i += 1
        return {key: value for key, value in material_info.items() if value != {}}


    def define_variables_name(self, dict):
        """
        Defines the variable names for the material properties and updates
        the dictionary with the appropriate names.

        Args:
            dict (dict): The dictionary containing material properties.
        """
        for mat, values in dict.items():
            if 'Plastic' in values and len(values['Plastic']) > 0:
                values['Plastic'] = {
                    "A": values['Plastic'][0],
                    "B": values['Plastic'][1],
                    "n": values['Plastic'][2],
                    "C1": values['Plastic'][3],
                    "C2": values['Plastic'][4],
                    "C3": values['Plastic'][5],
                    "e": values['Plastic'][6],
                    "k": values['Plastic'][7],
                    "Ts": values['Plastic'][8]}
                if 'Damage Initiation' in values and len(values['Damage Initiation']) > 0:
                    values['Damage Initiation'] = {
                        "D1": values['Damage Initiation'][0],
                        "D2": values['Damage Initiation'][1],
                        "D3": values['Damage Initiation'][2],
                        "D4": values['Damage Initiation'][3],
                        "D5": values['Damage Initiation'][4],
                        "Tm": values['Damage Initiation'][5],
                        "Tt": values['Damage Initiation'][6],
                        "e": values['Damage Initiation'][7],
                        "p": values['Damage Evolution'][-1][0]}

        # Save the updated material properties to a YAML file
        yaml_path = os.path.join(self.user_config, "material_properties.yaml")
        with open(yaml_path, "w", encoding="utf-8") as file:
            yaml.dump(dict, file, default_flow_style=False, allow_unicode=True, width=float("inf"))


    def get_list_with_parameters_name(self):
        """
        Collects the available material properties and saves them in the
        YAML file.

        Updates:
            self.materials_properties (dict): A dictionary with material names and 
            their properties as a list of booleans indicating availability.
        """
        self.materials_properties = {}
        yaml_path = os.path.join(self.user_config, "material_properties.yaml")
        if os.path.exists(yaml_path):
            with open(yaml_path, "r", encoding="utf-8") as file:
                data = yaml.safe_load(file)

                # Gather the material properties
                for material_name, material_data in data.items():
                    material_props = {}

                    material_props["Damage Initiation"] = "Damage Initiation" in material_data
                    material_props["Damage Evolution"] = "Damage Evolution" in material_data
                    material_props["Plastic"] = "Plastic" in material_data

                    self.materials_properties[material_name] = material_props
                YamlClass.save_yaml_info(self, self.project_infos_path, "4. Material Properties", self.materials_properties)


    def show_paramters_values(self):
        """
        Displays the material properties on the user interface.

        This method shows the values for the material properties based on
        the selected material.
        """
        self.ui.frame_material_model.hide()
        self.ui.frame_damage_model.hide()

        yaml_path = os.path.join(self.user_config, "material_properties.yaml")
        with open(yaml_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

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


    def save_parameters(self, call=None):
        """
        Saves the selected parameters to the project YAML file.

        Args:
            call (str, optional): The action to be performed, either "save" or "load".
        """
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
            YamlClass.save_yaml_info(self, self.project_infos_path, "5. Parameters to Iterate", checkbox_status)


        elif call == "load":
            if "5. Parameters to Iterate" in data:
                for param, value in data["5. Parameters to Iterate"].items():
                    if value == True:
                        checkbox = getattr(self.ui, f"checkBox_param_{param}", None)
                        if checkbox:
                            checkbox.setChecked(True)
            else:
                return

        GetParameters.show_parameters_limits(self)


    def show_parameters_limits(self):
        """
        Displays the limits of the parameters.
        """
        with open(self.project_infos_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        param_data = data["5. Parameters to Iterate"]
        for param, value in param_data.items():
            frame = getattr(self.ui, f"frame_limits_param_{param}", None)
            min = getattr(self.ui, f"lineEdit_min_param_{param}", None)
            max = getattr(self.ui, f"lineEdit_max_param_{param}", None)

            if value == True:
                frame.show()
                if param in data.get("6. Parameters Limits", {}):
                    min.setText(data["6. Parameters Limits"][param]["min"])
                    max.setText(data["6. Parameters Limits"][param]["max"])
            else:
                min.setText("")
                max.setText("")
                frame.hide()

        self.ui.frame_105.show()
        self.resize(1000, 600) if not self.isMaximized() else None


    def save_parameters_limits(self):
        """
        Save the limits of the parameters for later use.
        """
        next_page = True
        with open(self.project_infos_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        data["6. Parameters Limits"] = {}
        for param, value in data["5. Parameters to Iterate"].items():

            min_field = getattr(self.ui, f"lineEdit_min_param_{param}")
            max_field = getattr(self.ui, f"lineEdit_max_param_{param}")

            if value == True:
                try:
                    if float(min_field.text()) != "" and float(max_field.text()) != "" and float(max_field.text()) > float(min_field.text()):
                        data["6. Parameters Limits"][param] = {"max": max_field.text(), "min": min_field.text()}
                        with open(self.project_infos_path, "w", encoding="utf-8") as file:
                            yaml.dump(data, file, default_flow_style=False, allow_unicode=True, width=float("inf"))
                    else:
                        next_page = False
                except Exception as e:
                    next_page = False

        if next_page:
            self.ui.pages.setCurrentIndex(6)
        else:
            self.ui.label_limits_warning.show()
            QTimer.singleShot(3000, lambda: self.ui.label_limits_warning.hide())

