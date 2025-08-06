import os
import time
from typing import Any
from backend.optimization.pso_scripts.pso_setup import PsoSetup
from frontend.aux_files.show_status_message import StatusMessage
from backend.optimization.aux_files.aux_functions import AuxClass
from backend.optimization.pso_scripts.pso_manager import PsoManager
from backend.optimization.aux_files.thread_manager import WorkerThread

class OtimizationManager:
    """
    Manages the Particle Swarm Optimization (PSO) process,
    including configuration, thread execution, result tracking,
    and cleanup of temporary files generated during the optimization.
    """
    def __init__(self, main_window: Any):
        """
        Initializes the optimization manager by extracting all necessary
        information from the main window and starting the PSO process
        if no previous errors are tracked.

        Args:
            main_window (Any): Reference to the main GUI window containing user inputs and configurations.
        """
        self.error_tracking = main_window.error_tracking                       # True/False
        if not self.error_tracking:
            # General Info
            self.project_name = main_window.project_name                       # TT2207
            self.ui = main_window.ui                                           # Interface

            # Extract required data from the main window
            self.weights = main_window.weights                                 # [0.5, 0.1, 0.0, 0.2, 0.2]
            self.forces = main_window.forces                                   # True/False
            self.temp = main_window.temp                                       # True/False
            self.chip = main_window.chip                                       # True/False

            # Folder Paths 
            self.user_result_folder = main_window.user_result_folder           # C:/Users/adam-ua769pu3t3n7k4o/Pictures\TT2207
            self.chip_images = main_window.chip_images                         # C:/Users/adam-ua769pu3t3n7k4o/Pictures\TT2207\chip_images
            self.excel_files = main_window.excel_files                         # C:/Users/adam-ua769pu3t3n7k4o/Pictures\TT2207\excel_files
            self.odb_processing = main_window.odb_processing                   # C:/Users/adam-ua769pu3t3n7k4o/Pictures\TT2207\auxiliary_files/odb_processing
            self.simulation_inp_files = main_window.simulation_inp_files       # C:/Users/adam-ua769pu3t3n7k4o/Pictures\TT2207\auxiliary_files/simulation_inp_files
            self.python_files = main_window.python_files                       # C:/Users/adam-ua769pu3t3n7k4o/Pictures\TT2207\auxiliary_files/python_files_to_computers

            self.software_folder = main_window.software_folder                   # C:\MaterialOtimization
            self.project_folder = main_window.project_folder                       # C:\MaterialOtimization\TT2207
            self.log_folder = main_window.log_files                            # C:\MaterialOtimization\TT2207\logs           
            self.user_config = main_window.user_config                         # C:\MaterialOtimization\TT2207\config
            self.inp_path = main_window.inp_path                               # C:\MaterialOtimization\TT2207\defaut/INPFiles            
            self.graph_folder = main_window.graph_folder                       # C:\MaterialOtimization\TT2207\graph_results
            self.simulation_folder = main_window.simulation_folder             # C:\MaterialOtimization\TT2207\simulation_folder
            self.obj_path = main_window.obj_path                               # C:\MaterialOtimization\TT2207\json_and_obj_files/objFiles
            self.json_default_path = main_window.json_default_path             # C:\MaterialOtimization\TT2207\json_and_obj_files/jsonFiles
            
            # Yaml and txt Files Paths
            self.yaml_project_info = main_window.yaml_project_info                 # C:\MaterialOtimization\TT2207\info.yaml
            self.yaml_parameters = main_window.yaml_parameters             # C:\MaterialOtimization\TT2207\config\parameters.yaml
            self.yaml_computer_files = main_window.yaml_computer_files               # C:/Users/adam-ua769pu3t3n7k4o/Pictures\TT2207\auxiliary_files/python_files_to_computers\computers_list.yaml
            self.log_file = os.path.join(self.log_folder, "debug_optimization.txt")  # C:\MaterialOtimization\TT2207\logs\debug_optimization.txt
            
            self.subrotine_dir = main_window.subrotine_dir
            self.reload = main_window.reload
            self.process_finished = main_window.process_finished
            self.iteration_in_progress = main_window.iteration_in_progress
            self.abaqus_path = main_window.abaqus_path

            # Reset log file
            with open(self.log_file, "w") as f:
                f.write("=== Optimization starting ===\n\n")

            # Initialization of control variables
            self.stage = None
            self.target_values = {}
            self.parameters_boundry = {}
            
            self.initial_time = time.time()

            if not self.process_finished:
                self.call_pso_script()
            

    def call_pso_script(self) -> None:
        """
        Starts a worker thread to run the PSO algorithm.
        Connects thread signals to post-processing functions.
        """
        StatusMessage.set_text(self, "message-id_01")
        AuxClass.log(self, "  [Step 01] call_pso_script\n")

        try:
            self.thread = WorkerThread(lambda: self.start_pso(), name="PsoThread")
            self.thread.finished_signal.connect(lambda: AuxClass.finish_otimization(self))
            self.thread.finished_signal.connect(lambda: AuxClass.clean_folder(self))
            self.thread.start()
        except Exception as e:
            AuxClass.handle_error(self, e, "Error at call_pso_script")
       

    def start_pso(self) -> None:
        """
        Initializes the PSO variables and calls the main PSO execution method.
        """
        try:
            AuxClass.log(self, "\n  [Step 02] start_pso --> get_start_info\n")
            lb, ub, num_dimensions, velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history = PsoSetup.get_start_info(self)
            if not self.error_tracking:
                AuxClass.log(self, "\n\n  [Step 03] start_pso --> run_pso\n")
                PsoManager.run_pso(self, velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history, lb, ub, num_dimensions)
        except Exception as e:
            self.e = e
            AuxClass.handle_error(self, e, "Error in start_pso")





