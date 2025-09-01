import os
import re
import yaml
from PySide6.QtCore import QTimer
from backend.config.yaml_manager import YamlManager
from PySide6.QtWidgets import QMessageBox

class GetOutputs:
    def get_outputs_manager(self):
        data = GetOutputs.get_datas_from_ui(self)
        GetOutputs.atualize_ui(self)
        GetOutputs.verify_datas(self, data)


    def get_datas_from_ui(self):
        weights_raw = [self.ui.wfc.text(), self.ui.wfn.text(), self.ui.wt.text(), self.ui.wccr.text(), self.ui.wcsr.text()]
        self.forces = self.ui.forces.isChecked()
        self.temp = self.ui.temperature.isChecked()
        self.chip = self.ui.chip.isChecked()

        data = {
            "Forces": self.forces,
            "Temperature": self.temp,
            "Chip": self.chip,
            "Weights": weights_raw
        }
        return data


    def atualize_ui(self):
        # Adding information to graph combobox analysis
        if not self.forces:
            self.ui.frame_fn_result.hide()
            self.ui.frame_fc_result.hide()
            self.ui.results_fn.hide()
            self.ui.results_fc.hide()
            self.ui.combobox_analysis_type.removeItem(self.ui.combobox_analysis_type.findText("Forces"))
        if not self.temp:
            self.ui.frame_temperature_result.hide()
            self.ui.frame_temperature_path.hide()
            self.ui.results_temp.hide()
            self.ui.combobox_analysis_type.removeItem(self.ui.combobox_analysis_type.findText("Temperature vs. Penetration Depth"))
            self.ui.combobox_analysis_type.removeItem(self.ui.combobox_analysis_type.findText("Temperature vs. Time"))
        if not self.chip:
            self.ui.frame_csr_result.hide()
            self.ui.frame_ccr_result.hide()
            self.ui.results_ccr.hide()
            self.ui.results_csr.hide()
            self.ui.combobox_analysis_type.removeItem(self.ui.combobox_analysis_type.findText("Chip Format"))


    def verify_datas(self, data):
        if not (self.forces or self.temp or self.chip):
            QMessageBox.warning(self, "Error", "Please select at least one type of output (Forces, Temperature, or Chip).")
            return

        self.weights = []
        for w in data["Weights"]:
            try:
                value = float(w)
                if value < 0:
                    raise ValueError
                self.weights.append(value)
            except ValueError:
                QMessageBox.warning(self, "Error", f"Invalid weight: '{w}'. Please enter only numbers greater than zero.")
                return

        YamlManager.save_yaml_info(self, self.yaml_project_info, "03. Outputs", data)
        self.ui.pages.setCurrentIndex(4)
