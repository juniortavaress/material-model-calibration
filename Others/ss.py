import os 
import shutil 
import pandas as pd

odb_processing = r"S:/Junior/abaqus-with-python/otimization-scripts/new-version/material-model-calibration\Teste\auxiliary_files\odb_processing"
odb_files = r"S:/Junior/abaqus-with-python/otimization-scripts/new-version/material-model-calibration\Teste\obd_files"
excel_files = r"S:/Junior/abaqus-with-python/otimization-scripts/new-version/material-model-calibration\Teste\excel_files"
config = r"S:/Junior/abaqus-with-python/otimization-scripts/new-version/material-model-calibration\Teste\auxiliary_files\config"

for file in os.listdir(odb_processing):
    if file.endswith('.odb'):
        # self.call_count += 1
        odb_inp_path = os.path.join(odb_processing, file)
        odb_out_file = odb_files

        # if not os.path.exists(odb_out_file):
        #     os.makedirs(odb_out_file)
        # shutil.move(odb_inp_path, odb_out_file)
    
        df_temp_force = pd.read_excel(os.path.join(excel_files, "results_temp_and_forces.xlsx"), header=1)
        print(file[:-4], df_temp_force["Filename"])
        filtered_row = df_temp_force[df_temp_force["Filename"] == file[:-4]]
        simulated_forces = [filtered_row.iloc[0,7], filtered_row.iloc[0,3]]
        simulated_temperature = filtered_row.iloc[0,9]

        df_chip = pd.read_excel(os.path.join(excel_files, "results_chip_analysis.xlsx"), header=0)
        filtered_row = df_chip[df_chip["Filename"] == file[:-4]]
        chip_compression_ratio = filtered_row.iloc[0,5]
        chip_segmentation_ratio = filtered_row.iloc[0,6]


        results_dict = {"Filename": file, "Forces": simulated_forces, "Temperatures": simulated_temperature, "CCR": chip_compression_ratio, "CSR": chip_segmentation_ratio}
        print(results_dict)


        info = file.split("_int")
        condition = file.split("_int_")[0]
        param_info = f"int{info[1][:-4]}"
        iteration_number = (param_info.split("int_")[1]).split("_set_")[0]
        set_number = (param_info.split("int_")[1]).split("_set_")[1]
        print(iteration_number, set_number)

        import yaml
        yaml_path = os.path.join(config, "parameters.yaml")
        with open(yaml_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        for iteration, values in data.items():
            if iteration[-2:] == iteration_number:
                for set, param_values in values.items():
                    if set[-2:] == set_number:
                        param_set = param_values
        
        print(param_set)
        print(condition)
        print(param_info)

        if condition[4:] in self.target_values:
            target_cutting_force = self.target_values[condition[4:]].get("fc")
            target_normal_force = self.target_values[condition[4:]].get("fn")
            target_chip_compression_ratio = self.target_values[condition[4:]].get("ccr")
            target_chip_segentatio_ratio = self.target_values[condition[4:]].get("csr")
            targets = [target_cutting_force, target_normal_force, target_chip_compression_ratio, target_chip_segentatio_ratio]

        param_set = {'D2': 0.67, 'Ts': 665.64, 'p': 0.48}
        data = {"Iteration number": file.split("_int_")[1][:2], "Condition": file.split("_int_")[0]}
        
        for key, value in param_set.items():
            data[f"Parameter {key}"] = value

        data.update({
                "Normalized Error": 0,
                "Experiment Cutting Force": targets[0], "Simulation Cutting Force": simulated_forces[0], "Error Fc": 0,
                "Experiment Normal Force": targets[1], "Simulation Normal Force": simulated_forces[1], "Error Fn": 0,
                "Experiment CCR": targets[2], "Simulation CCR": chip_compression_ratio, "Error CCR": 0,
                "Experiment CSR": targets[3], "Simulation CSR": chip_segmentation_ratio, "Error CSR": 0})
        
        new_info = pd.DataFrame(data)

        data_path = os.path.join(self.excel_files, "datas.xlsx")

        if os.path.exists(data_path):
            old_df = pd.read_excel(data_path, engine="openpyxl", index_col=0)
            new_df = pd.concat([old_df, new_info], ignore_index=True)
        else:
            new_df = new_info

        # #print(new_df)
        new_df.index.name = "Simulation"
        new_df.to_excel(data_path, index=True, engine="openpyxl")