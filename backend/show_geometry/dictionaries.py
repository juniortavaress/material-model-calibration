from backend.show_geometry.general_functions import AuxFunctions

class GetDictionary():
    def __init__(self):
        super(GetDictionary, self).__init__()

    # Load data from JSON and store UI elements and corresponding values in a dictionary
    def defaut_datas(self):
        self.chip_elements = {self.ui.chipName: "ChipPlate",
                              self.ui.chipHeight: 0.01,
                              self.ui.chipWidth: 1.5,
                              self.ui.chipTrickness: 0.02,
                              self.ui.chipGlobalSize: 0.01,
                              self.ui.chipMininumFactor: 0.1,
                              self.ui.chipDeviationFactor: 0.1}

        self.tool_elements = {self.ui.toolName: "Tool",
                              self.ui.toolTrickness: 0.02,
                              self.ui.toolClearanceAngle: 3.0,
                              self.ui.toolRakeAngle: 12.0,
                              self.ui.toolClearanceDimension: 3.35,
                              self.ui.toolRakeDimension: 3.35,
                              self.ui.toolRadius: 0.08,
                              self.ui.toolPartition01: 1.5,
                              self.ui.toolPartition02: 1.14,
                              self.ui.toolGlobalSize: 0.1,
                              self.ui.toolDeviationFactor: 0.1,
                              self.ui.toolMinimumFactor: 0.1}

        self.eulerian_elements = {self.ui.eulerianName: "Eulerian",
                                  self.ui.eulerianWidth: 3.8,
                                  self.ui.eulerianHeight: 5.0,
                                  self.ui.eulerianTrickness: 0.02,
                                  self.ui.eulerianPartitionX1: 1.5,
                                  self.ui.eulerianPartitionX2: 2.7,
                                  self.ui.eulerianPartitionX3: 3.0,
                                  self.ui.eulerianPartitionX4: 3.3,
                                  self.ui.eulerianPartitionY1: 2.8,
                                  self.ui.eulerianPartitionY2: 1.3,
                                  self.ui.eulerianPartitionY3: 1.23,
                                  self.ui.eulerianPartitionY4: 1.1,
                                  self.ui.eulerianGlobalSize: 0.2,
                                  self.ui.eulerianDeviationFactor: 0.1,
                                  self.ui.eulerianMininumFactor: 0.1}

        self.assembly_elements = {self.ui.overWorkpiece: 0.05,
                                  self.ui.fromTool: 0.2,
                                  self.ui.xTool: 3.0,
                                  self.ui.yTool: 1.3,
                                  self.ui.feed: 0.05,
                                  self.ui.timePeriod: 0.003}




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
            'Deep of Cuth': self.ui.feed,
            'Time Period': self.ui.timePeriod
        }
        return [all_about_eulerian, all_about_chip, all_about_tool, all_about_assembly]



