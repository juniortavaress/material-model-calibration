import ast
import numpy as np
from backend.config.aux_functions import AuxClass
from backend.optimization.pso_scripts.pso_post_process import PostPso
from backend.optimization.pso_scripts.objective_function import ObjectiveFunction


class PsoSetup:
    def get_start_info(self) -> tuple[list[float], list[float], int, list, list, list, list, list, list, float, list]:
        """
        Load all necessary information and data to initialize or resume PSO.

        Returns:
            tuple: Contains (lb, ub, num_dimensions, velocities, positions,
                    personal_best_positions, personal_best_scores,
                    global_best_position, global_best_score, global_best_scores_history).
        """
        PsoSetup.get_initial_values(self)
        lb, ub, num_dimensions = PsoSetup.get_boundry(self)
    
        if self.main.reload:
            velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history = PsoSetup.load_positions(self)
        else:
            self.main.current_opt = 1
            velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history = PsoSetup.initial_parameters_pso(self, lb, ub, num_dimensions)

        return lb, ub, num_dimensions, velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history
    

    def get_initial_values(self) -> None:
        """
        Sets PSO parameters, cutting conditions, and target values from the project configuration.
        """
        cond_response = self.main.supabase.table("conditions").select("*").eq("project_id", self.main.project_id).execute()

        # Extract cutting conditions and experimental data
        self.target_values = {}
        if cond_response.data:
            for cond in cond_response.data:
                name = cond["name"]
                self.target_values[name] = {
                    "fc": float(cond.get("cutting_force", 0) or 0),
                    "fn": float(cond.get("normal_force", 0) or 0),
                    "ccr": float(cond.get("chip_compression", 0) or 0),
                    "csr": float(cond.get("chip_segmentation", 0) or 0)
                }
        # Extract parameter boundaries
        param_response = self.main.supabase.table("parameters").select("*").eq("project_id", self.main.project_id).execute()
        self.parameters_boundry = {}
        if param_response.data:
            for param in param_response.data:
                name = param["name"]
                self.parameters_boundry[name] = {
                    "min_value": param.get("min_value", None),
                    "max_value": param.get("max_value", None)
                }

        # Extract PSO and simulation settings
        sim_response = self.main.supabase.table("project_simulation").select("*").eq("project_id", self.main.project_id).execute()

        if sim_response.data and len(sim_response.data) > 0:
            sim_info = sim_response.data[0]
            self.cores_by_simulation = int(sim_info.get("cores_by_simulation", 4))
            self.number_of_iterations = int(sim_info.get("total_iterations", 20))
            self.number_of_particles = int(sim_info.get("particles", 4))
            self.cutting_conditions = int(sim_info.get("cutting_conditions", 1))
            self.fig = float(sim_info.get("fig", 2.0))
            self.fip = float(sim_info.get("fip", 2.0))
            self.w = float(sim_info.get("w", 0.5))
            self.main_computer = sim_info.get("main_computer", "Yes")


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
                lb.append(float(value)) if limit_type == "min_value" else ub.append(float(value))
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
            cur_response = self.main.supabase.table("current_optimization_data").select("*").eq("project_id", self.main.project_id).execute().data

            
            if cur_response:
                cur_opt_data = cur_response[0]
                self.number_of_iterations = self.number_of_iterations - self.main.current_opt + 1
                positions = np.array(ast.literal_eval(cur_opt_data["positions"]))
                velocities = np.array(ast.literal_eval(cur_opt_data["velocities"]))
     
            best_response = self.main.supabase.table("best_optimization_data").select("*").eq("project_id", self.main.project_id).execute().data
            if best_response:
                best_opt_data = best_response[0]
                personal_best_positions = np.array(ast.literal_eval(best_opt_data["personal_best_positions"]))
                personal_best_scores = ast.literal_eval(best_opt_data["personal_best_scores"])
                global_best_position = np.array(ast.literal_eval(best_opt_data["global_best_position"]))
                global_best_score = float(best_opt_data["global_best_score"])
                global_best_scores_history = ast.literal_eval(best_opt_data["global_best_scores_history"])

            return velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history
            
        except Exception as e:
            self.main.reload = False
            self.e = e
            self.main.error_tracking = True
            AuxClass._handle_exception(self, e, "Error at def verify_stage")
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
            
            # Initialize the best positions and scores
            personal_best_positions = [list(pos) for pos in positions]
            personal_best_scores = objective_function_pso(positions)

            print("positions:", len(positions))
            print("scores:", len(personal_best_scores))
            print("personal_best_positions:", len(personal_best_positions))

            global_best_position = personal_best_positions[np.argmin(personal_best_scores)]
            global_best_score = min(personal_best_scores)
            global_best_scores_history = [global_best_score]

            # Show datas in the interface and save info
            PostPso.save_best_results(self, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history)
            PostPso.last_iteration_info(self, velocities, positions) 
            return velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history
        
        except Exception as e:
            self.e = e
            self.main.error_tracking = True
            AuxClass._handle_exception(self, e, "Error at def initial_parameters_pso")
            return [], [], [], [], None, None, []


