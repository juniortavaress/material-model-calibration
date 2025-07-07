import os
import sys
import yaml
import shutil
import psutil
from PySide6.QtCore import QTimer
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
            self.ui.lineEdit_number_iteration.setText(str(data["7. PSO and Simulation"]["Iterations"]))
            self.ui.lineEdit_number_particles.setText(str(data["7. PSO and Simulation"]["Particles"]))
            self.ui.lineEdit_var1.setText(str(data["7. PSO and Simulation"]["fig"]))
            self.ui.lineEdit_var2.setText(str(data["7. PSO and Simulation"]["w"]))
            self.ui.lineEdit_var3.setText(str(data["7. PSO and Simulation"]["fip"]))
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

        core_by_simulation = self.ui.combobox_core_by_simulation.currentText()
        number_computer = self.ui.combobox_number_computer.currentText()
        main_computer = self.ui.combobox_main_computer.currentText()
        number_conditions = self.ui.label_number_conditions.text()

        try:
            self.error_tracking = False
            iterations = int(self.ui.lineEdit_number_iteration.text())
            particles = int(self.ui.lineEdit_number_particles.text())
            var1 = float(self.ui.lineEdit_var1.text())
            var2 = float(self.ui.lineEdit_var2.text())
            var3 = float(self.ui.lineEdit_var3.text())

            if iterations <= 0 or particles <= 0:
                self.error_tracking = True
            elif core_by_simulation == "None" or number_computer == "None" or main_computer == "None":
                self.error_tracking = True

        except:
            self.error_tracking = True

        if not self.error_tracking:
            data["7. PSO and Simulation"] = {
                "Cutting Conditions": number_conditions,
                "Iterations": iterations,
                "Particles": particles,
                "w": var2,
                "fig": var1,
                "fip": var3,
                "Cores by Simulation": core_by_simulation,
                "Computers": number_computer,
                "Main Computer": main_computer}

            YamlClass.save_yaml_info(self, self.project_infos_path, "7. PSO and Simulation", data["7. PSO and Simulation"])
            self.ui.pages.setCurrentIndex(10)
        else:
            self.ui.label_pso_result_warning.show()
            QTimer.singleShot(3000, lambda: self.ui.label_pso_result_warning.hide())


    def create_python_files(self):
        if getattr(sys, 'frozen', False):  
            base_path = sys._MEIPASS
        else:
            base_path = os.getcwd() 
    
        pararel_simulation_source = os.path.join(base_path, r"backend\pso_scripts\parallel_simulation.py")
        status_manager_source = os.path.join(base_path, r"backend\pso_scripts\status_manager.py")

        if not self.error_tracking:
            with open(self.project_infos_path, "r", encoding="utf-8") as file:
                data = yaml.safe_load(file) or {}

            defaut_file = os.path.join(base_path, r"backend\aux_files\aux_simulation\code_to_run_simulation.py")
            computers = data["7. PSO and Simulation"]["Computers"]
            cores_by_simulation = data["7. PSO and Simulation"]["Cores by Simulation"]
            main_activated = data["7. PSO and Simulation"]["Main Computer"]
            project_name = data["1. Info"]["Project Name"]

            i = 1 if main_activated == "Yes" else  2
            
            for computer in range(i, int(computers) + 1):
                computer_file = os.path.join(self.python_files, f"computer_0{computer}.py")
                with open(defaut_file, 'r') as file:
                    conteudo = file.read()
                conteudo_modificado_code_to_run_simulation = conteudo.replace("XX", f"0{computer}").replace("X", f"{computer}").replace("cores_by_simulation", cores_by_simulation).replace("project_name", project_name)
                with open(computer_file, 'w') as file:
                    file.write(conteudo_modificado_code_to_run_simulation)


                with open(pararel_simulation_source, 'r') as file:
                    conteudo = file.read()
                conteudo_modificado_parallel = conteudo.replace("from backend.pso_scripts.status_manager import StatusManager", "from status_manager import StatusManager")
                with open(os.path.join(self.python_files, "parallel_simulation.py"), 'w') as file:
                    file.write(conteudo_modificado_parallel)

            # shutil.copy(pararel_simulation_source, os.path.join(self.python_files, "parallel_simulation.py"))
            shutil.copy(status_manager_source, os.path.join(self.python_files, "status_manager.py"))


if __name__ == "__main__":
    cp = GetPsoAndSimulation()
    cp.create_python_files()
