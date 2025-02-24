# -*- coding: utf-8 -*-
import os
import ast
import yaml
import numpy as np
import pandas as pd

from backend.pso.simualtion_manager import SimulationManager
# from simualtion_manager import SimulationManager

class PsoManager():
    """
    Manages the Particle Swarm Optimization (PSO) algorithm.
    """
    def run_pso(self):
        """
        Runs the PSO algorithm to minimize the objective function.

        Returns:
            count_iteration (int): The number of iterations performed.
            best_position (array): The best position found during iterations.
            best_score (float): The best score (error) corresponding to the best position.
        """

        # Get initial values for PSO
        PsoManager.get_initial_values(self)

        # Define the objective function to be minimized
        objective_function_pso = lambda params: PsoManager.objective_function(self, params)

        # Verify project status
        self.reload = False
        # PsoManager.verify_stage(self)

        # Initialize variables for iteration control
        if not self.reload:
            num_int, lb, ub, num_particles, velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history = PsoManager.initial_parameters_pso(self, objective_function_pso)
        else:
            pass

        # # Perform the PSO iterations
        # best_position, best_score = PsoManager.pso_iterations(self, objective_function_pso, num_int, lb, ub, num_particles, velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history)
        # return self.count_iteration, best_position, best_score
        return self.count_iteration, [0,0,0], 0
        


    def get_initial_values(self):
        """
        Loads the initial values from the configuration file (YAML).
        """
        self.target_values = {}
        self.parameters_boundry = {}
        self.count_iteration = 1

        # Load the YAML file with project information
        with open(self.project_infos_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        # Process cutting conditions and experimental data
        if "3. Conditions" in data:
            conditions_info = data["3. Conditions"]
            for conditions, value in conditions_info.items():
                for info, info_value in value.items():
                    if info == "Cutting Properties":
                        name = f"v{info_value['velocity']}_h{info_value['deepCuth']}_gam{info_value['rakeAngle']}"
                    elif info == "Experimental Datas":
                        values = {"fc": float(info_value["cutting_force"]), "fn": float(info_value["normal_force"]), "ccr": float(info_value["chip_compression"]), "csr": float(info_value["chip_segmentation"])}
                        self.target_values[name] = values

        # Process parameter limits
        if "6. Parameters Limits" in data:
            self.parameters_boundry = data["6. Parameters Limits"]

        # Process PSO and simulation data
        if "7. PSO and Simulation" in data:
            self.number_of_cp = int(data["7. PSO and Simulation"]["Computers"])
            self.cores_by_simulation = int(data["7. PSO and Simulation"]["Cores by Simulation"])
            self.number_of_iterations = int(data["7. PSO and Simulation"]["Iterations"])
            self.number_of_particles = int(data["7. PSO and Simulation"]["Particles"])
            self.cutting_conditions = int(data["7. PSO and Simulation"]["Cutting Conditions"])
            self.fig = float(data["7. PSO and Simulation"]["fig"])
            self.fip = float(data["7. PSO and Simulation"]["fip"])
            self.w = float(data["7. PSO and Simulation"]["w"])
            self.main_computer = data["7. PSO and Simulation"]["Main Computer"]

        # Check the status of the optimization
        if "8. Otimization Datas" in data:
            if data["8. Otimization Datas"]["Status"] == "Done":
                print("COLOCA DIRETO NA PAGINA DE RESULTADOS")

            else:
                print(0)
                #pegar last datas
                #pegar quantas iteracors foram
                #new number interactions = number interactions - interacoes feitas
                #redireciona para a pagina de status
                #apagar arquivos da iteracao que falhou
                #print("DEU ERRADO TRUTA")


    def initial_parameters_pso(self, objective_function_pso):
        lb, ub = [], []
        num_int = self.number_of_iterations-1
        num_dimensions = len(self.parameters_boundry)
        
        # Define parameter bounds
        for _ , info in self.parameters_boundry.items():
            for type, value in info.items():
                lb.append(float(value)) if type == "min" else ub.append(float(value))

        # Initialize positions and velocities of the particles
        positions = np.round(np.random.uniform(low=lb, high=ub, size=(self.number_of_particles, num_dimensions)), 2)
        velocities = np.random.uniform(low=-1, high=1, size=(self.number_of_particles, num_dimensions))

        PsoManager.save_parameters(self, self.number_of_particles, positions)
        
        # Initialize the best positions and scores
        personal_best_positions = np.copy(positions)
        personal_best_scores = np.array(objective_function_pso(positions))
        global_best_position = personal_best_positions[np.argmin(personal_best_scores)]
        global_best_score = min(personal_best_scores)
        global_best_scores_history = [global_best_score]

        self.count_iteration += 1

        return num_int, lb, ub, self.number_of_particles, velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history


    def pso_iterations(self, objective_function_pso, num_int, lb, ub, num_particles, velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history, minfunc=1e-3):
        """
        Performs the PSO iterations to optimize the parameters.

        Returns:
            global_best_position (array): Best global position found after iterations.
            global_best_score (float): Best global score (error) found after iterations.
        """
        # Perform PSO optimization
        for iteration in range(num_int):
            for i in range(num_particles):
                r1, r2 = np.random.rand(), np.random.rand()

                # Update velocity and position based on the PSO equation
                velocities[i] = (self.w * velocities[i] + self.fip * r1 * (personal_best_positions[i] - positions[i]) + self.fig * r2 * (global_best_position - positions[i]))
                positions[i] += velocities[i]
                positions[i] = np.round(np.clip(positions[i], lb, ub), 2)
                PsoManager.save_parameters(self, num_particles, positions)

            # Evaluate the objective function for the current positions
            score = objective_function_pso(positions)

            # Update personal best positions and scores
            for i in range(num_particles):
                if score[i] < personal_best_scores[i]:
                    personal_best_scores[i] = score[i]
                    personal_best_positions[i] = positions[i]

                if score[i] < global_best_score:
                    global_best_score = score[i]
                    global_best_position = positions[i]

            global_best_scores_history.append(global_best_score)

            # Check stopping criteria
            if global_best_score < minfunc:
                print(f"Stopping criterion met at iteration {iteration+1}")
                break

            self.count_iteration += 1
        return global_best_position, global_best_score


    def objective_function(self, parameters=None):
        """
        Objective function calculates errors based on simulated forces and temperatures
        compared to experimental data.

        Returns:
            list: Errors for each parameter set.
        """
        error_list = []
        current_iteration = f"Iteration 0{self.count_iteration}"      

        # Format the parameters 
        for index, param in enumerate(parameters):
            formatted_coords = '[' + ', '.join(map(lambda x: str(np.round(x, 2)), param)) + ']'
            self.info_set[current_iteration][f"set-0{index+1}"]["Parameters Map"] = formatted_coords
        
        # Run the simulation
        SimulationManager.simulation_manager(self)

        # Get the error for each parameter set
        df = pd.read_excel(os.path.join(self.excel_files, "datas.xlsx") )

        for iteration, info in self.info_set.items():
            if iteration == current_iteration:
                for set_name, data in info.items():
                    param_values = ast.literal_eval(data["Parameters Map"])                     
                    param_columns = df.columns[3:3+len(param_values)]

                    filter_conditions = [] 
                    for i, value in enumerate(param_values): 
                        filter_conditions.append(df[param_columns[i]] == value)  

                    filtered_row = df[filter_conditions[0]] 
                    for condition in filter_conditions[1:]:  
                        filtered_row = filtered_row.loc[condition]
                    
                    if not filtered_row.empty:
                        self.info_set[current_iteration][set_name]["Error"] = filtered_row["Error"].mean()
                    else:
                        self.info_set[current_iteration][set_name]["Error"] = 1  

        # Creating list of error to return to the objective function
        for iteration, info in self.info_set.items():
            if iteration == current_iteration:
                for set_name, data in info.items():
                    error_list.append(data["Error"])

        print("\n\n===============================================\n\n")
        print("PRECISA VERIFICAR AQUI SE O ERRO TA INDO NA ORDEM CERTA")
        print("\nparameters: ", parameters)
        print("\nerror_list: ", error_list)
        print("\n\n===============================================\n\n")
        print("\n\n===============================================\n\n")
        print("INFO SET")
        print("\n", self.info_set)
        print("\n\n===============================================\n\n")
        return error_list


    def save_parameters(self, num_particles, positions):
        """
        Saves the current parameters to a JSON file.

        Args:
            num_particles (int): The number of particles.
            positions (array): The current positions of the particles.
        """
        # pass
        info_set_path = os.path.join(self.user_config, "parameters.yaml")
        if os.path.exists(info_set_path):
            with open(info_set_path, "r", encoding="utf-8") as file:
                self.info_set = yaml.safe_load(file) or {}  # Garante que não seja None
        else:
            self.info_set = {}

        iteration_key = f"Iteration {self.count_iteration:02}"
        self.info_set[iteration_key] = {}

        for i in range(num_particles):
            set_key = f"set-0{i+1}"
            self.info_set[iteration_key][set_key] = {}
            self.info_set[iteration_key][set_key]["Parameters"] = {}

            for j, (param_name, _) in enumerate(self.parameters_boundry.items()):
                param_value = positions[i, j]
                if isinstance(param_value, np.generic):
                    param_value = param_value.item()  
                self.info_set[iteration_key][set_key]["Parameters"][param_name] = param_value

        with open(info_set_path, "w") as file:
            yaml.dump(self.info_set, file)
        
  

    def save_interations_sets_error(self, set_errors):  
        
        for set_name, set_error in set_errors.items():
            self.info_set[self.count_iteration][set_name]["Error"] = set_error



if __name__ == "__main__":
    pso_manager = PsoManager()
    pso_manager.run_pso()


