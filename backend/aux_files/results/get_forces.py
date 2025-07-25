# -*- coding: utf-8 -*-
import os
import sys
import inspect
import json
import traceback
from odbAccess import openOdb

class GetForces():
    """
    A class to handle processing of ODB files and extracting reaction force data.
    """
    def __init__(self):
        """
        Initialize the GetForces instance, process ODB files, and extract data.
        """
        if len(sys.argv) > 1:
            self.odb_dir = sys.argv[1]
            self.json_dir = sys.argv[2]
        else:
            traceback.print_exc()
            sys.exit(1)
        
        # Get and verify result directories.
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))

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

            except Exception as e:
                traceback.print_exc()


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

        region_name = None
        for region in sets_and_nodes:
            if 'tool' in region.lower():  # Verifica se 'tool' está no nome da região
                region_name = region
                break

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