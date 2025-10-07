# -*- coding: utf-8 -*-
import os
import sys
import json
import traceback
from odbAccess import openOdb

class ReactionForceExtractor:
    """
    Extracts reaction force data from Abaqus ODB files and saves it as JSON.

    This class opens an Abaqus ODB file, locates the appropriate history region,
    extracts force data, and logs the process.
    """
    def __init__(self):
        """
        Initializes the extractor and starts the processing pipeline.

        Args:
            log_file (str): Path to the log file.
            json_dir (str): Directory to save the extracted JSON files.
            odb_file (str): Path to the Abaqus ODB file.
        """
        self.json_dir = os.getenv("JSON_DIRECTORY", ".")
        self.odb_file = os.getenv("ODB_FILE", "")
        self.log_file = os.path.join(os.getenv("LOG_DIRECTORY", "."), "debug_forces.txt")

        self._log("=== Starting Reaction Force Extraction ===")
        self._process_odb_file()
   

    def _log(self, message, level=None):
        """
        Writes a message to the log file.

        Args:
            message (str): Message to log.
            level (str, optional): Log level ('error' or None).
        """
        prefix = "[ERROR] " if level == "error" else ""
        with open(self.log_file, "a") as f:
            f.write(prefix + message + "\n")


    def _process_odb_file(self):
        """
        Processes all ODB files in the specified directory, extracting data
        and saving the results as JSON files.
        """
        filename = os.path.splitext(os.path.basename(self.odb_file))[0]
        output_folder = os.path.join(self.json_dir, filename)
        output_json_path = os.path.join(output_folder, "reaction_forces.json")

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        try:
            odb = openOdb(self.odb_file, readOnly=True)
            force_data  = self.extract_reaction_force_data(odb)
            odb.close()
            
            with open(output_json_path, "w") as json_file:
                self._log(" Saved OBJ: " + filename)
                json.dump(force_data , json_file, indent=4)

        except Exception as e:
            self._log("Error processing " + self.odb_file + ": " + str(e), level="error")
            self._log(traceback.format_exc(), level="error")


    def extract_reaction_force_data(self, odb):
        """
        Extracts reaction force history data from the ODB file.

        Args:
            odb (Odb): Opened Abaqus ODB file object.

        Returns:
            dict: Dictionary of history output data.
        """
        self._log("extract_reaction_force_data ")
        
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
        ReactionForceExtractor()
        sys.exit()
    except Exception as e:
        sys.exit(1)



        
        