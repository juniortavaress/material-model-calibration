import os 
import re
import yaml
import shutil
from PySide6.QtWidgets import QFileDialog
from frontend.aux_files.yaml_generator import YamlClass

class InpManager:
    def main(self):
        self.inp_path = r"C:/Users/adam-ua769pu3t3n7k4o/Documents/Results_04-02-2025/auxiliary_files\defaut/INPFiles"
        self.user_config = r"C:/Users/adam-ua769pu3t3n7k4o/Documents\Results_04-02-2025\config"

    def get_available_parameters(self):
        material_info = {}
        valid_properties = {"Damage Initiation", "Damage Evolution", "Plastic"}

        if os.path.exists(self.inp_path):
            files = os.listdir(self.inp_path)

            for filename in os.listdir(self.inp_path):
                # Settings
                i = 0
                current_material = None
                current_property = None
                material_info[filename] = {}
                path_to_inp = os.path.join(self.inp_path, filename)

                with open(path_to_inp, "r", encoding="utf-8") as inp_file:
                    lines = inp_file.readlines()

                while i < len(lines):
                    line = lines[i].strip()
                    
                    # Get Material Name
                    match_material = re.match(r"\*Material, name=\"?([^\"]+)\"?", line)
                    if match_material:
                        current_material = match_material.group(1).strip()
                        material_info[filename][current_material] = {}
                        current_property = None  # Resetar propriedade atual
                        i += 1
                        continue

                    # Get Properties Name
                    match_property = re.match(r"\*([A-Za-z\s\-]+)", line)
                    if match_property:
                        property_name = match_property.group(1).strip()
                        if property_name in valid_properties:
                            current_property = match_property.group(1).strip()
                            material_info[filename][current_material][current_property] = []
                        else:
                            current_property = None
                        i += 1
                        continue
                    
                    # Get Properties Values
                    if current_material and current_property:
                        if re.match(r"^[\d\.\-eE\s,]+$", line):  
                            values = [float(v) for v in re.split(r"[,\s]+", line) if v]

                            if current_property == "Damage Initiation" or current_property == "Plastic":
                                material_info[filename][current_material][current_property].extend(values)
                            else:
                                material_info[filename][current_material][current_property].append(values)
                        else:
                            current_property = None 

                    if re.match(r"\** INTERACTION PROPERTIES", line):
                        break
                    i += 1  

        yaml_path = os.path.join(self.user_config, "material_properties.yaml")
        with open(yaml_path, "w", encoding="utf-8") as file:
            yaml.dump(material_info, file, default_flow_style=False, allow_unicode=True, width=float("inf"))
            
          
    def get_list_with_parameters_name(self):
        self.materials_properties = {}
        yaml_path = os.path.join(self.user_config, "material_properties.yaml")
        if os.path.exists(yaml_path):
            with open(yaml_path, "r", encoding="utf-8") as file:
                data = yaml.safe_load(file)

                for file, file_data in data.items():
                    for material_name, material_data in file_data.items():
                        material_props = {}

                        material_props["Damage Initiation"] = "Damage Initiation" in material_data
                        material_props["Damage Evolution"] = "Damage Evolution" in material_data
                        material_props["Plastic"] = "Plastic" in material_data

                        self.materials_properties[material_name] = material_props
                YamlClass.save_yaml_info(self, self.project_infos_path, "Material Properties", self.materials_properties)
    

if __name__ == "__main__":
    getInp = InpManager()
    getInp.main()
    getInp.get_available_parameters()
    getInp.get_list_with_parameters_name()
