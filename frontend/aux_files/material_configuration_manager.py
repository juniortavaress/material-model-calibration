import os
import re
from PySide6.QtWidgets import QMessageBox

class MaterialParameterManager:
    """
    Manages material parameters by reading Abaqus input files (.inp),
    extracting relevant properties, mapping them to named variables,
    and persisting them to the database.
    """
        
    def manage_parameters_and_interface(self) -> None:
        """
        Executes the full workflow for material parameter management:
        1. Reads material data from input file.
        2. Maps raw values to named variables.
        3. Displays values in the UI.
        """
        if not self.error_tracking:
            material_info = MaterialParameterManager._read_material_parameters(self)
            MaterialParameterManager._map_variable_names(self, material_info)
            MaterialParameterManager._display_parameter_values(self)


    def _read_material_parameters(self) -> dict:
        """
        Parses the Abaqus input file (.inp) and extracts material properties.

        Returns:
            dict: Dictionary with material names as keys and their properties as nested dictionaries.
        """
        material_info = {}
        valid_properties = {"Damage Initiation", "Damage Evolution", "Plastic"}

        response = self.supabase.table("conditions").select("*").eq("project_id", self.project_id).order("id").limit(1).execute()
        if response.data and len(response.data) > 0:
            first_condition = response.data[0]
            path_to_inp = first_condition.get("inputfile")

            if path_to_inp and os.path.exists(path_to_inp):
                i = 0
                current_material = None
                current_property = None

                with open(path_to_inp, "r", encoding="utf-8") as inp_file:
                    lines = inp_file.readlines()

                while i < len(lines):
                    line = lines[i].strip()

                    match_material = re.match(r"\*Material, name=\"?([^\"]+)\"?", line)
                    if match_material:
                        current_material = match_material.group(1).strip()
                        material_info[current_material] = {}
                        current_property = None  
                        i += 1
                        continue

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


    def _map_variable_names(self, materials) -> None:
        """
        Maps raw material values to named variables and saves them to the database.

        Args:
            materials (dict): Dictionary of raw material properties.
        """
        for name, props in materials.items():
            if not props:
                continue

            plastic = props.get("Plastic", [])
            damage_init = props.get("Damage Initiation", [])
            damage_evolution = props.get("Damage Evolution", [])
            
            plastic_data = {
                "Plastic": {
                    "A": plastic[0],
                    "B": plastic[1],
                    "C1": plastic[3],
                    "C2": plastic[4],
                    "C3": plastic[5],
                    "Ts": plastic[8]
                }
            } if len(plastic) >= 9 else {}
            
            damage_init_data = {
                "Damage Initiation": {
                    "D1": damage_init[0],
                    "D2": damage_init[1],
                    "D3": damage_init[2],
                    "D4": damage_init[3],
                    "D5": damage_init[4],
                    "p": damage_evolution[-1][0] if damage_evolution else None
                }
            } if len(damage_init) >= 5 else {}
            
            record = {
                "project_id": self.project_id,
                "name": name,
                "plastic": plastic_data,
                "damage_initiation": damage_init_data,
                "damage_evolution": damage_evolution
            }

            existing = self.supabase.table("materials").select("*").eq("project_id", self.project_id).eq("name", name).execute().data
            if existing:
                self.supabase.table("materials").update(record) .eq("project_id", self.project_id) .eq("name", name) .execute()
            else:
                self.supabase.table("materials").insert(record).execute()


    def _display_parameter_values(self) -> None:
        """
        Displays the extracted and mapped material parameters in the UI.
        (Implementation placeholder — to be completed based on UI design.)
        """
        self.ui.frame_material_model.hide()
        self.ui.frame_damage_model.hide()

        self.ui.comboBox_material.clear()
        self.ui.comboBox_material_limits.clear()

        response = self.supabase.table("materials").select("*").eq("project_id", self.project_id).execute()

        if not response.data:
            return  

        for material in response.data:
            name = material["name"]
            self.ui.comboBox_material.addItem(name)
            self.ui.comboBox_material_limits.addItem(name)

        self.ui.comboBox_material.setCurrentIndex(0)
        self.ui.comboBox_material_limits.setCurrentIndex(0)

        first_material = response.data[0]
        plastic = first_material.get("plastic") or {}
        damage_init = first_material.get("damage_initiation") or {}
        plastic_values = plastic['Plastic']
        damage_values = damage_init['Damage Initiation']

        if plastic_values:
            self.ui.frame_material_model.show()
            self.ui.label_param_A.setText("{:0.4g}".format(plastic_values.get("A", 0)))
            self.ui.label_param_B.setText("{:0.4g}".format(plastic_values.get("B", 0)))
            self.ui.label_param_C1.setText("{:0.4g}".format(plastic_values.get("C1", 0)))
            self.ui.label_param_C2.setText("{:0.4g}".format(plastic_values.get("C2", 0)))
            self.ui.label_param_C3.setText("{:0.4g}".format(plastic_values.get("C3", 0)))
            self.ui.label_param_Ts.setText("{:0.4g}".format(plastic_values.get("Ts", 0)))

        if damage_values:
            self.ui.frame_damage_model.show()
            self.ui.label_param_D1.setText("{:0.4g}".format(damage_values.get("D1", 0)))
            self.ui.label_param_D2.setText("{:0.4g}".format(damage_values.get("D2", 0)))
            self.ui.label_param_D3.setText("{:0.4g}".format(damage_values.get("D3", 0)))
            self.ui.label_param_D4.setText("{:0.4g}".format(damage_values.get("D4", 0)))
            self.ui.label_param_D5.setText("{:0.4g}".format(damage_values.get("D5", 0)))
            self.ui.label_param_p.setText("{:0.4g}".format(damage_values.get("p", 0)))


    def save_parameters_from_material(self) -> None:
        """
        Saves the selected parameters marked for iteration and updates the UI
        to show limit input fields for each active parameter.
        """
        self.ui.pages.setCurrentIndex(7)
        param_checkboxes = {
            "A": self.ui.checkBox_param_A,
            "B": self.ui.checkBox_param_B,
            "C1": self.ui.checkBox_param_C1,
            "C2": self.ui.checkBox_param_C2,
            "C3": self.ui.checkBox_param_C3,
            "Ts": self.ui.checkBox_param_Ts,
            "D1": self.ui.checkBox_param_D1,
            "D2": self.ui.checkBox_param_D2,
            "D3": self.ui.checkBox_param_D3,
            "D4": self.ui.checkBox_param_D4,
            "D5": self.ui.checkBox_param_D5,
            "p": self.ui.checkBox_param_p}

        for param, checkbox in param_checkboxes.items():
            iterate_value = checkbox.isChecked()
            existing = self.supabase.table("parameters").select("*").eq("project_id", self.project_id).eq("name", param).execute().data
            
            if iterate_value:
                if existing:
                    self.supabase.table("parameters").update({
                        "iterate": iterate_value,
                    }).eq("project_id", self.project_id).eq("name", param).execute()
                else:
                    self.supabase.table("parameters").insert({
                        "project_id": self.project_id,
                        "name": param,
                        "iterate": iterate_value
                    }).execute()

        # Update UI visibility for limit fields
        for param in param_checkboxes:
            checkbox = getattr(self.ui, f"checkBox_param_{param}", None)
            frame = getattr(self.ui, f"frame_limits_param_{param}", None)
            frame.hide()
            parent = frame.parentWidget().parentWidget()

            if checkbox and checkbox.isChecked():
                frame.show()
                if parent and not parent.isVisible():
                    parent.show()


    def save_parameters_limits(self) -> None:
        """
        Validates and saves the min/max limits for each selected parameter.
        Displays an error message if any values are invalid.
        """
        all_valid = True

        response = self.supabase.table("parameters").select("*").eq("project_id", self.project_id).execute()
        if not response.data:
            QMessageBox.warning(self, "Error", "No parameters found for this project.")
            return
        
        for param_entry in response.data:
            param = param_entry["name"]
            checkbox = getattr(self.ui, f"checkBox_param_{param}", None)

            if not checkbox or not checkbox.isChecked():
                continue

            min_field = getattr(self.ui, f"lineEdit_min_param_{param}")
            max_field = getattr(self.ui, f"lineEdit_max_param_{param}")

            try:
                min_val = float(min_field.text())
                max_val = float(max_field.text())

                if max_val <= min_val:
                    all_valid = False
                    continue

                self.supabase.table("parameters").update({
                    "min_value": min_val,
                    "max_value": max_val,
                    "iterate": True
                }).eq("project_id", self.project_id).eq("name", param).execute()

            except ValueError:
                all_valid = False

        if all_valid:
            self.ui.pages.setCurrentIndex(8)
        else:
            QMessageBox.warning(
                self.ui,
                "Invalid Parameter Limits",
                "One or more parameters have invalid values. "
                "Ensure that maximum is greater than minimum and all fields are filled correctly."
            )