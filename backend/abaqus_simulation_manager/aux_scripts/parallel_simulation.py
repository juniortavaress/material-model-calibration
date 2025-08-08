import os
import yaml
import shutil
import psutil
import traceback
import subprocess
import concurrent.futures
from datetime import datetime
from filelock import FileLock
from typing import List, Tuple, Optional
from backend.abaqus_simulation_manager.aux_scripts.status_manager import StatusManager

class ParallelSimulation():
    """
    Manages the parallel execution of Abaqus simulations.
    """
    
    def run_all_simulations(self, server_folder, drive_folder, yaml_computer_list, odb_processing, abq_path, num_cores, cp_number) -> None:
        """
        Orchestrates the entire simulation process with periodic status updates.

        Args:
            server_folder (str): Path to the server folder where simulations run.
            drive_folder (str): Path to the drive folder for output files.
            yaml_computer_list (str): Path to the YAML file with simulation commands.
            odb_processing (bool): Flag indicating if odb files are being processed.
            num_cores (int): Number of CPU cores available for parallel simulations.
            cp_number (int): Identifier for the compute process or machine.
        """
        self.abaqus_path = abq_path
        StatusManager.schedule(lambda: StatusManager.reset_expired_tasks(yaml_computer_list, cp_number), 1800)
        StatusManager.schedule(lambda: StatusManager.update_status_and_timestamp(yaml_computer_list, odb_processing, cp_number), 600)

        while self._has_pending_simulations(yaml_computer_list):
            self._execute_simulation_batch(yaml_computer_list, server_folder, drive_folder, num_cores, cp_number)


    def _has_pending_simulations(self, yaml_path) -> bool:
        """
        Checks if there are any pending simulations marked as 'True' in the YAML file.

        Args:
            yaml_path (str): Path to the YAML file.

        Returns:
            bool: True if there are pending simulations; False otherwise.
        """
        with FileLock(yaml_path + ".lock"):
            computer_dict = self._read_and_write_yaml(yaml_path, "load")
        return any(str(value).startswith("True ") for key, value in computer_dict.items() if key.lower().startswith("comand"))


    def _execute_simulation_batch(self, yaml_path, server_folder, drive_folder, num_cores, cp_number) -> None:
        """
        Runs a batch of simulations in parallel according to available CPU cores.

        Args:
            yaml_path (str): Path to the YAML file with commands.
            server_folder (str): Path to the server folder.
            drive_folder (str): Path to the drive folder.
            num_cores (int): Number of CPU cores for each simulation.
            cp_number (int): Compute process identifier.
        """
        jobs_to_run = self._calculate_parallel_jobs(num_cores)
        inp_paths, yaml_keys = self._reserve_jobs(yaml_path, cp_number, jobs_to_run)
        commands = self._prepare_simulation_commands(server_folder, inp_paths, num_cores)
        self._run_simulations_concurrently(commands, server_folder, drive_folder, jobs_to_run, yaml_path, yaml_keys)
    

    def _calculate_parallel_jobs(self, num_cores) -> int:
        """
        Calculates how many simulations can run in parallel based on CPU usage.

        Args:
            num_cores (int): Number of cores required per simulation.

        Returns:
            int: Number of jobs that can be run in parallel (minimum 3).
        """
        jobs = 0
        while jobs < 2:
            threshold = 15  # max %CPU usage per core considered free
            usages = psutil.cpu_percent(percpu=True)
            physical_cores = psutil.cpu_count(logical=False)
            available = sum(1 for i, usage in enumerate(usages) if usage < threshold and i < physical_cores)
            jobs = max((available - 2) // num_cores, 0)
        return max(jobs, 3)

    
    def _reserve_jobs(self, yaml_path, cp_number, num_files) -> Tuple[List[str], List[str]]:
        """
        Marks the selected jobs as 'Running' and returns their input paths and keys.

        Args:
            yaml_path (str): Path to the YAML file.
            cp_number (int): Compute process identifier.
            num_files (int): Number of jobs to reserve.

        Returns:
            Tuple[List[str], List[str]]: List of input folder paths and corresponding YAML keys.
        """
        with FileLock(yaml_path + ".lock"):
            computer_dict = self._read_and_write_yaml(yaml_path, "load")
            command_keys = sorted((k for k in computer_dict if k.lower().startswith("comand")), key=lambda x: int(x[6:]))
            selected_keys = [k for k in command_keys if str(computer_dict[k]).startswith("True ")] [:num_files]

            path_list = []
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            for key in selected_keys:
                path = computer_dict[key][5:].strip()
                path_list.append(path)
                computer_dict[key] = f"Running ({cp_number} - {now}) {path}"

            self._read_and_write_yaml(yaml_path, "save", computer_dict)
            return path_list, selected_keys


    def _prepare_simulation_commands(self, server_folder, path_list, num_cores) -> List[Tuple[str, str]]:
        """
        Copies simulation files to the server folder and prepares commands for execution.

        Args:
            server_folder (str): Destination folder on the server.
            path_list (List[str]): List of source folders containing simulation input files.
            num_cores (int): Number of cores to use per simulation.

        Returns:
            List[Tuple[str, str]]: List of tuples with input directory and command string.
        """
        commands = []
        self.inpFiles = []

        for folder in path_list:
            if os.path.isdir(folder):
                destination_folder = os.path.join(server_folder, os.path.basename(folder))

                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                for file in os.listdir(folder):                  
                    source_path = os.path.join(folder, file)                  
                    destination_path = os.path.join(server_folder, os.path.basename(folder), file)

                    try:
                        shutil.copy2(source_path, destination_path) 
                        if file.endswith('.inp'):
                            self.inpFiles.append(destination_path)  
                    except Exception:
                        traceback.print_exc()

        for inp in self.inpFiles:
            inp_dir = os.path.dirname(inp)
            job_name = os.path.basename(inp).replace(".inp", "")
            command = rf'call {self.abaqus_path} job={job_name} cpus={num_cores} interactive'
            commands.append((inp_dir, command))
        return commands


    def _run_simulations_concurrently(self, commands, server_folder, drive_folder, num_file, yaml_path, yaml_keys) -> None:
        """
        Executes simulations concurrently using ThreadPoolExecutor.

        Args:
            commands (List[Tuple[str, str]]): List of tuples (input directory, command).
            server_folder (str): Server folder path.
            drive_folder (str): Drive folder path.
            num_file (int): Number of concurrent jobs.
            yaml_path (str): Path to YAML file.
            yaml_keys (List[str]): YAML keys for the jobs.
        """
        def aux_run_simulations(inp_dir, command, server_folder, drive_folder, yaml_path, yaml_keys) -> Optional[str]:
            """
            Auxiliary function to run a single simulation.

            Args:
                inp_dir (str): Directory containing the .inp file.
                command (str): Command to execute the simulation.
                server_folder (str): Server folder for simulation files.
                drive_folder (str): Drive folder for output files.
                yaml_path (str): Path to YAML file.
                yaml_keys (List[str]): YAML keys for the jobs.

            Returns:
                Optional[str]: Success message or error description.
            """
            retries = 3
            job_name = command.split('job=')[1].split()[0]
            output_file = os.path.join(inp_dir, f"{job_name}.odb")
            # print(command)
            # x = input("COLOCA A SIMULACAO AI:")

            for attempt in range(1, retries + 1):
                try:
                    print("COMANDO: ", command)
                    os.chdir(inp_dir)
                    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate()
                    print(f"stdout: {stdout.decode()}\n", f"stderr: {stderr.decode()}\n")
                    process.wait()

                    if os.path.exists(output_file):
                        self._move_odb(job_name, server_folder, drive_folder)
                        self._mark_jobs_as_completed(yaml_path, yaml_keys, f"{job_name}")
                        return "Sucess"
                    else:
                        print("Output file not found for {}. Retrying...".format(job_name))

                except Exception as e:
                    return f"Failed: {command}. Error: {str(e)}"
            
        # Execute simulations concurrently using ThreadPoolExecutor
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_file) as executor:
            futures = {executor.submit(aux_run_simulations, inp_dir, command, server_folder, drive_folder, yaml_path, yaml_keys): command for inp_dir, command in commands}

            for future in concurrent.futures.as_completed(futures):
                command = futures[future]
                try:                 
                    result = future.result()
                except Exception as e:
                    traceback.print_exc()
                    print(e)
        


    def _move_odb(self, job, server_folder, drive_folder) -> None:
        """
        Moves the generated .odb file from the server folder to the drive folder.

        Args:
            job (str): Job name.
            server_folder (str): Server folder path.
            drive_folder (str): Drive folder path.
        """
        try:
            destination_odb_folder = os.path.join(drive_folder, "auxiliary_files", "odb_processing")
            for folder_name in os.listdir(server_folder):
                if folder_name == job:
                    folder_path = os.path.join(server_folder, folder_name)
                    if os.path.isdir(folder_path) and folder_name.lower() != "defaut":
                        for root, _, files in os.walk(folder_path):
                            for file in files:
                                if file.endswith(".odb"):
                                    source_path = os.path.join(root, file) 
                                    destination_path = os.path.join(destination_odb_folder, file)  
                                    shutil.copy2(source_path, destination_path)
                                    os.remove(source_path)
        except:
            traceback.print_exc()


    def _mark_jobs_as_completed(self, yaml_path, selected_yaml_keys, file_key) -> None:
        """
        Marks jobs as completed in the YAML file.

        Args:
            yaml_path (str): Path to the YAML file.
            selected_yaml_keys (List[str]): List of YAML keys to update.
            file_key (str): Filename key to match in the job string.
        """
        with FileLock(yaml_path + ".lock"):
            computer_dict = self._read_and_write_yaml(yaml_path, "load")

            for key in selected_yaml_keys:
                value = computer_dict.get(key, "")
                if value.startswith("Running ") and file_key in value:
                    path = computer_dict[key][8:].strip()
                    computer_dict[key] = "False " + path
            self._read_and_write_yaml(yaml_path, "save", computer_dict)


    def _read_and_write_yaml(self, yaml_path, function, computer_dict = None) -> dict:
        """
        Reads or writes the YAML file based on the function argument.

        Args:
            yaml_path (str): Path to the YAML file.
            function (str): "load" to read or "save" to write.
            computer_dict (dict, optional): Data to write if function is "save".

        Returns:
            dict: The loaded dictionary when loading; empty dict on error or when saving.
        """
        try:
            if function == "load":
                with open(yaml_path, 'r') as file:
                    data = yaml.safe_load(file)
                    return data if isinstance(data, dict) else {}
            elif function == "save":
                with open(yaml_path, "w") as file:
                    yaml.dump(computer_dict, file)
        except Exception as e:
            import traceback
            traceback.print_exc()
            return {}
        
        