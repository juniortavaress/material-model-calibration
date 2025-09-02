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

        # Error tracking variable
        self.reload = False
        self.process_finished = False
        self.iteration_in_progress = False
        self.error_tracking = False

        # Activate buttons from interface
        ButtonsCallback.activate_buttons(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setStyleSheet("""
        QPushButton:focus { outline: none; }
        QCheckBox:focus { outline: none; }
        QRadioButton:focus { outline: none; }
        QComboBox:focus { outline: none; }
        QLineEdit:focus { outline: none; }
        QRadioButton::indicator:focus { outline: none; }
        QCheckBox::indicator:focus { outline: none; }
    """)

    widget = MainWindow()
    widget.resize(700, 300)
    widget.showMaximized()  
    widget.show()
     
    # Centralizar após mostrar
    # screen = app.primaryScreen()
    # screen_geometry = screen.geometry()
    # window_geometry = widget.frameGeometry()
    # center_point = screen_geometry.center()
    # window_geometry.moveCenter(center_point)
    # widget.move(window_geometry.topLeft())

    sys.exit(app.exec())
    