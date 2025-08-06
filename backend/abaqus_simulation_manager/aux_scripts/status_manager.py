import os
import yaml
import traceback
import threading
from filelock import FileLock
from typing import Optional, Dict, Any
from datetime import datetime, timedelta

class StatusManager():
    @staticmethod
    def schedule(func: callable, interval_seconds: int) -> None:
        """
        Schedule a function to run periodically in a separate daemon thread.
        """
        def wrapper():
            func()
            threading.Timer(interval_seconds, wrapper).start()
        threading.Thread(target=wrapper, daemon=True).start()


    @staticmethod
    def update_status_and_timestamp(yaml_path: str, odb_processing: str, cp_number: str) -> None:
        """
        Refreshes the timestamp of simulations marked as 'Running'.
        If a corresponding .odb file is found, timestamp is updated; otherwise, status is reset to 'False'.
        """
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
                        odb_file = os.path.basename(path) + ".odb"
                        odb_path = os.path.join(odb_processing, odb_file)
                        if not os.path.exists(odb_path):
                            computer_dict[key] = f"False {path}"
                        else:
                            computer_dict[key] = f"Running ({cp_info} - {now}) {path}"
                        
            if updated:
                StatusManager.read_and_write_yaml(yaml_path, "save", computer_dict)
                print(f"✅ Status/timestamps update completed at {now}")
            

    @staticmethod
    def reset_expired_tasks(yaml_path: str, cp_number: str) -> None:
        """
        Checks for running tasks from other computers that have not updated in over 30 minutes.
        Resets them to 'True' status.
        """
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
                    if now - timestamp > timedelta(minutes=30):
                        update = True
                        computer_dict[key] = f"True{command}"
                        print(f"[⚠️ Expired] Resetting {key} ({running_cp})")

                if update:
                    StatusManager.read_and_write_yaml(yaml_path, "save", computer_dict)


    @staticmethod
    def read_and_write_yaml(yaml_path: str, operation: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Reads or writes a YAML file, depending on the operation.

        Args:
            yaml_path: Path to the YAML file.
            operation: "load" to read, "save" to write.
            data: Dictionary to save (only used if operation is "save").

        Returns:
            Parsed dictionary if loading, empty dict on error or invalid structure.
        """
        try:
            if operation == "load":
                with open(yaml_path, 'r') as file:
                    data = yaml.safe_load(file)
                    return data if isinstance(data, dict) else {}
            elif operation == "save":
                with open(yaml_path, "w") as file:
                    yaml.dump(data, file)
        except Exception as e:
            print(f"[Erro ao acessar YAML] {e}")
            traceback.print_exc()
            return {}