# -*- coding: utf-8 -*-
# """ Define o terminal cd C:\ temp e usa o comando abaqus cae noGUI=S:/Junior/Abaqus+Python/PythonScriptforAbaqus/backend/main.py """
import sys
sys.dont_write_bytecode = True
import os
import json
import inspect
from abaqus import *
from abaqusConstants import *
import numpy as np
from part import *
from step import *
from material import *
from section import *
from assembly import *
from interaction import *
from mesh import *
from visualization import *
from connectorBehavior import *

class Main():
    def __init__(self):
        print("[Main] Iniciando execução...")
        Main.changeDirectory(self)
        Main.setupModel(self)
        Main.createGeometryAndAssembly(self)


    def changeDirectory(self):
        current_directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) # Path to the folder geometryAndAssembly
        self.main_directory = os.path.dirname(os.path.dirname(current_directory)) # Path to the folder backend
        work_directory = os.chdir(current_directory) # Define the main directory as geometryAndAssembly

    def setupModel(self):
        mdb.Model(modelType=STANDARD_EXPLICIT, name='restartMode')
        for model_name in list(mdb.models.keys()):
            if model_name != 'restartMode':
                del mdb.models[model_name]

        for job_name in list(mdb.jobs.keys()):
            del mdb.jobs[job_name]
        
        self.path_simulation_datas = r"C:\MaterialOtimization\TT1606\defaut\geometry_datas"
        self.path_INP = r"C:\MaterialOtimization\TT1606\defaut\INPFiles"
        self.path_CAE = r"C:\MaterialOtimization\TT1606\defaut\CAE"

    def createGeometryAndAssembly(self):
        # import imports
        from materials import Materials
        from create_chip_plate import ChipPlateModel
        from create_eulerian import EulerianModel
        from create_tool import ToolModel
        from assembly_and_simulation import AssemblyModel

        for files in os.listdir(self.path_simulation_datas):
            if files != "geometry_datas.json":

                with open(os.path.join(self.path_simulation_datas, files), 'r') as file:
                    data = json.load(file)

                ModelName = str(data['generalInformation']['modelName'])
                mdb.Model(modelType=STANDARD_EXPLICIT, name=ModelName)

                Materials(ModelName)
                ChipPlateModel(data)
                EulerianModel(data)
                ToolModel(data)
                fileName = files[:-5] 
                AssemblyModel(data, self.path_INP, self.path_CAE, fileName)

            try:
                del mdb.models['restartMode']
            except:
                pass

            os.chdir(self.path_CAE)
            mdb.saveAs(pathName='simulation_CAE')



model = Main()



