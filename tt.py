from datetime import datetime
from filelock import FileLock
import yaml


def read_and_write_yaml(yaml_path, function, computer_dict=None):
    try:
        if function == "load":
            with open(yaml_path, 'r') as file:
                data = yaml.safe_load(file)
                return data if isinstance(data, dict) else {}
        elif function == "save":
            with open(yaml_path, "w") as file:
                yaml.dump(computer_dict, file)
    except Exception as e:
        print(f"[Erro ao acessar YAML] {e}")
        import traceback
        traceback.print_exc()
        return {}

def _refresh_timestamps(yaml_path, odb_processing, cp_number):
    updated = False
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    computer_dict = read_and_write_yaml(yaml_path, "load")    

    with FileLock(yaml_path + ".lock"):
        for key, value in computer_dict.items():
            if isinstance(value, str) and value.startswith("Running"):
                parts = value.split()
                path = " ".join(parts[5:])
                cp_info = parts[1][1:]

                # print(parts)
                import os
                if cp_info == cp_number:
                    updated = True
                    odb_file = os.path.basename(path) + ".odb"
                    odb_path = os.path.join(odb_processing, odb_file)
                    if not os.path.exists(odb_path):
                        computer_dict[key] = f"False {path}"
                    else:
                        computer_dict[key] = f"Running ({cp_info} - {now}) {path}"
                    
        if updated:
            read_and_write_yaml(yaml_path, "save", computer_dict)
            print(f"✅ Status/timestamps update completed at {now}")

odb = r"C:/Users/adam-ua769pu3t3n7k4o/Pictures\TT2207\auxiliary_files/odb_processing"
yaml_path = r"C:/Users/adam-ua769pu3t3n7k4o/Pictures\TT2207\auxiliary_files/python_files_to_computers\computers_list.yaml"
_refresh_timestamps(yaml_path, odb, "cp01")