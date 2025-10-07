from PySide6.QtWidgets import QMessageBox

class OutputConfigurationManager:
    """
    Handles output configuration, UI synchronization, and database persistence.
    """

    def configure_outputs(self) -> None:
        """
        Executes the output configuration workflow:
        1. Collects parameters from the UI.
        2. Updates UI visibility based on selections.
        3. Validates and saves configuration to the database.
        """
        OutputConfigurationManager.collect_ui_inputs(self)
        OutputConfigurationManager.update_ui_visibility(self)
        OutputConfigurationManager.validate_and_save(self)


    def collect_ui_inputs(self) -> None:
        """
        Collects output-related parameters from the UI.
        """
        self.wfc = float(self.ui.wfc.text())
        self.wfn = float(self.ui.wfn.text())
        self.wccr = float(self.ui.wccr.text())
        self.wcsr = float(self.ui.wcsr.text())
        self.forces = self.ui.forces.isChecked()
        self.chip = self.ui.chip.isChecked()


    def update_ui_visibility(self) -> None:
        """
        Updates visibility of UI components based on selected output options.
        Hides related frames and removes analysis types if options are disabled.
        """
        if not self.forces:
            self.ui.frame_fn_result.hide()
            self.ui.frame_fc_result.hide()
            self.ui.results_fn.hide()
            self.ui.results_fc.hide()
            self.ui.combobox_analysis_type.removeItem(self.ui.combobox_analysis_type.findText("Forces"))
        if not self.chip:
            self.ui.frame_csr_result.hide()
            self.ui.frame_ccr_result.hide()
            self.ui.results_ccr.hide()
            self.ui.results_csr.hide()
            self.ui.combobox_analysis_type.removeItem(self.ui.combobox_analysis_type.findText("Chip Format"))


    def validate_and_save(self) -> None:
        """
        Validates selected output options and saves configuration to the database.
        Displays a warning if no output type is selected.
        """
        if not (self.forces or self.chip):
            QMessageBox.warning(self, "Error", "Please select at least one type of output (Forces, or Chip).")
            return

        existing = self.supabase.table("project_outputs").select("*").eq("project_id", self.project_id).execute().data

        config_data  = {
            "project_id": self.project_id,
            "forces": self.forces,
            "chip": self.chip,
            "weight_fc": self.wfc,
            "weight_fn": self.wfn,
            "weight_ccr": self.wccr,
            "weight_csr": self.wcsr
        }

        if existing:
            self.supabase.table("project_outputs").update(config_data ).eq("project_id", self.project_id).execute()
        else:
            self.supabase.table("project_outputs").insert(config_data ).execute()
        self.ui.pages.setCurrentIndex(5)
        