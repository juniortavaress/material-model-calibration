# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2021 replay file
# Internal Version: 2020_03_06-15.50.37 167380
# Run by adam-ua769pu3t3n7k4o on Fri Feb 21 12:56:02 2025
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=350.390594482422, 
    height=204.088897705078)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
execfile(
    's:/Junior/abaqus-with-python/otimization-scripts/new-version/material-model-calibration/backend/get_result_from_odb_file/get_chip_obj_file.py', 
    __main__.__dict__)
#: Model: S:/Junior/abaqus-with-python/otimization-scripts/new-version/material-model-calibration/Teste/auxiliary_files/odb_processing/sim_v1000_h100_gam-6_int_01_set_01.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     3
#: Number of Meshes:             3
#: Number of Element Sets:       7
#: Number of Node Sets:          11
#: Number of Steps:              1
#: Model: S:/Junior/abaqus-with-python/otimization-scripts/new-version/material-model-calibration/Teste/auxiliary_files/odb_processing/sim_v1000_h100_gam-6_int_01_set_02.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     3
#: Number of Meshes:             3
#: Number of Element Sets:       7
#: Number of Node Sets:          11
#: Number of Steps:              1
#: Model: S:/Junior/abaqus-with-python/otimization-scripts/new-version/material-model-calibration/Teste/auxiliary_files/odb_processing/sim_v166_h100_gam6_int_01_set_01.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     3
#: Number of Meshes:             3
#: Number of Element Sets:       7
#: Number of Node Sets:          11
#: Number of Steps:              1
#: Model: S:/Junior/abaqus-with-python/otimization-scripts/new-version/material-model-calibration/Teste/auxiliary_files/odb_processing/sim_v166_h100_gam6_int_01_set_02.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     3
#: Number of Meshes:             3
#: Number of Element Sets:       7
#: Number of Node Sets:          11
#: Number of Steps:              1
#* Exit code: 0
#* File 
#* "s:/Junior/abaqus-with-python/otimization-scripts/new-version/material-model-calibration/backend/get_result_from_odb_file/get_chip_obj_file.py", 
#* line 120, in <module>
#*     sys.exit()
