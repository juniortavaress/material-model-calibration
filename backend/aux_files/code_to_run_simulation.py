
import os
import sys
import json
import time
import yaml 
import traceback
from PySide6.QtWidgets import QApplication, QFileDialog

class ComputerXX():
    def __init__(self):
        print("======================================")
        print("\nINITIALIZING THE CODE AT COMPUTER XX\n")
        print("======================================\n")

    def get_setup(self):
        # Add Paths to sys
        sys.path.append(os.getcwd())
        server_folder = os.path.join(os.getenv("SystemDrive", "C:") , "\MaterialOtimization\project_name\SimulationFolder")
        drive_folder = QFileDialog.getExistingDirectory(None, "Selecione um Diretório")

        if not os.path.exists(server_folder):
            os.makedirs(server_folder)

        print(server_folder)
        ComputerXX.run_simulation(self, server_folder, drive_folder)


    def run_simulation(self, server_folder, drive_folder):
        while True:
            current_directory = os.path.dirname(os.path.abspath(__file__))
            info_pcXX = os.path.join(current_directory, "computers_list.yaml")

            with open(info_pcXX, "r") as file:
                data = yaml.safe_load(file)

            list_comp_XX = data["Computer X"]["files"]
            # print(list_comp_02)

            try:
                if data["Computer X"]["status"] == True:
                    id = "cpXX"
                    from pararel_simulation import PararelSimulation
                    simulation = PararelSimulation
                    simulation.start_simulation(simulation, id, list_comp_XX, server_folder, drive_folder, number_of_cores = cores_by_simulation)

                print("status", data["Computer X"]["files"])
                data["Computer X"]["status"] = False
                with open(info_pcXX, "w") as file:
                    json.dump(data, file, indent=4)
            except Exception as e:
                print("Erro na thread (class WorkerThread(QThread)):", e) 
                traceback.print_exc()
            time.sleep(600)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cp = ComputerXX()
    cp.get_setup()
