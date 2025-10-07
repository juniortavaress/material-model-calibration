import time
from zoneinfo import ZoneInfo
from dateutil.parser import isoparse
from datetime import datetime, timedelta

from backend.config.aux_functions import AuxClass
from backend.abaqus_simulation_manager.edit_input_file import InpEditor
from frontend.aux_files.tracking_message_manager import ProcessStatusLogger
from backend.abaqus_simulation_manager.parallel_simulation import ParallelSimulation


class SimulationManager:
    """
    Manages the full simulation workflow, including input file preparation,
    simulation execution, and result monitoring.
    """

    def __init__(self, optimization, main):
        """
        Initializes the SimulationManager with configuration and UI references.

        Args:
            optimization: Object containing optimization parameters and settings.
            main: Main application context with UI and Supabase access.
        """
        # self.ui = main.ui
        self.main = main
        self.optimization = optimization

        self._manage_simulations()
           

    def _manage_simulations(self) -> None:
        """
        Orchestrates the simulation process:
        1. Edits input files
        2. Starts parallel simulations (if main computer)
        3. Waits for all simulations to complete
        """
        # STEP-01
        if not self.main.iteration_in_progress:
            ProcessStatusLogger.set_log_to_ui(self, "message-id_02")
            try:    
                InpEditor.manager_edit(self)
            except Exception as e:
                self.main.error_tracking = True
                AuxClass._handle_exception(self, e, "SM - Editing INP Files")

        # STEP-02
        if not self.main.error_tracking and self.optimization.main_computer == "Yes":
            ProcessStatusLogger.set_log_to_ui(self, "message-id_03")
            try:
                response  = self.main.supabase.table("computers").select("id, computer_number").eq("project_id", self.main.project_id).eq("computer_id", self.main.pc_id).execute()
                computer_number = response .data[0]["computer_number"]
                self._start_parallel_simulation(computer_number)
            except Exception as e:
                self.main.error_tracking = True
                AuxClass._handle_exception(self, e, "SM - Running Simulation")

        # STEP-03
        if not self.main.error_tracking:
            try:
                self._wait_for_all_simulations()
            except Exception as e:
                self.main.error_tracking = True
                AuxClass._handle_exception(self, e, "SM - Waiting Simulations")


    def _start_parallel_simulation(self, computer_number) -> None:
        """
        Initializes the PSO variables and calls the main PSO execution method.
        """
        cp_id = f"cp{str(computer_number).zfill(2)}"
        self.sim_thread = ParallelSimulation(self.main, self.optimization.cores_by_simulation, cp_id)
        self.sim_thread.run_all_simulations()


    def _wait_for_all_simulations(self) -> None:
        """
        Monitors the status of all auxiliary computers and waits until all simulations are complete.
        Deactivates computers that have not updated within 10 minutes.
        """
        while True:
            self._get_computers_status()
            response = self.main.supabase.table("results").select("error").eq("project_id", self.main.project_id).eq("iteration_number", self.main.current_opt).execute()
            if all(r["error"] is not None for r in response.data):
                break

            print("⏳ Waiting for all simulations to complete...")
            time.sleep(2700)


    def _get_computers_status(self) -> None:
        """
        Checks the status of all auxiliary computers in the current project.

        This method compares the last update timestamp of each computer (excluding the main computer)
        against the current time. If a computer has not updated within the last
        10 minutes, it is considered inactive and will be:
            - Marked as inactive in the 'computers' table.
            - Unassigned from any simulation commands in the 'simulation_commands' table.

        Active computers are logged as "activated", while inactive ones are logged as "deactivated".
        """
        
        now = datetime.now(ZoneInfo("Europe/Berlin"))

        main_comp_response = self.main.supabase.table("computers").select( "computer_number").eq("project_id", self.main.project_id).eq("computer_id", self.main.pc_id).execute()
        main_number = main_comp_response.data[0]["computer_number"]

        comp_response = self.main.supabase.table("computers").select("id, computer_number, last_update, status").eq("project_id", self.main.project_id).execute()
        for comp in comp_response.data:
            if comp["computer_number"] == main_number:
                continue

            last_update_raw = comp["last_update"]
            is_active = False

            if last_update_raw is not None:
                last_update = isoparse(last_update_raw)
                print("time", (now - last_update))
                is_active = (now - last_update) <= timedelta(minutes=10)

            if not is_active:
                if comp["status"]:
                    cp_id = f'cp{comp["computer_number"]:02d}'
                    self.main.supabase.table("computers").update({"status": False,"last_update": None}).eq("id", comp["id"]).execute()
                    self.main.supabase.table("simulation_commands").update({"status": False,"computer_id": None}).eq("project_id", self.main.project_id).eq("computer_id", cp_id).execute()
                    print(f'{comp["computer_number"]}: deactivated')
            else:
                print(f'{comp["computer_number"]}: activated')

