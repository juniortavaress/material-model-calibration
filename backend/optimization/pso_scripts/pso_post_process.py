import os
import numpy as np
import pandas as pd
from frontend.aux_files.tracking_message_manager import ProcessStatusLogger


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

        for i in range(num_particles):
            set_number = i + 1

            # Monta os valores para salvar
            param_values = {}
            for j, (param_name, _) in enumerate(self.parameters_boundry.items()):
                param_value = positions[i][j]
                param_value = param_value.item() if isinstance(param_value, np.generic) else param_value
                db_field = f"parameter_{param_name}"  # Ex: 'A' -> 'parameter_a'
                # print('db_field', db_field)
                param_values[db_field] = param_value

            response = self.main.supabase.table("conditions").select("*").eq("project_id", self.main.project_id).execute()
            db_conditions = response.data if response.data else []
            for cond in db_conditions:
                cond_name = cond["name"]

                # Verifica se já existe um registro no banco
                response = (
                    self.main.supabase
                    .from_('results')
                    .select('id')
                    .eq('project_id', self.main.project_id)
                    .eq('condition_name', cond_name)
                    .eq('iteration_number', self.main.current_opt)
                    .eq('parameter_set', set_number)
                    .limit(1)
                    .execute()
                )

                data = response.data
                if data:
                    # Atualiza registro existente
                    result_id = data[0]['id']
                    self.main.supabase.from_('results').update(param_values).eq('id', result_id).execute()
                else:
                    # Insere novo registro
                    new_row = {
                        'project_id': self.main.project_id,
                        'condition_name': cond_name,
                        'iteration_number': self.main.current_opt,
                        'parameter_set': set_number,
                        **param_values
                    }
                    self.main.supabase.from_('results').insert(new_row).execute()
            
            PostPso.save_current_iteration(self, velocities, positions)

        
    def save_current_iteration(self, velocities, positions):
        record = self.main.supabase.table("current_optimization_data").select("*").eq("project_id", self.main.project_id).execute().data

        data_to_save = {
            "project_id": self.main.project_id,
            "iteration": self.main.current_opt,
            "velocities": str(PostPso.to_list_if_numpy(velocities)),
            "positions": str(PostPso.to_list_if_numpy(positions)),
        }

        if record:
            # Atualiza a linha existente
            self.main.supabase.table("current_optimization_data") \
                .update(data_to_save).eq("project_id", self.main.project_id).execute()
        else:
            # Insere uma nova linha
            self.main.supabase.table("current_optimization_data") \
                .insert(data_to_save).execute()


    def last_iteration_info(self, velocities, positions) -> None:
        """
        Save the last optimization information to the database.
        """
        record = self.main.supabase.table("last_optimization_data").select("*").eq("project_id", self.main.project_id).execute().data
        velocities_str = str(PostPso.to_list_if_numpy(velocities))
        positions_str = str(PostPso.to_list_if_numpy(positions))
        
        data_to_save = {
            "project_id": self.main.project_id,
            "remaining_iterations": self.number_of_iterations,
            "velocities": velocities_str,
            "positions": positions_str,
        }

        if record:
            # Atualiza a linha existente
            self.main.supabase.table("last_optimization_data").update(data_to_save).eq("project_id", self.main.project_id).execute()
        else:
            # Insere uma nova linha
            self.main.supabase.table("last_optimization_data").insert(data_to_save).execute()

    
    def save_best_results(self, personal_best_positions, personal_best_scores, global_best_position, global_best_score, global_best_scores_history):
        record = self.main.supabase.table("best_optimization_data").select("*").eq("project_id", self.main.project_id).execute().data

        data_to_save = {
            "project_id": self.main.project_id,
            "personal_best_positions": str(PostPso.to_list_if_numpy(personal_best_positions)),
            "personal_best_scores": str(personal_best_scores),
            "global_best_position": str(PostPso.to_list_if_numpy(global_best_position)),
            "global_best_score": float(global_best_score),
            "global_best_scores_history": str(global_best_scores_history)
        }

        if record:
            # Atualiza a linha existente
            self.main.supabase.table("best_optimization_data") \
                .update(data_to_save).eq("project_id", self.main.project_id).execute()
        else:
            # Insere uma nova linha
            self.main.supabase.table("best_optimization_data") \
                .insert(data_to_save).execute()    
            

    def save_parameters(self, num_particles, positions) -> None:
        """
        Saves the current parameters to a JSON file.

        Args:
            num_particles (int): The number of particles.
            positions (array): The current positions of the particles.
        """
        response = self.main.supabase.table("conditions").select("*").eq("project_id", self.main.project_id).execute()
        db_conditions = response.data if response.data else []
        parameter_names = list(self.parameters_boundry.keys())  # ['A','B','C1',...]
    
        for i in range(num_particles):
            set_number = i + 1
            iteration_number = self.main.current_opt

            # Prepare parameters dictionary
            params_dict = {}
            for j, param_name in enumerate(parameter_names):
                value = positions[i][j]
                value = value.item() if isinstance(value, np.generic) else value
                params_dict[f"parameter_{param_name}"] = value


            # Define the unique key for upsert
            for cond in db_conditions:
                cond_name = cond["name"]

                base_filter = (
                    self.main.supabase.table("results")
                    .select("id")
                    .eq("project_id", self.main.project_id)
                    .eq("iteration_number", iteration_number)
                    .eq("parameter_set", set_number)
                    .eq("condition_name", cond_name)
                    .execute()
                )
                    
                upsert_data = {
                    "project_id": self.main.project_id,
                    "condition_name": cond_name,
                    "iteration_number": iteration_number,
                    "parameter_set": set_number,
                    **params_dict
                }

                if base_filter.data:  
                    # se já existe → update
                    record_id = base_filter.data[0]["id"]
                    self.main.supabase.table("results").update(upsert_data).eq("id", record_id).execute()
                else:
                    # se não existe → insert
                    self.main.supabase.table("results").insert(upsert_data).execute()