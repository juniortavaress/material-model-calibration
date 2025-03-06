import subprocess

abaqus_command_temperatures = r'C:\SIMULIA\Commands\abq2021.bat python S:\Junior\abaqus-with-python\otimization-scripts\new-version\material-model-calibration\backend\get_result_from_odb_file\get_temps.py'

result = subprocess.run(abaqus_command_temperatures, shell=True, capture_output=True, text=True)

print("Saída padrão:", result.stdout)
print("Erro (se houver):", result.stderr)
