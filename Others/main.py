# from odbAccess import openOdb
import subprocess
import sys
import os 
# from convert_obj_to_excel import GetChipMeasure

current_path = os.getcwd()
abaqus_command = rf'C:\SIMULIA\Commands\abq2021.bat cae script={current_path}\backend\get_result_from_odb_file\get_forces.py'
result = subprocess.run(abaqus_command, shell=True, capture_output=True, check=True, text=True)
print(result)
# GetChipMeasure.main_to_chip_results()




# abaqus_command_temperatures = rf'C:\SIMULIA\Commands\abq2021.bat python {dir}\get_temps.py'

