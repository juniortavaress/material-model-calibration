# -*- coding: utf-8 -*-
import os
import sys
import yaml
import json
import traceback
import argparse
from odbAccess import openOdb


class GetTemps():
    """
    Class to process ODB files and extract temperature data.
    """

    def __init__(self, log_file, odb_dir, json_dir, current_iteration, yaml_project_info):
        """
        Initialize the TemperatureExtractor class.

        Args:
            log_file (str): Path to the log file.
            odb_dir (str): Directory containing ODB files.
            json_dir (str): Directory to save extracted JSON files.
            project_info_path (str): Path to the project information YAML file.
        """
        self.log_file = log_file
        self.odb_dir = odb_dir
        self.json_dir = json_dir
        self.yaml_project_info = yaml_project_info

        self._log("=== Processing Files ===")
        node_range_strs = self._load_project_node_ranges()
        self._process_odb_files(current_iteration, node_range_strs)


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
        parser.add_argument("yaml_project_info", help="Diretório com as informacoes do projeto")

        args = parser.parse_args()
        with open(log_file, "w") as f:
            f.write("=== Forces Extraction Log ===\n")
            f.write("ODB path: {}\n".format(args.odb_dir))
            f.write("JSON path: {}\n".format(args.json_dir))
            f.write("Projetct path: {}\n\n".format(args.yaml_project_info))
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


    def _load_project_node_ranges(self):
        """
        Initializes the temperature ranges and tool node mappings.
        """
        with open(self.yaml_project_info, "r") as file:
            data = yaml.safe_load(file)
        
        node_map  = {}
        for _, info_condition in data["05. Conditions"].items():
            if isinstance(info_condition, dict):
                h = "h" + info_condition["Cutting Properties"]["deepCuth"]
                path = info_condition["Cutting Properties"]["tempPath"]
                node_map [h] = path

        self._log("Extracted Node Range Map: {}".format(node_map))
        return node_map 


    def _process_odb_files(self, current_iteration, node_range_strs):
        """
        Process all ODB files in the specified directory.

        Args:
            node_range_map (dict): Node path mapping per cutting depth.
        """
        # Step 1: List all ODB files in the directory
        try:
            iteration_str = "it_" + str(current_iteration).zfill(2)
            odb_files = [file for file in os.listdir(self.odb_dir) if file.endswith(".odb") and iteration_str in file]

            # odb_files = [file for file in os.listdir(self.odb_dir) if file.endswith(".odb") and f"it_{str(current_iteration).zfill(2)}" in file]
            
            if not odb_files:
                self._log("No ODB files found in directory: {}".format(self.odb_dir))
                return
        except Exception as e:
                self._log("Failed to list ODB files: {}".format(str(e)), level="error")
                self._log(traceback.format_exc(), level="error")
                return

        # Step 2: Process each ODB file
        for odb_file in odb_files:
            filename = os.path.splitext(odb_file)[0]
            odb_file_path = os.path.join(self.odb_dir, odb_file)
            output_folder = os.path.join(self.json_dir, filename)
            output_json_path = os.path.join(output_folder, "temperature.json")

            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            
            # Step 3: Open the ODB 
            try: 
                cond = filename.split("_")[1]
                with open(self.yaml_project_info, "r") as file:
                    data_cond = yaml.safe_load(file)

                # Itera sobre as condições e verifica se o "name" é o que você deseja
                
                for _, condition  in data_cond["05. Conditions"].items():
                    if condition ["Cutting Properties"]["name"] == cond:
                        h_value_key = "h{}".format(condition ["Cutting Properties"]["deepCuth"])

                # Check if extracted parameters match the predefined mappings
                if h_value_key in node_range_strs:
                    node_range_str = node_range_strs[h_value_key]
                    data = self._extract_data(odb_file_path, node_range_str)
    
                    self._log("TERMINOU")
                    
                # Save the data as a JSON file and 
                with open(output_json_path, "w") as file:
                    json.dump(data, file, indent=4)

            except Exception as e:
                pass
                # traceback.print_exc()


    def _extract_data(self, odb_file, node_range_str):
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
            # traceback.print_exc()
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
    try:
        log_directory = os.getenv("LOG_DIRECTORY", ".")
        log_file = os.path.join(log_directory, "debug_temp.txt")
        args = GetTemps._parse_arguments(log_file)
        GetTemps(log_file, args.odb_dir, args.json_dir, args.cur_iteration, args.yaml_project_info)
    except Exception as e:
        sys.exit(1)
