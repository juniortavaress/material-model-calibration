import numpy as np
from typing import List, Optional
from backend.abaqus_simulation_manager.simualtion_manager import SimulationManager
from frontend.aux_files.show_status_message import StatusMessage
from backend.abaqus_results_extractor.results_manager import GetResults
from create_graphs import createPlots

class ObjectiveFunction():
    def objective_function(self, parameters: Optional[List[List[float]]] = None) -> List[float]:
        """
        Objective function for optimization, calculates the error between
        simulated results and experimental data for a given parameter set.

        Args:
            parameters (List[List[float]]): A list of parameter sets to simulate.

        Returns:
            List[float]: List of error values corresponding to each parameter set.
        """
        error_list = []
        current_iteration = f"Iteration {(self.count_iteration):02d}"   
        

        # Format and store parameters in the internal info_set structure.        
        for index, param in enumerate(parameters):
            # print('parameters', parameters)
            formatted_coords = '[' + ', '.join(map(lambda x: str(np.round(x, 4)), param)) + ']'
            self.info_set.setdefault(current_iteration, {}).setdefault(f"set-0{index+1}", {})["Parameters Map"] = formatted_coords

        # Run simulation and extract results
        SimulationManager(self)
        StatusMessage.set_text(self, "message-id_04")         
        result_extractor = GetResults(self, execution_mode="embedded")

        self.info_set, error_list = result_extractor.result_call(self, forces=self.forces, temperature=self.temp, chip=self.chip, current_iteration=current_iteration)  

        self.number_of_iterations -= 1
        # createPlots.graphs_manager(self)    
        return error_list





