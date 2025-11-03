import os 
import logging
from typing import Optional
from PySide6.QtWidgets import QFileDialog


class ConditionManager:
    """
    Manages simulation conditions and their interaction with the GUI.
    """ 

    def update_ui_from_selected_condition(self) -> None:
        """
        Updates GUI fields based on the selected condition from the combobox.
        """
        selected_ui = self.ui.comboBox_condition.currentText()  # ex: "Condition 01"
        selected = "cond" + selected_ui.split()[-1] if selected_ui else None
            
        response = self.supabase.table("conditions").select("*").eq("project_id", self.project_id).eq("name", selected).execute()

        if response.data and len(response.data) > 0:
            condition = response.data[0]  
            self.ui.lineEdit_velocity.setText(str(condition.get("velocity") or ""))
            self.ui.lineEdit_deepCuth.setText(str(condition.get("deepcuth") or ""))
            self.ui.lineEdit_rakeAngle.setText(str(condition.get("rakeangle") or ""))
            self.ui.label_input.setText(str(condition.get("inputfile") or ""))
            self.ui.lineEdit_cutting_force.setText(str(condition.get("cutting_force") or ""))
            self.ui.lineEdit_normal_force.setText(str(condition.get("normal_force") or ""))
            self.ui.lineEdit_CCR.setText(str(condition.get("chip_compression") or ""))
            self.ui.lineEdit_CSR.setText(str(condition.get("chip_segmentation") or ""))
        else:
            self.ui.lineEdit_velocity.clear()
            self.ui.lineEdit_deepCuth.clear()
            self.ui.lineEdit_rakeAngle.clear()
            self.ui.label_input.clear()
            self.ui.lineEdit_cutting_force.clear()
            self.ui.lineEdit_normal_force.clear()
            self.ui.lineEdit_CCR.clear()
            self.ui.lineEdit_CSR.clear()


    def select_input_file(self) -> None:
        """
        Opens a file dialog for the user to select an input file.
        """
        input_file, _ = QFileDialog.getOpenFileName(self)
        self.ui.label_input.setText(input_file)


    def _upload_default_inp_to_db(self, condition_id, inp_path) -> str:
        """
        Uploads a .inp file to Supabase Storage and returns its public URL.

        Args:
            condition_id (str): Condition identifier.
            inp_path (str): Path to the input file.

        Returns:
            Optional[str]: Public URL or None if upload fails.
        """
        if inp_path:
            try:
                if not os.path.isfile(inp_path):
                    logging.error(f"File not found: {inp_path}")
                    return None

                with open(inp_path, "rb") as file:
                    file_data = file.read()

                bucket_name = "inp-default-files"
                storage_path = f"{self.project_id}/default_inp/sim_{condition_id}.inp"

                upload_response = self.supabase_storage.storage.from_(bucket_name).update(storage_path, file_data)
                if hasattr(upload_response, "error") and upload_response.error:
                    logging.error(f"Upload error: {upload_response.error.message}")
                    return None

                public_url = self.supabase_storage.storage.from_(bucket_name).get_public_url(storage_path)
                return public_url

            except Exception as e:
                logging.exception(f"Unexpected error during file upload: {e}")
                return None


    def save_condition(self, call=None) -> None:
        """
        Saves the current condition to the database and updates the combobox if needed.

        Args:
            call (str, optional): If "new", adds a new condition to the combobox.
        """
        condition_name = self.ui.comboBox_condition.currentText()
        cond_id = "cond" + condition_name.split()[-1]
        inp_path = self.ui.label_input.text()
        
        velocity = ConditionManager._is_valid_float(self.ui.lineEdit_velocity.text().replace(',', '.'))
        deep_cuth = ConditionManager._is_valid_float(self.ui.lineEdit_deepCuth.text().replace(',', '.'))
        rake_angle = ConditionManager._is_valid_float(self.ui.lineEdit_rakeAngle.text().replace(',', '.').replace('+', ''))
        cutting_force = ConditionManager._is_valid_float(self.ui.lineEdit_cutting_force.text().replace(',', '.'))
        normal_force = ConditionManager._is_valid_float(self.ui.lineEdit_normal_force.text().replace(',', '.'))
        chip_compression = ConditionManager._is_valid_float(self.ui.lineEdit_CCR.text().replace(',', '.'))
        chip_segmentation = ConditionManager._is_valid_float(self.ui.lineEdit_CSR.text().replace(',', '.'))
        inp_public_url = ConditionManager._upload_default_inp_to_db(self, cond_id, inp_path)

        if all([velocity, deep_cuth, rake_angle, inp_public_url]): 
            existing = self.supabase.table("conditions").select("*").eq("project_id", self.project_id).eq("name", cond_id).execute().data

            condition_data = {
                "project_id": self.project_id,
                "name": cond_id,
                "velocity": velocity,
                "deepcuth": deep_cuth,
                "rakeangle": rake_angle,
                "inputfile": inp_path,
                "inp_link": inp_public_url,
                "cutting_force": cutting_force,
                "normal_force": normal_force,
                "chip_compression": chip_compression,
                "chip_segmentation": chip_segmentation
            }
            
            if existing:
                self.supabase.table("conditions").update(condition_data).eq("id", existing[0]["id"]).execute()
            else:
                self.supabase.table("conditions").insert(condition_data).execute()
          
            if call == "new":
                new_condition = f"Condition 0{self.ui.comboBox_condition.count() + 1}"
                self.ui.comboBox_condition.addItem(new_condition)
                self.ui.comboBox_condition.setCurrentIndex(self.ui.comboBox_condition.findText(new_condition))
        else:
            self.error_tracking = True
  

    @staticmethod
    def _is_valid_float(value) -> Optional[str]:
        """
        Checks if a string can be converted to a float.

        Args:
            value (str): Input string.

        Returns:
            Optional[str]: Original string if valid, otherwise None.
        """
        try:
            float(value)
            return value
        except:
            return None
        



        