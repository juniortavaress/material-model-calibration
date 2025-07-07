import os 
import re 
import yaml 
import numpy as np 

class InpEditor():
    def manager_edit(self):
        """
        Main function to edit inp files based on parameters in a YAML file.
        Returns a list of directories where the modified INP files are saved and a dictionary of index names.
        """
        # Creating variables
        lis_dir_inp = []
        index_names = {}
        global_index = 0

        # Loading datas
        yaml_path = os.path.join(self.user_config, "parameters.yaml")
        with open(yaml_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
        dict_param_to_change = data[sorted(data.keys())[-1]]     
        
        # Loop through the parameter sets and apply changes to corresponding inp files
        for set, info in dict_param_to_change.items():
            for file in os.listdir(self.inp_path):
                file_path = os.path.join(self.inp_path, file)
                filename = os.path.basename(file_path)[:-4]

                with open(file_path, 'r') as file:
                    lines = file.readlines()

                for param, value in info["Parameters"].items():  
                    if param == "A":
                        lines = InpEditor.change_A(self, lines, value)
                    elif param == "B":
                        lines = InpEditor.change_B(self, lines, value)
                    elif param == "C1":
                        lines = InpEditor.change_C1(self, lines, value)
                    elif param == "C2":
                        lines = InpEditor.change_C2(self, lines, value)
                    elif param == "C3":
                        lines = InpEditor.change_C3(self, lines, value)
                    elif param == "D1":
                        lines = InpEditor.change_D1(self, lines, value)
                    elif param == "D2":
                        lines = InpEditor.change_D2(self, lines, value)
                    elif param == "D3":
                        lines = InpEditor.change_D3(self, lines, value)
                    elif param == "D4":
                        lines = InpEditor.change_D4(self, lines, value)
                    elif param == "D5":
                        lines = InpEditor.change_D5(self, lines, value)
                    elif param == "Ts":
                        lines = InpEditor.change_Ts(self, lines, value)
                    elif param == "k":
                        lines = InpEditor.change_k(self, lines, value)
                    elif param == "n":
                        lines = InpEditor.change_n(self, lines, value)
                    elif param == "p":
                        lines = InpEditor.change_p(self, lines, value)
                    else:
                        pass
        
                # Saving inp file modified
                params = f"{filename}_it_{int(sorted(data.keys())[-1][-3:]):02}_set_{int(set[-2:]):02}.inp"
                dir_inp = os.path.join(self.simulation_inp_files, params[:-4])

                if not os.path.exists(dir_inp):
                    os.makedirs(dir_inp)
                    with open(os.path.join(dir_inp, params), 'w') as file:
                        file.writelines(lines)
                lis_dir_inp.append(dir_inp)

                index_names[global_index] = params[:-4]
                global_index += 1
        return lis_dir_inp, index_names


    def change_A(self, lines, A):
        pattern = r"^\*Plastic, hardening=USER*"  
        for i, line in enumerate(lines):
            if re.match(pattern, line):
                values = lines[i + 1].split(',')
                values[0] = f"{A:>7}" 
                lines[i + 1] = ','.join(values)  
                break
        return lines
    

    def change_B(self, lines, B):
        pattern = r"^\*Plastic, hardening=USER*"  
        for i, line in enumerate(lines):
            if re.match(pattern, line):
                values = lines[i + 1].split(',')
                values[1] = f"{B:>7}" 
                lines[i + 1] = ','.join(values)  
                break
        return lines
    

    def change_n(self, lines, n):
        pattern = r"^\*Plastic, hardening=USER*"  
        for i, line in enumerate(lines):
            if re.match(pattern, line):
                values = lines[i + 1].split(',')
                values[2] = f"{n:>7}" 
                lines[i + 1] = ','.join(values)  
                break
        return lines
    

    def change_C1(self, lines, C1):
        pattern = r"^\*Plastic, hardening=USER*"  
        for i, line in enumerate(lines):
            if re.match(pattern, line):
                values = lines[i + 1].split(',')
                values[3] = f"{C1:>7}" 
                lines[i + 1] = ','.join(values)  
                break
        return lines
    

    def change_C2(self, lines, C2):
        pattern = r"^\*Plastic, hardening=USER*"  
        for i, line in enumerate(lines):
            if re.match(pattern, line):
                values = lines[i + 1].split(',')
                values[4] = f"{C2:>7}" 
                lines[i + 1] = ','.join(values)  
                break
        return lines
    

    def change_C3(self, lines, C3):
        pattern = r"^\*Plastic, hardening=USER*"  
        for i, line in enumerate(lines):
            if re.match(pattern, line):
                values = lines[i + 1].split(',')
                values[5] = f"{C3:>7}" 
                lines[i + 1] = ','.join(values)  
                break
        return lines
       

    def change_k(self, lines, k):
        pattern = r"^\*Plastic, hardening=USER*"  
        for i, line in enumerate(lines):
            if re.match(pattern, line):
                values = lines[i + 1].split(',')
                values[7] = f"{k:>7}" 
                lines[i + 1] = ','.join(values)  
                break
        return lines


    def change_Ts(self, lines, Ts):
        pattern = r"^\*Plastic, hardening=USER*"  
        for i, line in enumerate(lines):
            if re.match(pattern, line):
                lines[i] = "*Plastic, hardening=USER, properties=9\n"
                values = lines[i + 2].split(',')
                values[0] = f"{Ts:>7}" 
                lines[i + 2] = ','.join(values)  
                break
        return lines
        

    def change_D1(self, lines, value):
        pattern = r"^\*Damage Initiation.*JOHNSON COOK.*"  
        for i, line in enumerate(lines):
            if re.match(pattern, line):
                values = lines[i + 1].split(',')
                values[0] = f"{value:>7}"   
                lines[i + 1] = ','.join(values)  
                break
        return lines
    

    def change_D2(self, lines, value):
        pattern = r"^\*Damage Initiation.*JOHNSON COOK.*"  
        for i, line in enumerate(lines):
            if re.match(pattern, line):
                values = lines[i + 1].split(',')
                values[1] = f"{value:>7}"   
                lines[i + 1] = ','.join(values)  
                break
        return lines
    

    def change_D3(self, lines, value):
        pattern = r"^\*Damage Initiation.*JOHNSON COOK.*"  
        for i, line in enumerate(lines):
            if re.match(pattern, line):
                values = lines[i + 1].split(',')
                values[2] = f"{value:>7}"   
                lines[i + 1] = ','.join(values)  
                break
        return lines
    

    def change_D4(self, lines, value):
        pattern = r"^\*Damage Initiation.*JOHNSON COOK.*"  
        for i, line in enumerate(lines):
            if re.match(pattern, line):
                values = lines[i + 1].split(',')
                values[3] = f"{value:>7}"   
                lines[i + 1] = ','.join(values)  
                break
        return lines
    

    def change_D5(self, lines, value):
        pattern = r"^\*Damage Initiation.*JOHNSON COOK.*"  
        for i, line in enumerate(lines):
            if re.match(pattern, line):
                values = lines[i + 1].split(',')
                values[4] = f"{value:>7}"   
                lines[i + 1] = ','.join(values)  
                break
        return lines
    

    def change_p(self, lines, p):
        pattern = r"^\*Damage Evolution.*"  
        for i, line in enumerate(lines):
            if re.match(pattern, line):
                start_line = i + 1
                break
        
        beta, u_pl = 3.00, 0.01649
        L = np.array([0, 0.0003298, 0.0006596, 0.0009894, 0.0013192, 0.001649, 0.0019788, 0.0023086, 0.0026384, 0.0029682, 0.003298, 0.0036278, 0.0039576, 0.0042874, 0.0046172, 0.004947, 0.0052768, 
                    0.0056066, 0.0059364, 0.0062662, 0.006596, 0.0069258, 0.0072556, 0.0075854, 0.0079152, 0.008245, 0.0085748, 0.0089046, 0.0092344, 0.0095642, 0.009894, 0.0102238, 0.0105536, 
                    0.0108834, 0.0112132, 0.011543, 0.0118728, 0.0122026, 0.0125324, 0.0128622, 0.013192, 0.0135218, 0.0138516, 0.0141814, 0.0145112, 0.014841, 0.0151708, 0.0155006, 0.0158304, 
                    0.0161602, 0.01649])
        D_de = (1 - np.exp(-beta * (L / u_pl))) / (1 - np.exp(-beta)) * p

        for i, value in enumerate(D_de):
            line_index = start_line + i
            values = lines[line_index].split(',')
            values[0] = f"{value:.9f}"
            lines[line_index] = ','.join(values)
        return lines
