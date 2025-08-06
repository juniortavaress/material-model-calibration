import os
import yaml

class YamlManager:
    def save_yaml_info(self, yaml_path, condition, datas):
        """
        Save or update YAML files.
        """
        if os.path.exists(yaml_path):
            existing_data = YamlManager.load_yaml(self, yaml_path)
        else:
            existing_data = {}

        existing_data[condition] = datas
        
        os.makedirs(os.path.dirname(yaml_path), exist_ok=True)
        with open(yaml_path, "w", encoding="utf-8") as file:
            yaml.dump(existing_data, file, default_flow_style=False, allow_unicode=True, width=float("inf"))

    
    def load_yaml(self, path):
        """
        Loads YAML project information safely.

        Returns:
            dict: Parsed YAML content.
        """
        with open(path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file) or {}
        return data


