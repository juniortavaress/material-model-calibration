import logging
import numpy as np
from typing import List
from collections import defaultdict
from frontend.aux_files.tracking_message_manager import ProcessStatusLogger
from backend.abaqus_simulation_manager.simualtion_manager import SimulationManager
from backend.abaqus_results_extractor.convert_datas_to_excel.results_processor import ResultsManager

class ObjectiveFunction():
    def objective_function(self) -> List[float]:
        """
        Objective function for optimization, calculates the error between
        simulated results and experimental data for a given parameter set.

        Args:
            parameters (List[List[float]]): A list of parameter sets to simulate.

        Returns:
            List[float]: List of error values corresponding to each parameter set.
        """
        SimulationManager(self, self.main)
        ProcessStatusLogger.set_log_to_ui(self, "message-id_04")   

        best_set_data = ResultsManager.update_best_parameter_set(self)
        error_list = ObjectiveFunction._calculate_errors_from_results(self, self.main.current_opt)

        ObjectiveFunction.delete_inp_files_by_iteration(self)
        self.main.current_opt += 1
        if self.ui.combobox_iteration.findText(str(self.main.current_opt).zfill(2)) == -1:
            self.ui.combobox_iteration.addItem(str(self.main.current_opt).zfill(2))
        
        # Update iteration counter
        self.number_of_iterations -= 1
        return error_list


    def _calculate_errors_from_results(self, current_iteration):
        """
        Computes average error per parameter set for the current iteration.

        Args:
            current_iteration (str): Iteration identifier.

        Returns:
            List of mean errors per parameter set.
        """
        error_list = []        
        response = self.main.supabase.table("results").select("*") \
            .eq("project_id", self.main.project_id) \
            .eq("iteration_number", current_iteration) \
            .execute()

        set_errors = defaultdict(list)
        for row in response.data:
            set_num = row["parameter_set"]
            error = row.get("error")

            if error is not None:
                set_errors[set_num].append(error)

        error_list = []
        for set_num in sorted(set_errors.keys()):  # ordenado pelo número do set
            mean_error = float(np.mean(set_errors[set_num]))
            error_list.append(mean_error)        
        return error_list
    

    def delete_inp_files_by_iteration(self):
        """
        Deletes all .inp files in storage that belong to a specific iteration.
        """
        iteration = self.main.current_opt - 1
        if iteration > 0:
            try:
                bucket = "inp-default-files"
                folder_path = f"{self.main.project_id}/edited_inp"
                iteration_tag = f"_it_{str(iteration).zfill(2)}_"

                # List files
                list_response = self.main.supabase_storage.storage.from_(bucket).list(folder_path)

                # Check for listing error
                if isinstance(list_response, dict) and list_response.get("error"):
                    logging.error(f"Error listing files in bucket '{bucket}': {list_response['error']['message']}")
                    return

                # Filter matching files
                files_to_delete = [
                    f"{folder_path}/{file['name']}"
                    for file in list_response
                    if file["name"].endswith(".inp") and iteration_tag in file["name"]
                ]

                if not files_to_delete:
                    logging.info(f"No .inp files found for iteration {iteration}.")
                    return

                # Delete files
                delete_response = (self.main.supabase_storage.storage.from_(bucket).remove(files_to_delete))

                if isinstance(delete_response, dict) and delete_response.get("error"):
                    logging.error(f"Error deleting files: {delete_response['error']['message']}")
                else:
                    logging.info(f"{len(files_to_delete)} files deleted for iteration {iteration}.")

            except Exception as error:
                logging.error(f"Unexpected error while deleting files for iteration {iteration}: {error}")