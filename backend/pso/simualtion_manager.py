import os
import yaml
import shutil
import traceback
import numpy as np
from backend.pso.edit_input_file import InpEditor
from frontend.aux_files.show_status_message import StatusMessage
from backend.get_result_from_odb_file.main_results import getResults


class SimulationManager:
    def __init__(self):
        print("SimulationManager")

    def simulation_manager(self):
        """
        Manages the simulation workflow: editing input files, running simulations,
        transferring output files, and collecting results.
        """
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
            try:
                splits = np.array_split(lis_dir_inp, self.number_of_cp)
                
                if self.main_computer == "Yes":
                    computer_dict = {f"Computer {i+1}": {"status": bool(split.tolist()), "files": split.tolist()} for i, split in enumerate(splits)}
                else:
                    computer_dict = {f"Computer {i+2}": {"status": bool(split.tolist()), "files": split.tolist()} for i, split in enumerate(splits)}

                with open(os.path.join(self.python_files, "computers_list.yaml"), "w") as file:
                    yaml.dump(computer_dict, file)
                
            except Exception as e:
                SimulationManager.except_function(self, e, "Creating list for computers")

        # Step 4: Run the simulation
        if not self.error_tracking and self.main_computer == "Yes":
            try:
                StatusMessage.set_text(self, "message-id_03")
                if computer_dict["Computer 1"]["status"] == True:
                    SimulationManager.run_simulation(self, "cp1", computer_dict["Computer 1"]["files"])
            except Exception as e:
                SimulationManager.except_function(self, e, "Rodando Simulação")


        while True:
            yaml_path = os.path.join(self.python_files, "computers_list.yaml")
            with open(yaml_path, "r") as file:
                data = yaml.safe_load(file)

            all_finished = True
            for computers, infos in data.items():
                for info_type, value in infos.items():
                    if info_type == "status":
                        if value:
                            all_finished = False  
            if all_finished:
                break
            else:
                import time
                time.sleep(5)

        # Step 5: Collect simulation results
        if not self.error_tracking:
            try:    
                StatusMessage.set_text(self, "message-id_04")
                getResults.result_call(self)
            except Exception as e:
                SimulationManager.except_function(self, e, "Collecting results")


        # if not self.error_tracking:
        #     try:    
        #         SimulationManager.copy_file(self, "ODB")
        #     except Exception as e:
        #         SimulationManager.except_function(self, e, "Moving ODB")
        

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


    def run_simulation(self, id, path_list_to_inp_folders):
        """
        Starts the Abaqus simulation using a parallel processing framework.
        """
        from backend.pso.pararel_simulation import PararelSimulation
        number_of_cores = 4
        drive_folder = self.user_result_folder
        self.server_folder = os.path.join(os.getenv("SystemDrive", "C:") , f"\MaterialOtimization\{self.project_name}\simulation_folder")
        PararelSimulation.start_simulation(self, id, path_list_to_inp_folders, self.server_folder, drive_folder, number_of_cores)
       

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


