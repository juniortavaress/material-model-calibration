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
    

    # def add_result_names_to_combobox(self, current_iteration):
    #     selected_iteration = str(current_iteration).zfill(2)
    #     response = self.main.supabase.table("results").select("condition_name, iteration_number, parameter_set") \
    #         .eq("project_id", self.main.project_id) \
    #         .eq("iteration_number", current_iteration) \
    #         .execute()

    #     names = set()
    #     for row in response.data:
    #         iteration = str(row["iteration_number"]).zfill(2)
    #         if iteration == selected_iteration:
    #             condition = row["condition_name"]
    #             iteration = row["iteration_number"]
    #             set_num = row["parameter_set"]
    #             name = f"{condition}_it_{str(iteration).zfill(2)}_set_{str(set_num).zfill(2)}"
    #             names.add(name)

    #     for name in sorted(names):
    #         if self.ui.combobox_file.findText(name) == -1:
    #             self.ui.combobox_file.addItem(name)
        



