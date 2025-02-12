
import os
import sys
import json
import time

class ComputerX():
    def __init__(self):
        print("======================================")
        print("\nINITIALIZING THE CODE AT COMPUTER X\n")
        print("======================================\n")

    def run_simulations(self):
        # Add Paths to sys
        sys.path.append(os.getcwd())

        # Getting Paths
        from file_utils import FileUtils
        file = FileUtils()
        file.create_folders(self)

        while True:
            info_pcX = os.path.join(self.status_dir, "status_file.json")

            with open(info_pcX, "r") as file:
                data = json.load(file)

            list_comp_X = data["Simulation-list-pcX"]["list_comp_X"]
            # print(list_comp_02)

            try:
                if data["Simulation-list-pcX"]["status"] == True:
                    id = "cpX"
                    from otimization_algorithm.pararel_simulation import PararelSimulation
                    simulation = PararelSimulation
                    simulation.start_simulation(simulation, id, list_comp_X, number_of_cores = CORES, number_pararell_sim = PARARELL)

                print("status", data["Simulation-list-pcX"]["status"])
                data["Simulation-list-pcX"]["status"] = False
                with open(info_pcX, "w") as file:
                    json.dump(data, file, indent=4)
            except:
                pass

            time.sleep(600)

if __name__ == "__main__":
    cp = ComputerX()
    cp.run_simulations()
