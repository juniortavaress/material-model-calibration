import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from frontend.interface.ui_form import Ui_MainWindow

from frontend.aux_files.buttons_callback import ButtonsCallback
from frontend.aux_files.variables_manager import ManagerVariables


sys.dont_write_bytecode = True
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.test = False
        self.error_tracking = False
        ButtonsCallback.activate_buttons(self)

    # def __setattr__(self, name, value):
    #     if name not in self.__dict__:
    #         ManagerVariables.print_paths(self)
    #     super().__setattr__(name, value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
