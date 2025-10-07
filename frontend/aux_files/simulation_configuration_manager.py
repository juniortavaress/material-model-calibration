import psutil
from PySide6.QtWidgets import QMessageBox

class SimulationConfiguratorManager:
    """
    Handles configuration, validation, and persistence of Particle Swarm Optimization (PSO)
    and simulation parameters. Also updates the UI with system resource availability.
    """
    def update_simulation_info(self) -> None:
        """
        Updates the UI with the number of cutting conditions and available physical CPU cores.
        """
        response = self.supabase.table("conditions").select("id").eq("project_id", self.project_id).execute()
        condition_count = len(response.data) if response.data else 0
        self.ui.label_number_conditions.setText(str(condition_count))
        SimulationConfiguratorManager._get_available_cores(self)
        self.ui.pages.setCurrentIndex(9)



    def _get_available_cores(self):
        """
        Calculates the number of available physical CPU cores based on usage threshold
        and updates the UI accordingly.
        """
        usage_threshold = 8
        cpu_usage = psutil.cpu_percent(percpu=True)
        physical_cores = psutil.cpu_count(logical=False)
        self.availableCores = sum(1 for i, usage in enumerate(cpu_usage) if usage < usage_threshold and i < physical_cores)
        self.ui.label_cores.setText(str(self.availableCores))
        

    def validate_and_save_config(self) -> None:
        """
        Validates PSO and simulation parameters from the UI.
        If valid, saves the configuration to the database.
        Displays an error message if validation fails.
        """
        core_selection = self.ui.combobox_core_by_simulation.currentText()
        main_computer = self.ui.combobox_main_computer.currentText()
        condition_count = self.ui.label_number_conditions.text()

        try:
            self.error_tracking = False
            iterations = int(self.ui.lineEdit_number_iteration.text())
            particles = int(self.ui.lineEdit_number_particles.text())
            inertia_weight = float(self.ui.lineEdit_w.text())
            cognitive_coeff = float(self.ui.lineEdit_fig.text())
            social_coeff = float(self.ui.lineEdit_fip.text())

            invalid_values = (
                iterations <= 0 or
                particles <= 0 or
                core_selection == "None" or
                main_computer == "None"
            )
            self.error_tracking = invalid_values

        except:
            self.error_tracking = True

        if self.error_tracking:
            QMessageBox.warning(self, "Error", "There are one or more parameters with invalid values.")
            return
        
        simulation_data = {
            "project_id": self.project_id,
            "cores_by_simulation": core_selection,
            "cutting_conditions": condition_count,
            "total_iterations": iterations,
            "main_computer": main_computer,
            "particles": particles,
            "w": inertia_weight,
            "fig": social_coeff,
            "fip": cognitive_coeff,
        }

        existing = self.supabase.table("project_simulation").select("*").eq("project_id", self.project_id).execute().data
        if existing:
            self.supabase.table("project_simulation").update(simulation_data).eq("project_id", self.project_id).execute()
        else:
            self.supabase.table("project_simulation").insert(simulation_data).execute()
        self.ui.pages.setCurrentIndex(10)


  
