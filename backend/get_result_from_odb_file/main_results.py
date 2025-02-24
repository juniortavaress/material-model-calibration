# -*- coding: utf-8 -*-
import os
import yaml
import shutil
import subprocess
import pandas as pd
import multiprocessing
from backend.get_result_from_odb_file.convert_json_to_excel import DataConverter
from backend.get_result_from_odb_file.convert_obj_to_excel import GetChipMeasure


class getResults():
    """
    Class to handle results extraction and conversion processes.
    """
    def result_call(self):
        """
        Calls all necessary methods to extract and convert results, and create data outputs.
        """
        getResults.manage_abaqus_script(self)
        getResults.convert_json_to_excel(self)
        getResults.create_datas(self)
        

    def manage_abaqus_script(self):
        """
        Executes Abaqus scripts to extract temperatures, forces and chip from ODB files in parallel.
        """
        global error_track
        error_track = False
        dir = os.path.dirname(os.path.abspath(__file__))

        # Define Abaqus command strings
        abaqus_command_temperatures = rf'C:\SIMULIA\Commands\abq2021.bat python {dir}\get_temps.py'
        abaqus_command_forces = rf'C:\SIMULIA\Commands\abq2021.bat python {dir}\get_forces.py'
        abaqus_command_chip_obj = rf'C:\SIMULIA\Commands\abq2021.bat cae script={dir}\get_chip_obj_file.py'
        commands = [abaqus_command_forces, abaqus_command_temperatures, abaqus_command_chip_obj]
        # commands = [abaqus_command_forces, abaqus_command_temperatures]
        commands = [abaqus_command_chip_obj]
    
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
        DataConverter.main_json_to_excel(self)
        GetChipMeasure.main_to_chip_results(self)


    def create_datas(self):
        """
        Extracts results from the simulation output files and converts them into a structured format.
        """
        for file in os.listdir(self.odb_processing):
            if file.endswith('.odb'):
                odb_inp_path = os.path.join(self.odb_processing, file)
                odb_out_file = os.path.join(self.odb_files, file)

                if not os.path.exists(self.odb_files):
                    os.makedirs(self.odb_files)
                shutil.move(odb_inp_path, odb_out_file)

                info = file.split("_int")
                condition = file.split("_int_")[0]
                param_info = f"int{info[1][:-4]}"
                iteration_number = (param_info.split("int_")[1]).split("_set_")[0]
                set_number = (param_info.split("int_")[1]).split("_set_")[1]

                df_temp_force = pd.read_excel(os.path.join(self.excel_files, "results_temp_and_forces.xlsx"), header=1)
                filtered_row = df_temp_force[df_temp_force["Filename"] == file[:-4]]
                simulated_cutting_forces = filtered_row.iloc[0,7]
                simulated_normal_forces = filtered_row.iloc[0,3]
                simulated_temperature = filtered_row.iloc[0,9]

                df_chip = pd.read_excel(os.path.join(self.excel_files, "results_chip_analysis.xlsx"), header=0)
                filtered_row = df_chip[df_chip["Filename"] == file[:-4]]
                chip_compression_ratio = filtered_row.iloc[0,5]
                chip_segmentation_ratio = filtered_row.iloc[0,6]

                yaml_path = os.path.join(self.user_config, "parameters.yaml")
                with open(yaml_path, "r", encoding="utf-8") as file:
                    data = yaml.safe_load(file)

                for iteration, values in data.items():
                    if iteration[-2:] == iteration_number:
                        for set, param_values in values.items():
                            if set[-2:] == set_number:
                                param_set = param_values["Parameters"]

                if condition[4:] in self.target_values:
                    target_cutting_force = self.target_values[condition[4:]].get("fc")
                    target_normal_force = self.target_values[condition[4:]].get("fn")
                    target_chip_compression_ratio = self.target_values[condition[4:]].get("ccr")
                    target_chip_segentatio_ratio = self.target_values[condition[4:]].get("csr")

                error_fc = abs((target_cutting_force - simulated_cutting_forces)/target_cutting_force)
                error_fn = abs((target_normal_force - simulated_normal_forces)/target_normal_force)
                error_ccr = abs((target_chip_compression_ratio - chip_compression_ratio)/target_chip_compression_ratio)
                error_csr = abs((target_chip_segentatio_ratio - chip_segmentation_ratio)/target_chip_segentatio_ratio)
                error = (0.5 * error_fc) + (0.1 * error_fn) + (0.2 * error_ccr) + (0.2 * error_csr)

                data = {"Iteration number": iteration_number, "Condition": condition[4:]}

                for key, value in param_set.items():
                    data[f"Parameter {key}"] = value

                data.update({
                    "Error": error,
                    "Experiment Cutting Force": target_cutting_force, "Simulation Cutting Force": simulated_cutting_forces, "Error Fc": error_fc,
                    "Experiment Normal Force": target_normal_force, "Simulation Normal Force": simulated_normal_forces, "Error Fn": error_fn,
                    "Experiment CCR": target_chip_compression_ratio, "Simulation CCR": chip_compression_ratio, "Error CCR": error_ccr,
                    "Experiment CSR": target_chip_segentatio_ratio, "Simulation CSR": chip_segmentation_ratio, "Error CSR": error_csr})
                

                new_info = pd.DataFrame([data])
                data_path = os.path.join(self.excel_files, "datas.xlsx")

                if os.path.exists(data_path):
                    old_df = pd.read_excel(data_path, engine="openpyxl", index_col=0)
                    new_df = pd.concat([old_df, new_info], ignore_index=True)
                else:
                    new_df = new_info

                new_df.index.name = "Simulation"
                new_df.to_excel(data_path, index=True, engine="openpyxl")
