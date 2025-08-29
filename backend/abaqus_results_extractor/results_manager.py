# -*- coding: utf-8 -*-
import os
import sys
import ast
import yaml
import time
import shutil
import subprocess
import pandas as pd
import multiprocessing
from typing import Tuple, Optional, List
sys.dont_write_bytecode = True
from backend.abaqus_results_extractor.convert_datas_to_excel.excel_manager import ExcelManager
from backend.abaqus_results_extractor.convert_datas_to_excel.process_forces import ForceProcessor
from backend.abaqus_results_extractor.convert_datas_to_excel.process_temp import TempProcessor
from backend.abaqus_results_extractor.convert_datas_to_excel.process_chip import ChipProcessor


class GetResults():
    """
    Main class responsible for managing the process of extracting, converting, and organizing
    results from simulation files, such as forces, temperatures, and chip geometry data.
    """
    def __init__(self, otimization_manager, execution_mode: str = "embedded", project_folder: Optional[str] = None):
        """
        Initializes the GetResults object with all required paths and environment variables.
        """
        self.error_track: bool = False
        self.execution_mode = execution_mode        
        self._init_paths_standalone(project_folder) if execution_mode == "standalone" else self._init_paths_embedded(otimization_manager)
        
        os.environ.update({
            "ODB_DIRECTORY": self.odb_processing,
            "OBJ_DIRECTORY": self.obj_path,
            "LOG_DIRECTORY": self.log_files,
            "CUR_ITERATION": str(self.count_iteration)
        })


    def _init_paths_standalone(self, project_folder: str):
            self.software_folder: str = os.getcwd()
            self.excel_files: str = os.path.join(project_folder, "Outputs", "excel")
            self.log_files: str = os.path.join(project_folder, "Outputs", "log")
            self.obj_path: str = os.path.join(project_folder, "Outputs", "obj")
            self.json_default_path: str = os.path.join(project_folder, "Outputs", "json")
            self.graph_folder: str = os.path.join(project_folder, "Outputs", "chip_datas")
            self.chip_images: str = os.path.join(project_folder, "Outputs", "chip_img")
            self.odb_processing: str = os.path.join(project_folder, "Datas", "ODB")
            self.yaml_project_info: str = os.path.join(project_folder, "Datas", "info.yaml")
            self.scripts_path = os.path.join(self.software_folder, "backend", "extract_results_from_odb")
            self.wfc, self.wfn, self.wt, self.wccr, self.wcsr = 0.5, 0.1, 0.0, 0.2, 0.2
            [os.makedirs(folder, exist_ok=True) for folder in [self.excel_files, self.log_files, self.obj_path, self.json_default_path, self.graph_folder, self.chip_images]]


    def _init_paths_embedded(self, otimization_manager):
            # General Info
            self.weights = otimization_manager.weights                              # [0.5, 0.1, 0.0, 0.2, 0.2]
            self.info_set = otimization_manager.info_set
            self.count_iteration = otimization_manager.count_iteration
            self.wfc, self.wfn, self.wt, self.wccr, self.wcsr = self.weights[0], self.weights[1], self.weights[2], self.weights[3], self.weights[4]    

            # Folder Paths
            self.software_folder = otimization_manager.software_folder                 # C:\MaterialOtimization
            self.excel_files = otimization_manager.excel_files                      # C:/Users/adam-ua769pu3t3n7k4o/Pictures\TT2207\excel_files
            self.chip_images = otimization_manager.chip_images                      # C:/Users/adam-ua769pu3t3n7k4o/Pictures\TT2207\chip_images
            self.odb_processing = otimization_manager.odb_processing                # C:/Users/adam-ua769pu3t3n7k4o/Pictures\TT2207\auxiliary_files/odb_processing

            self.project_folder = otimization_manager.project_folder                    # C:\MaterialOtimization\TT2207
            self.log_files = otimization_manager.log_folder                         # C:\MaterialOtimization\TT2207\logs 
            self.user_config = otimization_manager.user_config                      # C:\MaterialOtimization\TT2207\config  
            self.graph_folder = otimization_manager.graph_folder                    # C:\MaterialOtimization\TT2207\graph_results
            self.simulation_folder = otimization_manager.simulation_folder          # C:\MaterialOtimization\TT2207\simulation_folder
            self.obj_path = otimization_manager.obj_path                            # C:\MaterialOtimization\TT2207\json_and_obj_files/objFiles
            self.json_default_path = otimization_manager.json_default_path          # C:\MaterialOtimization\TT2207\json_and_obj_files/jsonFiles
            self.yaml_parameters = otimization_manager.yaml_parameters          # C:\MaterialOtimization\TT2207\json_and_obj_files/jsonFiles
            
            self.abaqus_path = otimization_manager.abaqus_path

            # Yaml and Others Files Paths
            self.yaml_project_info = otimization_manager.yaml_project_info        # C:\MaterialOtimization\TT2207\info.yaml
            # self.scripts_path = os.path.join(os.getcwd(), "backend", "abaqus_results_extractor", "extract_results_from_odb")   
            self.scripts_path = otimization_manager.scripts_path
            

    def result_call(self, otimization_manager, forces: bool, temperature: bool, chip: bool, current_iteration: str) -> Tuple[Optional[dict], Optional[dict], Optional[dict]]:
        """
        Triggers the full workflow of running the scripts and converting results to Excel.

        Args:
            forces (bool): Whether to process forces.
            temperature (bool): Whether to process temperature.
            chip (bool): Whether to process chip geometry.

        Returns:
            Tuple containing force, temperature, and chip summaries respectively.
        """
        ExcelManager.create_excel_results(self, forces, temperature, chip)

        self._run_abaqus_scripts(forces, temperature, chip)

        while True:
            # Verifica se o diretório está vazio
            if not os.listdir(self.obj_path):
                print("Diretório está vazio. Aguardando...")
                self._run_abaqus_scripts(forces, temperature, chip)
                time.sleep(10)  # Espera 1 segundo antes de checar novamente
            else:
                print("Diretório não está mais vazio. Encerrando loop.")
                break

        self._clean_directory("end")
        self._convert_json_to_excel(otimization_manager, forces, temperature, chip)

        if self.execution_mode == "embedded":
            error_list = []
            self._transfer_odb_files()
            df = pd.read_excel(os.path.join(self.excel_files, "datas.xlsx"))
            error_list = self._calculate_errors_from_results(df, current_iteration, error_list)
            
            with open(os.path.join(self.user_config, "parameters.yaml"), "w") as file:
                yaml.dump(self.info_set, file)
            return self.info_set, error_list
        

    def _run_abaqus_scripts(self, forces: bool, temperature: bool, chip: bool) -> None:
        """
        Executes Abaqus scripts in parallel to extract simulation data.

        Args:
            forces (bool): Whether to extract force data.
            temperature (bool): Whether to extract temperature data.
            chip (bool): Whether to extract chip geometry.

        Side Effects:
            Updates self.error_track if any subprocess reports an error.
        """
        process_names, commands = [], []
  
        # Define Abaqus command strings
        # abaqus_cmd = os.path.join("C:", os.sep, "SIMULIA", "Commands", "abq2021.bat")
        if forces:
            process_names.append("get_forces")
            script_path = os.path.join(self.scripts_path, "get_forces.py")
            abaqus_command_forces = rf'{self.abaqus_path} python {script_path} {self.odb_processing} {self.json_default_path} {self.count_iteration}'
            commands.append(abaqus_command_forces)

        if temperature:
            process_names.append("get_temp")
            script_path = os.path.join(self.scripts_path, "get_temps.py")
            abaqus_command_temperatures = rf'{self.abaqus_path} python {script_path} {self.odb_processing} {self.json_default_path} {self.count_iteration} {self.yaml_project_info}'
            commands.append(abaqus_command_temperatures)

        if chip:
            process_names.append("get_chip")
            script_path = os.path.join(self.scripts_path, "get_chip_obj_file.py")
            abaqus_command_chip_obj = rf'{self.abaqus_path} cae script={script_path}'
            commands.append(abaqus_command_chip_obj)
        
        # Start processes for each Abaqus script
        queues = []
        processes = []
        
        print("commands", commands)

        for name, command in zip(process_names, commands):
            process_name = f"Process_{name}"
            queue = multiprocessing.Queue()
            process = multiprocessing.Process(target=self.get_data_from_odb, args=(command, queue))
            process.name = process_name
            processes.append(process)
            queues.append(queue)
            process.start()

        # Wait for all processes to finish
        for process in processes:
            process.join()
        self.error_track = any(q.get() for q in queues)


    def get_data_from_odb(self, abaqus_command: str, queue: multiprocessing.Queue) -> None:
        """
        Executes an Abaqus subprocess command and puts the result status into a queue.

        Args:
            abaqus_command (str): The command string to be executed.
            queue (multiprocessing.Queue): Queue to communicate success/failure to parent process.
        """
        try:
            queue.put(False)
            result = subprocess.run(abaqus_command, shell=True, capture_output=True, check=True, text=True)
            if "Error" in result.stdout or "Error" in result.stderr:
                queue.put(True)
                
        except subprocess.CalledProcessError as e:
            queue.put(True)

 
    def _convert_json_to_excel(self, otimization_manager, forces: bool, temperature: bool, chip: bool) -> Tuple[Optional[dict], Optional[dict], Optional[dict]]:
        """
        Processes JSON and OBJ outputs and compiles them into an Excel report.

        Args:
            forces (bool): Process force data if True.
            temperature (bool): Process temperature data if True.
            chip (bool): Process chip data if True.

        Returns:
            Tuple: (forces_summary, temperature_summary, chip_summary)
        """
        self.chip_datas = {}
        self.force_and_temp_datas = {}
        forces_summary, temperature_summary, chip_summary = None, None, None

        processor01 = ForceProcessor(self.json_default_path, self.graph_folder)
        processor02 = TempProcessor(self.json_default_path, self.graph_folder)
        processor03 = ChipProcessor(self.obj_path, self.graph_folder, self.yaml_project_info, self.chip_images, self.count_iteration)

        for file in os.listdir(self.odb_processing):
            if f"it_{str(self.count_iteration).zfill(2)}" in file:
                base_name_file = file[:-4]
                otimization_manager.ui.combobox_file.addItems([base_name_file])
                if forces:
                    forces_summary = processor01.process_file(base_name_file, exp_width = 4.0, sim_width = 0.02, start_pct = 0.25, end_pct = 1.00)
                    
                if temperature:
                    temperature_summary = processor02.process_file(base_name_file, temperature_threshold = 60)

                if chip:
                    chip_summary = processor03.process_file(base_name_file)

                ExcelManager.create_datas(self, base_name_file, forces_summary, temperature_summary, chip_summary)

        
        return forces_summary, temperature_summary, chip_summary
            

    @staticmethod
    def _clean_directory(stage: str = "start") -> None:
        """
        Removes files from the current working directory whose filenames contain
        any of the specified keywords.

        The keywords to look for are "acis" and "rpy". Only files (not directories)
        matching these keywords will be deleted.

        Prints the name of each removed file or an error message if removal fails.
        """
        if stage == "end":
            key_words_to_delete = ["acis", "rpy", "pyc"]
            for file_name in os.listdir(os.getcwd()):
                file_path = os.path.join(os.getcwd(), file_name)
                if os.path.isfile(file_path) and any(keyword in file_name for keyword in key_words_to_delete):
                    try:
                        os.remove(file_path)
                    except Exception as e:
                        pass


    def _calculate_errors_from_results(self, df, current_iteration, error_list):
        """
        Match parameter sets with simulation results and compute errors.

        Args:
            df (pd.DataFrame): DataFrame with simulation results.
            iteration (str): Current iteration to process.

        Returns:
            List[float]: List of error values.
        """
        for iteration, info in self.info_set.items():
            if iteration == current_iteration:
                for set_name, data in info.items():
                    param_values = ast.literal_eval(data["Parameters Map"])                     
                    param_columns = df.columns[4:4+len(param_values)]

                    filter_conditions = [] 
                    for i, value in enumerate(param_values): 
                        filter_conditions.append(df[param_columns[i]] == value)  

                    filtered_row = df[filter_conditions[0]] 
                    for condition in filter_conditions[1:]:  
                        filtered_row = filtered_row.loc[condition]
                    
                    errors = filtered_row["Error"]
                    if errors.isnull().any():
                        self.info_set[current_iteration][set_name]["Error"] = "1"
                    else:
                        self.info_set[current_iteration][set_name]["Error"] = str(errors.mean())

        for iteration, info in self.info_set.items():
            if iteration == current_iteration:
                for set_name, data in info.items():
                    error_list.append(float(data["Error"]))
        return error_list
    

    def _transfer_odb_files(self):
        """
        Transfers .odb files from the simulation directory to the results directory.
        """
        for file in os.listdir(self.odb_processing):
            src_path = os.path.join(self.odb_processing, file)
            dst_dir = os.path.join(self.simulation_folder, file[:-4])
            os.makedirs(dst_dir, exist_ok=True)
            dst_path = os.path.join(dst_dir, file)
            shutil.copy2(src_path, dst_path)
            os.remove(src_path)



# if __name__ == "__main__":
#     # Initialize and run processing
#     GetResults._clean_directory()
#     processor = GetResults(execution_mode = "standalone")
#     forces_summary, temperature_summary, chip_summary = processor.result_call(forces = True, temperature = False, chip = True)



        
