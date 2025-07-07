from datetime import datetime, timedelta
from filelock import FileLock
import yaml
import threading

class StatusManager():
    @staticmethod
    def schedule(func, interval_seconds):
        def wrapper():
            func()
            threading.Timer(interval_seconds, wrapper).start()
        threading.Thread(target=wrapper, daemon=True).start()

    @staticmethod
    def _refresh_timestamps(yaml_path, cp_number):

        updated = False
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        computer_dict = StatusManager.read_and_write_yaml(yaml_path, "load")    

        with FileLock(yaml_path + ".lock"):
            for key, value in computer_dict.items():
                if isinstance(value, str) and value.startswith("Running"):
                    parts = value.split()
                    path = " ".join(parts[5:])
                    cp_info = parts[1][1:]
                    
                    if cp_info == cp_number:
                        updated = True
                        computer_dict[key] = f"Running ({cp_info} - {now}) {path}"
                        
            if updated:
                StatusManager.read_and_write_yaml(yaml_path, "save", computer_dict)
                print(f"✅ Timestamps atualizados para {now}")
            

    @staticmethod
    def _verify_expired(yaml_path, cp_number):
        
        update = False
        now = datetime.now()
        computer_dict = StatusManager.read_and_write_yaml(yaml_path, "load")

        with FileLock(yaml_path + ".lock"):
            for key, value in computer_dict.items():
                if isinstance(value, str) and value.startswith("Running"):
                    prefix, command = value.split(")", 1)
                    prefix = prefix.replace("Running (", "")
                    running_cp, timestamps_str = prefix.split(" - ", 1)

                    if running_cp == cp_number:
                        continue

                    timestamp = datetime.strptime(timestamps_str, "%Y-%m-%d %H:%M:%S")
                    if now - timestamp > timedelta(seconds=30):
                        update = True
                        computer_dict[key] = f"True {command}"
                        print(f"[⚠️ Expired] Resetting {key} ({running_cp})")

                if update:
                    StatusManager.read_and_write_yaml(yaml_path, "save", computer_dict)

    @staticmethod
    def read_and_write_yaml(yaml_path, function, computer_dict=None):
        if function == "load":
            with open(yaml_path, 'r') as file:
                return yaml.safe_load(file)
        elif function == "save":
            with open(yaml_path, "w") as file:
                yaml.dump(computer_dict, file)
        