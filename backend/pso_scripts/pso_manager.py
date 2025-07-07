# -*- coding: utf-8 -*-
import os
import ast
import yaml
import traceback
import numpy as np
import pandas as pd
from backend.pso_scripts.simualtion_manager import SimulationManager
from frontend.aux_files.show_status_message import StatusMessage


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
        # Setting variables
        self.reload = False
        self.process_finished = False
        self.target_values = {}
        self.parameters_boundry = {}
        self.count_iteration = 1
    
        # Get initial values for PSO
        PsoManager.get_initial_values(self)
        lb, ub, num_dimensions = PsoManager.get_boundry(self)

        # Verify project status
        velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history = PsoManager.verify_stage(self)
        PsoManager.verify_iteration_progress(self)

        if not self.process_finished:
            # Define the objective function to be minimized
            objective_function_pso = lambda params: PsoManager.objective_function(self, params)

            # Initialize variables for iteration control
            if not self.reload:
                velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history = PsoManager.initial_parameters_pso(self, objective_function_pso, lb, ub, num_dimensions)

            # Perform the PSO iterations
            PsoManager.pso_iterations(self, objective_function_pso, lb, ub, velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history)
            
            # Showing datas
            PsoManager.show_datas(self, "finished")
        
        
    def get_initial_values(self):
        """
        Loads the initial values from the configuration file (YAML).
        """
        # Load the YAML file with project information
        with open(self.project_infos_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        # Process cutting conditions and experimental data
        if "3. Conditions" in data:
            conditions_info = data["3. Conditions"]
            for conditions, value in conditions_info.items():
                for info, info_value in value.items():
                    if info == "Cutting Properties":
                        name = info_value['name']
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

    def verify_iteration_progress(self):
        self.iteration_in_progress = False
        drive_folder = self.user_result_folder
        yaml_path = os.path.join(drive_folder, "auxiliary_files", "python_files_to_computers", "computers_list.yaml")
       
        with open(yaml_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
        
        for key, value in data.items():
            if value.startswith("True") or value.startswith("Running"):
                self.iteration_in_progress = True

        

    def verify_stage(self):
        """
        Verify the atual stage of the otimization and load datas
        """
        # Load the YAML file with project information
        with open(self.project_infos_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
            

        # Check the status of the optimization
        try:
            # If optimization is done, stop the process
            if "8. Otimization Datas" in data:
                if data["8. Otimization Datas"]["Status"] == "Done":
                    self.process_finished = True
                    return None, None, None, None, None, None, None
                    
                # If optimization is not done, load and update the iteration data
                self.reload = True
                self.count_iteration = int(data["7. PSO and Simulation"]["Iterations"])
                self.number_of_iterations = int(data["8. Otimization Datas"]["Remaining Iterations"])
                self.count_iteration = self.count_iteration - self.number_of_iterations + 1

                try:
                    positions = eval(data["8. Otimization Datas"]["Last Iteration Values"]["positions"]["value"])
                    velocities = eval(data["8. Otimization Datas"]["Last Iteration Values"]["velocities"]["value"])
                    personal_best_positions = eval(data["8. Otimization Datas"]["Last Iteration Values"]["personal_best_position"]["value"])
                    personal_best_scores =  eval(data["8. Otimization Datas"]["Last Iteration Values"]["personal_best_score"]["value"])
                    global_best_position = eval(data["8. Otimization Datas"]["Last Iteration Values"]["global_best_position"]["value"])
                    global_best_score = float(data["8. Otimization Datas"]["Last Iteration Values"]["global_best_score"]["value"])
                    global_best_scores_history = eval(data["8. Otimization Datas"]["Last Iteration Values"]["global_best_score_history"]["value"])
                    return velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history
                except Exception as e:
                    self.reload = False
                    return None, None, None, None, None, None, None                   
            
            # If optimization doesnt exist, stop the process
            else: 
                data["8. Otimization Datas"] = {
                    "Status": "pending", 
                    "Remaining Iterations": self.number_of_iterations, 
                    "Last Iteration Values": {
                        "velocities": None, 
                        "positions": None, 
                        "personal_best_position": None, 
                        "global_best_position": None, 
                        "personal_best_score": None, 
                        "global_best_score": None, 
                        "global_best_score_history": None}}
                with open(self.project_infos_path, "w", encoding="utf-8") as file:
                    yaml.safe_dump(data, file, allow_unicode=True, default_flow_style=False)
                return None, None, None, None, None, None, None

        except Exception as e:
            PsoManager._handle_error(self, e, "Error at def verify_stage")


    def get_boundry(self):
        """
        Returns the lower and upper boundaries of parameters and the number of dimensions.
        """
        lb, ub = [], []
        for _ , info in self.parameters_boundry.items():
            for type, value in info.items():
                lb.append(float(value)) if type == "min" else ub.append(float(value))
        return lb, ub, len(self.parameters_boundry) 


    def initial_parameters_pso(self, objective_function_pso, lb, ub, num_dimensions):
        """
        Initializes the parameters for the first PSO iteration.
        """
        try:
            # Initialize positions and velocities of the particles
            positions = np.round(np.random.uniform(low=lb, high=ub, size=(self.number_of_particles, num_dimensions)), 4).tolist()
            velocities = np.random.uniform(low=-1, high=1, size=(self.number_of_particles, num_dimensions)).tolist()
            PsoManager.save_parameters(self, self.number_of_particles, positions)
            
            # Initialize the best positions and scores
            personal_best_positions = [list(pos) for pos in positions]
            personal_best_scores = objective_function_pso(positions)
            global_best_position = personal_best_positions[np.argmin(personal_best_scores)]
            global_best_score = min(personal_best_scores)
            global_best_scores_history = [global_best_score]

            # Show datas in the interface and save info
            PsoManager.show_datas(self)
            PsoManager.save_iteration_info(self, velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history)
            return velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history
        
        except Exception as e:
            PsoManager._handle_error(self, e, "Error at def initial_parameters_pso")


    def pso_iterations(self, objective_function_pso, lb, ub, velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history, minfunc=1e-3):
        """
        Performs the PSO iterations to optimize the parameters.

        Returns:
            global_best_position (array): Best global position found after iterations.
            global_best_score (float): Best global score (error) found after iterations.
        """
        try:
            
            # Perform PSO optimization
            for iteration in range(self.number_of_iterations):
                if not self.iteration_in_progress:
                    print("TAMO AQUI CAMBADA")
                    for i in range(self.number_of_particles):
                        r1, r2 = np.random.rand(), np.random.rand()

                        # Update velocity and position based on the PSO equation
                        velocities[i] = (self.w * np.array(velocities[i]) + 
                                        self.fip * r1 * (np.array(personal_best_positions[i]) - np.array(positions[i])) + 
                                        self.fig * r2 * (np.array(global_best_position) - np.array(positions[i])))
                        positions[i] += velocities[i]
                        positions[i] = np.round(np.clip(positions[i], lb, ub), 4)
                        PsoManager.save_parameters(self, self.number_of_particles, positions)
                    
                if self.iteration_in_progress:
                    PsoManager.save_parameters(self, self.number_of_particles, positions)

                # Evaluate the objective function for the current positions
                score = objective_function_pso(positions)
                self.iteration_in_progress = False

                # Update personal best positions and scores
                for i in range(self.number_of_particles):
                    if float(score[i]) < float(personal_best_scores[i]):
                        personal_best_scores[i] = score[i]
                        personal_best_positions[i] = positions[i]
                    if score[i] < global_best_score:
                        global_best_score = score[i]
                        global_best_position = positions[i]
                global_best_scores_history.append(global_best_score)

                # # Check stopping criteria
                # if global_best_score < minfunc:
                #     print(f"Stopping criterion met at iteration {iteration+1}")
                #     break

                PsoManager.show_datas(self)
                
                velocities = [v.tolist() for v in velocities]  
                positions = [p.tolist() for p in positions] 




                PsoManager.save_iteration_info(self, velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history)
            return global_best_position, global_best_score
        except Exception as e:
            PsoManager._handle_error(self, e, "Error at def pso_iterations")


    def objective_function(self, parameters=None):
        """
        Objective function calculates errors based on simulated forces and temperatures
        compared to experimental data.

        Returns:
            list: Errors for each parameter set.
        """
        # try:
        error_list = []
        current_iteration = f"Iteration 0{self.count_iteration}" if self.count_iteration < 10 else f"Iteration {self.count_iteration}"      

        # Format the parameters 
        for index, param in enumerate(parameters):
            formatted_coords = '[' + ', '.join(map(lambda x: str(np.round(x, 4)), param)) + ']'
            self.info_set[current_iteration][f"set-0{index+1}"]["Parameters Map"] = formatted_coords
        
        # Run the simulation
        SimulationManager.simulation_manager(self)

        # Get the error for each parameter set
        df = pd.read_excel(os.path.join(self.excel_files, "datas.xlsx"))

        for iteration, info in self.info_set.items():

            # print('\n\n\n')
            # print(iteration)
            # print(current_iteration)
            # print('\n\n\n')

            if iteration == current_iteration:
                for set_name, data in info.items():

                    param_values = ast.literal_eval(data["Parameters Map"])                     
                    param_columns = df.columns[4:4+len(param_values)]

                    filter_conditions = [] 
                    for i, value in enumerate(param_values): 
                        filter_conditions.append(df[param_columns[i]] == value)  

                    filtered_row = df[filter_conditions[0]] 

                    for condition in filter_conditions[1:]:  
                        filtered_row = filtered_row.loc[condition]
                    
                    # print('\n\n\n')
                    # print(df)
                    # print(param_values)
                    # print('param_columns', param_columns)
                    # print("filtered_row", filtered_row)
                    # print("filter_conditions", filter_conditions)

                    # print('\n\n\n')

                    if not filtered_row.empty:
                        self.info_set[current_iteration][set_name]["Error"] = str(filtered_row["Error"].mean())
                    else:
                        self.info_set[current_iteration][set_name]["Error"] = 1  

        # Creating list of error to return to the objective function
        for iteration, info in self.info_set.items():
            if iteration == current_iteration:
                for set_name, data in info.items():
                    error_list.append(float(data["Error"]))

        info_set_path = os.path.join(self.user_config, "parameters.yaml")
        with open(info_set_path, "w") as file:
            yaml.dump(self.info_set, file)

        return error_list
    
        # except Exception as e:
        #     PsoManager._handle_error(self, e, "Error at def objective_function")
        

    def save_parameters(self, num_particles, positions):
        """
        Saves the current parameters to a JSON file.

        Args:
            num_particles (int): The number of particles.
            positions (array): The current positions of the particles.
        """
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
                param_value = positions[i][j]
                if isinstance(param_value, np.generic):
                    param_value = param_value.item()  
                self.info_set[iteration_key][set_key]["Parameters"][param_name] = param_value

        with open(info_set_path, "w") as file:
            yaml.dump(self.info_set, file)
        

    def save_iteration_info(self, velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history):
        """ Save iteration infos for restart if necessary """
        self.count_iteration += 1
        self.number_of_iterations -= 1

        with open(self.project_infos_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        last_iteration_values = {
            "velocities": {"type": str(type(velocities)), "value": str(velocities)},
            "positions": {"type": str(type(positions)), "value": str(positions)},
            "personal_best_position": {"type": str(type(personal_best_positions)), "value": str(personal_best_positions)},
            "personal_best_score": {"type": str(type(personal_best_scores)), "value": str(personal_best_scores)},
            "global_best_position": {"type": str(type(global_best_position)), "value": str(global_best_position)},
            'global_best_score': {"type": str(type(global_best_score)), "value": str(global_best_score)},
            "global_best_score_history": {"type": str(type(global_best_scores_history)), "value": str(global_best_scores_history)}}
        
        data["8. Otimization Datas"]["Last Iteration Values"] = last_iteration_values
        data["8. Otimization Datas"]["Remaining Iterations"] = self.number_of_iterations

        if self.number_of_iterations == 0:
            data["8. Otimization Datas"]["Status"] = "Done"

        with open(self.project_infos_path, "w", encoding="utf-8") as file:
            yaml.safe_dump(data, file, allow_unicode=True, default_flow_style=False)


    def show_datas(self, call=None):
        """ Get datas to show in the interface """
        best_set = None
        min_error = float("inf")

        iteration_number = self.count_iteration - 1 if call == "finished" else self.count_iteration
        current_iteration = f"Iteration {int(iteration_number):02d}"   

        # print("\n\nCURRENT ITERATION", current_iteration)
        # print("\n\nINFO SET", self.info_set)

        iteration_number = (self.count_iteration - 1) if call == "finished" else self.count_iteration

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
            self.error_cutting_force = filtered_mean["Error Fc"]
            self.error_normal_force = filtered_mean["Error Fn"]
            self.error_CCR = filtered_mean["Error CCR"]
            self.error_CSR = filtered_mean["Error CSR"]
            StatusMessage.set_text(self, message)
        

    def _handle_error(self, exception, stage):
        """
        Handles errors by logging them, updating error tracking, and sending a status message.
        """
        print("DEU ERRO CARALHO")
        self.e = exception
        self.stage = stage
        self.error_tracking = True
        StatusMessage.set_text(self, "message-error")
        traceback.print_exc()
        input("precione enter para seguir")




