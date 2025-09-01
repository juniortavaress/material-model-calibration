import os
import yaml
import numpy as np
import pandas as pd
from frontend.aux_files.show_status_message import StatusMessage

from backend.config.yaml_manager import YamlManager

class PostPso:
    @staticmethod
    def to_list_if_numpy(obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        # Caso seja lista de arrays ou misturado
        if isinstance(obj, list) and any(isinstance(i, np.ndarray) for i in obj):
            return [i.tolist() if isinstance(i, np.ndarray) else i for i in obj]
        return obj

    def save_position_velocity(self, num_particles, positions, velocities):
        if os.path.exists(self.yaml_parameters):
            self.info_set = YamlManager.load_yaml(self, self.yaml_parameters)
        else:
            self.info_set = {}

        iteration_key = f"Iteration {self.count_iteration:02}"
        self.info_set[iteration_key] = {}

        for i in range(num_particles):
            set_key = f"set-0{i+1}"
            self.info_set[iteration_key][set_key] = {}
            self.info_set[iteration_key][set_key]["Parameters"] = {}

            for j, (param_name, _) in enumerate(self.parameters_boundry.items()):
                param_value = positions[i][j]
                param_value = param_value.item() if isinstance(param_value, np.generic) else param_value
                self.info_set[iteration_key][set_key]["Parameters"][param_name] = param_value

        with open(self.yaml_parameters, "w") as file:
            yaml.dump(self.info_set, file)
        
        PostPso.save_current_iteration(self, velocities, positions)

        
    def save_current_iteration(self, velocities, positions):
        data = YamlManager.load_yaml(self, self.yaml_project_info)
        current_optimization_section = data.setdefault("10. Current Optimization", {})
        current_optimization_section.update({
            "velocities": str(PostPso.to_list_if_numpy(velocities)), 
            "positions": str(PostPso.to_list_if_numpy(positions)), 
            "Iteration": self.count_iteration})
        with open(self.yaml_project_info, "w", encoding="utf-8") as file:
            yaml.safe_dump(data, file, allow_unicode=True, default_flow_style=False)






    def last_iteration_info(self, velocities, positions) -> None:
        data = YamlManager.load_yaml(self, self.yaml_project_info)
        last_optimization_section = data.setdefault("12. Last Otimization Datas", {})
        last_optimization_section.update({
            "velocities": str(PostPso.to_list_if_numpy(velocities)),
            "positions": str(PostPso.to_list_if_numpy(positions)),
            "Remaining Iterations": self.number_of_iterations
        })
        with open(self.yaml_project_info, "w", encoding="utf-8") as file:
            yaml.safe_dump(data, file, allow_unicode=True, default_flow_style=False)


    
    def save_best_results(self, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history):
        data = YamlManager.load_yaml(self, self.yaml_project_info)
        best_optimization_section = data.setdefault("11. Best Otimization Datas", {})
        best_optimization_section.update({
            "personal_best_position": str(PostPso.to_list_if_numpy(personal_best_positions)),
            "personal_best_score": str(personal_best_scores),
            "global_best_position": str(PostPso.to_list_if_numpy(global_best_position)),
            "global_best_score": str(global_best_score),
            "global_best_score_history": str(global_best_scores_history),
        })
        with open(self.yaml_project_info, "w", encoding="utf-8") as file:
            yaml.safe_dump(data, file, allow_unicode=True, default_flow_style=False)











    def show_datas(self, call=None) -> None:
        """
        Updates the interface with results from the best performing particle set.

        Args:
            call (str, optional): If set to "finished", retrieves final best set. Otherwise, uses current iteration.
        """
        best_set = None
        min_error = float("inf")
        iteration_number = self.count_iteration 
        current_iteration = f"Iteration {int(iteration_number):02d}"   

        if call == "finished":
            message = "message-id_06"
            for iteration, data_int in self.info_set.items():
                    for set, data_set in data_int.items():
                        if float(data_set["Error"]) < min_error:
                            min_error = float(data_set["Error"])
                            best_set = int(set.split("t-")[1])
        else:
            message = "message-id_05"
            for iteration, data_int in self.info_set.items():
                if iteration == current_iteration:
                    for set, data_set in data_int.items():
                        if float(data_set["Error"]) < min_error:
                            min_error = float(data_set["Error"])
                            best_set = int(set.split("t-")[1])

        if best_set is not None:
            data_path = os.path.join(self.excel_files, "datas.xlsx")
            df_info = pd.read_excel(data_path, engine="openpyxl")
            filtered_mean = df_info[(df_info["Iteration Number"] == iteration_number) & (df_info["Parameter Set"] == int(best_set))].mean(numeric_only=True)            
            set = f"set-0{best_set}" if best_set < 10 else f"set-{best_set}"
            self.best_parameters = self.info_set[current_iteration][set]["Parameters"]
            self.error = filtered_mean["Error"]

            if self.forces:
                self.error_cutting_force = filtered_mean["Error Fc"]
                self.error_normal_force = filtered_mean["Error Fn"]

            if self.chip:
                self.error_CCR = filtered_mean["Error CCR"]
                self.error_CSR = filtered_mean["Error CSR"]

            if self.temp:
                self.error_temp = filtered_mean["Error Temperature"]
            StatusMessage.set_text(self, message)
        




    def save_parameters(self, num_particles, positions) -> None:
        """
        Saves the current parameters to a JSON file.

        Args:
            num_particles (int): The number of particles.
            positions (array): The current positions of the particles.
        """
        if os.path.exists(self.yaml_parameters):
            self.info_set = YamlManager.load_yaml(self, self.yaml_parameters)
        else:
            self.info_set = {}

        iteration_key = f"Iteration {self.count_iteration:02}"
        self.info_set[iteration_key] = {}

        for i in range(num_particles):
            set_key = f"set-0{i+1}"
            self.info_set[iteration_key][set_key] = {}
            self.info_set[iteration_key][set_key]["Parameters"] = {}

            for j, (param_name, _) in enumerate(self.parameters_boundry.items()):
                param_value = positions[i][j]
                param_value = param_value.item() if isinstance(param_value, np.generic) else param_value
                self.info_set[iteration_key][set_key]["Parameters"][param_name] = param_value

        with open(self.yaml_parameters, "w") as file:
            yaml.dump(self.info_set, file)