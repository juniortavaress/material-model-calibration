from frontend.aux_files.yaml_generator import YamlClass
from frontend.aux_files.get_conditions import GetCondition
from frontend.aux_files.get_parameters import GetParameters
from frontend.aux_files.get_pso_and_simulation_info import GetPsoAndSimulation
from backend.pso.start_otimization import OtimizationManager
from backend.pso.pso_manager import PsoManager

class ButtonsCallback():
    def __init__(self):
        super(ButtonsCallback, self).__init__()

    
    def activate_buttons(self):
        # Initial Interface Conditions
        self.ui.frame_105.hide()

        self.ui.frame_temperature.hide()
        self.ui.label_login_warning.hide()
        self.ui.label_path_warning.hide()
        self.ui.label_condition_warning.hide()
        self.ui.label_limits_warning.hide()
        self.ui.label_pso_result_warning.hide()
        self.ui.button_result.setEnabled(False)
        self.ui.button_settings_next_page.setEnabled(False)

        self.resize(1000, 400) if not self.isMaximized() else None
        self.ui.pages.setCurrentIndex(0)


        # Page 01 - Project Name
        self.ui.button_login_next_page.clicked.connect(lambda: YamlClass.create_login_credentials(self))
        self.ui.button_login_next_page.clicked.connect(lambda: YamlClass.set_software_config_path(self, "start"))
        self.ui.button_login_next_page.clicked.connect(lambda: GetPsoAndSimulation.verify_gui_stage(self))
        # self.ui.button_login_next_page.clicked.connect(lambda: YamlClass.verify_gui_stage(self))


        # Page 02 - Abaqus and Results Path
        self.ui.button_abaqus.clicked.connect(lambda: YamlClass.set_software_config_path(self))
        self.ui.button_result.clicked.connect(lambda: YamlClass.set_user_config_path(self))
        self.ui.button_settings_next_page.clicked.connect(lambda: self.ui.pages.setCurrentIndex(2))
        self.ui.button_settings_next_page.clicked.connect(lambda: GetCondition.set_conditions(self)) # Para quando tem valores salvos
            

        # Page 03 - Explanation for creating the conditions
        self.ui.button_conditions_limitation_next_page.clicked.connect(lambda: self.ui.pages.setCurrentIndex(3))
        self.ui.button_conditions_limitation_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(1))


        # Page 04 - Create Conditions
        self.ui.button_conditions_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(2))
        self.ui.comboBox_condition.currentIndexChanged.connect(lambda: GetCondition.change_combobox_info(self))
        self.ui.button_input_file.clicked.connect(lambda: GetCondition.get_input_path(self))
        self.ui.button_newCondition.clicked.connect(lambda: GetCondition.get_defaut_user_conditions(self, "new"))
        self.ui.button_conditions_next_page.clicked.connect(lambda: GetParameters.save_parameters(self, "load"))
        self.ui.button_conditions_next_page.clicked.connect(lambda: GetCondition.save_conditions(self))
        self.ui.button_conditions_next_page.clicked.connect(lambda: GetParameters.parameter_and_interface_manager(self))


        # Page 05 - Selection of Parameters to Calibrate
        self.ui.button_parameter_selection_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(3))
        self.ui.button_parameter_selection_next_page.clicked.connect(lambda: self.ui.pages.setCurrentIndex(5))
        self.ui.button_parameter_selection_next_page.clicked.connect(lambda: GetParameters.save_parameters(self, "save"))


        # Page 06 - Parameters Boundary Definition
        self.ui.button_parameter_limits_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(4))
        self.ui.button_parameter_limits_next_page.clicked.connect(lambda: GetParameters.save_parameters_limits(self))


        # Page 07 - PSO Explanation
        self.ui.button_pso_explanation_next_page.clicked.connect(lambda: self.ui.pages.setCurrentIndex(7))
        self.ui.button_pso_explanation_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(5))
        self.ui.button_pso_explanation_next_page.clicked.connect(lambda: GetPsoAndSimulation.load_info(self))


        # Page 08 - PSO Parameters Definition
        self.ui.button_pso_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(6))
        self.ui.button_pso_next_page.clicked.connect(lambda: GetPsoAndSimulation.save_info(self))
        self.ui.button_pso_next_page.clicked.connect(lambda: OtimizationManager.main(self))


        # Page 09 - Model Calibration
        self.ui.button_code_tracking_next_page.clicked.connect(lambda: self.ui.pages.setCurrentIndex(9))
        self.ui.button_code_tracking_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(7))


        # Page 10 - Results Visualization
        self.ui.button_result_back.clicked.connect(lambda: self.ui.pages.setCurrentIndex(8))
