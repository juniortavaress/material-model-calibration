import traceback
from PySide6.QtCore import QThread, Signal

class WorkerThread(QThread):
    """
    A worker thread class that allows running a function in a separate thread.

    It emits signals when the task is finished or when an error occurs.

    Attributes:
        finished_signal (Signal): A signal emitted when the task is finished.
        error_signal (Signal): A signal emitted if an error occurs during execution.
    """
        
    finished_signal = Signal()  
    error_signal = Signal(str)  
    
    def __init__(self, function, name="WorkerThread", parent=None):
        """
        Initializes the WorkerThread with the given function to execute.
        """
        super().__init__(parent)
        self.function = function
        self.setObjectName(name)


    def run(self):
        """
        Executes the function in the worker thread and handles any exceptions.

        If the function completes successfully, the finished_signal is emitted.
        If an exception occurs, the error_signal is emitted with the error message.
        """
        try:
            self.function()
            self.finished_signal.emit()
        except Exception as e:
            traceback.print_exc()
            self.error_signal.emit(str(e))
