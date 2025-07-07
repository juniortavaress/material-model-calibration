import os
import sys
import time
import traceback
from PySide6.QtWidgets import QApplication, QFileDialog
from parallel_simulation import ParallelSimulation

class ComputerXX():
    """
    Manages simulation initialization and execution on Computer 02.
    """
        
    def __init__(self):
        print("=" * 40)
        print("INITIALIZING COMPUTER XX")
        print("=" * 40)


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
        server_folder = os.path.join(os.getenv("SystemDrive", "C:"), "MaterialOtimization", "project_name", "simulation_folder")
        drive_folder = QFileDialog.getExistingDirectory(None, "Selecione um Diretório")

        if not os.path.exists(server_folder):
            os.makedirs(server_folder)

        self.run_simulation_loop(server_folder, drive_folder)


    def run_simulation_loop(self, server_folder, drive_folder):
        """
        Run simulations continuously and verify for new simulations every 10 minutes.
        """
        while True:
            try:
                sim = ParallelSimulation()  
                sim.run_all_simulations(server_folder, drive_folder, num_cores=4, cp_number="cpXX")

            except Exception as e:
                traceback.print_exc()

            time.sleep(600)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ComputerXX().get_setup()