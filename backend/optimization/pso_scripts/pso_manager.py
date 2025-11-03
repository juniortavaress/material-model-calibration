# -*- coding: utf-8 -*-
import logging 
import numpy as np
from typing import List, Tuple
from backend.config.aux_functions import AuxClass
from backend.optimization.pso_scripts.objective_function import ObjectiveFunction
from backend.optimization.pso_scripts.pso_post_process import PostPso

class PsoManager:
    """
    Class responsible for managing the Particle Swarm Optimization (PSO) process.
    """

    def run_pso(self, velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history, lb, ub, num_dimensions) -> None:
        """
        Executes the PSO optimization routine.

        Args:
            velocities (list): List of velocity vectors for all particles.
            positions (list): Current positions of particles.
            personal_best_positions (list): Best known positions for each particle.
            personal_best_scores (list): Best scores for each particle.
            global_best_position (list): Best known global position.
            global_best_score (float): Score of the global best position.
            global_best_scores_history (list): Historical best scores across iterations.
            lb (list): Lower bounds for each parameter.
            ub (list): Upper bounds for each parameter.
            num_dimensions (int): Dimensionality of the problem space.
        """
        objective_function_pso = lambda: ObjectiveFunction.objective_function(self)
        PsoManager.pso_iterations(self, objective_function_pso, lb, ub, velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history)
        

    def pso_iterations(self, objective_function_pso, lb, ub, velocities, positions, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history, minfunc=1e-3) -> Tuple[List[float], float]:
        """
        Runs the PSO iterations and updates all swarm data accordingly.

        Args:
            objective_function_pso: Objective function callable.
            lb: Lower bounds.
            ub: Upper bounds.
            velocities: Velocities of particles.
            positions: Current positions of particles.
            personal_best_positions: Best positions per particle.
            personal_best_scores: Best scores per particle.
            global_best_position: Best position found.
            global_best_score: Score of best position.
            global_best_scores_history: History of global best scores.
            minfunc: Minimum function value for early stopping.

        Returns:
            Tuple of final best position and score.
        """
        try:
            for iteration in range(self.number_of_iterations):
                if not self.main.iteration_in_progress:
                    for i in range(self.number_of_particles):
                        r1, r2 = np.random.rand(), np.random.rand()

                        # Update velocity
                        inertia = self.w * np.array(velocities[i])
                        cognitive = self.fip * r1 * (np.array(personal_best_positions[i]) - positions[i])
                        social = self.fig * r2 * (np.array(global_best_position) - positions[i])
                        velocities[i] = inertia + cognitive + social

                        # Update position with bounds
                        positions[i] = np.round(np.clip(positions[i] + velocities[i], lb, ub), 4)

                    PostPso.save_current_iteration(self, velocities, positions)
                    PostPso.save_parameters(self, self.number_of_particles, positions)
                else:
                    # PostPso.save_parameters(self, self.number_of_particles, positions)
                    pass

                # Evaluate the objective function for the current positions
                score = objective_function_pso()
                self.main.iteration_in_progress = False

                # Update personal best positions and scores
                for i in range(self.number_of_particles):
                    if float(score[i]) < float(personal_best_scores[i]):
                        personal_best_scores[i] = score[i]
                        personal_best_positions[i] = positions[i]
                    if score[i] < global_best_score:
                        global_best_score = score[i]
                        global_best_position = positions[i]
                global_best_scores_history.append(global_best_score)

                # Check stopping criteria
                if global_best_score < minfunc:
                    logging.info(f"Stopping criterion met at iteration {iteration + 1}")
                    break              
                
                # Attempt conversion for serialization
                try:
                    velocities = [v.tolist() for v in velocities]  
                    positions = [p.tolist() for p in positions]
                except Exception as e:
                    logging.error(f"Failed to convert velocities or positions to list: {e}")

                PostPso.save_best_results(self, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history)
                PostPso.last_iteration_info(self, velocities, positions)

            return global_best_position, global_best_score
        
        except Exception as e:
            self.e = e
            self.main.error_tracking = True
            AuxClass._handle_exception(self, e, "Error at def pso_iterations")
   