import os
import yaml
import shutil
import traceback
import numpy as np
from backend.pso_scripts.edit_input_file import InpEditor
from frontend.aux_files.show_status_message import StatusMessage
from backend.get_result_from_odb_file.main_results import GetResults


class SimulationManager:
    def __init__(self):
        print("SimulationManager")

    def simulation_manager(self):
        """
        Manages the simulation workflow: editing input files, running simulations,
        transferring output files, and collecting results.
        """
        print("fddf")
        if not self.iteration_in_progress:
            # Step 1: Edit the .inp file
            try:    
                StatusMessage.set_text(self, "message-id_02")
                lis_dir_inp, self.index_names = InpEditor.manager_edit(self)
            except Exception as e:
                SimulationManager.except_function(self, e, "Editing inp file")
                
            # Step 2: Putting compiled files together 
            if not self.error_tracking:
                try:
                    SimulationManager.copy_file(self, "CompiledFiles")
                except Exception as e:
                    SimulationManager.except_function(self, e, "Transferring compiled files")

            # Step 3: Creating list for computers
            if not self.error_tracking:
                print("ff")
                try:
                    lines = []
                    for i, file_path in enumerate(lis_dir_inp):
                        lines.append(f"Comand{i}: True {file_path}")

                    with open(os.path.join(self.python_files, "computers_list.yaml"), "w") as file:
                        file.write("\n".join(lines))
                    
                except Exception as e:
                    SimulationManager.except_function(self, e, "Creating list for computers")


        # Step 4: Run the simulation
        if not self.error_tracking and self.main_computer == "Yes":
            try:
                StatusMessage.set_text(self, "message-id_03")
                SimulationManager.run_simulation(self)
            except Exception as e:
                SimulationManager.except_function(self, e, "Rodando Simulação")


        while True:
            yaml_path = os.path.join(self.python_files, "computers_list.yaml")
            with open(yaml_path, "r") as file:
                data = yaml.safe_load(file)

            all_finished = True
            for key, value in data.items():
                if key.lower().startswith("comand"):
                    status_str = str(value).split()[0].lower()  
                    if status_str in ("True", "Running"):
                        all_finished = False
                        break 

            if all_finished:
                break
            else:
                import time
                time.sleep(5)

        # Step 5: Collect simulation results
        if not self.error_tracking:
            try:    
                StatusMessage.set_text(self, "message-id_04")
                GetResults.result_call(self)
            except Exception as e:
                SimulationManager.except_function(self, e, "Collecting results")


        if not self.error_tracking:
            try:    
                SimulationManager.copy_file(self, "ODB")
            except Exception as e:
                SimulationManager.except_function(self, e, "Moving ODB")
        

    def copy_file(self, type):
        """
        Transfers .odb files from the simulation directory to the results directory.
        """
        if type == "ODB":
            destination_odb_folder = self.server_folder
            os.makedirs(destination_odb_folder, exist_ok=True)
            for file in os.listdir(self.odb_processing):
                source_path = os.path.join(self.odb_processing, file)
                os.makedirs(os.path.join(destination_odb_folder, file[:-4]), exist_ok=True)
                destination_path = os.path.join(destination_odb_folder, file[:-4], file)  
                shutil.copy2(source_path, destination_path)
                os.remove(source_path)

        elif type == "CompiledFiles":
            compiled_files_dir = os.path.join(self.software_path, "compiled")
            for folder_name in os.listdir(self.simulation_inp_files):
                folder_path = os.path.join(self.simulation_inp_files, folder_name)
                if folder_name.lower() != "defaut" and folder_name.lower() != "info":
                    source_path_list = ["abaqus_v6.env", "explicitU-D.dll", "explicitU.dll"]
                    for file in source_path_list:
                        source_path = os.path.join(compiled_files_dir, file)
                        destination_path = os.path.join(folder_path, file)
                        shutil.copy2(source_path, destination_path)


    def run_simulation(self):
        """
        Starts the Abaqus simulation using a parallel processing framework.
        """
        from backend.pso_scripts.parallel_simulation import ParallelSimulation

        cp_number = "cp01"
        number_of_cores = 4
        drive_folder = self.user_result_folder
        self.server_folder = os.path.join(os.getenv("SystemDrive", "C:") , f"\MaterialOtimization\{self.project_name}\simulation_folder")
        sim = ParallelSimulation()
        sim.run_all_simulations(self.server_folder, drive_folder, number_of_cores, cp_number)


    def except_function(self, exception, stage):
        """
        Handles exceptions by saving error data to a log file and re-raising the exception.
        """
        self.e = exception
        self.stage = stage
        self.error_tracking = True
        StatusMessage.set_text(self, "message-error")
        print(f"Error in {stage}:", exception)
        traceback.print_exc()


