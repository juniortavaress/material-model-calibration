
from backend.aux_files.aux_geometry.layout.graphLayout import GraphLayout
from backend.aux_files.aux_geometry.auxFiles.dictionaries import GetDictionary
from backend.aux_files.aux_geometry.auxFiles.generalFunctions import AuxFunctions

class PageLayout():
    def __init__(self):
        super(PageLayout, self).__init__()

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
                break
            elif info.text().strip() and info != non_numerical_label:
                try:
                    float(info.text())
                except:
                    all_Infos = False
                    AuxFunctions.warning(self, label_warning, "The parameter " + key + "\n must be a number value with dot as decimal separator!")

        return all_Infos


    # Sets which iteration variables are enabled based on the current selection
    def set_iteration_variables_enabled(self):
        comboBoxComponents = [self.ui.P01, self.ui.stepP01, self.ui.P02, self.ui.stepP02]
        labelComponents = [self.ui.minP01, self.ui.maxP01, self.ui.minP02, self.ui.maxP02]
        components = [self.ui.P01, self.ui.minP01, self.ui.maxP01, self.ui.stepP01, self.ui.P02, self.ui.minP02, self.ui.maxP02, self.ui.stepP02]
        if self.ui.numberOfVariables.currentIndex() == 1:
            [component.setEnabled(True) for component in components[:4]]
            [component.setEnabled(False) for component in components[4:]]
            [component.setText(" ") for component in labelComponents[2:]]
            [component.setCurrentIndex(0) for component in comboBoxComponents[2:]]
        elif self.ui.numberOfVariables.currentIndex() == 2:
            [component.setEnabled(True) for component in components]
        else:
            [component.setEnabled(False) for component in components]
            [component.setText(" ") for component in labelComponents]
            [component.setCurrentIndex(0) for component in comboBoxComponents]



