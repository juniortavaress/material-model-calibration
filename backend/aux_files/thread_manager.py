from PySide6.QtCore import QThread, Signal


class WorkerThread(QThread):
    finished_signal = Signal()  # Sinal para indicar que terminou
    error_signal = Signal(str)  # Sinal para indicar erro

    def __init__(self, function, name="WorkerThread", parent=None):
        super().__init__(parent)
        self.function = function
        self.setObjectName(name)

    def run(self):
        try:
            self.function()
            self.finished_signal.emit()
        except Exception as e:
            self.error_signal.emit(str(e))
