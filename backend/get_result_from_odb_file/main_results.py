# -*- coding: utf-8 -*-
import os
import yaml
import subprocess
import multiprocessing

from backend.get_result_from_odb_file.excel_manager import ExcelManager
from backend.get_result_from_odb_file.convert_json_to_excel import DataConverter
from backend.get_result_from_odb_file.convert_obj_to_excel import GetChipMeasure


class GetResults():
    """
    Class to handle results extraction and conversion processes.
    """
    def __init__(self):
        GetResults.result_call(self)


    def result_call(self):
        """
        Calls all necessary methods to extract and convert results, and create data outputs.
        """
        # a = input("ve se os odb tao no processing")
        ExcelManager.create_excel_results(self)
        GetResults.manage_abaqus_script(self)
        GetResults.convert_json_to_excel(self)
        ExcelManager.create_datas(self)
        

    def manage_abaqus_script(self):
        """
        Executes Abaqus scripts to extract temperatures, forces and chip from ODB files in parallel.
        """
        global error_track
        error_track = False

        # Defining Paths to Chip Analysis
        GetResults.create_path_to_chip_analysis(self)
   
        # Define Abaqus command strings
        # abaqus_command_temperatures = rf'C:\SIMULIA\Commands\abq2021.bat python {self.software_path}\extract_results\get_temps.py {self.odb_processing} {self.json_defaut_path} {self.project_infos_path}'
        abaqus_command_forces = rf'C:\SIMULIA\Commands\abq2021.bat python {self.software_path}\extract_results\get_forces.py {self.odb_processing} {self.json_defaut_path}'
        abaqus_command_chip_obj = rf'C:\SIMULIA\Commands\abq2021.bat cae script={self.software_path}\extract_results\get_chip_obj_file.py'

        with open(self.project_infos_path, "r") as file:
            data = yaml.safe_load(file)
        
        first_condition = next(iter(data["3. Conditions"].values()))
        path = first_condition["Cutting Properties"]["tempPath"]
        
        # if path:
        #     process_names = ["get_forces", "get_temps", "get_chip"]
        #     commands = [abaqus_command_forces, abaqus_command_temperatures, abaqus_command_chip_obj]
        # else:
        
        process_names = ["get_forces", "get_chip"]
        commands = [abaqus_command_chip_obj, abaqus_command_forces]
    
        # print('VERIFICA OS COMANDO AI MEU QUERIDO', commands)

        # Start processes for each Abaqus script
        processes = []
        # print('process_names', process_names)
        
        for name, command in zip(process_names, commands):
            process_name = f"Process_{name}"
            process = multiprocessing.Process(target=GetResults.get_data_from_odb, args=(command, ))
            process.name = process_name
            processes.append(process)
            process.start()

        # Wait for all processes to finish
        for process in processes:
            process.join()

        # Track any errors that occurred
        self.error_tracking = error_track


    def get_data_from_odb(abaqus_command):
        """
        Executes an Abaqus command to extract data from an ODB file.
        """
        try:
            result = subprocess.run(abaqus_command, shell=True, capture_output=True, check=True, text=True)
            if "Error" in result.stdout or "Error" in result.stderr:
                print("ERROR", result.stdout)
                print("ERROR", result.stderr)
                error_track = True
                
        except subprocess.CalledProcessError as e:
            print(f"Error executing Abaqus command: {e}")
            error_track = True


    def convert_json_to_excel(self):
        """
        Converts the generated JSON files into Excel format using the conversion script.
        """
        # input("TEMP:")

        self.chip_datas = {}
        self.force_and_temp_datas = {}

        for file in os.listdir(self.odb_processing):
            base_name_file = file[:-4]
            GetChipMeasure.main_to_chip_results(self, base_name_file)
            DataConverter.main_json_to_excel(self, base_name_file)
            self.ui.combobox_file.addItems([base_name_file])
        
        

    def create_path_to_chip_analysis(self):
        if os.path.exists(self.software_config_path):
            with open(self.software_config_path, "r", encoding="utf-8") as file:
                existing_data = yaml.safe_load(file) or {}

        existing_data.update({"odb_processing": self.odb_processing, "obj_path": self.obj_path})
        with open(self.software_config_path, "w", encoding="utf-8") as file:
            yaml.dump(existing_data, file, default_flow_style=False, allow_unicode=True, width=float("inf"))


if __name__ == "__main__":
    GetResults()
