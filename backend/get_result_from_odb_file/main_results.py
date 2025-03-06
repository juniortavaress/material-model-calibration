# -*- coding: utf-8 -*-
import os
import yaml
import shutil
import subprocess
import pandas as pd
import multiprocessing

from backend.get_result_from_odb_file.excel_manager import ExcelManager
from backend.get_result_from_odb_file.convert_json_to_excel import DataConverter
from backend.get_result_from_odb_file.convert_obj_to_excel import GetChipMeasure


class getResults():
    """
    Class to handle results extraction and conversion processes.
    """
    def __init__(self):
        getResults.result_call(self)


    def result_call(self):
        """
        Calls all necessary methods to extract and convert results, and create data outputs.
        """
        # input = ("ve se os odb tao no processing")
        ExcelManager.create_excel_results(self)
        getResults.manage_abaqus_script(self)
        getResults.convert_json_to_excel(self)
        
        

    def manage_abaqus_script(self):
        """
        Executes Abaqus scripts to extract temperatures, forces and chip from ODB files in parallel.
        """
        global error_track
        error_track = False
        dir = os.path.dirname(os.path.abspath(__file__))

        # Define Abaqus command strings
        print(self.obj_path)
        abaqus_command_temperatures = rf'C:\SIMULIA\Commands\abq2021.bat python {dir}\get_temps.py {self.odb_processing} {self.json_defaut_path}'
        abaqus_command_forces = rf'C:\SIMULIA\Commands\abq2021.bat python {dir}\get_forces.py {self.odb_processing} {self.json_defaut_path}'
        abaqus_command_chip_obj = rf'C:\SIMULIA\Commands\abq2021.bat cae script={dir}\get_chip_obj_file.py'

        # commands = [abaqus_command_forces, abaqus_command_temperatures, abaqus_command_chip_obj]
        # commands = [abaqus_command_forces, abaqus_command_temperatures]
        commands = [abaqus_command_chip_obj, abaqus_command_forces]
    
        # Start processes for each Abaqus script
        processes = []
        process_names = ["get_temps", "get_forces", "get_chip"]
        for name, command in zip(process_names, commands):
            process_name = f"Process_{name}"
            process = multiprocessing.Process(target=getResults.get_data_from_odb, args=(command, ))
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
                error_track = True
                
        except subprocess.CalledProcessError as e:
            # Log the error and set error flag
            print(f"Error executing Abaqus command: {e}")
            error_track = True


    def convert_json_to_excel(self):
        """
        Converts the generated JSON files into Excel format using the conversion script.
        """
        input("coloca os json da temp ai")

        self.chip_datas = {}
        self.force_and_temp_datas = {}

        for file in os.listdir(self.odb_processing):
            base_name_file = file[:-4]
            GetChipMeasure.main_to_chip_results(self, base_name_file)
            DataConverter.main_json_to_excel(self, base_name_file)
        ExcelManager.create_datas(self)
        







if __name__ == "__main__":
    getResults()