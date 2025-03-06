import os
import yaml
import shutil
import pandas as pd
import openpyxl
from openpyxl.styles import Alignment, Font
from openpyxl.worksheet.table import Table, TableStyleInfo

class ExcelManager():
    def create_excel_results(self):
        # Get parameters names
        yaml_path = os.path.join(self.user_config, "parameters.yaml")
        with open(yaml_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
        param_set = next((param_values["Parameters"] for values in data.values() for param_values in values.values()))
        parameter_names = list(param_set.keys())

        # Creating the excel file to save the datas
        data_path = os.path.join(self.excel_files, "datas.xlsx")
        if not os.path.exists(data_path):
            columns = ["Iteration number", "Parameter Set", "Condition", "Error", "Error Fc", "Error Fn", "Error CCR", "Error CSR"]
            
            parameter_columns = [f"Parameter {key}" for key in parameter_names]
            print(parameter_columns)
            # columns.extend(parameter_columns)
            columns = columns[:3] + parameter_columns + columns[3:]
            df = pd.DataFrame(columns=columns)   
            df = pd.DataFrame(0, columns=columns, index=range(1))
            df.index.name = "Simulation"
            df.to_excel(data_path, index=True, engine="openpyxl")
        # ExcelManager.format_file(self, data_path)


    def create_datas(self):
        """
        Extracts results from the simulation output files and converts them into a structured format.
        """
        for filename, force_and_temp_datas in self.force_and_temp_datas.items():
            file = filename
            chip_datas = self.chip_datas[filename]

            odb_inp_path = os.path.join(self.odb_processing, file)
            output_dir = os.path.join(self.software_path, self.project_name, "odb_processed")
            odb_out_file = os.path.join(output_dir, f"{file}.odb")

            # if not os.path.exists(output_dir):
            #     os.makedirs(output_dir)
            # shutil.move(odb_inp_path, odb_out_file)

            info = file.split("_int")
            condition = file.split("_int_")[0]
            param_info = f"int{info[1]}"
            iteration_number = (param_info.split("int_")[1]).split("_set_")[0]
            set_number = (param_info.split("int_")[1]).split("_set_")[1]

            simulated_cutting_forces = force_and_temp_datas["Cutting Force [N].mean"]
            simulated_normal_forces = force_and_temp_datas["Normal Force [N].mean"]
            simulated_temperature = force_and_temp_datas["Maximum Temperature at Last Frame [°C]"]
            chip_compression_ratio = chip_datas["Chip Compression Ratio (CCR)"]
            chip_segmentation_ratio = chip_datas["Chip Segmentatio Ratio (CSR)"]

            yaml_path = os.path.join(self.user_config, "parameters.yaml")
            with open(yaml_path, "r", encoding="utf-8") as file:
                data = yaml.safe_load(file)

            for iteration, values in data.items():
                if iteration[-2:] == iteration_number:
                    for set, param_values in values.items():
                        if set[-2:] == set_number:
                            param_set = param_values["Parameters"]

            if condition[4:] in self.target_values:
                target_cutting_force = self.target_values[condition[4:]].get("fc")
                target_normal_force = self.target_values[condition[4:]].get("fn")
                target_chip_compression_ratio = self.target_values[condition[4:]].get("ccr")
                target_chip_segentatio_ratio = self.target_values[condition[4:]].get("csr")

            error_fc = (simulated_cutting_forces - target_cutting_force)/target_cutting_force
            error_fn = (simulated_normal_forces - target_normal_force)/target_normal_force
            error_ccr = (chip_compression_ratio - target_chip_compression_ratio)/target_chip_compression_ratio
            error_csr = (chip_segmentation_ratio - target_chip_segentatio_ratio)/target_chip_segentatio_ratio
            error = (0.5 * abs(error_fc)) + (0.1 * abs(error_fn)) + (0.2 * abs(error_ccr)) + (0.2 * abs(error_csr))

            data = {"Iteration number": int(iteration_number), "Parameter Set": int(set_number),"Condition": condition[4:]}

            for key, value in param_set.items():
                data[f"Parameter {key}"] = value

            data.update({
                "Error": error,
                "Error Fc": error_fc,
                "Error Fn": error_fn,
                "Error CCR": error_ccr,
                "Error CSR": error_csr})
            
            new_info = pd.DataFrame([data])
            data_path = os.path.join(self.excel_files, "datas.xlsx")

            old_df = pd.read_excel(data_path, engine="openpyxl", index_col=0)
            new_df = pd.concat([old_df, new_info], ignore_index=True)
            y = input("testa ai")
            new_df = new_df.loc[~(new_df == 0).all(axis=1)]  


            new_df.index.name = "Simulation"
            new_df.to_excel(data_path, index=True, engine="openpyxl")

            # Defining the best set 
            df_information = pd.read_excel(data_path, engine="openpyxl", index_col=0)
            df_information.index.name = "Simulation"
            df_information["Best Set of Iteraction"] = df_information.groupby("Iteration number")["Error"].transform(lambda x: df_information.loc[x.idxmin(), "Parameter Set"])
            column_order = df_information.columns.tolist()  
            column_order.insert(2, column_order.pop(column_order.index("Best Set of Iteraction")))  # Move "Best Set" para a posição 3
            df_information = df_information[column_order]   
            df_information.to_excel(data_path, index=True, engine="openpyxl")
            # ExcelManager.format_file(self, data_path)


    def format_file(self, data_path):
        # Ajustar formatação do Excel
        wb = openpyxl.load_workbook(data_path)  # Abrir o arquivo Excel
        ws = wb.active  # Selecionar a aba ativa

        # Ajustar largura das colunas e centralizar o texto
        bold_font = Font(bold=True)
        for cell in ws[1]:  # Primeira linha (cabeçalho)
            cell.font = bold_font

        for col in ws.columns:
            max_length = 0
            col_letter = col[0].column_letter  # Letra da coluna no Excel

            for cell in col:
                if cell.value:
                    cell.alignment = Alignment(horizontal="center", vertical="center")  # Centralizar texto
                    max_length = max(max_length, len(str(cell.value)))  # Verificar maior tamanho do texto

            ws.column_dimensions[col_letter].width = max_length + 2  # Ajustar largura da coluna

        for col in ws.columns:
            for cell in col:
                if cell.value and isinstance(cell.value, (int, float)):
                    # Verificar se o nome da coluna começa com "Error"
                    if ws.cell(row=1, column=cell.column).value.startswith("Error"):
                        # Aplicar formato de porcentagem para as células de erro
                        cell.number_format = '0.00%'


        # # Definir o intervalo da tabela (assumindo que a tabela começa na célula A1 e vai até o final dos dados)
        # table_range = f"A1:{openpyxl.utils.get_column_letter(ws.max_column)}{ws.max_row}"

        # # Criar a tabela
        # table = Table(displayName="ResultsTable", ref=table_range)

        # # Aplicar estilo à tabela
        # style = TableStyleInfo(
        #     showFirstColumn=False,
        #     showLastColumn=False,
        #     showRowStripes=True,
        #     showColumnStripes=True
        # )
        # table.tableStyleInfo = style

        # # Adicionar a tabela à planilha
        # ws.add_table(table)

        # Salvar as modificações
        wb.save(data_path)
        wb.close()