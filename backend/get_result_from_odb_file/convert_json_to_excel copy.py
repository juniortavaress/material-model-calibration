# -*- coding: utf-8 -*-
import os 
import json
import pandas as pd
import numpy as np
# from backend.get_result_from_odb_file.excel_utils import ExcelUtils

class DataConverter():
    def __init__(self):
        self.excel_files = r"S:/Junior/abaqus-with-python/otimization-scripts/new-version/material-model-calibration\Teste\excel_files"
        self.json_defaut_path = r"S:/Junior/abaqus-with-python/otimization-scripts/new-version/material-model-calibration\Teste\auxiliary_files\json_and_obj_files/jsonFiles"

        DataConverter.main_json_to_excel(self)
        

    def main_json_to_excel(self):
        """
        Main function to process JSON files and generate an Excel file with results.
        """
        excel_output_file = os.path.join(self.excel_files, "results_temp_and_forces.xlsx")

        # Constants
        WORKPIECE_WIDTH_EXPERIMENT = 4
        WORKPIECE_WIDTH_SIMULATION = 0.02
        START_PERCENT = 0.25
        END_PERCENT = 1.00
        TEMPERATURE_THRESHOLD = 60

        DataConverter.process_json_to_excel(self.json_defaut_path, excel_output_file, START_PERCENT, END_PERCENT, WORKPIECE_WIDTH_EXPERIMENT, WORKPIECE_WIDTH_SIMULATION, TEMPERATURE_THRESHOLD)


    @staticmethod
    def process_json_to_excel(folder_path, output_file, start_percent, end_percent, workpiece_width_experiment, workpiece_width_simulation, temperature_threshold):
        """
        Process all JSON files in a folder and save combined data and statistics to an Excel file.

        Args:
            folder_path (str): Path to the folder containing JSON files.
            output_file (str): Path to the output Excel file.
            start_percent (float): Start percentage of the data range.
            end_percent (float): End percentage of the data range.
            workpiece_width_experiment (float): Width of the workpiece used in the experiment.
            workpiece_width_simulation (float): Width of the simulated workpiece.
            temperature_threshold (float): Temperature threshold for calculations.
        """        
        stats_list = []
        # try:
        with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
            stats_df = pd.DataFrame(stats_list)
            stats_df.to_excel(writer, sheet_name="Evaluation Statistics", index=False, startrow=2, header=False)
            stats_sheet = writer.sheets["Evaluation Statistics"]
            
            for folder in os.listdir(folder_path):
                folder_full_path = os.path.join(folder_path, folder)
                if os.path.isdir(folder_full_path):
                    for filename in os.listdir(folder_full_path):
                        if filename == 'reaction_forces.json':
                            json_file_path_forces = os.path.join(folder_full_path, filename)
                        elif filename == 'temperature.json':
                            json_file_path_temp = os.path.join(folder_full_path, filename)
                        else: 
                            pass
                # DataConverter.json_to_combined_excel(writer, stats_list, start_percent, end_percent, workpiece_width_experiment, workpiece_width_simulation, temperature_threshold, json_file_path_forces, json_file_path_temp)
            
                # stats_df = pd.DataFrame(stats_list)
                # stats_df.to_excel(writer, sheet_name="Evaluation Statistics", index=False, startrow=2, header=False)
                # ExcelUtils.format_statistics_sheet_xlsxwriter(stats_sheet, writer.book, temperature_threshold, start_percent, end_percent)




    @staticmethod
    def json_to_combined_excel(writer, stats_list, start_percent, end_percent, workpiece_width_experiment, workpiece_width_simulation, temperature_threshold, json_file_path_forces = None, json_file_path_temp = None):
        """
        Function to process a JSON file and save data into an Excel sheet

        Args:
            json_file (str): Path to the JSON file.
            writer (pandas.ExcelWriter): Excel writer object to save the data.
            stats_list (list): List to store calculated statistics.
            start_percent (float): Start percentage of the data range for statistics.
            end_percent (float): End percentage of the data range for statistics.
            workpiece_width_experiment (float): Width of the workpiece used in the experiment.
            workpiece_width_simulation (float): Width of the simulated workpiece.
            temperature_threshold (float): Temperature threshold for additional calculations.
        """
        try:
            if json_file_path_forces:
                with open(json_file_path_forces, 'r') as file:
                    data = json.load(file)

                combined_forces_df_with_results = DataConverter.combine_forces_data(data, workpiece_width_experiment, workpiece_width_simulation)
                forces_stats = DataConverter.calculate_forces_statistics(combined_forces_df_with_results, start_percent, end_percent)
            else:
                forces_stats = {}

            if json_file_path_temp:
                with open(json_file_path_temp, 'r') as file:
                    data = json.load(file)

                combined_temp_df_with_results = DataConverter.combine_temp_data(data)
                temp_stats = DataConverter.calculate_temp_statistics(combined_temp_df_with_results, temperature_threshold)
            else:
                temp_stats = {}

            combined_df = pd.merge(combined_forces_df_with_results, combined_temp_df_with_results, how="outer", on="Dummy")
            combined_df.drop(columns=["Dummy"], inplace=True)
            file_name = os.path.basename(os.path.dirname(json_file_path_forces))
            sheet_name = os.path.basename(os.path.dirname(json_file_path_forces))[:31]
            combined_df.to_excel(writer, sheet_name=sheet_name, index=False)

            # Flatten stats dictionary for easy insertion into the stats list
            stats_flat = {
                "Filename": file_name,
                "Normal Force [N].min": round(forces_stats["Cutting Normal Force FcN [N]"]["min"], 2),
                "Normal Force [N].max": round(forces_stats["Cutting Normal Force FcN [N]"]["max"], 2),
                "Normal Force [N].mean": round(forces_stats["Cutting Normal Force FcN [N]"]["mean"], 2),
                "Normal Force [N].std": round(forces_stats["Cutting Normal Force FcN [N]"]["std"], 2),
                "Cutting Force [N].min": round(forces_stats["Cutting Force Fc [N]"]["min"], 2),
                "Cutting Force [N].max": round(forces_stats["Cutting Force Fc [N]"]["max"], 2),
                "Cutting Force [N].mean": round(forces_stats["Cutting Force Fc [N]"]["mean"], 2),
                "Cutting Force [N].std": round(forces_stats["Cutting Force Fc [N]"]["std"], 2),
                "Maximum Temperature at Last Frame [°C]": round(temp_stats["Max Temperature Last Frame [°C]"], 2),
                f"Penetration Depth for Last Frame < {temperature_threshold}°C [µm]": round(temp_stats[f"Penetration Depth for Last Frame < {temperature_threshold}°C [µm]"], 2) if temp_stats[f"Penetration Depth for Last Frame < {temperature_threshold}°C [µm]"] else None,
                "Temperature at Maximum Temperature at 1st Node [°C]": round(temp_stats["Temperature at Maximum Temperature at 1st Node [°C]"], 2),
                f"Penetration Depth for Frame with Tmax [µm]": round(temp_stats[f"Penetration Depth at Max Node < {temperature_threshold}°C [µm]"], 2) if temp_stats[f"Penetration Depth at Max Node < {temperature_threshold}°C [µm]"] else None
                }

            stats_list.append(stats_flat)
            ExcelUtils.add_forces_graps_to_excel(writer, sheet_name, combined_forces_df_with_results) # Add charts
            ExcelUtils.add_temp_graps_to_excel(writer, sheet_name, combined_temp_df_with_results) # Add charts
                
        except Exception as e:
            print(f"Error processing file {json_file_path_forces}: {e}")


    @staticmethod
    def combine_forces_data(data, workpiece_width_experiment, workpiece_width_simulation):
        """
        Combines the data of RF1 and RF2 into a single DataFrame.

        Args:
            data (dict): Dictionary containing the force data (RF1, RF2).
            filename (str): The JSON file name to be used as sheet name.

        Returns:
            pd.DataFrame: Combined dataframe of the forces.
        """
        rf1_df = pd.DataFrame(data["RF1"], columns=["Time [s]", "Force [N]"])
        rf2_df = pd.DataFrame(data["RF2"], columns=["Time [s]", "Force [N]"])
        rf_list = {"rf1": rf1_df, "rf2": rf2_df}

        for name, rf in rf_list.items():
            rf["Time [ms]"] = (rf["Time [s]"]*1000).round(2)
            new_column_name = "Cutting Force [N]" if name == "rf1" else "Normal Force [N]"
            rf[new_column_name] = (rf["Force [N]"] * workpiece_width_experiment / workpiece_width_simulation * (-1)).round(2)
            rf.drop(columns=["Time [s]", "Force [N]"], inplace=True)

        combined_df = pd.merge(rf1_df, rf2_df, on="Time [ms]", how="outer")
        combined_df["Dummy"] = range(1, len(combined_df) + 1)
        return combined_df


    @staticmethod
    def calculate_forces_statistics(df, start_percent, end_percent):
        """
        Calculates forces statistics (min, max, mean, std) for forces in the specified range.

        Args:
            df (pd.DataFrame): DataFrame with experiment results.
            start_percent (float): Start percentage of the data range.
            end_percent (float): End percentage of the data range.

        Returns:
            dict: Dictionary with calculated statistics for cutting and normal forces.
        """
        length = len(df)
        start_index, end_index = int(length * start_percent), int(length * end_percent) - 1

        stats = {
            "Cutting Normal Force FcN [N]": df["Normal Force [N]"].iloc[start_index:end_index + 1].agg(['min', 'max', 'mean', 'std']),
            "Cutting Force Fc [N]": df["Cutting Force [N]"].iloc[start_index:end_index + 1].agg(['min', 'max', 'mean', 'std']),}
        return stats


    @staticmethod
    def combine_temp_data(data):
        """
        Combines temperature data from various sources into a single DataFrame.

        Args:
            data (dict): Dictionary containing temperature data from different paths and nodes.

        Returns:
            pd.DataFrame: Combined DataFrame with formatted and cleaned temperature data.
        """
        # Extract temperature data for last frame, max temp, and time profiles
        temp_last_frame_df = pd.DataFrame(data["Temperature Profile - Path (Last Frame)"])
        temp_max_value_df = pd.DataFrame(data["Temperature Profile - Path (Max Temp at 1st Node)"])
        temp_first_node_df = pd.DataFrame(data["Temperature Profile - Time (1st Node)"])

        # Convert penetration depth from mm to µm and clean unnecessary columns
        temp_last_frame_df["Temperature Last Frame [°C]"] = temp_last_frame_df["Temperature [C]"].round(2)
        temp_last_frame_df["Penetration Depth [µm]"] = (temp_last_frame_df["Distance [mm]"] * 1000).round(2)
        temp_last_frame_df.drop(columns=["Temperature [C]", "Distance [mm]", "Node"], inplace=True)

        # Retain only max temperature at the first node and clean unnecessary columns
        temp_max_value_df["Temperature at Max Temperature Node [°C]"] = temp_max_value_df["Temperature [C]"].round(2)
        temp_max_value_df.drop(columns=["Temperature [C]", "Distance [mm]", "Node"], inplace=True)

        # Convert time from seconds to milliseconds and round temperatures
        temp_first_node_df["Time [ms]"] = (temp_first_node_df["Tempo [s]"] * 1000).round(2)
        temp_first_node_df["Temperature First Node [°C]"] = temp_first_node_df["NT11 (Temperatura) [C]"].round(2)

        # Add an auxiliary 'Dummy' column for merging DataFrames
        temp_last_frame_df["Dummy"] = range(1, len(temp_last_frame_df) + 1)
        temp_max_value_df["Dummy"] = range(1, len(temp_max_value_df) + 1)
        temp_first_node_df["Dummy"] = range(1, len(temp_first_node_df) + 1)

        # Combine DataFrames using 'Dummy' column
        combined_df = pd.merge(temp_max_value_df, temp_first_node_df, how="outer", on="Dummy")
        combined_df = pd.merge(combined_df, temp_last_frame_df, how="outer", on="Dummy")

        # Remove the auxiliary 'Dummy' column
        combined_df.drop(columns=["Dummy"], inplace=True)

        # Add empty columns for additional structure in the final output
        combined_df[" "] = np.nan
        combined_df[""] = np.nan

        # Rearrange columns into a specific order for final output
        combined_df = combined_df[[
            " ",
            "Penetration Depth [µm]",
            "Temperature Last Frame [°C]",
            "Temperature at Max Temperature Node [°C]",
            "",
            "Time [ms]",
            "Temperature First Node [°C]"
        ]]

        combined_df["Dummy"] = range(1, len(combined_df) + 1)
        return combined_df


    @staticmethod
    def calculate_temp_statistics(df, temperature_threshold):
        """
        Calculate temperature and penetration depth statistics..

        Args:
            df (pd.DataFrame): The DataFrame containing temperature and force data.
            stats (dict): Dictionary to store calculated statistics.
            temperature_threshold (float): The temperature threshold for filtering data.

        Returns:
            dict: Updated statistics dictionary.
        """
        # Check for temperature data in the last frame
        if "Temperature Last Frame [°C]" in df.columns:
            max_temp_last_frame = df["Temperature Last Frame [°C]"].max()
        else:
            print("Temperature column not found for the last frame.")
            max_temp_last_frame = None

        # Check for penetration depth where temperature is below the threshold
        temp_below_threshold = df[df["Temperature Last Frame [°C]"] < temperature_threshold]
        if not temp_below_threshold.empty:
            min_depth_last_frame = temp_below_threshold["Penetration Depth [µm]"].min()
        else:
            print(f"No values below {temperature_threshold}°C found.")
            min_depth_last_frame = None

        # Check for temperature data at max temperature node
        if "Temperature at Max Temperature Node [°C]" in df.columns:
            max_temp_at_max_node = df["Temperature at Max Temperature Node [°C]"].max()
        else:
            print("Temperature column not found for the max temperature node.")
            max_temp_at_max_node = None

        # Check for penetration depth where temperature at the max node is below the threshold
        temp_below_threshold = df[df["Temperature at Max Temperature Node [°C]"] < temperature_threshold]
        if not temp_below_threshold.empty:
            min_depth_at_max_node = temp_below_threshold["Penetration Depth [µm]"].min()
        else:
            print(f"No values below {temperature_threshold}°C found.")
            min_depth_at_max_node = None

        # Add results to statistics
        stats = {
            "Max Temperature Last Frame [°C]": max_temp_last_frame,
            f"Penetration Depth for Last Frame < {temperature_threshold}°C [µm]": min_depth_last_frame,
            "Temperature at Maximum Temperature at 1st Node [°C]": max_temp_at_max_node,
            f"Penetration Depth at Max Node < {temperature_threshold}°C [µm]": min_depth_at_max_node}
        return stats


if __name__ == "__main__":
    DataConverter()
