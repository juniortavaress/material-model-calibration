from backend.aux_files.aux_geometry.geometry.getGeometry import GetGeometry
from backend.aux_files.aux_geometry.auxFiles.generalFunctions import AuxFunctions
import json

class DataInicialization():
    def __init__(self):
        super(DataInicialization, self).__init__()

    # Load data from JSON and store UI elements and corresponding values in a dictionary
    def get_defaut_datas(self):
        with open('dataDefautInput.json', 'r') as file:
            data = json.load(file)

        self.chip_elements = {self.ui.chipName: str(data['chipPlateData']['createPartInformation']['Name']),
                              self.ui.chipHeight: str(data['chipPlateData']['createPartInformation']['Height']),
                              self.ui.chipWidth: str(data['chipPlateData']['createPartInformation']['Width']),
                              self.ui.chipTrickness: str(data['chipPlateData']['createPartInformation']['Trickness']),
                              self.ui.chipGlobalSize: str(data['chipPlateData']['createMeshInformation']['globalSize']),
                              self.ui.chipMininumFactor: str(data['chipPlateData']['createMeshInformation']['minSizeFactor']),
                              self.ui.chipDeviationFactor: str(data['chipPlateData']['createMeshInformation']['deviationFactor']),
                              self.ui.chipOtherInfo: "defaut"}

        self.tool_elements = {self.ui.toolName: str(data['toolData']['createPartInformation']['Name']),
                              self.ui.toolTrickness: str(data['toolData']['createPartInformation']['Trickness']),
                              self.ui.toolClearanceAngle: str(data['toolData']['createPartInformation']['clearanceAngle']),
                              self.ui.toolRakeAngle: str(data['toolData']['createPartInformation']['rakeAngle']),
                              self.ui.toolClearanceDimension: str(data['toolData']['createPartInformation']['clearanceFaceDimension']),
                              self.ui.toolRakeDimension: str(data['toolData']['createPartInformation']['rakeFaceDimension']),
                              self.ui.toolRadius: str(data['toolData']['createPartInformation']['Radius']),
                              self.ui.toolPartition01: str(data['toolData']['createPartitionInformation']['partition01']),
                              self.ui.toolPartition02: str(data['toolData']['createPartitionInformation']['partition02']),
                              self.ui.toolGlobalSize: str(data['toolData']['createMeshInformation']['globalSize']),
                              self.ui.toolDeviationFactor: str(data['toolData']['createMeshInformation']['deviationFactor']),
                              self.ui.toolMinimumFactor: str(data['toolData']['createMeshInformation']['minSizeFactor'])}

        self.eulerian_elements = {self.ui.eulerianName: str(data['eulerianData']['createPartInformation']['Name']),
                                  self.ui.eulerianWidth: str(data['eulerianData']['createPartInformation']['Width']),
                                  self.ui.eulerianHeight: str(data['eulerianData']['createPartInformation']['Height']),
                                  self.ui.eulerianTrickness: str(data['eulerianData']['createPartInformation']['Trickness']),
                                  self.ui.eulerianPartitionX1: str(data['eulerianData']['createParticionInformation']['x_points'][0]),
                                  self.ui.eulerianPartitionX2: str(data['eulerianData']['createParticionInformation']['x_points'][1]),
                                  self.ui.eulerianPartitionX3: str(data['eulerianData']['createParticionInformation']['x_points'][2]),
                                  self.ui.eulerianPartitionX4: str(data['eulerianData']['createParticionInformation']['x_points'][3]),
                                  self.ui.eulerianPartitionY1: str(data['eulerianData']['createParticionInformation']['y_points'][0]),
                                  self.ui.eulerianPartitionY2: str(data['eulerianData']['createParticionInformation']['y_points'][1]),
                                  self.ui.eulerianPartitionY3: str(data['eulerianData']['createParticionInformation']['y_points'][2]),
                                  self.ui.eulerianPartitionY4: str(data['eulerianData']['createParticionInformation']['y_points'][3]),
                                  self.ui.eulerianGlobalSize: str(data['eulerianData']['createMeshInformation']['globalSize']),
                                  self.ui.eulerianDeviationFactor: str(data['eulerianData']['createMeshInformation']['deviationFactor']),
                                  self.ui.eulerianMininumFactor: str(data['eulerianData']['createMeshInformation']['minSizeFactor'])}

        self.assembly_elements = {self.ui.overWorkpiece: str(data['assemblyAndSimulationData']['chipPlatePosition']['clearanceOverWorkpiece']),
                                  self.ui.fromTool: str(data['assemblyAndSimulationData']['chipPlatePosition']['distanceFromTool']),
                                  self.ui.xTool: str(data['assemblyAndSimulationData']['toolPosition']['xPosition']),
                                  self.ui.yTool: str(data['assemblyAndSimulationData']['toolPosition']['yPosition']),
                                  self.ui.feed: str(data['assemblyAndSimulationData']['toolPosition']['feed']),
                                  self.ui.timePeriod: str(data['assemblyAndSimulationData']['stepsAndHistoryInformation']['timePeriod'])}


        DataInicialization.set_defaut_infos(self)

    # Update the UI elements based on the checkbox state
    def set_defaut_infos(self):
        elements = [self.chip_elements, self.tool_elements, self.eulerian_elements, self.assembly_elements]
        for element in elements:
            for key, value in element.items():
                key.setText(value if self.ui.defautValues.isChecked() else "")

        if self.ui.defautValues.isChecked():
            GetGeometry.set_info(self)
        else:
            self.ui.saveButton.setEnabled(False)
            self.ax_geometry.clear()
            self.ax_geometry.set_axis_off()
            self.canvas_geometry.draw()
            [self.ui.tabWidget.setTabIcon(value, QIcon()) for value in [0, 1, 2, 3]]









