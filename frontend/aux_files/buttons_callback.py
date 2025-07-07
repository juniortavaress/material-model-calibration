from frontend.aux_files.get_conditions import GetCondition
from frontend.aux_files.get_parameters import GetParameters
from frontend.aux_files.get_pso_and_simulation_info import GetPsoAndSimulation

from backend.config.config_software import SoftwareConfig
from backend.pso_scripts.start_otimization import OtimizationManager
from backend.get_result_from_odb_file.create_graphs import createPlots

from backend.show_geometry.get_geometry import GetGeometry
from backend.show_geometry.dictionaries import GetDictionary
from backend.show_geometry.graph_setup import GraphManager
from backend.show_geometry.general_functions import AuxFunctions

from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QFileDialog
from PySide6.QtGui import QIcon

class ButtonsCallback():
    """Handles the callback functions for buttons in the user interface."""
        
    def activate_buttons(self):
        """Activate the buttons and configure initial interface conditions."""
        SoftwareConfig.software_setup(self)
        
        # # Initial Interface Conditions
        self.ui.frame_95.hide()
        self.ui.frame_105.hide()
        self.ui.frame_temperature.hide()
        self.ui.label_login_warning.hide()
        self.ui.label_path_warning.hide()
        self.ui.label_condition_warning.hide()
        self.ui.label_limits_warning.hide()
        self.ui.label_pso_result_warning.hide()
        self.ui.button_settings_next_page.setEnabled(False)
        self.ui.frame_20.hide()
        self.ui.pages.setCurrentIndex(0)

        # Page 01 - Project Name
        self.ui.button_login_next_page.clicked.connect(lambda: SoftwareConfig.project_setup(self))
        self.ui.button_login_next_page.clicked.connect(lambda: SoftwareConfig.verify_gui_stage(self))
        self.ui.button_login_next_page.clicked.connect(lambda: self.showMaximized())

        # Page 02 - Abaqus and Results Path
        self.ui.button_abaqus.clicked.connect(lambda: SoftwareConfig.set_software_config_path(self))
        self.ui.button_result.clicked.connect(lambda: SoftwareConfig.get_results_folders(self))
        self.ui.button_settings_next_page.clicked.connect(lambda: self.ui.pages.setCurrentIndex(2))
        self.ui.button_result.clicked.connect(lambda: SoftwareConfig.set_user_config_path(self))
        self.ui.button_settings_next_page.clicked.connect(lambda: GetCondition.set_conditions(self)) # Para quando tem valores salvos
            
        # Page 03 - Explanation for creating the conditions
        self.ui.button_conditions_limitation_next_page.clicked.connect(lambda: self.ui.pages.setCurrentIndex(3))
        self.ui.button_conditions_limitation_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(1))

        # Page 04 - Create setup or import setup
        self.ui.button_import_inp.clicked.connect(lambda: AuxFunctions.save_create_setup_option(self, "import"))

        # self.ui.button_import_inp.clicked.connect(lambda: AuxFunctions.save_create_setup_option(self, "import"))


        self.ui.button_create_geometry.clicked.connect(lambda: AuxFunctions.save_create_setup_option(self, "create"))


        # Page 05 - Define geometry values (only in the case of create geometry with the software)
        GraphManager.canvas(self)
        self.ui.tabWidget.currentChanged.connect(lambda: GetGeometry.set_info(self))
        self.ui.defautValues.stateChanged.connect(lambda: GetGeometry.get_defaut_datas(self))

        self.ui.button_create_geometry_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(3))
        self.ui.button_create_geometry_apply.clicked.connect(lambda: GetGeometry.set_info(self))
        self.ui.button_create_geometry_next.clicked.connect(lambda: GetGeometry.set_info(self))

        # Page 06 - Create Conditions
        self.ui.button_conditions_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(3))
        self.ui.comboBox_condition.currentIndexChanged.connect(lambda: GetCondition.change_combobox_info(self))
        self.ui.button_input_file.clicked.connect(lambda: GetCondition.get_input_path(self))
        self.ui.button_newCondition.clicked.connect(lambda: GetCondition.get_defaut_user_conditions(self, "new"))






        self.ui.button_conditions_next_page.clicked.connect(lambda: GetParameters.save_parameters(self, "load"))
        self.ui.button_conditions_next_page.clicked.connect(lambda: GetCondition.save_conditions(self))
        self.ui.button_conditions_next_page.clicked.connect(lambda: GetParameters.parameter_and_interface_manager(self))

        # edita os dados com os valores definidos no condition e gera os arquivos

        # datas input -> C:\MaterialOtimization\P1206\defaut\geometry_info
            # edita esse arquivo ja nomeando da forma correta
            # quando for no condition transforma isso no input

        # inp output -> S:\Junior\drive\PROJETO\auxiliary_files\simulation_inp_files




        # Page 07 - Selection of Parameters to Calibrate
        self.ui.button_parameter_selection_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(5))
        self.ui.button_parameter_selection_next_page.clicked.connect(lambda: self.ui.pages.setCurrentIndex(7))
        self.ui.button_parameter_selection_next_page.clicked.connect(lambda: GetParameters.save_parameters(self, "save"))

        # Page 08 - Parameters Boundary Definition
        self.ui.button_parameter_limits_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(6))
        self.ui.button_parameter_limits_next_page.clicked.connect(lambda: GetParameters.save_parameters_limits(self))

        # Page 09 - PSO Explanation
        self.ui.button_pso_explanation_next_page.clicked.connect(lambda: self.ui.pages.setCurrentIndex(9))
        self.ui.button_pso_explanation_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(7))
        self.ui.button_pso_explanation_next_page.clicked.connect(lambda: GetPsoAndSimulation.load_info(self))

        # Page 10 - PSO Parameters Definition
        self.ui.button_pso_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(8))
        self.ui.button_pso_next_page.clicked.connect(lambda: GetPsoAndSimulation.save_info(self))
        self.ui.button_pso_next_page.clicked.connect(lambda: OtimizationManager.main(self))

        # Page 11 - Model Calibration
        self.ui.button_code_tracking_next_page.clicked.connect(lambda: self.ui.pages.setCurrentIndex(11))
        self.ui.button_code_tracking_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(9))

        # Page 12 - Results Visualization
        self.ui.button_result_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(10))
        self.ui.combobox_file.currentIndexChanged.connect(lambda: createPlots.graphs_manager(self))
        self.ui.combobox_analysis_type.currentIndexChanged.connect(lambda: createPlots.graphs_manager(self))


