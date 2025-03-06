import os 
import yaml
import shutil
import psutil
import traceback
import subprocess
import concurrent.futures


class PararelSimulation():
    def __init__(self):
        super(PararelSimulation, self).__init__()

    def start_simulation(self, id, list_folder_path, server_folder, drive_folder, number_of_cores):  
        """
        Start the simulation process by retrieving input files 
        and running simulations in parallel.

        Args:
            list_folder_path (list): List of folder paths containing .inp files.
            number_of_cores (int): Number of CPU cores to use for each simulation.
            number_parallel_sim (int): Number of parallel simulations to run.
        """           
        self.path = list_folder_path
        self.number_of_cores = number_of_cores
        self.numberFiles = PararelSimulation.calculate_number_pararel_simulation(self, number_of_cores)
        PararelSimulation.getINPFile(self, server_folder)
        PararelSimulation.runSimulations(self, id, server_folder, drive_folder)
    

    def calculate_number_pararel_simulation(self, number_of_cores):
        threshold = 8
        cpu_percentages = psutil.cpu_percent(percpu=True)
        num_physical_cores = psutil.cpu_count(logical=False)
        availableCores = sum(1 for i, usage in enumerate(cpu_percentages) if usage < threshold and i < num_physical_cores)
        return int((availableCores - 2) / number_of_cores)

        

    def getINPFile(self, server_folder):
        """
        Retrieve all .inp files from the provided directories.

        This method scans each folder in the provided list of paths and 
        collects the full paths of files with the `.inp` extension.
        """
        self.inpFiles = []
        for folder_path in self.path:
            if os.path.isdir(folder_path):
                for file in os.listdir(folder_path):
                    source_path = os.path.join(folder_path, file)
                    destination_path = os.path.join(server_folder, os.path.basename(folder_path))

                    if not os.path.exists(destination_path):
                        os.makedirs(destination_path)

                    if file.endswith('.inp'):
                        try:
                            shutil.copy2(source_path, destination_path) 
                            self.inpFiles.append(os.path.join(destination_path, file))  
                        except Exception as e:
                            print(f"Error copying {source_path} to {destination_path}: {e}")
                    else:
                        try:
                            shutil.move(source_path, destination_path) 
                        except Exception as e:
                            pass

        self.commands = []
        for inp in self.inpFiles:
            inp_dir = os.path.dirname(inp)
            command = rf'call C:\SIMULIA\Commands\abq2021.bat job={os.path.basename(inp)[:-4]} cpus={self.number_of_cores} interactive'
            self.commands.append((inp_dir, command))


    def runSimulations(self, id, server_folder, drive_folder):
        """
        Run the Abaqus simulations in parallel.

        Each simulation command is constructed based on the input files, 
        and simulations are executed concurrently using a thread pool executor.
        """       
        def runSimulationAux(inp_dir, command, server_folder, drive_folder):
            retries = 3
            job_name = command.split('job=')[1].split()[0]
            output_file = os.path.join(inp_dir, f"{job_name}.odb")

            for attempt in range(1, retries + 1):
                try:
                    os.chdir(inp_dir)
                    # process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    # stdout, stderr = process.communicate()
                    # print(f"stdout: {stdout.decode()}\n", f"stderr: {stderr.decode()}\n")
                    # process.wait()

                    ##############################

                    input("coloca ai a sim")

                    ##############################

                    filename = command.split("job=")[1].split()[0]
                    if os.path.exists(output_file):
                        PararelSimulation.move_odb(self, filename, server_folder, drive_folder)
                        return "Sucess"
                    else:
                        print("Output file not found for {}. Retrying...".format(job_name))

                except Exception as e:
                    return f"Failed: {command}. Error: {str(e)}"
            
        # Using ThreadPoolExecutor to manage the queue of simulations
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.numberFiles) as executor:
            # Submit all commands to the executor
            futures = {executor.submit(runSimulationAux, inp_dir, command, server_folder, drive_folder): command for inp_dir, command in self.commands}

            # Process as they complete
            for future in concurrent.futures.as_completed(futures):
                command = futures[future]
                try:                 
                    result = future.result()

                    yaml_path = os.path.join(drive_folder, "auxiliary_files\python_files_to_computers\computers_list.yaml")
                    with open(yaml_path, "r") as file:
                        data = yaml.safe_load(file)

                    data[f"Computer {id[-1:]}"]["status"] = False
                    with open(yaml_path, "w") as file:
                        yaml.dump(data, file)

                except Exception as e:
                    print(f"Simulation {command} generated an exception: {e}")
        

    def move_odb(self, filename, server_folder, drive_folder):
        try:
            destination_odb_folder = os.path.join(drive_folder, r"auxiliary_files\odb_processing")
            for folder_name in os.listdir(server_folder):
                if folder_name == filename:
                    folder_path = os.path.join(server_folder, folder_name)
                    if os.path.isdir(folder_path) and folder_name.lower() != "defaut":
                        for root, dirs, files in os.walk(folder_path):
                            for file in files:
                                if file.endswith(".odb"):
                                    source_path = os.path.join(root, file) 
                                    destination_path = os.path.join(destination_odb_folder, file)  
                                    shutil.copy2(source_path, destination_path)
                                    os.remove(source_path)
        except:
            traceback.print_exc()
