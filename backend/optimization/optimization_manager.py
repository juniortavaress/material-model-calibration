import os
import time
from backend.config.aux_functions import AuxClass
from backend.optimization.pso_scripts.pso_setup import PsoSetup
from backend.optimization.pso_scripts.pso_manager import PsoManager
from backend.optimization.aux_files.thread_manager import WorkerThread
from frontend.aux_files.tracking_message_manager import ProcessStatusLogger


class OtimizationManager:
    """
    Manages the Particle Swarm Optimization (PSO) process,
    including configuration, thread execution, result tracking,
    and cleanup of temporary files generated during the optimization.
    """
    def __init__(self, main):
        """
        Initializes the optimization manager by extracting all necessary
        information from the main window and starting the PSO process
        if no previous errors are tracked.

        Args:
            main_window (Any): Reference to the main GUI window containing user inputs and configurations.
        """
        self.main = main
        self.ui = main.ui
        self.log_file = os.path.join(self.main.log_files, "debug_optimization.txt")
        
        if not self.main.error_tracking:
            # Initialization of control variables
            self.stage = None
            self.target_values = {}
            self.parameters_boundry = {}
            
            self.initial_time = time.time()

            if not self.main.process_finished:
                self.call_pso_script()
            

    def call_pso_script(self) -> None:
        """
        Starts a worker thread to run the PSO algorithm.
        Connects thread signals to post-processing functions.
        """
        ProcessStatusLogger.set_log_to_ui(self, "message-id_01")

        try:
            self.thread = WorkerThread(lambda: self.start_pso(), name="PsoThread")
            self.thread.finished_signal.connect(lambda: AuxClass.finish_otimization(self))
            self.thread.finished_signal.connect(lambda: AuxClass.clean_folder(self))
            self.thread.start()
        except Exception as e:
            self.emain.error_tracking = True
            AuxClass._handle_exception(self, e, "Error at call_pso_script")
       

    def start_pso(self) -> None:
        """
        Initializes the PSO variables and calls the main PSO execution method.
        """
        try:
            lb, ub, num_dimensions, velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history = PsoSetup.get_start_info(self)

            if not self.main.error_tracking:
                PsoManager.run_pso(self, velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history, lb, ub, num_dimensions)
        except Exception as e:
            self.e = e
            self.main.error_tracking = True
            AuxClass._handle_exception(self, e, "Error in start_pso")





