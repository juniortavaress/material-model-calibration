
import os
import sys
import json
import time
import yaml 
import traceback
from pararel_simulation import PararelSimulation
from PySide6.QtWidgets import QApplication, QFileDialog

class ComputerXX():
    """
    This class handles the initialization and execution of simulations on Computer XX.
    It manages directories, paths, and interacts with the simulation process.
    """
        
    def __init__(self):
        """
        Initializes the ComputerXX class and prints the initialization message.
        """
        print("======================================")
        print("\nINITIALIZING THE CODE AT COMPUTER XX\n")
        print("======================================\n")


    def get_setup(self):
        """
        Sets up the necessary directories for simulation and initiates the 
        simulation run process.

        - Adds paths to sys.path.
        - Prompts the user to select a directory for the simulation.
        - Creates the server folder if it does not exist.
        - Calls the run_simulation method to start the simulation.
        """
        sys.path.append(os.getcwd())
        server_folder = os.path.join(os.getenv("SystemDrive", "C:") , "\MaterialOtimization\project_name\simulation_folder")
        drive_folder = QFileDialog.getExistingDirectory(None, "Selecione um Diretório")

        if not os.path.exists(server_folder):
            os.makedirs(server_folder)
        ComputerXX.run_simulation(self, server_folder, drive_folder)


    def run_simulation(self, server_folder, drive_folder):
        """
        Runs the simulation process in a loop. It reads the configuration file, checks 
        the status of Computer X, and starts the simulation if conditions are met.

        The loop continues indefinitely, checking the status and running the simulation
        every 10 minutes.

        Args:
            server_folder (str): The folder path for the server directory.
            drive_folder (str): The folder path for the user's selected directory.
        """
        while True:
            current_directory = os.path.dirname(os.path.abspath(__file__))
            info_pcXX = os.path.join(current_directory, "computers_list.yaml")

            with open(info_pcXX, "r") as file:
                data = yaml.safe_load(file)

            list_comp_XX = data["Computer X"]["files"]

            try:
                if data["Computer X"]["status"] == True:
                    id = "cpXX"
                    simulation = PararelSimulation
                    simulation.start_simulation(simulation, id, list_comp_XX, server_folder, drive_folder, number_of_cores = cores_by_simulation)

            except Exception as e:
                traceback.print_exc()

            # Sleep for 600 seconds (10 minutes) before checking again
            time.sleep(600)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cp = ComputerXX()
    cp.get_setup()
