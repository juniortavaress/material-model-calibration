
class GetDictionary():
    def __init__(self):
        super(GetDictionary, self).__init__()

    # Returns a dictionary containing default iteration information settings
    def iteration_info(self):
        iteration_info = {"Feed": {"activated": False, "min": 0, "max": 0, "step": 0},
                          "rakeAngle": {"activated": False, "min": 0, "max": 0, "step": 0},
                          "clearanceAngle": {"activated": False, "min": 0, "max": 0, "step": 0},
                          "timePeriod": {"activated": False, "min": 0, "max": 0, "step": 0}}
        return iteration_info


    # Returns the current parameters for iterations based on UI settings
    def iteration_parameters(self):
        values = [[self.ui.P01, self.ui.minP01, self.ui.maxP01, self.ui.stepP01], [self.ui.P02, self.ui.minP02, self.ui.maxP02, self.ui.stepP02]]
        values = [values[0]] if self.ui.numberOfVariables.currentText() == "1" else values
        return values


    # Collects data from the UI and formats it into a structured dictionary.
    def datas_from_ui(self, data):
        # Collects Eulerian data
        data["eulerianData"] = {
                    "createPartInformation": {
                        "Name": self.ui.eulerianName.text(),
                        "Width": float(self.ui.eulerianWidth.text()),
                        "Trickness": float(self.ui.eulerianTrickness.text()),
                        "Height": float(self.ui.eulerianHeight.text())
                    },
                    "createParticionInformation": {
                        "x_points": sorted([
                            float(self.ui.eulerianPartitionX1.text()),
                            float(self.ui.eulerianPartitionX2.text()),
                            float(self.ui.eulerianPartitionX3.text()),
                            float(self.ui.eulerianPartitionX4.text())
                        ]),
                        "y_points": sorted([
                            float(self.ui.eulerianPartitionY1.text()),
                            float(self.ui.eulerianPartitionY2.text()),
                            float(self.ui.eulerianPartitionY3.text()),
                            float(self.ui.eulerianPartitionY4.text())
                        ], reverse=True)
                    },
                    "createMeshInformation": {
                        "globalSize": float(self.ui.eulerianGlobalSize.text()),
                        "deviationFactor": float(self.ui.eulerianDeviationFactor.text()),
                        "minSizeFactor": float(self.ui.eulerianMininumFactor.text())
                    }
                }

        # Collects Chip Plate data
        data["chipPlateData"] = {
            "createPartInformation": {
                "Name": self.ui.chipName.text(),
                "Width": float(self.ui.chipWidth.text()),
                "Trickness": float(self.ui.chipTrickness.text()),
                "Height": float(self.ui.chipHeight.text())
            },
            "createMeshInformation": {
                "globalSize": float(self.ui.chipGlobalSize.text()),
                "deviationFactor": float(self.ui.chipDeviationFactor.text()),
                "minSizeFactor": float(self.ui.chipMininumFactor.text())
            }
        }

        # Collects Tool data
        data["toolData"] = {
            "createPartInformation": {
                "Name": self.ui.toolName.text(),
                "Trickness": float(self.ui.toolTrickness.text()),
                "clearanceAngle": float(self.ui.toolClearanceAngle.text()),
                "rakeAngle": float(self.ui.toolRakeAngle.text()),
                "clearanceFaceDimension": float(self.ui.toolClearanceDimension.text()),
                "rakeFaceDimension": float(self.ui.toolRakeDimension.text()),
                "Radius": float(self.ui.toolRadius.text())
            },
            "createPartitionInformation": {
                "partition01": float(self.ui.toolPartition01.text()),
                "partition02": float(self.ui.toolPartition02.text())
            },
            "createMeshInformation": {
                "globalSize": float(self.ui.toolGlobalSize.text()),
                "deviationFactor": float(self.ui.toolDeviationFactor.text()),
                "minSizeFactor": float(self.ui.toolMinimumFactor.text()),
                "radiusMeshSize": 0.01,
                "noseBiasMaxMeshSize": 0.06,
                "partition02MeshSize": 0.1,
                "noseBiasMinMeshSize": 0.01
            }
        }

        # Collects Assembly and Simulation data
        data["assemblyAndSimulationData"] = {
            "chipPlatePosition": {
                "clearanceOverWorkpiece": float(self.ui.overWorkpiece.text()),
                "distanceFromTool": float(self.ui.fromTool.text())
            },
            "toolPosition": {
                "xPosition": float(self.ui.xTool.text()),
                "yPosition": float(self.ui.yTool.text()),
                "feed": float(self.ui.feed.text())
            },
            "stepsAndHistoryInformation": {
                "timePeriod": float(self.ui.timePeriod.text())
            }
        }
        return data


    # Retrieves a dictionary containing all UI fields to check for validity.
    def get_infos_to_check_gui_fields(self):
        all_about_eulerian = {
                    'Name': self.ui.eulerianName,
                    'Height': self.ui.eulerianHeight,
                    'Width': self.ui.eulerianWidth,
                    'Trickness': self.ui.eulerianTrickness,
                    'Global Size': self.ui.eulerianGlobalSize,
                    'Deviation Factor': self.ui.eulerianDeviationFactor,
                    'Minimum Factor': self.ui.eulerianMininumFactor,
                    'X1': self.ui.eulerianPartitionX1,
                    'X2': self.ui.eulerianPartitionX2,
                    'X3': self.ui.eulerianPartitionX3,
                    'X4': self.ui.eulerianPartitionX4,
                    'Y1': self.ui.eulerianPartitionY1,
                    'Y2': self.ui.eulerianPartitionY2,
                    'Y3': self.ui.eulerianPartitionY3,
                    'Y4': self.ui.eulerianPartitionY4
                }

        all_about_chip = {
            'Name': self.ui.chipName,
            'Height': self.ui.chipHeight,
            'Width': self.ui.chipWidth,
            'Trickness': self.ui.chipTrickness,
            'Global Size': self.ui.chipGlobalSize,
            'Deviation Factor': self.ui.chipDeviationFactor,
            'Minimum Factor': self.ui.chipMininumFactor
        }

        all_about_tool = {
            'Name': self.ui.toolName,
            'Trickness': self.ui.toolTrickness,
            'Rake Angle': self.ui.toolRakeAngle,
            'Rake Dimension': self.ui.toolRakeDimension,
            'Clearance Angle': self.ui.toolClearanceAngle,
            'Clearance Dimension': self.ui.toolClearanceDimension,
            'Radius': self.ui.toolRadius,
            'Partition 01': self.ui.toolPartition01,
            'Partition 02': self.ui.toolPartition02,
            'Global Size': self.ui.toolGlobalSize,
            'Deviation Factor': self.ui.toolDeviationFactor,
            'Minimum Factor': self.ui.toolMinimumFactor
        }

        all_about_assembly = {
            'Clearance Over Workpiece': self.ui.overWorkpiece,
            'Distance From Tool': self.ui.fromTool,
            'Feed': self.ui.feed,
            'Time Period': self.ui.timePeriod
        }
        return [all_about_eulerian, all_about_chip, all_about_tool, all_about_assembly]


    # Returns the color associated with the given index or based on UI selection.
    def get_colors(self, index):
        colors = [
                    '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFC300',
                    '#DAF7A6', '#581845', '#900C3F', '#C70039', '#FF5733',
                    '#FF8D1B', '#33FFBD', '#33A1FF', '#FF33D4', '#FFD700',
                    '#A6D8D2', '#D25D9E', '#5DD25C', '#D21D5D', '#5C75D2'
                ]

        if index:
            color = colors[index % len(colors)]
        elif self.ui.typeOfAnalisys.currentText() == 'NT11' or self.ui.typeRF.currentText() == 'RF1':
            color = 'r'
        elif self.ui.typeOfAnalisys.currentText() == 'RF' and self.ui.typeRF.currentText() == 'RF2':
            color = '#003366'
        elif self.ui.typeOfAnalisys.currentText() == 'RF' and self.ui.typeRF.currentText() == 'RF3':
            color = '#8b5ea7'
        else:
            color = 'r'

        return color
