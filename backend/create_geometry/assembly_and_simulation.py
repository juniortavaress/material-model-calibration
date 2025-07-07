# -*- coding: utf-8 -*-
from imports import *

class AssemblyModel():
    def __init__(self, data, path_INP, path_CAE, filename):
        # Creating Assembly
        self.dataInput(data)
        self.assemblyPositions()
        self.stepsAndHistory()
        self.setInteractions()
        self.setContactAndConstraints()
        self.setBoundaryConditionsAndPredefinedFields()
        self.submitSimulation(path_INP, path_CAE, filename)

    def dataInput(self, data):
        # Calling Model
        self.ModelName = str(data['generalInformation']['modelName'])
        self.m = mdb.models[self.ModelName]
        # Defining Variables
        self.xToolPosition = data['assemblyAndSimulationData']['toolPosition']['xPosition']
        self.yToolPosition = data['assemblyAndSimulationData']['toolPosition']['yPosition']
        self.xChipPlatePosition = self.xToolPosition - data['chipPlateData']['createPartInformation']['Width'] - data['assemblyAndSimulationData']['chipPlatePosition']['distanceFromTool']
        self.yChipPlatePosition = self.yToolPosition + data['assemblyAndSimulationData']['chipPlatePosition']['clearanceOverWorkpiece']
        self.Feed = float(-data['assemblyAndSimulationData']['toolPosition']['feed'])
        self.StepName = "CuttingStep"
        self.TimePeriod = data['assemblyAndSimulationData']['stepsAndHistoryInformation']['timePeriod']

    def assemblyPositions(self):
        # Setting the default coordinate system to Cartesian
        self.m.rootAssembly.DatumCsysByDefault(CARTESIAN)
        # Creating instances of parts in the assembly
        self.m.rootAssembly.Instance(dependent=ON, name='ChipPlate-1', part=self.m.parts['ChipPlate'])
        self.m.rootAssembly.Instance(dependent=ON, name='Eulerian-1', part=self.m.parts['Eulerian'])
        self.m.rootAssembly.Instance(dependent=ON, name='Tool-1', part=self.m.parts['Tool'])
        # Positioning the Chip Plate
        self.m.rootAssembly.translate(instanceList=('ChipPlate-1', ), vector=(self.xChipPlatePosition, self.yChipPlatePosition, 0.0))
        # Positioning the Tool
        self.m.rootAssembly.translate(instanceList=('Tool-1', ), vector=(self.xToolPosition, self.yToolPosition, 0.0))
        # Applying the Feed to the Tool
        self.m.rootAssembly.translate(instanceList=('Tool-1', ), vector=(0.0, self.Feed, 0.0))
        # Creating an assembly set that includes multiple parts
        self.m.rootAssembly.Set(cells=self.m.rootAssembly.instances['ChipPlate-1'].cells.getSequenceFromMask(mask=('[#1 ]', ), )+\
            self.m.rootAssembly.instances['Eulerian-1'].cells.getSequenceFromMask(mask=('[#1ffffff ]', ), )+\
            self.m.rootAssembly.instances['Tool-1'].cells.getSequenceFromMask(mask=('[#7f ]', ), ), name='AssembleSet')
    
    def stepsAndHistory(self):
        # print('123')
        # Creating a new step for the simulation
        self.m.TempDisplacementDynamicsStep(improvedDtMethod=ON, name=self.StepName, previous='Initial', timePeriod=self.TimePeriod)
        # Defining field outputs for the new step
        # self.m.FieldOutputRequest(createStepName='CuttingStep', 
        # name='FieldOutput', variables=('U', 'UT', 'UR', 'V', 'VT', 'VR', 'A', 'AT', 'AR', 'RBANG', 'RBROT', 'RF', 'RT', 'RM', 'CF', 'SF', 'SQEQ', 'NFORC', 'NFORCSO', 'RBFOR', 
        # 'BF', 'GRAV', 'P', 'HP', 'IWCONWEP', 'TRSHR', 'TRNOR', 'VP', 'STAGP', 'SBF', 'CSTRESS', 'CDISP', 'CSLIPR', 'CTANDIR', 'CFORCE', 'CTHICK', 'FSLIPR', 'FSLIP', 'CFRICWORK', 
        # 'PPRESS', 'ENER', 'ELEN', 'ELEDEN', 'EDCDEN', 'EDT', 'NT', 'TEMP', 'HFL', 'HFLA', 'HTL', 'HTLA', 'RFL',  'TEMPMAVG'))
        self.m.FieldOutputRequest(createStepName='CuttingStep', name='FieldOutput', variables=('NT', 'HFL'))

        # Creating history outputs 
        self.m.HistoryOutputRequest(createStepName='CuttingStep', name='CuttingForce', numIntervals=1000, rebar=EXCLUDE, region= self.m.rootAssembly.allInstances['Tool-1'].sets['ToolRP'], sectionPoints=DEFAULT, variables=('RF1', 'RF2', 'RF3'))
        self.m.HistoryOutputRequest(createStepName='CuttingStep', name='IHE_ALL', numIntervals=1000, rebar=EXCLUDE, region=self.m.rootAssembly.sets['AssembleSet'], sectionPoints=DEFAULT, variables=('ALLIHE', ))
        self.m.HistoryOutputRequest(createStepName='CuttingStep', name='IHE_Bilanz', numIntervals=1000, rebar=EXCLUDE, region=self.m.rootAssembly.allInstances['Eulerian-1'].sets['EulerDomain'], sectionPoints=DEFAULT, variables=('ALLIHE', ))
        self.m.HistoryOutputRequest(createStepName='CuttingStep', name='IHE_TOOL', numIntervals=1000, rebar=EXCLUDE, region=self.m.rootAssembly.allInstances['Tool-1'].sets['ToolDomain'], sectionPoints=DEFAULT, variables=('ALLIHE', ))
        self.m.HistoryOutputRequest(createStepName='CuttingStep', name='IHE_Workpiece', numIntervals=1000, rebar=EXCLUDE, region=self.m.rootAssembly.allInstances['Eulerian-1'].sets['WorkpieceDomain'], sectionPoints=DEFAULT, variables=('ALLIHE', ))
        self.m.HistoryOutputRequest(createStepName='CuttingStep', name='Temperature_Tool', rebar=EXCLUDE, region=self.m.rootAssembly.allInstances['Tool-1'].sets['ToolTemperatureOutputSet'], sectionPoints=DEFAULT, variables=('NT', ))

    def setInteractions(self):
        # Define contact properties between different parts
        # Contact chip-plate-contact
        self.m.ContactProperty('chip-plate-contact')
        self.m.interactionProperties['chip-plate-contact'].TangentialBehavior(dependencies=0, directionality=ISOTROPIC, elasticSlipStiffness=None, formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, pressureDependency=OFF, shearStressLimit=None, slipRateDependency=OFF, table=((0.01, ), ), temperatureDependency=OFF)
        self.m.interactionProperties['chip-plate-contact'].NormalBehavior(allowSeparation=ON, constraintEnforcementMethod=DEFAULT, pressureOverclosure=HARD)
        # Contact self-contact
        self.m.ContactProperty('self-contact')
        self.m.interactionProperties['self-contact'].TangentialBehavior(dependencies=0, directionality=ISOTROPIC, elasticSlipStiffness=None, formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, pressureDependency=OFF, shearStressLimit=None, slipRateDependency=OFF, table=((0.015, ), ), temperatureDependency=OFF)
        self.m.interactionProperties['self-contact'].NormalBehavior(allowSeparation=ON, constraintEnforcementMethod=DEFAULT, pressureOverclosure=HARD)
        # Contact tool-chip-contact
        self.m.ContactProperty('tool-chip-contact')
        self.m.interactionProperties['tool-chip-contact'].TangentialBehavior(dependencies=0, directionality=ISOTROPIC, elasticSlipStiffness=None, formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, pressureDependency=OFF, shearStressLimit=None, slipRateDependency=OFF, table=((0.46, 100.0), (0.46, 150.0), (0.46, 200.0), (0.459979, 225.0), (0.459888, 250.0), (0.459703, 275.0), (0.459407, 300.0)), temperatureDependency=ON)
        self.m.interactionProperties['tool-chip-contact'].NormalBehavior(allowSeparation=ON, constraintEnforcementMethod=DEFAULT, pressureOverclosure=HARD)
        self.m.interactionProperties['tool-chip-contact'].ThermalConductance(clearanceDependency=OFF, definition=TABULAR, dependenciesP=0, massFlowRateDependencyP=OFF, pressureDepTable=((10000.0, 0.0), (10000.0, 1000.0)), pressureDependency=ON, temperatureDependencyP=OFF)
        # self.m.interactionProperties['tool-chip-contact'].HeatGeneration(conversionFraction=0.9, secondaryFraction=0.5)
        self.m.interactionProperties['tool-chip-contact'].HeatGeneration(conversionFraction=0.9)
        # Defining the contact interaction in the simulation step
        self.m.ContactExp(createStepName='CuttingStep', name='contact')

    def setContactAndConstraints(self):
        # Assigning contact properties and setting up constraints between parts
        self.m.interactions['contact'].includedPairs.setValuesInStep(stepName='CuttingStep', useAllstar=ON)
        self.m.interactions['contact'].contactPropertyAssignments.appendInStep(assignments=((GLOBAL, SELF, 'tool-chip-contact'), (self.m.rootAssembly.instances['ChipPlate-1'].surfaces['ChipPlateSurface'], 'Eulerian-1.da718-1', 'chip-plate-contact')), stepName='CuttingStep')
        self.m.RigidBody(bodyRegion=self.m.rootAssembly.instances['Tool-1'].sets['ToolDomain'], name='ToolConstraint', refPointRegion=self.m.rootAssembly.instances['Tool-1'].sets['ToolRP'])
        self.m.RigidBody(bodyRegion=self.m.rootAssembly.instances['ChipPlate-1'].sets['PlateDomain'], name='ChipPlateConstraint', refPointRegion=self.m.rootAssembly.instances['ChipPlate-1'].sets['PlateRP'])

    def setBoundaryConditionsAndPredefinedFields(self):
        # Setting boundary conditions for the simulation
        self.m.VelocityBC(amplitude=UNSET, createStepName='CuttingStep', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-WorkpieceBottom', region=self.m.rootAssembly.instances['Eulerian-1'].sets['WorkpieceBottom'], v1=833.33, v2=0.0, v3=0.0, vr1=0.0, vr2=0.0, vr3=0.0)
        self.m.VelocityBC(amplitude=UNSET, createStepName='CuttingStep', distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-zLock', region=self.m.rootAssembly.instances['Eulerian-1'].sets['EulerDomain'], v1=UNSET, v2=UNSET, v3=0.0, vr1=UNSET, vr2=UNSET, vr3=UNSET)
        self.m.EncastreBC(createStepName='CuttingStep', localCsys=None, name='ToolFix', region=self.m.rootAssembly.instances['Tool-1'].sets['ToolRP'])
        self.m.EncastreBC(createStepName='CuttingStep', localCsys=None, name='ChipPlateFix', region=self.m.rootAssembly.instances['ChipPlate-1'].sets['PlateRP'])
        # Defining the initial velocity and temperature for the simulation
        self.m.Velocity(distributionType=MAGNITUDE, field='', name='cuttingMove', omega=0.0, region=self.m.rootAssembly.instances['Eulerian-1'].sets['WorkpieceDomain'], velocity1=833.33)
        self.m.Temperature(createStepName='Initial', crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, distributionType=UNIFORM, magnitudes=(29.0, ), name='InitialTemperature', region=self.m.rootAssembly.sets['AssembleSet'])
        self.m.MaterialAssignment(assignmentList=((self.m.rootAssembly.instances['Eulerian-1'].sets['EulerDomain'], (0, )), (self.m.rootAssembly.instances['Eulerian-1'].sets['WorkpieceDomain'], (1, ))), instanceList=(self.m.rootAssembly.instances['Eulerian-1'], ), name='MaterialAssignment', useFields=False)

    def submitSimulation(self, path_INP, path_CAE, filename):
        # Creating and submitting the simulation job
        job = mdb.Job(activateLoadBalancing=False, atTime=None, contactPrint=OFF, 
        description='', echoPrint=OFF, explicitPrecision=SINGLE, historyPrint=OFF, 
        memory=90, memoryUnits=PERCENTAGE, model=self.ModelName, modelPrint=OFF, 
        multiprocessingMode=DEFAULT, name=filename, nodalOutputPrecision=SINGLE, 
        numCpus=6, numDomains=6, queue=None, 
        resultsFormat=ODB, scratch='', type=ANALYSIS, userSubroutine='', waitHours=
        0, waitMinutes=0)

        # Writing the INP file        
        os.chdir(path_INP)
        job.writeInput(consistencyChecking=OFF)

