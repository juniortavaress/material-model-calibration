import traceback
from PySide6.QtCore import QThread, Signal

class WorkerThread(QThread):
    finished_signal = Signal()  
    error_signal = Signal(str)  
    otimization_signal = Signal(str)
    
    def __init__(self, function, name="WorkerThread", parent=None):
        super().__init__(parent)
        self.function = function
        self.setObjectName(name)

    def run(self):
        try:
            self.function()
            self.finished_signal.emit()
        except Exception as e:
            print("Erro na thread (class WorkerThread(QThread)):", e) 
            traceback.print_exc()
            self.error_signal.emit(str(e))
