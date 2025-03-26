import os 
import yaml
import shutil
import psutil
import traceback
import subprocess
import concurrent.futures


class PararelSimulation():
    """
    A class to handle parallel simulation execution using Abaqus.

    The class manages the retrieval of input files, execution of simulations 
    in parallel, and the movement of output files to a designated directory.
    """
    def __init__(self):
        """ Initialize the PararelSimulation object. """
        super(PararelSimulation, self).__init__()


    def start_simulation(self, id, list_folder_path, server_folder, drive_folder, number_of_cores):  
        """
        Start the simulation process by retrieving input files 
        and running simulations in parallel.

        Args:
            id (str): The identifier for the computer or simulation group.
            list_folder_path (list): List of folder paths containing .inp files.
            server_folder (str): The folder on the server where the simulation files are stored.
            drive_folder (str): The folder on the drive where the output files will be stored.
            number_of_cores (int): Number of CPU cores to use for each simulation.
        """        
        self.path = list_folder_path
        self.number_of_cores = number_of_cores
        self.numberFiles = PararelSimulation.calculate_number_pararel_simulation(self, number_of_cores)
        PararelSimulation.getINPFile(self, server_folder)
        PararelSimulation.runSimulations(self, id, server_folder, drive_folder)
    

    def calculate_number_pararel_simulation(self, number_of_cores):
        """
        Calculate the number of parallel simulations that can be run based on available CPU cores.

        Args:
            number_of_cores (int): Number of CPU cores to allocate for each simulation.

        Returns:
            int: The number of parallel simulations that can be executed.
        """
        number_of_files = 0
        while number_of_files < 2:
            threshold = 8
            cpu_percentages = psutil.cpu_percent(percpu=True)
            num_physical_cores = psutil.cpu_count(logical=False)
            availableCores = sum(1 for i, usage in enumerate(cpu_percentages) if usage < threshold and i < num_physical_cores)
            number_of_files = int((availableCores - 2) / number_of_cores)
        return number_of_files

        
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
                    destination_folder = os.path.join(server_folder, os.path.basename(folder_path))
                    destination_path = os.path.join(server_folder, os.path.basename(folder_path), file)

                    if not os.path.exists(destination_folder):
                        os.makedirs(destination_folder)

                    if file.endswith('.inp'):
                        try:
                            shutil.copy2(source_path, destination_path) 
                            self.inpFiles.append(destination_path)  
                        except Exception as e:
                            traceback.print_exc()
                    else:
                        try:
                            if not os.path.exists(destination_path):
                                shutil.move(source_path, destination_path) 
                        except Exception as e:
                            traceback.print_exc()

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
                    print("TRY")
                    print(command)

                    os.chdir(inp_dir)
                    

                    print("Diretório atual:", os.getcwd())
                    # print("Comando:", command)

                    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate()
                    print(f"stdout: {stdout.decode()}\n", f"stderr: {stderr.decode()}\n")
                    process.wait()

                    # x = input("simulacao")

                    filename = command.split("job=")[1].split()[0]
                    print('aaaaaaaaaaaaa', os.path.exists(output_file))
                    if os.path.exists(output_file):
                        PararelSimulation.move_odb(self, filename, server_folder, drive_folder)
                        return "Sucess"
                    else:
                        print("Output file not found for {}. Retrying...".format(job_name))

                except Exception as e:
                    return f"Failed: {command}. Error: {str(e)}"
            
        # Execute simulations concurrently using ThreadPoolExecutor
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.numberFiles) as executor:
            futures = {executor.submit(runSimulationAux, inp_dir, command, server_folder, drive_folder): command for inp_dir, command in self.commands}

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
                    traceback.print_exc()
        

    def move_odb(self, filename, server_folder, drive_folder):
        """
        Move the .odb file from the simulation folder to the destination folder.

        Args:
            filename (str): The name of the .odb file to move.
            server_folder (str): The server folder where the simulation files are stored.
            drive_folder (str): The drive folder where the output files will be stored.
        """
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
