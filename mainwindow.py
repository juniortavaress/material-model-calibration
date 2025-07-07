import sys
# Prevent Python from generating .pyc files
sys.dont_write_bytecode = True

from PySide6.QtWidgets import QApplication, QMainWindow
from frontend.interface.ui_form import Ui_MainWindow
from frontend.aux_files.buttons_callback import ButtonsCallback
from frontend.aux_files.variables_manager import ManagerVariables


class MainWindow(QMainWindow):
    """Main application window."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
        # Error tracking variable
        self.error_tracking = False

        # Activate buttons from interface
        ButtonsCallback.activate_buttons(self)


    # def __setattr__(self, name, value):
    #     """Override setattr to track variable assignments."""
    #     if not hasattr(self, name):  
    #         ManagerVariables.print_paths(self)
    #     super().__setattr__(name, value)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()

    widget.resize(700, 300)  # define tamanho antes do show
    widget.show()

    # Centralizar após mostrar
    screen = app.primaryScreen()
    screen_geometry = screen.geometry()
    window_geometry = widget.frameGeometry()
    center_point = screen_geometry.center()
    window_geometry.moveCenter(center_point)
    widget.move(window_geometry.topLeft())

    sys.exit(app.exec())
    