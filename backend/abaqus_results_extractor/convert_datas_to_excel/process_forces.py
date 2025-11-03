import os 
import json
import logging
import traceback
import pandas as pd 


class ForceProcessor():
    def __init__(self, main):
        """
        Initialize ForceProcessor.

        Parameters:
            json_input_dir (str): Path to the directory containing simulation JSON folders.
            output_excel_dir (str): Path where the Excel results will be stored.
        """
        self.main = main
        self.results_summary = {}
        
        
    def process_file(self, filename: str, exp_width: float = 4.0, sim_width: float = 0.02, start_pct: float = 0.25, end_pct: float = 1.00) -> dict:
        """
        Main entry point to process a single simulation case.

        Parameters:
            case_name (str): Name of the folder containing the JSON data.
            exp_width (float): Width used in the experiment (mm).
            sim_width (float): Width used in the simulation (mm).
            start_pct (float): Start percentage for statistics calculation.
            end_pct (float): End percentage for statistics calculation.
        """
        try:
            json_folder = os.path.join(self.main.json_default_path, filename)
            if not os.path.isdir(json_folder):
                return

            json_file = os.path.join(json_folder, "reaction_forces.json")
            if not os.path.isfile(json_file):
                return

            df = self._load_and_prepare_data(json_file, exp_width, sim_width)
            self._export_to_excel(df, filename)
            self._compute_statistics(df, filename, start_pct, end_pct)
            return self.results_summary
        except Exception as e:
            logging.error(f"❌ Erro ao gerar gráfico:")
            logging.error("🔍 Traceback:\n%s", traceback.format_exc())


    def _load_and_prepare_data(self, json_path: str, exp_width: float, sim_width: float) -> pd.DataFrame:
        """
        Loads and combines force data from JSON, applying physical scaling.

        Returns:
            pd.DataFrame: Combined and processed force data.
        """
        with open(json_path, 'r') as file:
            data = json.load(file)

        rf1_df = pd.DataFrame(data["RF1"], columns=["Time [s]", "Force [N]"])
        rf2_df = pd.DataFrame(data["RF2"], columns=["Time [s]", "Force [N]"])
        rf_list = {"rf1": rf1_df, "rf2": rf2_df}

        for name, rf in rf_list.items():
            rf["Time [ms]"] = (rf["Time [s]"]*1000).round(2)
            new_column_name = "Cutting Force [N]" if name == "rf1" else "Normal Force [N]"
            rf[new_column_name] = (rf["Force [N]"] * exp_width / sim_width * (-1)).round(2)
            rf.drop(columns=["Time [s]", "Force [N]"], inplace=True)

        combined_df = pd.merge(rf1_df, rf2_df, on="Time [ms]", how="outer")
        combined_df["Dummy"] = range(1, len(combined_df) + 1)
        combined_df = combined_df.drop(columns=["Dummy"])
        return combined_df


    def _export_to_excel(self, df: pd.DataFrame, filename: str):
        """
        Export processed temperature data to Excel file.

        Args:
            df (pd.DataFrame): Processed DataFrame to be saved.
            case_name (str): Sheet name prefix for this case.
        """
        filename = filename[4:][:31]
        df = df.rename(columns={
            "Time [ms]": "time",
            "Cutting Force [N]": "cutting_force",
            "Normal Force [N]": "normal_force"
        })

        time_list = df["time"].tolist()
        cutting_list = df["cutting_force"].tolist()
        normal_list = df["normal_force"].tolist()

        record = {
            "project_id": self.main.project_id,
            "filename": filename,
            "time": time_list,
            "cutting_force": cutting_list,
            "normal_force": normal_list
        }

        existing = self.main.supabase.table("simulation_forces_results")\
            .select("id")\
            .eq("project_id", self.main.project_id)\
            .eq("filename", filename)\
            .execute()

        if existing.data and len(existing.data) > 0:
            record_id = existing.data[0]["id"]
            self.main.supabase.table("simulation_forces_results")\
                .update(record)\
                .eq("id", record_id)\
                .execute()
        else:
            self.main.supabase.table("simulation_forces_results")\
                .insert(record)\
                .execute()


    def _compute_statistics(self, df: pd.DataFrame, filename: str, start_pct: float, end_pct: float):
        """
        Computes summary statistics for cutting and normal forces.

        Results are saved in self.results_summary under the given case_name.
        """
        total_len = len(df)
        start_idx = int(total_len * start_pct)
        end_idx = int(total_len * end_pct)

        stats = {
            "Cutting Normal Force FcN [N]": df["Normal Force [N]"].iloc[start_idx:end_idx + 1].agg(['min', 'max', 'mean', 'std']),
            "Cutting Force Fc [N]": df["Cutting Force [N]"].iloc[start_idx:end_idx + 1].agg(['min', 'max', 'mean', 'std']),}
        
        self.results_summary[filename] = {
            "Normal Force [N].mean": round(stats ["Cutting Normal Force FcN [N]"]["mean"], 2),
            "Cutting Force [N].mean": round(stats ["Cutting Force Fc [N]"]["mean"], 2)}


