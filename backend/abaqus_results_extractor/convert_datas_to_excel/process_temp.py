import os 
import json
import pandas as pd

class TempProcessor():
    """
    A class to process temperature simulation data stored in JSON format.
    It loads data, formats it, exports to Excel, and computes summary statistics.
    """
        
    def __init__(self, json_input_dir: str, output_excel_dir: str):
        """
        Initialize TempProcessor.

        Args:
            json_input_dir (str): Directory containing input JSON folders.
            output_excel_dir (str): Directory where Excel output will be saved.
        """
        self.json_input_dir = json_input_dir
        self.output_excel_dir = output_excel_dir
        self.results_summary = {}
        
        
    def process_file(self, filename: str, temperature_threshold: float = 60.0) -> dict:
        """
        Process a single simulation case.

        Args:
            case_name (str): Name of the folder containing the temperature JSON.
            temperature_threshold (float): Threshold temperature for filtering depth.

        Returns:
            dict: Summary statistics for the case.
        """
        json_folder = os.path.join(self.json_input_dir, filename)
        if not os.path.isdir(json_folder):
            return

        json_file = os.path.join(json_folder, "temperature.json")
        if not os.path.isfile(json_file):
            return

        df = self._load_and_prepare_data(json_file)
        self._export_to_excel(df, filename)
        self._compute_statistics(df, filename, temperature_threshold)
        return self.results_summary


    def _load_and_prepare_data(self, json_path: str) -> pd.DataFrame:
        """
        Load and format temperature data from JSON file.

        Args:
            json_path (str): Path to temperature.json file.

        Returns:
            pd.DataFrame: Combined DataFrame with formatted temperature data.
        """
        with open(json_path, 'r') as file:
            data = json.load(file)

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

        # # Add an auxiliary 'Dummy' column for merging DataFrames
        temp_last_frame_df["Dummy"] = range(1, len(temp_last_frame_df) + 1)
        temp_max_value_df["Dummy"] = range(1, len(temp_max_value_df) + 1)
        temp_first_node_df["Dummy"] = range(1, len(temp_first_node_df) + 1)

        # Combine DataFrames using 'Dummy' column
        combined_df = pd.merge(temp_max_value_df, temp_first_node_df, how="outer", on="Dummy")
        combined_df = pd.merge(combined_df, temp_last_frame_df, how="outer", on="Dummy")

        # Remove the auxiliary 'Dummy' column
        combined_df.drop(columns=["Dummy"], inplace=True)

        # Rearrange columns into a specific order for final output
        combined_df = combined_df[[
            "Penetration Depth [µm]",
            "Temperature Last Frame [°C]",
            "Temperature at Max Temperature Node [°C]",
            "Time [ms]",
            "Temperature First Node [°C]"
        ]]
        return combined_df
    

    def _export_to_excel(self, df: pd.DataFrame, filename: str):
        """
        Export processed temperature data to Excel file.

        Args:
            df (pd.DataFrame): Processed DataFrame to be saved.
            case_name (str): Sheet name prefix for this case.
        """
        temperature_file = os.path.join(self.output_excel_dir, "temperature_result.xlsx")

        if os.path.exists(temperature_file):
            with pd.ExcelWriter(temperature_file, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                df.to_excel(writer, sheet_name=filename[4:][:31], index=False)
        else:
            df.to_excel(temperature_file, sheet_name=filename[4:][:31], index=False, engine="openpyxl")


    def _compute_statistics(self, df: pd.DataFrame, filename: str, temperature_threshold: float):
        """
        Compute summary statistics for temperature and penetration depth.

        Args:
            df (pd.DataFrame): DataFrame containing the temperature data.
            filename (str): Current case name for result labeling.
            temperature_threshold (float): Threshold for temperature depth filtering.
        """
        # Check for temperature data in the last frame
        if "Temperature Last Frame [°C]" in df.columns:
            max_temp_last_frame = df["Temperature Last Frame [°C]"].max()
        else:
            max_temp_last_frame = None

        # Check for penetration depth where temperature is below the threshold
        temp_below_threshold = df[df["Temperature Last Frame [°C]"] < temperature_threshold]
        if not temp_below_threshold.empty:
            min_depth_last_frame = temp_below_threshold["Penetration Depth [µm]"].min()
        else:
            min_depth_last_frame = None

        # Check for temperature data at max temperature node
        if "Temperature at Max Temperature Node [°C]" in df.columns:
            max_temp_at_max_node = df["Temperature at Max Temperature Node [°C]"].max()
        else:
            max_temp_at_max_node = None

        # Check for penetration depth where temperature at the max node is below the threshold
        temp_below_threshold = df[df["Temperature at Max Temperature Node [°C]"] < temperature_threshold]
        if not temp_below_threshold.empty:
            min_depth_at_max_node = temp_below_threshold["Penetration Depth [µm]"].min()
        else:
            min_depth_at_max_node = None

        # Add results to statistics
        stats = {
            "Max Temperature Last Frame [°C]": max_temp_last_frame,
            f"Penetration Depth for Last Frame < {temperature_threshold}°C [µm]": min_depth_last_frame,
            "Temperature at Maximum Temperature at 1st Node [°C]": max_temp_at_max_node,
            f"Penetration Depth at Max Node < {temperature_threshold}°C [µm]": min_depth_at_max_node}
        
        self.results_summary[filename] = {
            "Maximum Temperature at Last Frame [°C]": round(stats.get("Max Temperature Last Frame [°C]", 0), 2)}


if __name__ == "__main__":
    json_default_path = r"output_files/json"
    graph_folder = r"output_files/img"
    odb_processing = r"output_files/odb"

    processor = TempProcessor(json_default_path, graph_folder)
    for file in os.listdir(odb_processing):
        filename = file[:-4]
        results_summary = processor.process_file(filename)

