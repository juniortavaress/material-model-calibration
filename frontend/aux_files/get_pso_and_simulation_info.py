import os
import yaml
import shutil
import psutil
from frontend.aux_files.yaml_generator import YamlClass


class GetPsoAndSimulation:
    def load_info(self):
        GetPsoAndSimulation.show_pso_and_results_info(self)
        GetPsoAndSimulation.show_available_cores(self)


    def show_pso_and_results_info(self):
        with open(self.project_infos_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file) or {}

        if "7. PSO and Simulation" not in data and "3. Conditions" in data:
            self.ui.label_number_conditions.setText(str(len(data["3. Conditions"])))
        else:
            self.ui.label_number_conditions.setText(data["7. PSO and Simulation"]["Cutting Conditions"])
            self.ui.lineEdit_number_iteration.setText(data["7. PSO and Simulation"]["Iterations"])
            self.ui.lineEdit_number_particles.setText(data["7. PSO and Simulation"]["Particles"])
            self.ui.lineEdit_var1.setText(data["7. PSO and Simulation"]["fig"])
            self.ui.lineEdit_var2.setText(data["7. PSO and Simulation"]["w"])
            self.ui.lineEdit_var3.setText(data["7. PSO and Simulation"]["fip"])
            self.ui.combobox_core_by_simulation.setCurrentText(data["7. PSO and Simulation"]["Cores by Simulation"])
            self.ui.combobox_number_computer.setCurrentText(data["7. PSO and Simulation"]["Computers"])
            self.ui.combobox_main_computer.setCurrentText(data["7. PSO and Simulation"]["Main Computer"])


    def show_available_cores(self):
        threshold = 8
        cpu_percentages = psutil.cpu_percent(percpu=True)
        num_physical_cores = psutil.cpu_count(logical=False)
        self.availableCores = sum(1 for i, usage in enumerate(cpu_percentages) if usage < threshold and i < num_physical_cores)
        self.ui.label_cores.setText(str(self.availableCores))


    def save_info(self):
        GetPsoAndSimulation.generate_yaml_info(self)
        GetPsoAndSimulation.create_python_files(self)


    def generate_yaml_info(self):
        with open(self.project_infos_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file) or {}

        if "7. PSO and Simulation" not in data:
            data["7. PSO and Simulation"] = {}

        data["7. PSO and Simulation"] = {"Cutting Conditions": self.ui.label_number_conditions.text(),
                                        "Iterations": self.ui.lineEdit_number_iteration.text(),
                                        "Particles": self.ui.lineEdit_number_particles.text(),
                                        "w": self.ui.lineEdit_var2.text(),
                                        "fig": self.ui.lineEdit_var1.text(),
                                        "fip": self.ui.lineEdit_var3.text(),
                                        "Cores by Simulation": self.ui.combobox_core_by_simulation.currentText(),
                                        "Computers": self.ui.combobox_number_computer.currentText(),
                                        "Main Computer": self.ui.combobox_main_computer.currentText()}

        YamlClass.save_yaml_info(self, self.project_infos_path, "7. PSO and Simulation", data["7. PSO and Simulation"])


    def create_python_files(self):
        with open(self.project_infos_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file) or {}

        defaut_file = r"backend\aux_files\code_to_run_simulation.py"
        computers = data["7. PSO and Simulation"]["Computers"]
        cores = data["7. PSO and Simulation"]["Cores by Simulation"]
        main_activated = data["7. PSO and Simulation"]["Main Computer"]

        i = 1 if main_activated == "No" else  2
        for computer in range(i, int(computers) + 1):
            computer_file = os.path.join(self.python_files, f"computer_0{computer}.py")
            with open(defaut_file, 'r') as file:
                conteudo = file.read()

            conteudo_modificado = conteudo.replace("X", f"0{computer}").replace("CORES", cores)

            with open(computer_file, 'w') as file:
                file.write(conteudo_modificado)



