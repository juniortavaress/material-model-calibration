import os
import yaml
import shutil
import psutil
import traceback
import subprocess
import concurrent.futures
from filelock import FileLock
from datetime import datetime
from backend.pso_scripts.status_manager import StatusManager

class ParallelSimulation():
    """
    Manages the parallel execution of Abaqus simulations.
    """
    
    def run_all_simulations(self, server_folder, drive_folder, num_cores, cp_number):
        yaml_path = os.path.join(drive_folder, "auxiliary_files", "python_files_to_computers", "computers_list.yaml")

        StatusManager.schedule(lambda: StatusManager._verify_expired(yaml_path, cp_number), 1800)
        StatusManager.schedule(lambda: StatusManager._refresh_timestamps(yaml_path, cp_number), 600)

        while self._has_pending_simulations(yaml_path):
            self._start_simulations(yaml_path, server_folder, drive_folder, num_cores, cp_number)


    def _has_pending_simulations(self, yaml_path):
        with FileLock(yaml_path + ".lock"):
            computer_dict = self._read_and_write_yaml(yaml_path, "load")
        return any(str(value).startswith("True ") for key, value in computer_dict.items() if key.lower().startswith("comand"))


    def _start_simulations(self, yaml_path, server_folder, drive_folder, num_cores, cp_number):  
        num_files = self._calculate_parallel_jobs(num_cores)
        path_list, selected_keys = self._get_pending_commands(yaml_path, cp_number, num_files)
        commands = self._collect_inp_files(server_folder, path_list, num_cores)

        self._run_simulations(commands, server_folder, drive_folder, num_files)
        self._mark_completed(yaml_path, selected_keys)
    

    def _calculate_parallel_jobs(self, num_cores):
        number_of_files = 0
        while number_of_files < 2:
            threshold = 8
            cpu_percentages = psutil.cpu_percent(percpu=True)
            num_physical_cores = psutil.cpu_count(logical=False)
            availableCores = sum(1 for i, usage in enumerate(cpu_percentages) if usage < threshold and i < num_physical_cores)
            number_of_files = int((availableCores - 2) / num_cores)

        if number_of_files < 3:
            number_of_files = 3

        return number_of_files

    

    def _get_pending_commands(self, yaml_path, cp_number, num_files):
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


    def _collect_inp_files(self, server_folder, path_list, num_cores):
        commands = []
        self.inpFiles = []

        for folder in path_list:
            if os.path.isdir(folder):

                destination_folder = os.path.join(server_folder, os.path.basename(folder))
                print(destination_folder)
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
            command = rf'call C:\SIMULIA\Commands\abq2021.bat job={job_name} cpus={num_cores} interactive'
            commands.append((inp_dir, command))
        return commands


    def _run_simulations(self, commands, server_folder, drive_folder, num_file):
            
        """
        Run the Abaqus simulations in parallel.

        Each simulation command is constructed based on the input files, 
        and simulations are executed concurrently using a thread pool executor.
        """    
 
        def aux_run_simulations(inp_dir, command, server_folder, drive_folder):
            """
            Auxiliary function to run a single simulation.

            Args:
                inp_dir (str): The directory containing the .inp file.
                command (str): The command to execute the simulation.
                server_folder (str): The server folder for storing simulation files.
                drive_folder (str): The drive folder for storing output files.
            """
            retries = 3
            job_name = command.split('job=')[1].split()[0]
            output_file = os.path.join(inp_dir, f"{job_name}.odb")

            for attempt in range(1, retries + 1):
                try:
                    # x = input("COLOCA A SIMULACAO:")

                    os.chdir(inp_dir)
                    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate()
                    print(f"stdout: {stdout.decode()}\n", f"stderr: {stderr.decode()}\n")
                    process.wait()

                    if os.path.exists(output_file):
                        self._move_odb(job_name, server_folder, drive_folder)
                        return "Sucess"
                    else:
                        print("Output file not found for {}. Retrying...".format(job_name))

                except Exception as e:
                    return f"Failed: {command}. Error: {str(e)}"
            
        # Execute simulations concurrently using ThreadPoolExecutor
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_file) as executor:
            print(commands)
            futures = {executor.submit(aux_run_simulations, inp_dir, command, server_folder, drive_folder): command for inp_dir, command in commands}

            
            for future in concurrent.futures.as_completed(futures):
                command = futures[future]
                try:                 
                    result = future.result()
                except Exception as e:
                    traceback.print_exc()
        


    def _move_odb(self, job, server_folder, drive_folder):
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
            print("except")
            traceback.print_exc()


    def _mark_completed(self, yaml_path, selected_yaml_keys):
        
        with FileLock(yaml_path + ".lock"):
            computer_dict = self._read_and_write_yaml(yaml_path, "load")

            for key in selected_yaml_keys:
                if computer_dict[key].startswith("Running "):
                    path = computer_dict[key][8:].strip()
                    computer_dict[key] = "False " + path

            self._read_and_write_yaml(yaml_path, "save", computer_dict)


    def _read_and_write_yaml(self, yaml_path, function, computer_dict=None):
        try:
            if function == "load":
                with open(yaml_path, 'r') as file:
                    data = yaml.safe_load(file)
                    return data if isinstance(data, dict) else {}
            elif function == "save":
                with open(yaml_path, "w") as file:
                    yaml.dump(computer_dict, file)
        except Exception as e:
            print(f"[Erro ao acessar YAML] {e}")
            import traceback
            traceback.print_exc()
            return {}
        
        