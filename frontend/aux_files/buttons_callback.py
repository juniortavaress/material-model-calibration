from frontend.aux_files.create_graphs import createPlots
from frontend.aux_files.get_conditions import GetCondition
from frontend.aux_files.get_parameters import GetParameters
from frontend.aux_files.get_outputs_to_analyse import GetOutputs
from frontend.aux_files.get_pso_and_simulation_info import GetPsoAndSimulation

from backend.config.config_software import SoftwareConfig
from backend.show_geometry.graph_setup import GraphManager
from backend.show_geometry.general_functions import AuxFunctions
from backend.optimization.optimization_manager import OtimizationManager


class ButtonsCallback():
    """Handles the callback functions for buttons in the user interface."""
        
    def activate_buttons(self):
        """Activate the buttons and configure initial interface conditions."""
        # Page 00 - Starting the Code
        ButtonsCallback._initial_conditions(self)
        SoftwareConfig.software_setup(self)
        GraphManager.canvas(self)

        # Page 01 - Project Name
        self.ui.button_login_next_page.clicked.connect(lambda: SoftwareConfig.project_setup(self))
        
        # Page 02 - Abaqus and Results Path
        self.ui.button_settings_next_page.clicked.connect(lambda: SoftwareConfig.get_results_and_abaqus_folders(self, None)) 
        self.ui.button_abaqus.clicked.connect(lambda: SoftwareConfig.get_results_and_abaqus_folders(self, "abq"))
        self.ui.button_result.clicked.connect(lambda: SoftwareConfig.get_results_and_abaqus_folders(self, "result"))      
            
        # Page 03 - Explanation for creating the conditions
        self.ui.button_conditions_limitation_next_page.clicked.connect(lambda: self.ui.pages.setCurrentIndex(3))
        self.ui.button_conditions_limitation_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(1))

        # Page 04 - Select outputs to analyse
        self.ui.button_output_analysis_next.clicked.connect(lambda: GetOutputs.get_outputs_manager(self))
        self.ui.button_output_analysis_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(2))

        # Page 05 - Create setup or import setup
        self.ui.button_import_inp.clicked.connect(lambda: AuxFunctions.save_create_setup_option(self, "import"))
        self.ui.button_create_geometry.clicked.connect(lambda: AuxFunctions.save_create_setup_option(self, "create"))

        # Page 06.1 - Define geometry values (only in the case of create geometry with the software)
        # self.ui.tabWidget.currentChanged.connect(lambda: GetGeometry.set_info(self))
        # self.ui.defautValues.stateChanged.connect(lambda: GetGeometry.get_defaut_datas(self))
        # self.ui.button_create_geometry_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(4))
        # self.ui.button_create_geometry_apply.clicked.connect(lambda: GetGeometry.set_info(self))
        # self.ui.button_create_geometry_next.clicked.connect(lambda: GetGeometry.set_info(self))

        # Page 06.2 - Create Conditions
        self.ui.button_conditions_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(4))
        self.ui.comboBox_condition.currentIndexChanged.connect(lambda: GetCondition.change_combobox_info(self))
        self.ui.button_input_file.clicked.connect(lambda: GetCondition.get_input_path(self))
        self.ui.button_newCondition.clicked.connect(lambda: GetCondition.get_user_conditions(self, "new"))
        self.ui.button_conditions_next_page.clicked.connect(lambda: ButtonsCallback._procedures_on_the_create_conditions_page(self))

        # Page 07 - Selection of Parameters to Calibrate
        self.ui.button_parameter_selection_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(6))
        self.ui.button_parameter_selection_next_page.clicked.connect(lambda: GetParameters.save_parameters(self))
        # self.ui.button_parameter_selection_next_page.clicked.connect(lambda: ())

        # Page 08 - Parameters Boundary Definition
        self.ui.button_parameter_limits_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(7))
        self.ui.button_parameter_limits_next_page.clicked.connect(lambda: GetParameters.save_parameters_limits(self))

        # Page 09 - PSO Explanation
        self.ui.button_pso_explanation_next_page.clicked.connect(lambda: GetPsoAndSimulation.show_pso_and_results_info(self))
        self.ui.button_pso_explanation_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(8))

        # Page 10 - PSO Parameters Definition
        self.ui.button_pso_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(9))
        self.ui.button_pso_next_page.clicked.connect(lambda: ButtonsCallback._save_info_and_start_otimization(self))

        # Page 11 - Tracking Page
        self.ui.button_code_tracking_next_page.clicked.connect(lambda: self.ui.pages.setCurrentIndex(12))

        # Page 12 - Results Visualization
        self.ui.button_result_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(11))
        self.ui.combobox_file.currentIndexChanged.connect(lambda: createPlots.graphs_manager(self))
        self.ui.combobox_analysis_type.currentIndexChanged.connect(lambda: createPlots.graphs_manager(self))

    def _initial_conditions(self):
        # Initial Interface Conditions
        self.ui.frame_95.hide()
        # self.ui.frame_105.hide()
        self.ui.frame_plastic.hide()
        self.ui.frame_damage.hide()
        self.ui.button_create_geometry.hide()
        self.ui.button_create_geometry.setEnabled(False)
        # Defining start page
        self.ui.pages.setCurrentIndex(0)

    def _procedures_on_the_create_conditions_page(self):
        GetCondition.get_user_conditions(self)
        import_geometry = GetCondition.manage_inp_files(self)
        GetParameters.parameter_and_interface_manager(self, import_geometry)

    def _save_info_and_start_otimization(self):
        GetPsoAndSimulation.save_info(self)
        OtimizationManager(self)
