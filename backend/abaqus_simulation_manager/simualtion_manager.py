import os
import time
import yaml
import shutil
import traceback
import numpy as np
from backend.abaqus_simulation_manager.aux_scripts.edit_input_file import InpEditor
from backend.abaqus_simulation_manager.aux_scripts.parallel_simulation import ParallelSimulation
from frontend.aux_files.show_status_message import StatusMessage
from backend.config.yaml_manager import YamlManager

class SimulationManager:
    """
    Manages the overall simulation workflow including input file preparation,
    simulation execution, and result monitoring.
    """
    def __init__(self, otimization_manager):
        """
        Initializes the SimulationManager with parameters and paths from the optimization manager.
        
        Args:
            otimization_manager: Object containing all configuration and path information.
        """
        # Variables
        self.project_name = otimization_manager.project_name                     # Ex: TT2207
        self.main_computer = otimization_manager.main_computer
        self.error_tracking = otimization_manager.error_tracking
        self.count_iteration = otimization_manager.count_iteration
        self.cutting_conditions = otimization_manager.cutting_conditions
        self.number_of_particles = otimization_manager.number_of_particles
        self.cores_by_simulation = otimization_manager.cores_by_simulation
        self.iteration_in_progress = otimization_manager.iteration_in_progress
    
        # Paths to Simulation Manager     
        self.ui = otimization_manager.ui                                        # Interface
        self.software_folder = otimization_manager.software_folder              # C:\MaterialOtimization
        self.user_config = otimization_manager.user_config                      # C:\MaterialOtimization\TT2207\config
        self.inp_path = otimization_manager.inp_path                            # C:\MaterialOtimization\TT2207\defaut/INPFiles            
        self.simulation_folder = otimization_manager.simulation_folder          # C:\MaterialOtimization\TT2207\simulation_folder
        self.odb_processing = otimization_manager.odb_processing                # C:/Users/adam-ua769pu3t3n7k4o/Pictures\TT2207\auxiliary_files/odb_processing
        self.user_result_folder = otimization_manager.user_result_folder        # C:/Users/adam-ua769pu3t3n7k4o/Pictures\TT2207
        self.simulation_inp_files = otimization_manager.simulation_inp_files    # C:/Users/adam-ua769pu3t3n7k4o/Pictures\TT2207\auxiliary_files/simulation_inp_files
        self.python_files = otimization_manager.python_files                    # C:/Users/adam-ua769pu3t3n7k4o/Pictures\TT2207\auxiliary_files/python_files_to_computers
        self.yaml_computer_files = otimization_manager.yaml_computer_files      # C:/Users/adam-ua769pu3t3n7k4o/Pictures\TT2207\auxiliary_files/python_files_to_computers\computers_list.yaml
        self.yaml_parameters = otimization_manager.yaml_parameters      # C:/Users/adam-ua769pu3t3n7k4o/Pictures\TT2207\auxiliary_files/python_files_to_computers\computers_list.yaml
        
        self.subrotine_dir = otimization_manager.subrotine_dir
        self.abaqus_path = otimization_manager.abaqus_path
        
        # Start the simulation manager
        self._manage_simulations()
           

    def _manage_simulations(self) -> None:
        """
        Orchestrates the full simulation process:
        1. Edits .inp files
        2. Transfers compiled files
        3. Creates YAML command list
        4. Executes simulations
        5. Waits for completion
        """
        print("aqui")
        print(self.iteration_in_progress)
        if not self.iteration_in_progress:
            # Step 1: Edit the .inp file
            StatusMessage.set_text(self, "message-id_02")
            try:    
                lis_dir_inp, self.index_names = InpEditor.manager_edit(self)
            except Exception as e:
                self._handle_exception(e, "Editing inp file")
                
            # Step 2: Putting compiled files together 
            if not self.error_tracking:
                try:
                    self._copy_compiled_files()
                except Exception as e:
                    self._handle_exception(e, "Transferring compiled files")

            # Step 3: Creating list for computers
            if not self.error_tracking:
                try:
                    lines = []
                    for i, file_path in enumerate(lis_dir_inp):
                        name = f"Comand{i:02}" if i < 10 else f"Comand{i}"
                        lines.append(f"{name}: True {file_path}")
                    with open(self.yaml_computer_files, "w") as file:
                        file.write("\n".join(lines))
                except Exception as e:
                    self._handle_exception(e, "Creating list for computers")

        # Step 4: Run the simulation
        if not self.error_tracking and self.main_computer == "Yes":
            try:
                StatusMessage.set_text(self, "message-id_03")
                self._start_parallel_simulation()
            except Exception as e:
                self._handle_exception(e, "Rodando Simulação")

        # Step 5: Waits others computers
        self._wait_for_all_simulations()
         

    def _copy_compiled_files(self) -> None:
        """
        Copies necessary compiled files (DLLs, .env) into each simulation folder.
        """
        for folder_name in os.listdir(self.simulation_inp_files):
            folder_path = os.path.join(self.simulation_inp_files, folder_name)
            if folder_name.lower() != "defaut" and folder_name.lower() != "info":
                source_path_list = ["abaqus_v6.env", "explicitU-D.dll", "explicitU.dll"]
                for file in source_path_list:
                    source_path = os.path.join(self.subrotine_dir, file)
                    destination_path = os.path.join(folder_path, file)
                    shutil.copy2(source_path, destination_path)


    def _start_parallel_simulation(self) -> None:
        """
        Initializes the ParallelSimulation class and runs the simulations.
        """
        sim = ParallelSimulation()
        sim.run_all_simulations(server_folder=self.simulation_folder, drive_folder=self.user_result_folder, yaml_computer_list=self.yaml_computer_files, odb_processing=self.odb_processing, abq_path = self.abaqus_path, num_cores=4, cp_number="cp01")


    def _wait_for_all_simulations(self) -> None:
        """
        Continuously checks whether all simulations are complete by:
        - Reading the YAML command list
        - Verifying the number of completed .odb files
        """
        while True:
            data = YamlManager.load_yaml(self, self.yaml_computer_files)

            all_finished = True
            for key, value in data.items():
                if key.lower().startswith("comand"):
                    status_str = str(value).split()[0].lower()  
                    if status_str in ("True", "Running"):
                        all_finished = False
                        break 

            if all_finished:
                count = 0
                for files in os.listdir(self.odb_processing):
                    if f"it_{str(self.count_iteration).zfill(2)}" in files:
                        count += 1

                if count == self.cutting_conditions*self.number_of_particles:
                    break
            else:
                time.sleep(10)

    
    def _handle_exception(self, exception: Exception, stage: str) -> None:
        """
        Handles and logs exceptions that occur during any simulation stage.
        
        Args:
            exception: The exception object raised.
            stage: Description of the stage where the error occurred.
        """
        self.e = exception
        self.stage = stage
        self.error_tracking = True
        StatusMessage.set_text(self, "message-error")
        print(f"Error in {stage}:", exception)
        traceback.print_exc()
