# -*- coding: utf-8 -*-
import os
import sys
import json
import traceback
import argparse
from odbAccess import openOdb

class GetForces():
    """
    Class to process ODB files and extract reaction force data.

    This class opens Abaqus ODB files, extracts reaction force history data,
    saves the results in JSON files, and logs the processing steps.
    """

    def __init__(self, log_file, odb_dir, json_dir, current_iteration):
        """
        Initializes the instance and starts processing the ODB files.

        Args:
            log_file (str): Path to the log file.
            odb_dir (str): Directory containing the ODB files to process.
            json_dir (str): Directory to save the extracted JSON files.
        """
        self.log_file = log_file
        self.odb_dir = odb_dir
        self.json_dir = json_dir

        self._log("=== Processing Files ===")
        self._process_odb(current_iteration)


    @staticmethod
    def _parse_arguments(log_file):
        """
        Parses command line arguments.

        Args:
            log_file (str): Path to the log file to record the parsed arguments.

        Returns:
            argparse.Namespace: Object containing 'odb_dir' and 'json_dir' arguments.
        """
        parser = argparse.ArgumentParser(description="Extrai forças de reação de arquivos ODB.")
        parser.add_argument("odb_dir", help="Diretório com arquivos .odb")
        parser.add_argument("json_dir", help="Diretório para salvar os JSONs extraídos")
        parser.add_argument("cur_iteration", help="Iteracao atual")

        args = parser.parse_args()
        with open(log_file, "w") as f:
            f.write("=== Forces Extraction Log ===\n")
            f.write("ODB path: {}\n".format(args.odb_dir))
            f.write("JSON path: {}\n\n".format(args.json_dir))
        return args
    

    def _log(self, message, level = None):
        """
        Appends a message to the log file with optional severity.

        Args:
            message (str): Log message.
            level (str): Optional log level ('info' or 'error').
        """
        prefix = "[ERROR] " if level == "error" else ""
        with open(self.log_file, "a") as f:
            f.write(prefix + message + "\n")


    def _process_odb(self, current_iteration):
        """
        Processes all ODB files in the specified directory, extracting data
        and saving the results as JSON files.
        """
        # Step 1: List all ODB files in the directory
        try:
            iteration_str = "it_" + str(current_iteration).zfill(2)
            odb_files = [file for file in os.listdir(self.odb_dir) if file.endswith(".odb") and iteration_str in file]
            # odb_files = [file for file in os.listdir(self.odb_dir) if file.endswith(".odb") and f"it_{str(current_iteration).zfill(2)}" in file]
            
            if not odb_files:
                self._log("No ODB files found in directory: " + self.odb_dir, level="info")
                return

        except Exception as e:
                self._log("Failed to list files in" + self.odb_dir + ":" + str(e), level="error")
                self._log(traceback.format_exc(), level="error")
                return
        
        # Step 2: Process each ODB file
        for i, odb_file in enumerate(odb_files):
            self._log(("\n" if i > 0 else "") + "File: " + odb_file)
            filename = os.path.splitext(odb_file)[0]
            odb_file_path = os.path.join(self.odb_dir, odb_file)
            output_folder = os.path.join(self.json_dir, filename)
            output_json_path = os.path.join(output_folder, "reaction_forces.json")

            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            # Step 3: Open the ODB 
            try:
                odb = openOdb(odb_file_path, readOnly=True)
                
                # Step 4: Extract forces
                history_outputs = self.extract_reaction_force_data(odb)
                odb.close()

                # Step 5: Save the extracted data as a JSON file
                with open(output_json_path, "w") as file:
                    self._log(" Saved OBJ: " + filename)
                    json.dump(history_outputs, file, indent=4)

            except Exception as e:
                self._log("Error processing " + odb_file + ": " + str(e), level="error")


    def extract_reaction_force_data(self, odb):
        """
        Extracts reaction force data from the given ODB file.

        Args:
            odb (Odb): Opened Abaqus ODB file object.

        Returns:
            dict: Dictionary containing reaction force data for each output in the specified region.
        """
        # Access the 'Cutting Step' in the ODB file
        step_names = odb.steps.keys()
        step = odb.steps[step_names[-1]]
        history_outputs = {}

        # Get the available history regions from the step
        sets_and_nodes = step.historyRegions.keys()

        """ 
        When creating the part, it must have 'Tool' in the name 
        """
        region_name = None
        for region in sets_and_nodes:
            if 'tool' in region.lower(): 
                region_name = region
                break
        self._log(" Extract Region Name: " + region_name)

        region = step.historyRegions[region_name]
        # Iterate through the available history outputs in the selected region
        for output_name in region.historyOutputs.keys():
            data = region.historyOutputs[output_name].data
            history_outputs[output_name] = data  
        return history_outputs
    

if __name__ == "__main__":
    try:
        log_directory = os.getenv("LOG_DIRECTORY", ".")
        log_file = os.path.join(log_directory, "debug_forces.txt")
        args = GetForces._parse_arguments(log_file)
        GetForces(log_file, args.odb_dir, args.json_dir, args.cur_iteration)
    except Exception as e:
        sys.exit(1)


        