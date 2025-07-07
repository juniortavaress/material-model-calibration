import os
import numpy as np

from PySide6.QtGui import QIcon
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QFileDialog

from backend.show_geometry.graph_setup import GraphManager
from backend.show_geometry.dictionaries import GetDictionary
from backend.show_geometry.general_functions import AuxFunctions


class GetGeometry():
    def __init__(self):
        super(GetGeometry, self).__init__()

    # Get info from GUI and if all required information is provided, generate the 3D graph, otherwise clear the previous plot
    def set_info(self):
        # try:
        PAGE_MAPPINGS = {0: 'Eulerian', 1: 'ChipPlate', 2: 'Tool', 3: 'Assembly'}
        geometry = PAGE_MAPPINGS[self.ui.tabWidget.currentIndex()]
        all_Infos = GetGeometry.check_general_infos(self, self.ui.tabWidget.currentIndex())
        # except:
        #     all_Infos = False
        #     print("except set_info")

        # print('all_Infos', all_Infos)

        if all_Infos != False:
            print("NOTES\n", all_Infos)
            GraphManager.plot_3d_graph(self, geometry)
            self.ui.button_create_geometry_next.setEnabled(True)
            self.ui.button_create_geometry_next.clicked.connect(lambda: self.ui.pages.setCurrentIndex(5))
            self.ui.button_create_geometry_next.clicked.connect(lambda: GetGeometry.save_infos(self))
            self.ui.button_create_geometry_apply.clicked.connect(lambda: GetGeometry.save_infos(self))

        else:
            GraphManager.canvas(self)
            # self.ui.tabWidget.setTabIcon(self.ui.tabWidget.currentIndex(), QIcon())
            self.ui.button_create_geometry_next.setEnabled(False)

        for widget in self.ui.geometryPage.findChildren(QLineEdit):
            widget.textChanged.connect(lambda: self.ui.button_create_geometry_next.setEnabled(True))
            # widget.textChanged.connect(lambda: self.ui.tabWidget.setTabIcon(self.ui.tabWidget.currentIndex(), QIcon()))

    def get_defaut_datas(self):
        GetDictionary.defaut_datas(self)
        GetGeometry.set_defaut_infos(self)

    # Update the UI elements based on the checkbox state
    def set_defaut_infos(self):
        elements = [self.chip_elements, self.tool_elements, self.eulerian_elements, self.assembly_elements]
        for element in elements:
            for key, value in element.items():
                key.setText(str(value) if self.ui.defautValues.isChecked() else "")

        if self.ui.defautValues.isChecked():
            GetGeometry.set_info(self)
        else:
            GraphManager.canvas(self)
            [self.ui.tabWidget.setTabIcon(value, QIcon()) for value in [0, 1, 2, 3]]

    # Check if all the general information are filled with the right content
    def check_general_infos(self, page):
        all_Infos = True
        all_infos_widgets = GetDictionary.get_infos_to_check_gui_fields(self)

        page_mappings = {
            0: (all_infos_widgets[0], self.ui.eulerianWarning, self.ui.eulerianName),
            3: (all_infos_widgets[3], self.ui.assemblyWarning, 'defaut'),
            2: (all_infos_widgets[2], self.ui.toolWarning, self.ui.toolName),
            1: (all_infos_widgets[1], self.ui.chipWarning, self.ui.chipName)}

        infos_widget, label_warning, non_numerical_label = page_mappings[page]

        for key, info in infos_widget.items():
            if not info.text().strip():
                all_Infos = False
                AuxFunctions.warning(self, label_warning, "Set all parameters")
                return all_Infos

            elif info.text().strip() and info != non_numerical_label and info != "":
                try:
                    float(info.text())
                except:
                    all_Infos = False
                    AuxFunctions.warning(self, label_warning, "The parameter " + key + "\n must be a number value with dot as decimal separator!")
                    return all_Infos

        return all_Infos


    # Save the user inputs calling other functions
    def save_infos(self):

        data = {"generalInformation": {"modelName": "PythonModel"}}
        data = GetDictionary.datas_from_ui(self, data)
        AuxFunctions.save_dict(os.path.join(self.defaut_geometry, "geometry_datas.json"), data)

        # print(os.path.join(self.defaut_geometry, "geometry_datas.json"))
        # ICON_CHECKMARK = QIcon(':/new_Icons/Icons/checkmark.png')
        # [self.ui.tabWidget.setTabIcon(value, ICON_CHECKMARK) for value in [0, 1, 2, 3]] if self.ui.defautValues.isChecked() else self.ui.tabWidget.setTabIcon(self.ui.tabWidget.currentIndex(), ICON_CHECKMARK)

