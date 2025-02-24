import os 
import re
import json
import yaml
import subprocess
import concurrent.futures
import psutil
import time
import shutil
from backend.get_result_from_odb_file.main_results import getResults
# from get_result_from_odb_file.main_results import getResults

class PararelSimulation():
    def __init__(self):
        super(PararelSimulation, self).__init__()

    def start_simulation(self, id, list_folder_path, number_of_cores, number_pararell_sim):  
        """
        Start the simulation process by retrieving input files 
        and running simulations in parallel.

        Args:
            list_folder_path (list): List of folder paths containing .inp files.
            number_of_cores (int): Number of CPU cores to use for each simulation.
            number_parallel_sim (int): Number of parallel simulations to run.
        """   

        # for i, file in enumerate(list_folder_path):
        #     print(id, file)  
        
        self.path = list_folder_path
        self.number_of_cores = number_of_cores
        self.numberFiles = number_pararell_sim

        PararelSimulation.getINPFile(self)
        PararelSimulation.runSimulations(self, id)
        

    def getINPFile(self):
        """
        Retrieve all .inp files from the provided directories.

        This method scans each folder in the provided list of paths and 
        collects the full paths of files with the `.inp` extension.
        """
        self.inpFiles = []

        for folder_path in self.path:
            if os.path.isdir(folder_path):
                for file in os.listdir(folder_path):
                    if file.endswith('.inp'):
                        filepath = os.path.join(folder_path, file)
                        self.inpFiles.append(filepath)


        self.commands = []
        for inp in self.inpFiles:
            inp_dir = os.path.dirname(inp)
            command = rf'call C:\SIMULIA\Commands\abq2021.bat job={os.path.basename(inp)[:-4]} cpus={self.number_of_cores} interactive'
            self.commands.append((inp_dir, command))


    def runSimulations(self, id):
        """
        Run the Abaqus simulations in parallel.

        Each simulation command is constructed based on the input files, 
        and simulations are executed concurrently using a thread pool executor.
        """       

        def runSimulationAux(inp_dir, command):
            retries = 3
            job_name = command.split('job=')[1].split()[0]
            output_file = os.path.join(inp_dir, f"{job_name}.odb")

            for attempt in range(1, retries + 1):
                try:
                    os.chdir(inp_dir)
                    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                    stdout, stderr = process.communicate()
                    print(f"stdout: {stdout.decode()}\n", f"stderr: {stderr.decode()}\n")
                    process.wait()           
        
                    filename = command.split("job=")[1].split()[0]

                    if os.path.exists(output_file):
                        print("Simulation completed successfully: {}".format(output_file))
                        PararelSimulation.move_odb(self, filename)
                        return "Sucess"
                        
                    else:
                        print("Output file not found for {}. Retrying...".format(job_name))

                except Exception as e:
                    return f"Failed: {command}. Error: {str(e)}"

            # if self.process:
            #     return "Success"
            

        # Using ThreadPoolExecutor to manage the queue of simulations
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.numberFiles) as executor:
            # Submit all commands to the executor
            futures = {executor.submit(runSimulationAux, inp_dir, command): command for inp_dir, command in self.commands}

            # Process as they complete
            for future in concurrent.futures.as_completed(futures):
                command = futures[future]
                try:                 
                    result = future.result()

                    print("54444444444444444444", result)

                    yaml_path = os.path.join(self.python_files, "computers_list.yaml")
                    with open(yaml_path, "r") as file:
                        data = yaml.safe_load(file)
                    
                    data[f"Computer {id[-1:]}"]["status"] = False

                    with open(yaml_path, "w") as file:
                        yaml.dump(data, file)

                except Exception as e:
                    print(f"Simulation {command} generated an exception: {e}")
        

    def move_odb(self, filename):
        try:
            destination_odb_folder = self.odb_processing
            for folder_name in os.listdir(self.simulation_inp_files):
                print(12, folder_name)
                if folder_name == filename:
                    folder_path = os.path.join(self.simulation_inp_files, folder_name)
                    if os.path.isdir(folder_path) and folder_name.lower() != "defaut":
                        for root, dirs, files in os.walk(folder_path):
                            for file in files:
                                if file.endswith(".odb"):
                                    source_path = os.path.join(root, file) 
                                    destination_path = os.path.join(destination_odb_folder, file)  
                                    shutil.copy2(source_path, destination_path)
                                    os.remove(source_path)
        except:
            print("ERROR MOVENDO O FILE")

if __name__ == "__main__":
    
    a = PararelSimulation()
    a.start_simulation()