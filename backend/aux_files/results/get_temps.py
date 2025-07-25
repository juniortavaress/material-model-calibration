# -*- coding: utf-8 -*-
import os
import re
import sys
import yaml
import json
import inspect
import traceback
from odbAccess import openOdb
sys.dont_write_bytecode = True

class GetTemps:
    """Class to process ODB files and extract temperature data."""
    def __init__(self):
        """
        Initialize the GetTemps instance, process ODB files, and extract data.
        """
        if len(sys.argv) > 1:
            self.odb_dir = sys.argv[1]
            self.json_dir = sys.argv[2]
            self.project_infos_path = sys.argv[3]
        else:
            traceback.print_exc()
            sys.exit(1)
        
        # Get and verify result directories.
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))

        # Initialize mappings for node ranges and tool nodes and process ODB files
        node_range_strs = GetTemps.initialize_data(self)
        self._process_odb_files(node_range_strs)


    def initialize_data(self):
        """
        Initializes the temperature ranges and tool node mappings.
        """
        with open(self.project_infos_path, "r") as file:
            data = yaml.safe_load(file)
        
        node_range_strs = {}
        for condition, info_condition in data["3. Conditions"].items():
            h = "h" + info_condition["Cutting Properties"]["deepCuth"]
            path = info_condition["Cutting Properties"]["tempPath"]
            node_range_strs[h] = path

        return node_range_strs


    def _process_odb_files(self, node_range_strs):
        """
        Process all ODB files in the folder.

        Args:
            node_range_strs (dict): Mappings of `h_value` to node range strings.
            spanwinkel_nodes (dict): Mappings of `gam_value` to tool node labels.
        """
        odb_files = [file for file in os.listdir(self.odb_dir) if file.endswith(".odb")]

        # Loop through each ODB file and process it
        for odb_file in odb_files:
            filename = os.path.splitext(odb_file)[0]
            odb_file_path = os.path.join(self.odb_dir, odb_file)
            output_folder = os.path.join(self.json_dir, filename)
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            output_json = os.path.join(output_folder, "temperature.json")
            
            try: 

                cond = filename.split("_")[1]
                with open(self.project_infos_path, "r") as file:
                    data_cond = yaml.safe_load(file)

                # Itera sobre as condições e verifica se o "name" é o que você deseja
                for condition, info in data_cond["3. Conditions"].items():
                    if info["Cutting Properties"]["name"] == cond:
                        h_value_key = "h{}".format(info["Cutting Properties"]["deepCuth"])
                

                # Check if extracted parameters match the predefined mappings
                if h_value_key in node_range_strs:
                    node_range_str = node_range_strs[h_value_key]
                    data = self._extract_data(filename, odb_file_path, node_range_str)
    
                # Save the data as a JSON file and 
                with open(output_json, "w") as file:
                    json.dump(data, file, indent=4)

            except Exception as e:
                traceback.print_exc()


    def _extract_data(self, filename, odb_file, node_range_str):
        """
        Extract temperature data from the ODB file.

        Args:
            odb_file (str): Path to the ODB file.
            node_range_str (str): Range string of nodes to analyze.
            tool_node_label (int): Node label for the tool.
        """
        # Open the ODB file and prepare data by extracting the step, instance, node path, and distances
        odb = openOdb(odb_file, readOnly=True)
        step, eulerian_instance_name, node_path, distances = self._prepare_odb_data(odb, node_range_str)

        if not step:
            return
        
        # Prepare the data for output
        data = {"Temperature Profile - Path (Last Frame)": (self._get_temp_profile(step.frames[-1], eulerian_instance_name, node_path, distances)),
                "Temperature Profile - Path (Max Temp at 1st Node)": (self._get_max_temp_profile(step, eulerian_instance_name, node_path, distances)),
                "Temperature Profile - Time (1st Node)": self._get_time_temp_profile(step, eulerian_instance_name, node_path[0])}

        # Close odb
        odb.close()
        return data


    @staticmethod
    def _prepare_odb_data(odb, node_range_str):
        """
        Prepare ODB data by checking the step and instance and computing distances.

        Args:
            odb (Odb): Opened ODB object.
            node_range_str (str): Node range string to analyze.

        Returns:
            tuple: Step, instance name, node path, and distances along the path.
        """
        # Get the cutting step from the ODB file
        step_names = odb.steps.keys()
        step = odb.steps[step_names[-1]]

        instance_names = odb.rootAssembly.instances 
        for key in instance_names.keys():
            if (key[:5]).lower() == "euler":
                instance_name = key

        # Check if the instance exists in the ODB file
        if instance_name not in odb.rootAssembly.instances:
            traceback.print_exc()
            return None, None, None, None

        # Get the instance, generate node path and calculate distances along the path
        instance = odb.rootAssembly.instances[instance_name]
        node_path = GetTemps.generate_node_path(node_range_str)
        distances = GetTemps.calculate_distances(instance.nodes, node_path)
        return step, instance_name, node_path, distances


    @staticmethod
    def generate_node_path(node_range_str):
        """
        Generates a list of node labels based on the node range string.

        :param node_range_str: A string defining node ranges
        :return: A list of node labels
        """
        node_ranges = node_range_str.split(', ')
        node_labels = []

        for node_range in node_ranges:
            if ':' in node_range:
                # Verarbeite Knotenbereiche
                start, end, step = map(int, node_range.split(':'))
                node_labels.extend(range(start, end + step, step))  # +step, um sicherzustellen, dass der Endknoten enthalten ist
            else:
                # Verarbeite einzelne Knotenlabels
                node_labels.append(int(node_range))   
        return node_labels
    

    @staticmethod
    def calculate_distances(nodes, node_path):
        """Calculate cumulative distances between nodes along a path."""
        coords = {node.label: node.coordinates for node in nodes}
        distances = [0.0]
        for i in range(1, len(node_path)):
            dist = sum(
                (coords[node_path[i]][j] - coords[node_path[i - 1]][j]) ** 2
                for j in range(3)
            ) ** 0.5
            distances.append(distances[-1] + dist)
        return distances
    
    
    @staticmethod
    def _get_temp_profile(frame, eulerian_instance_name, node_path, distances):
        """Extract temperature profile along the specified path."""
        if 'NT11' in frame.fieldOutputs:
            temperature_field = frame.fieldOutputs['NT11']
            
            temp_data = {}
            for value in temperature_field.values:
                if value.instance.name == eulerian_instance_name and value.nodeLabel in node_path:
                    temp_data[value.nodeLabel] = value.data  

        return [{"Node": node, "Temperature [C]": temp_data[node], "Distance [mm]": dist}
                for node, dist in zip(node_path, distances) if node in temp_data]
    
    
    @staticmethod
    def _get_max_temp_profile(step, eulerian_instance_name, node_path, distances):
        """Find the frame with the maximum temperature at the first node."""
        max_temp = -float('inf')
        max_temp_frame_index = -1
        first_node_temps = []
        
        # Iterate over frames starting from 80% of the total frames
        end_index = int(len(step.frames)) 
        start_index = int(len(step.frames)*0.8)

        for i in range(start_index, end_index):
            frame = step.frames[i]
            if 'NT11' in frame.fieldOutputs:
                temperature_field = frame.fieldOutputs['NT11']
                for value in temperature_field.values:
                    if value.instance.name == eulerian_instance_name and value.nodeLabel == node_path[0]:
                        first_node_temps.append((i, value.data)) 
                        break

        # Find the frame with the maximum temperature at the first node
        for frame_index, temp in first_node_temps:
            if temp > max_temp:
                max_temp = temp
                max_temp_frame_index = frame_index
        
        # Return the temperature profile for the frame with the maximum temperature
        return GetTemps._get_temp_profile(step.frames[max_temp_frame_index], eulerian_instance_name, node_path, distances)
    

    @staticmethod
    def _get_time_temp_profile(step, eulerian_instance_name, first_node_label):
        """Extract the temperature profile over time at the specific frame."""
        temps  = []
        for frame in step.frames:
            if 'NT11' in frame.fieldOutputs:
                temperature_field = frame.fieldOutputs['NT11']
                for value in temperature_field.values:
                    if value.instance.name == eulerian_instance_name and value.nodeLabel == first_node_label:
                        temps .append({
                            "Tempo [s]": frame.frameValue,
                            "NT11 (Temperatura) [C]": value.data
                        })
                        break
        return temps

if __name__ == "__main__":
    GetTemps()