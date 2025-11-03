import httpx
from supabase import create_client, ClientOptions

from frontend.aux_files.results_plot_manager import ResultsPlotManager
from frontend.aux_files.conditions_configuration_manager import ConditionManager
from frontend.aux_files.material_configuration_manager import MaterialParameterManager
from frontend.aux_files.output_configuration_manager import OutputConfigurationManager
from frontend.aux_files.simulation_configuration_manager import SimulationConfiguratorManager

from backend.config.config_software import SoftwareConfig
from backend.optimization.optimization_manager import OtimizationManager


class ButtonsCallback:
    """
    Handles all button callbacks and UI navigation logic for the application.
    """
        
    def activate_buttons(self) -> None:
        """
        Connects UI buttons to their respective callback functions and initializes the interface.
        """
        self.main_cp = False
        ButtonsCallback._initialize_state(self)
        SoftwareConfig.software_setup(self)
        
        
        try:
            self.ui.combobox_analysis_type.insertItem(0, "Convergence Analysis")
            self.ui.combobox_analysis_type.removeItem(self.ui.combobox_analysis_type.findText("None"))
            self.ui.combobox_file.removeItem(self.ui.combobox_file.findText("None"))
            self.ui.combobox_iteration.removeItem(self.ui.combobox_iteration.findText("None"))
            self.ui.combobox_iteration.addItem("01")
            self.ui.combobox_iteration.addItem("02")
        except:
            pass

        # Page 01 - Project Setup
        self.ui.button_login_next_page.clicked.connect(lambda: ButtonsCallback._handle_project_setup(self))

        # Page 02 - Abaqus Path
        self.ui.button_abaqus.clicked.connect(lambda: SoftwareConfig.get_results_and_abaqus_folders(self, "abq"))

        # Page 10 - Results Visualizaer
        self.ui.pushButton_extract_graph.clicked.connect(lambda: ResultsPlotManager.extract_otimization_info(self, 'graph'))
        self.ui.pushButton_extract_data.clicked.connect(lambda: ResultsPlotManager.extract_otimization_info(self, 'data'))
        self.ui.combobox_file.currentIndexChanged.connect(lambda: ResultsPlotManager.graphs_manager(self, '01'))
        self.ui.combobox_analysis_type.currentIndexChanged.connect(lambda: ResultsPlotManager.graphs_manager(self, '02'))

        self.ui.combobox_tracking_graph.currentIndexChanged.connect(lambda: ResultsPlotManager.update_tracking_view(self))
        self.ui.combobox_analysis_type.currentIndexChanged.connect(lambda: ResultsPlotManager.update_tracking_view(self))
        self.ui.combobox_iteration.currentIndexChanged.connect(lambda: ResultsPlotManager.filter_files_by_iteration(self))


    def _handle_project_setup(self) -> None:
        """
        Handles project setup and activates the appropriate button set.
        """
        SoftwareConfig.project_setup(self)
        ResultsPlotManager.update_tracking_view(self)
        ButtonsCallback._activate_main_buttons(self) if self.main_cp else ButtonsCallback._activate_aux_buttons(self)
        #self.ui.pages.setCurrentIndex(1)
            
            
    def _activate_main_buttons(self) -> None:
        """
        Connects buttons for the main workflow.
        """
        # Page 02 - Abaqus Path
        self.ui.button_settings_next_page.clicked.connect(lambda: SoftwareConfig.get_results_and_abaqus_folders(self, None))

        # Page 03 - Explanation for creating the conditions
        self.ui.button_conditions_limitation_next_page.clicked.connect(lambda: self.ui.pages.setCurrentIndex(3))
        self.ui.button_conditions_limitation_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(1))

        # Page 04 - Select outputs to analyse
        self.ui.button_output_analysis_next.clicked.connect(lambda: OutputConfigurationManager.configure_outputs(self))
        self.ui.button_output_analysis_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(2))

        # Page 05 - Create Conditions
        self.ui.button_conditions_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(3))
        self.ui.comboBox_condition.currentIndexChanged.connect(lambda: ConditionManager.update_ui_from_selected_condition(self))
        self.ui.button_input_file.clicked.connect(lambda: ConditionManager.select_input_file(self))
        self.ui.button_newCondition.clicked.connect(lambda: ConditionManager.save_condition(self, "new"))
        self.ui.button_conditions_next_page.clicked.connect(lambda: ButtonsCallback._handle_condition_creation(self))

        # Page 06 - Selection of Parameters to Calibrate
        self.ui.button_parameter_selection_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(5))
        self.ui.button_parameter_selection_next_page.clicked.connect(lambda: MaterialParameterManager.save_parameters_from_material(self))

        # Page 07 - Parameters Boundary Definition
        self.ui.button_parameter_limits_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(6))
        self.ui.button_parameter_limits_next_page.clicked.connect(lambda: MaterialParameterManager.save_parameters_limits(self))

        # Page 08 - PSO Explanation
        self.ui.button_pso_explanation_next_page.clicked.connect(lambda: SimulationConfiguratorManager.update_simulation_info(self))
        self.ui.button_pso_explanation_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(7))

        # Page 09 - PSO Parameters Definition
        self.ui.button_pso_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(8))
        self.ui.button_pso_next_page.clicked.connect(lambda: ButtonsCallback._start_optimization(self))

        # Page 10 - Results Visualization
        self.ui.button_result_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(10))


    def _activate_aux_buttons(self) -> None:
        """
        Connects buttons for auxiliary workflows.
        """
        self.ui.button_settings_next_page.clicked.connect(lambda: SoftwareConfig.start_aux_optimization(self))
        

    def _initialize_state(self) -> None:
        """
        Initializes internal state and Supabase clients.
        """
        self.reload = False
        self.process_finished = False
        self.iteration_in_progress = False
        self.error_tracking = False
        self.current_opt = 1

        self.ui.lineEdit_password.setText('1007')
        self.ui.lineEdit_project_name.setText('Optimization1007')

        self.ui.frame_plastic.hide()
        self.ui.frame_damage.hide()
        self.ui.pages.setCurrentIndex(0)

        supabase_url = 'https://dbbvsfnxsyvkjrcoeakh.supabase.co'
        supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRiYnZzZm54c3l2a2pyY29lYWtoIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1ODUyMzIzNywiZXhwIjoyMDc0MDk5MjM3fQ.eggQomAbqZUbXwldB3ICj0DB6qp76bb6Opgi_p6UIC8'
        options = ClientOptions(httpx_client=httpx.Client(timeout=60.0))
        options_storage = ClientOptions(httpx_client=httpx.Client(timeout=60.0))
        self.supabase = create_client(supabase_url, supabase_key, options=options)
        self.supabase_storage = create_client(supabase_url, supabase_key, options=options_storage)

        

    def _handle_condition_creation(self) -> None:
        """
        Saves condition and material parameters, then navigates to the next page.
        """
        ConditionManager.save_condition(self)
        MaterialParameterManager.manage_parameters_and_interface(self)
        self.ui.pages.setCurrentIndex(6)


    def _start_optimization(self) -> None:
        """
        Validates simulation configuration and starts the optimization process.
        """
        SimulationConfiguratorManager.validate_and_save_config(self)
        OtimizationManager(self)
