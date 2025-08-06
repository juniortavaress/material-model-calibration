import sys
sys.dont_write_bytecode = True

from PySide6.QtWidgets import QApplication, QMainWindow
from frontend.interface.ui_form import Ui_MainWindow
from frontend.aux_files.buttons_callback import ButtonsCallback


class MainWindow(QMainWindow):
    """Main application window."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        print("main")
        # PRECISO PEGAR ISSO DA UI DEPOIS 
        # self.weights = [0.5, 0.1, 0.0, 0.2, 0.2]
        # self.forces, self.temp, self.chip = True, False, True
        
        print("main")
        
        # Error tracking variable
        self.reload = False
        self.process_finished = False
        self.iteration_in_progress = False
        self.error_tracking = False

        # Activate buttons from interface
        ButtonsCallback.activate_buttons(self)


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
    