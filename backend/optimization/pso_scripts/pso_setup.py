import yaml
import numpy as np
from backend.optimization.aux_files.aux_functions import AuxClass
from backend.optimization.pso_scripts.pso_post_process import PostPso
from backend.optimization.pso_scripts.objective_function import ObjectiveFunction

from backend.config.yaml_manager import YamlManager

class PsoSetup:
    def get_start_info(self) -> tuple[list[float], list[float], int, list, list, list, list, list, list, float, list]:
        """
        Load all necessary information and data to initialize or resume PSO.

        Returns:
            tuple: Contains (lb, ub, num_dimensions, velocities, positions,
                    personal_best_positions, personal_best_scores,
                    global_best_position, global_best_score, global_best_scores_history).
        """
        AuxClass.log(self, "    [Step 2.1] get_start_info --> Retrieving initial configuration values...\n")
        PsoSetup.get_initial_values(self)

        AuxClass.log(self, "    [Step 2.2] get_start_info --> Retrieving parameter boundaries...\n")
        lb, ub, num_dimensions = PsoSetup.get_boundry(self)

        AuxClass.log(self, "    [Step 2.3] get_start_info --> Verifying current PSO stage...\n")
    
        if self.reload:
            velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history = PsoSetup.load_positions(self)
        else:
            AuxClass.log(self, "    [Step 2.4] get_start_info --> Initializing PSO parameters for first run...\n")
            self.count_iteration = 1
            velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history = PsoSetup.initial_parameters_pso(self, lb, ub, num_dimensions)

        return lb, ub, num_dimensions, velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history
    

    def get_initial_values(self) -> None:
        """
        Load initial values from the YAML configuration file.
        Sets PSO parameters, cutting conditions, and target values from the project configuration.
        """
        data = YamlManager.load_yaml(self, self.yaml_project_info)

        # Extract cutting conditions and experimental data
        if "3. Conditions" in data:
            for _, value in data["3. Conditions"].items():
                if not isinstance(value, dict):
                    continue

                for key, val in value.items():
                    if key == "Cutting Properties":
                        name = val['name']
                    elif key == "Experimental Datas":
                        self.target_values[name] = {"fc": float(val["cutting_force"]), "fn": float(val["normal_force"]), "ccr": float(val["chip_compression"]), "csr": float(val["chip_segmentation"])}

        # Extract parameter boundaries
        self.parameters_boundry = data.get("6. Parameters Limits", {})

        # Extract PSO and simulation settings
        pso_info = data.get("7. PSO and Simulation", {})
        self.number_of_cp = int(pso_info.get("Computers", 1))
        self.cores_by_simulation = int(pso_info.get("Cores by Simulation", 4))
        self.number_of_iterations = int(pso_info.get("Iterations", 20))
        self.number_of_particles = int(pso_info.get("Particles", 4))
        self.cutting_conditions = int(pso_info.get("Cutting Conditions", 1))
        self.fig = float(pso_info.get("fig", 2.0))
        self.fip = float(pso_info.get("fip", 2.0))
        self.w = float(pso_info.get("w", 0.5))
        self.main_computer = pso_info.get("Main Computer", "Yes")


    def get_boundry(self) -> tuple[list[float], list[float], int]:
        """
        Retrieve lower and upper boundaries for each optimization parameter.

        Returns:
            tuple: A tuple (lb, ub, num_dimensions), where:
                lb (list[float]): Lower bounds
                ub (list[float]): Upper bounds
                num_dimensions (int): Number of parameters
        """
        lb, ub = [], []
        for _ , info in self.parameters_boundry.items():
            for limit_type, value in info.items():
                lb.append(float(value)) if limit_type == "min" else ub.append(float(value))
        return lb, ub, len(self.parameters_boundry) 


    def load_positions(self) -> tuple | None:
        """
        Check if the optimization is already completed or if previous data should be resumed.

        Returns:
            tuple: PSO state (velocities, positions, personal_best_positions, personal_best_scores,
                            global_best_position, global_best_score, global_best_scores_history).
                    If finished or error, returns tuple of Nones.
        """
        try:
            data = YamlManager.load_yaml(self, self.yaml_project_info)
            opt_data = data.get("8. Otimization Datas", None)

            import ast
            self.number_of_remain_iterations = int(opt_data.get("Remaining Iterations", 0))
            self.count_iteration = self.number_of_iterations - self.number_of_remain_iterations + 1
            last_it = opt_data.get("Last Iteration Values", {})

            # Usar ast.literal_eval para converter string em estrutura Python
            positions = np.array(ast.literal_eval(last_it["positions"]["value"]))
            velocities = np.array(ast.literal_eval(last_it["velocities"]["value"]))
            personal_best_positions = np.array(ast.literal_eval(last_it["personal_best_position"]["value"]))
            personal_best_scores = ast.literal_eval(last_it["personal_best_score"]["value"])
            global_best_position = np.array(ast.literal_eval(last_it["global_best_position"]["value"]))
            global_best_score = float(last_it["global_best_score"]["value"])
            global_best_scores_history = ast.literal_eval(last_it["global_best_score_history"]["value"])
   
            AuxClass.log(self, f"       verify_stage --> Reloaded previous iteration data (Iteration {self.count_iteration})")
            return velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history
            
        except Exception as e:
            self.reload = False
            self.e = e
            AuxClass.log(self, "        [ERROR] verify_stage --> Failed to load previous iteration data. Starting fresh.")
            AuxClass.handle_error(self, e, "Error at def verify_stage")
            return (None,) * 7
    

    def initial_parameters_pso(self, lb, ub, num_dimensions) -> tuple[list, list, list, list, list, float, list]:
        """
        Initialize particles, velocities, and fitness values for the first PSO iteration.

        Args:
            lb (list[float]): Lower boundaries
            ub (list[float]): Upper boundaries
            num_dimensions (int): Dimensionality of the search space

        Returns:
            tuple: Initial PSO state
        """
        objective_function_pso = lambda params: ObjectiveFunction.objective_function(self, params)
        
        try:
            # Initialize positions and velocities of the particles
            positions = np.round(np.random.uniform(low=lb, high=ub, size=(self.number_of_particles, num_dimensions)), 4).tolist()
            velocities = np.random.uniform(low=-1, high=1, size=(self.number_of_particles, num_dimensions)).tolist()
            
            PostPso.save_position_velocity(self, self.number_of_particles, positions, velocities)
            # PostPso.save_initial_data(self, self.number_of_particles, positions, velocities)
            # PostPso.save_iteration_info(self, velocities, positions)
            
            # Initialize the best positions and scores
            personal_best_positions = [list(pos) for pos in positions]
            personal_best_scores = objective_function_pso(positions)
            global_best_position = personal_best_positions[np.argmin(personal_best_scores)]
            global_best_score = min(personal_best_scores)
            global_best_scores_history = [global_best_score]

            # Show datas in the interface and save info
            PostPso.show_datas(self)
            PostPso.save_best_results(self, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history)
            AuxClass.log(self, "        initial_parameters_pso --> Initial PSO parameters successfully created.")
            return velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history
        
        except Exception as e:
            self.e = e
            AuxClass.handle_error(self, e, "Error at def initial_parameters_pso")
            return [], [], [], [], None, None, []


