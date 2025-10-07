import os 
import re 
import requests
import numpy as np 
from typing import List


class InpEditor():
    """
    Class responsible for editing Abaqus .inp files using parameter sets
    retrieved from a database and uploading the edited files to Supabase Storage.
    """

    def manager_edit(self) -> List[str]:
        """
        Edits the default .inp files based on the latest parameter sets 
        for the current optimization iteration and uploads them to Supabase Storage.

        Returns:
            List[str]: Public URLs of the uploaded modified .inp files.
        """
        edited_inp_urls = []
        bucket_name = "inp-default-files"
        default_inp_folder = f"{self.main.project_id}/default_inp"
        
        default_file = self.main.supabase_storage.storage.from_(bucket_name).list(default_inp_folder)
       
        # Pega todos os sets da última iteração
        response = self.main.supabase.table("results").select("*").eq("project_id", self.main.project_id).eq("iteration_number", self.main.current_opt).execute()
        if not response.data:
            return []

        param_columns = [
            "parameter_A","parameter_B","parameter_C1","parameter_C2","parameter_C3",
            "parameter_D1","parameter_D2","parameter_D3","parameter_D4","parameter_D5",
            "parameter_Tm","parameter_Ts","parameter_Tt", "parameter_n","parameter_p"
        ]

        param_sets = {
            f"set-{row['parameter_set']:02}": {
                key.replace("parameter_", ""): row[key]
                for key in param_columns if row.get(key) is not None
            } for row in response.data
        }

        # Modify each default inp file with each parameter set
        for set_key, parameters in param_sets.items():
            for file in default_file:
                file_name = file["name"]
                full_path = f"{default_inp_folder}/{file_name}"
                file_base = os.path.splitext(file_name)[0]
                file_url  = self.main.supabase_storage.storage.from_(bucket_name).get_public_url(full_path)

                response = requests.get(file_url)
                if response.status_code == 200:
                    lines = InpEditor._edit_variables(self, response.text.splitlines(keepends=True), parameters)
                    new_filename = f"{file_base}_it_{int(self.main.current_opt):02}_set_{int(set_key[-2:]):02}.inp"
                    url = InpEditor._upload_inp_to_supabase(self, new_filename, lines)
                    edited_inp_urls.append(url)

        self.main.supabase.table("simulation_commands").delete().eq("project_id", self.main.project_id).execute()

        commands = [{
            "project_id": self.main.project_id,
            "iteration_number": self.main.current_opt,
            "command": url,
            "status": False,
            "computer_id": None
        } for url in edited_inp_urls]

        self.main.supabase.table("simulation_commands").insert(commands).execute()
        return edited_inp_urls


    def _edit_variables(self, lines: List[str], parameters: dict) -> List[str]:
        """
        Applies parameter _changes to the content of a .inp file.

        Args:
            lines (List[str]): Original lines of the .inp file.
            parameters (dict): Dictionary of parameter names and values.

        Returns:
            List[str]: Modified lines of the .inp file.
        """
        for param, value in parameters.items():
            if param == "A":
                lines = InpEditor._change_A(self, lines, value)
            elif param == "B":
                lines = InpEditor._change_B(self, lines, value)
            elif param == "C1":
                lines = InpEditor._change_C1(self, lines, value)
            elif param == "C2":
                lines = InpEditor._change_C2(self, lines, value)
            elif param == "C3":
                lines = InpEditor._change_C3(self, lines, value)
            elif param == "D1":
                lines = InpEditor._change_D1(self, lines, value)
            elif param == "D2":
                lines = InpEditor._change_D2(self, lines, value)
            elif param == "D3":
                lines = InpEditor._change_D3(self, lines, value)
            elif param == "D4":
                lines = InpEditor._change_D4(self, lines, value)
            elif param == "D5":
                lines = InpEditor._change_D5(self, lines, value)
            elif param == "Ts":
                lines = InpEditor._change_Ts(self, lines, value)
            elif param == "k":
                lines = InpEditor._change_k(self, lines, value)
            elif param == "n":
                lines = InpEditor._change_n(self, lines, value)
            elif param == "p":
                lines = InpEditor._change_p(self, lines, value)
            else:
                pass
        return lines
            

    def _upload_inp_to_supabase(self, filename: str, lines: List[str]) -> str:
        """
        Uploads a modified .inp file to Supabase Storage and returns its public URL.

        Args:
            filename (str): Name of the .inp file to be uploaded.
            lines (List[str]): Content of the .inp file.

        Returns:
            str: Public URL of the uploaded file, or None if upload failed.
        """
        try:
            file_data = "".join(lines).encode("utf-8")
            bucket = "inp-default-files"
            storage_path = f"{self.main.project_id}/edited_inp/{filename}"

            upload_response = self.main.supabase_storage.storage.from_(bucket).update(storage_path, file_data)
            if hasattr(upload_response, "error") and upload_response.error:
                print(f"❌ Upload error: {upload_response.error.message}")
                return None

            return self.main.supabase_storage.storage.from_(bucket).get_public_url(storage_path)

        except Exception as error:
            print(f"❌ Unexpected error during upload: {error}")
            return None


    def _change_A(self, lines, A):
        pattern = r"^\*Plastic, hardening=USER*"  
        for i, line in enumerate(lines):
            if re.match(pattern, line):
                values = lines[i + 1].split(',')
                values[0] = f"{A:>7}" 
                lines[i + 1] = ','.join(values)  
                break
        return lines
    

    def _change_B(self, lines, B):
        pattern = r"^\*Plastic, hardening=USER*"  
        for i, line in enumerate(lines):
            if re.match(pattern, line):
                values = lines[i + 1].split(',')
                values[1] = f"{B:>7}" 
                lines[i + 1] = ','.join(values)  
                break
        return lines
    

    def _change_n(self, lines, n):
        pattern = r"^\*Plastic, hardening=USER*"  
        for i, line in enumerate(lines):
            if re.match(pattern, line):
                values = lines[i + 1].split(',')
                values[2] = f"{n:>7}" 
                lines[i + 1] = ','.join(values)  
                break
        return lines
    

    def _change_C1(self, lines, C1):
        pattern = r"^\*Plastic, hardening=USER*"  
        for i, line in enumerate(lines):
            if re.match(pattern, line):
                values = lines[i + 1].split(',')
                values[3] = f"{C1:>7}" 
                lines[i + 1] = ','.join(values)  
                break
        return lines
    

    def _change_C2(self, lines, C2):
        pattern = r"^\*Plastic, hardening=USER*"  
        for i, line in enumerate(lines):
            if re.match(pattern, line):
                values = lines[i + 1].split(',')
                values[4] = f"{C2:>7}" 
                lines[i + 1] = ','.join(values)  
                break
        return lines
    

    def _change_C3(self, lines, C3):
        pattern = r"^\*Plastic, hardening=USER*"  
        for i, line in enumerate(lines):
            if re.match(pattern, line):
                values = lines[i + 1].split(',')
                values[5] = f"{C3:>7}" 
                lines[i + 1] = ','.join(values)  
                break
        return lines
       

    def _change_k(self, lines, k):
        pattern = r"^\*Plastic, hardening=USER*"  
        for i, line in enumerate(lines):
            if re.match(pattern, line):
                values = lines[i + 1].split(',')
                values[7] = f"{k:>7}" 
                lines[i + 1] = ','.join(values)  
                break
        return lines


    def _change_Ts(self, lines, Ts):
        pattern = r"^\*Plastic, hardening=USER*"  
        for i, line in enumerate(lines):
            if re.match(pattern, line):
                lines[i] = "*Plastic, hardening=USER, properties=9\n"
                values = lines[i + 2].split(',')
                values[0] = f"{Ts:>7}" 
                lines[i + 2] = ','.join(values)  
                break
        return lines
        

    def _change_D1(self, lines, value):
        pattern = r"^\*Damage Initiation.*JOHNSON COOK.*"  
        for i, line in enumerate(lines):
            if re.match(pattern, line):
                values = lines[i + 1].split(',')
                values[0] = f"{value:>7}"   
                lines[i + 1] = ','.join(values)  
                break
        return lines
    

    def _change_D2(self, lines, value):
        pattern = r"^\*Damage Initiation.*JOHNSON COOK.*"  
        for i, line in enumerate(lines):
            if re.match(pattern, line):
                values = lines[i + 1].split(',')
                values[1] = f"{value:>7}"   
                lines[i + 1] = ','.join(values)  
                break
        return lines
    

    def _change_D3(self, lines, value):
        pattern = r"^\*Damage Initiation.*JOHNSON COOK.*"  
        for i, line in enumerate(lines):
            if re.match(pattern, line):
                values = lines[i + 1].split(',')
                values[2] = f"{value:>7}"   
                lines[i + 1] = ','.join(values)  
                break
        return lines
    

    def _change_D4(self, lines, value):
        pattern = r"^\*Damage Initiation.*JOHNSON COOK.*"  
        for i, line in enumerate(lines):
            if re.match(pattern, line):
                values = lines[i + 1].split(',')
                values[3] = f"{value:>7}"   
                lines[i + 1] = ','.join(values)  
                break
        return lines
    

    def _change_D5(self, lines, value):
        pattern = r"^\*Damage Initiation.*JOHNSON COOK.*"  
        for i, line in enumerate(lines):
            if re.match(pattern, line):
                values = lines[i + 1].split(',')
                values[4] = f"{value:>7}"   
                lines[i + 1] = ','.join(values)  
                break
        return lines
    

    def _change_p(self, lines, p):
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
