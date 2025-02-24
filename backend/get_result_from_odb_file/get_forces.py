# -*- coding: utf-8 -*-
import os
import sys
import inspect
import json
from odbAccess import openOdb

class GetForces():
    """
    A class to handle processing of ODB files and extracting reaction force data.
    """
    def __init__(self):
        """
        Initialize the GetForces instance, process ODB files, and extract data.
        """
        # Get and verify result directories.
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))
        self.odb_dir = r"S:/Junior/abaqus-with-python/otimization-scripts/new-version/material-model-calibration\Teste\auxiliary_files\odb_processing"
        self.json_dir = r"S:/Junior/abaqus-with-python/otimization-scripts/new-version/material-model-calibration\Teste\auxiliary_files\defaut/jsonFiles"       

        # Process ODB files
        self._process_odb_files()

    
    def _process_odb_files(self):
        """
        Process all ODB files in the folder.
        """
        odb_files = [file for file in os.listdir(self.odb_dir) if file.endswith(".odb")]

        # Loop through each ODB file and process it
        for odb_file in odb_files:
            filename = os.path.splitext(odb_file)[0]
            odb_file_path = os.path.join(self.odb_dir, odb_file)
            output_folder = os.path.join(self.json_dir, filename)
            output_json_path = os.path.join(output_folder, "reaction_forces.json")

            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            try:
                odb = openOdb(odb_file_path, readOnly=True)
                # Extract reaction force data from the ODB file
                history_outputs = self.extract_reaction_force_data(odb)
                odb.close()

                # Save the extracted data as a JSON file
                with open(output_json_path, "w") as file:
                    json.dump(history_outputs, file, indent=4)
                # print("Data from forces were successfully saved to {}".format(output_json_path))

            except Exception as e:
                print("Error processing file {0}: {1}".format(filename, e))


    def extract_reaction_force_data(self, odb):
        """
        Extracts reaction force data from the ODB file.

        Args:
            odb (Odb): The Abaqus ODB file object.

        Returns:
            dict: A dictionary containing the reaction force data for each output in the specified region.
        """
        # Access the 'Cutting Step' in the ODB file
        step_names = odb.steps.keys()
        step = odb.steps[step_names[-1]]
        history_outputs = {}

        # Get the available history regions from the step
        sets_and_nodes = step.historyRegions.keys()

        # Select the last region as the region of interest (e.g., a node or part)
        region_name = sets_and_nodes[-1]
        region = step.historyRegions[region_name]

        # Iterate through the available history outputs in the selected region
        for output_name in region.historyOutputs.keys():
            data = region.historyOutputs[output_name].data
            history_outputs[output_name] = data  # Store the data for each output
        return history_outputs
    

if __name__ == "__main__":
    GetForces()