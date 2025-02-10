from frontend.aux_files.yaml_generator import YamlClass
from frontend.aux_files.get_conditions import GetCondition
from frontend.aux_files.aux_layout import SetLayout
from frontend.aux_files.get_parameters import GetParameters
from backend.inp_configuration import InpManager

class ButtonsCallback():
    def __init__(self):
        super(ButtonsCallback, self).__init__()

    
    def activate_buttons(self):
        # self.condition_path = False
        # YamlClass.create_login_credentials(self)



        # Initial Interface Conditions
        SetLayout.change_page(self, 0)
        self.ui.button_result.setEnabled(False)
        self.ui.button_settings_next_page.setEnabled(False)

       
        # Page 01 - Project Name
        self.ui.button_login_next_page.clicked.connect(lambda: YamlClass.create_login_credentials(self))
        self.ui.button_login_next_page.clicked.connect(lambda: YamlClass.set_software_config_path(self, "start"))


        # Page 02 - Abaqus and Results Path
        self.ui.button_abaqus.clicked.connect(lambda: YamlClass.set_software_config_path(self))
        self.ui.button_result.clicked.connect(lambda: YamlClass.set_user_config_path(self))
        self.ui.button_settings_next_page.clicked.connect(lambda: SetLayout.change_page(self, 2))
        self.ui.button_settings_next_page.clicked.connect(lambda: GetCondition.set_conditions(self))
            

        # Page 03 - Explanation for creating the conditions
        self.ui.button_conditions_limitation_next_page.clicked.connect(lambda: SetLayout.change_page(self, 3))
        self.ui.button_conditions_limitation_back.clicked.connect(lambda: SetLayout.change_page(self, 1))


        # Page 04 - Create Conditions
        self.ui.button_conditions_next_page.clicked.connect(lambda: GetCondition.move_inp_files(self))
        self.ui.button_conditions_next_page.clicked.connect(lambda: GetCondition.get_defaut_user_conditions(self))
        self.ui.button_input_file.clicked.connect(lambda: GetCondition.get_input_path(self))
        self.ui.button_newCondition.clicked.connect(lambda: GetCondition.get_defaut_user_conditions(self, "new"))
        self.ui.comboBox_condition.currentIndexChanged.connect(lambda: GetCondition.change_combobox_info(self))
        self.ui.button_conditions_back.clicked.connect(lambda: SetLayout.change_page(self, 2))

        self.ui.button_conditions_next_page.clicked.connect(lambda: GetParameters.save_parameters(self, "load"))



        # Page 05 - Selection of Parameters to Calibrate
        self.ui.pages.currentChanged.connect(lambda: SetLayout.enable_properties(self))
        self.ui.button_parameter_selection_back.clicked.connect(lambda: SetLayout.change_page(self, 3))
        self.ui.button_parameter_selection_next_page.clicked.connect(lambda: SetLayout.change_page(self, 5))
        self.ui.button_parameter_selection_next_page.clicked.connect(lambda: GetParameters.save_parameters(self, "save"))


        # Page 06 - Parameters Boundary Definition
        self.ui.button_parameter_limits_next_page.clicked.connect(lambda: SetLayout.change_page(self, 6))
        self.ui.button_parameter_limits_back.clicked.connect(lambda: SetLayout.change_page(self, 4))

        # Page 07 - PSO Explanation
        self.ui.button_pso_explanation_next_page.clicked.connect(lambda: SetLayout.change_page(self, 7))
        self.ui.button_pso_explanation_back.clicked.connect(lambda: SetLayout.change_page(self, 5))


        """


        Antes de continuar revisar todo o codigo e tentar causar erro


        """


        # Page 08 - PSO Parameters Definition
        self.ui.button_pso_next_page.clicked.connect(lambda: SetLayout.change_page(self, 8))
        self.ui.button_pso_back.clicked.connect(lambda: SetLayout.change_page(self, 6))

        # Page 09 - Model Calibration
        self.ui.button_code_tracking_next_page.clicked.connect(lambda: SetLayout.change_page(self, 9))
        self.ui.button_code_tracking_back.clicked.connect(lambda: SetLayout.change_page(self, 7))

        # Page 10 - Results Visualization
        self.ui.button_result_back.clicked.connect(lambda: SetLayout.change_page(self, 8))
