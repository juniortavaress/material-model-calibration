import re
import math
import numpy as np
from collections import defaultdict
from typing import Dict, List, Optional      

class ResultsManager():
    """
    Handles result processing and storage in the database,
    including error calculation and best parameter set tracking.
    """
    def store_simulation_results(self, filename: str, forces_summary: Dict, chip_summary: Dict) -> None:
        """
        Calculates simulation errors against experimental values and stores results in the database.

        Args:
            filename (str): Simulation filename.
            forces_summary (dict): Simulated force results.
            chip_summary (dict): Simulated chip geometry results.
        """
        error_fc, error_fn, error_ccr, error_csr = None, None, None, None
        simulated_cutting_forces = simulated_normal_forces = None
        chip_compression_ratio = chip_segmentation_ratio = None
        iteration_number, set_number, condition = ResultsManager._extract_file_info(self, filename)
        target_values = ResultsManager._fetch_target_values(self, condition)

        if forces_summary: 
            simulated_cutting_forces = forces_summary[filename]["Cutting Force [N].mean"]
            simulated_normal_forces = forces_summary[filename]["Normal Force [N].mean"]
            error_fc = (simulated_cutting_forces - target_values[0])/target_values[0]
            error_fn = (simulated_normal_forces - target_values[1])/target_values[1]
        
        if chip_summary:
            chip_compression_ratio = chip_summary[filename]["Chip Compression Ratio (CCR)"]
            chip_segmentation_ratio = chip_summary[filename]["Chip Segmentatio Ratio (CSR)"]
            error_ccr = (chip_compression_ratio - target_values[2])/target_values[2] if chip_compression_ratio is not None else None
            error_csr = (chip_segmentation_ratio - target_values[3])/target_values[3] if chip_segmentation_ratio is not None else None
    
        if chip_summary and (error_ccr is None or error_csr is None):
            combined_error = None
        elif forces_summary and (error_fn is None or error_fc is None):
            combined_error = None
        else:

            efc = error_fc if error_fc is not None else 0
            efn = error_fn if error_fn is not None else 0
            eccr = error_ccr if error_ccr is not None else 0
            ecsr = error_csr if error_csr is not None else 0
            combined_error = math.sqrt((self.main.wfc * efc ** 2) + (self.main.wfn * efn ** 2) + (self.main.wccr * eccr ** 2) + (self.main.wcsr * ecsr ** 2))

        data = {
                "project_id": self.main.project_id,
                "iteration_number": iteration_number,
                "parameter_set": set_number,
                "condition_name": condition,
                "simulated_cutting_force": round(simulated_cutting_forces, 2) if simulated_cutting_forces is not None else None,
                "error_fc": error_fc,
                "simulated_normal_force": round(simulated_normal_forces, 2) if simulated_normal_forces is not None else None,
                "error_fn": error_fn,
                "simulated_compression_ratio": round(chip_compression_ratio, 2) if chip_compression_ratio is not None else None,
                "error_ccr": error_ccr,
                "simulated_segmentation_ratio": round(chip_segmentation_ratio, 2) if chip_segmentation_ratio is not None else None,
                "error_csr": error_csr,
                "error": combined_error
            }

        existing = self.main.supabase.table("results").select("*")\
            .eq("project_id", self.main.project_id)\
            .eq("iteration_number", iteration_number)\
            .eq("parameter_set", set_number)\
            .eq("condition_name", condition)\
            .execute()

        if existing.data:
            self.main.supabase.table("results").update(data)\
                .eq("project_id", self.main.project_id)\
                .eq("iteration_number", iteration_number)\
                .eq("parameter_set", set_number)\
                .eq("condition_name", condition)\
                .execute()
        else:
            self.main.supabase.table("results").insert(data).execute()


    
    def update_best_parameter_set(self) -> None:
        """
        Identifies and stores the best parameter set for the current iteration based on error averages.
        """
        results = self.main.supabase.table("results").select("*")\
            .eq("project_id", self.main.project_id)\
            .eq("iteration_number", self.main.current_opt)\
            .execute()
        
        set_errors = defaultdict(list)
        for row in results.data:
            set_num = row["parameter_set"]
            error = row.get("error", 0)  
            set_errors[set_num].append(error)

        mean_errors = {
            set_num: np.mean([e for e in errors if e is not None])
            for set_num, errors in set_errors.items()
        }
        best_set = min(mean_errors, key=mean_errors.get)

        self.main.supabase.table("results").update({"best_set": best_set})\
            .eq("project_id", self.main.project_id)\
            .eq("iteration_number", self.main.current_opt)\
            .execute()


    def _extract_file_info(self, filename: str) -> tuple[str, str, str]:
        """
        Extracts iteration number, parameter set, and condition name from a filename.

        Args:
            filename (str): Input filename.

        Returns:
            Tuple[int, int, str]: (iteration_number, set_number, condition)
        """
        cond = re.search(r'cond\d{2}', filename).group(0)
        it = int(re.search(r'it_(\d{2})', filename).group(1))
        set = int(re.search(r'set_(\d{2})', filename).group(1))
        return it, set, cond
        

    def _fetch_target_values(self, condition: str) -> List[Optional[float]]:
        """
        Retrieves experimental target values for a given condition.

        Args:
            condition (str): Condition name.

        Returns:
            List[Optional[float]]: [fc, fn, ccr, csr]
        """
        target_values={}
        response = self.main.supabase.table("conditions").select("*").eq("project_id", self.main.project_id).eq("name", condition).execute()
        if response.data:
            for cond in response.data:
                name = cond.get("name")
                values = {
                    "fc": float(cond.get("cutting_force")) if cond.get("cutting_force") is not None else None,
                    "fn": float(cond.get("normal_force")) if cond.get("normal_force") is not None else None,
                    "ccr": float(cond.get("chip_compression")) if cond.get("chip_compression") is not None else None,
                    "csr": float(cond.get("chip_segmentation")) if cond.get("chip_segmentation") is not None else None
                }
                target_values[name] = values
                
            if condition in target_values:
                target_cutting_force = target_values[condition].get("fc", None)
                target_normal_force = target_values[condition].get("fn", None)
                target_chip_compression_ratio = target_values[condition].get("ccr", None)
                target_chip_segentation_ratio = target_values[condition].get("csr", None)
        return [target_cutting_force, target_normal_force, target_chip_compression_ratio, target_chip_segentation_ratio]
        

