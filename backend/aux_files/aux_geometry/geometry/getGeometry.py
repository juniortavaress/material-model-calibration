
from backend.aux_files.aux_geometry.layout.pageLayout import PageLayout
from backend.aux_files.aux_geometry.layout.graphLayout import GraphLayout
from backend.aux_files.aux_geometry.geometry.facesGenerator import FacesGenerator
from backend.aux_files.aux_geometry.auxFiles.generalFunctions import AuxFunctions
from backend.aux_files.aux_geometry.auxFiles.dictionaries import GetDictionary
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QFileDialog
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class GetGeometry():
    def __init__(self):
        super(GetGeometry, self).__init__()

    # Get info from GUI and if all required information is provided, generate the 3D graph, otherwise clear the previous plot
    def set_info(self):
        try:
            PAGE_MAPPINGS = {0: 'Eulerian', 1: 'ChipPlate', 2: 'Tool', 3: 'Assembly'}
            geometry = PAGE_MAPPINGS[self.ui.tabWidget.currentIndex()]
            all_Infos = PageLayout.check_general_infos(self, self.ui.tabWidget.currentIndex())
        except:
            all_Infos = None

        if all_Infos:
            GetGeometry.plot_3d_graph(self, geometry)
            self.ui.chipWarning.setText("")
        else:
            self.ax_geometry.clear()
            self.ax_geometry.set_axis_off()
            self.canvas_geometry.draw()
            self.ui.tabWidget.setTabIcon(self.ui.tabWidget.currentIndex(), QIcon())

        for widget in self.ui.geometryPage.findChildren(QLineEdit):
            widget.textChanged.connect(lambda: self.ui.saveButton.setEnabled(False))
            widget.textChanged.connect(lambda: self.ui.tabWidget.setTabIcon(self.ui.tabWidget.currentIndex(), QIcon()))


    # Plots the 3D geometry based on the selected type
    def plot_3d_graph(self, geometry):
        self.ax_geometry.clear()
        if self.ui.tabWidget.currentIndex() == 3:
            partitions = sorted([float(self.ui.eulerianPartitionY1.text()), float(self.ui.eulerianPartitionY2.text()), float(self.ui.eulerianPartitionY3.text()), float(self.ui.eulerianPartitionY4.text())], reverse=True)[1]
            x = sorted([float(self.ui.eulerianPartitionX1.text()), float(self.ui.eulerianPartitionX2.text()), float(self.ui.eulerianPartitionX3.text()), float(self.ui.eulerianPartitionX4.text())])[2]
            self.ui.xTool.setText(str(x))
            self.ui.yTool.setText(str(partitions))
            self.xChipPlatePosition = x - float(self.ui.chipWidth.text()) - float(self.ui.fromTool.text())
            self.zChipPlatePosition = partitions + float(self.ui.overWorkpiece.text())

        faces = FacesGenerator.call_faces(self, geometry)
        alpha = 0.2 if geometry == 'Eulerian' else 1.0
        self.ax_geometry.add_collection3d(Poly3DCollection(faces, facecolors='#009c94', linewidths=1, edgecolors='white', alpha=alpha))
        GraphLayout.axis_layout(self, geometry)
        GraphLayout.resize(self)
        # self.ui.saveButton.setEnabled(True)


    # Save the user inputs calling other functions
    def save_infos(self):
        try:
            data = AuxFunctions.open_dict('dict', self.path_datas_input)
        except:
            data = {"generalInformation": {"modelName": "PythonModel"}}

        try:
            data = GetDictionary.datas_from_ui(self, data)
            AuxFunctions.save_dict(self.path_datas_input, data)
            AuxFunctions.clean_and_create_folder(self, self.path_folder_simulation_datas)
            AuxFunctions.save_dict(self.path_datas_single_simulation, data)
            self.ui.iterationButton.setEnabled(True)
            print('Saved (Geometry/getGeometry.py -> save_infos)')
        except:
            print('Unable to save the information. (Geometry/getGeometry.py -> save_infos)')

        ICON_CHECKMARK = QIcon(':/icons/Icons/checkmark.png')
        [self.ui.tabWidget.setTabIcon(value, ICON_CHECKMARK) for value in [0, 1, 2, 3]] if self.ui.defautValues.isChecked() else self.ui.tabWidget.setTabIcon(self.ui.tabWidget.currentIndex(), ICON_CHECKMARK)



