import os
import re
import yaml
from PySide6.QtCore import QTimer
from backend.config.yaml_manager import YamlManager
from PySide6.QtWidgets import QMessageBox

class GetParameters:
    """
    Class responsible for managing material properties and parameters.
    It handles reading, defining, saving, and displaying material data
    from YAML files and INP files.
    """
        
    def parameter_and_interface_manager(self, import_geometry) -> None:
        """
        Manages the retrieval and visualization of parameter data 
        based on the geometry import state and error tracking.
        
        Args:
            import_geometry (bool): Indicates whether the geometry is being imported (True) 
                                    or created within the application (False).
        """  
        if not self.error_tracking and import_geometry:
            material_info = GetParameters.get_available_parameters(self)
            GetParameters.define_variables_name(self, material_info)
            GetParameters.get_list_with_parameters_name(self)
            GetParameters.show_paramters_values(self)

        elif not self.error_tracking and not import_geometry:
            print("CODE NEEDS TO BE IMPLEMENTED HERE")


    def get_available_parameters(self) -> dict:
        """
        Reads the material parameters from the input file and returns the data
        in a structured dictionary format.

        Returns:
            dict: A dictionary with material names as keys and their properties as values.
        """
        material_info = {}
        valid_properties = {"Damage Initiation", "Damage Evolution", "Plastic"}

        if os.path.exists(self.yaml_project_info):
            data = YamlManager.load_yaml(self, self.yaml_project_info)

            for _, info in data.items():
                for condition, value in info.items():
                    if condition == "Condition 01":
                        path_to_inp = value["Cutting Properties"]["inputFile"]

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


    def define_variables_name(self, dict) -> None:
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

        with open(self.yaml_materials_properties, "w", encoding="utf-8") as file:
            yaml.dump(dict, file, default_flow_style=False, allow_unicode=True, width=float("inf"))


    def get_list_with_parameters_name(self) -> None:
        """
        Collects the available material properties and saves them in the
        YAML file.

        Updates:
            self.materials_properties (dict): A dictionary with material names and 
            their properties as a list of booleans indicating availability.
        """
        self.materials_properties = {}
        if os.path.exists(self.yaml_materials_properties):
            data = YamlManager.load_yaml(self, self.yaml_materials_properties)
            for material_name, material_data in data.items():
                material_props = {}
                material_props["Damage Initiation"] = "Damage Initiation" in material_data
                material_props["Damage Evolution"] = "Damage Evolution" in material_data
                material_props["Plastic"] = "Plastic" in material_data
                self.materials_properties[material_name] = material_props
            YamlManager.save_yaml_info(self, self.yaml_project_info, "06. Material Properties", self.materials_properties)


    def show_paramters_values(self) -> None:
        """
        Displays the material properties on the user interface.

        This method shows the values for the material properties based on
        the selected material.
        """
        self.ui.frame_material_model.hide()
        self.ui.frame_damage_model.hide()

        data = YamlManager.load_yaml(self, self.yaml_materials_properties)
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


    def save_parameters(self) -> None:
        """
        Saves the selected parameters to the project YAML file.
        """
        self.ui.pages.setCurrentIndex(8)
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
        YamlManager.save_yaml_info(self, self.yaml_project_info, "07. Parameters to Iterate", checkbox_status)

        self.ui.frame_105.show()
        for param in param_checkboxes:
            checkbox = getattr(self.ui, f"checkBox_param_{param}", None)
            frame = getattr(self.ui, f"frame_limits_param_{param}", None)
            frame.hide()

            # print(frame)s
            
            if checkbox and checkbox.isChecked():
                # print(checkbox)
                frame.show()


    def save_parameters_limits(self) -> None:
        """
        Save the limits of the parameters for later use.
        """
        next_page = True
        data = YamlManager.load_yaml(self, self.yaml_project_info)

        data["08. Parameters Limits"] = {}
        for param, value in data["07. Parameters to Iterate"].items():
            min_field = getattr(self.ui, f"lineEdit_min_param_{param}")
            max_field = getattr(self.ui, f"lineEdit_max_param_{param}")

            if value == True:
                try:
                    if float(min_field.text()) != "" and float(max_field.text()) != "" and float(max_field.text()) > float(min_field.text()):
                        data["08. Parameters Limits"][param] = {"max": max_field.text(), "min": min_field.text()}
                        with open(self.yaml_project_info, "w", encoding="utf-8") as file:
                            yaml.dump(data, file, default_flow_style=False, allow_unicode=True, width=float("inf"))
                    else:
                        next_page = False
                except Exception as e:
                    next_page = False

        if next_page:
            self.ui.pages.setCurrentIndex(9)
        else:
            QMessageBox.warning(self, "Error", "There are one or more conditions with invalid values, the maximum value must be greater than the minimum value.")
