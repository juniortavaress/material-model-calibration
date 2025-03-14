import os
import time
import shutil
import traceback
from backend.pso.pso_manager import PsoManager
from backend.aux_files.thread.thread_manager import WorkerThread
from frontend.aux_files.show_status_message import StatusMessage

class OtimizationManager:
    """
    Manages the execution of the Particle Swarm Optimization (PSO) algorithm,
    including handling threads, tracking errors, and cleaning up temporary files.
    """
    def main(self):
        """
        Initiates the optimization process if no errors are present.
        """
        if not self.error_tracking:
            self.e = None
            self.stage = None
            self.initial_time = time.time()
            OtimizationManager.call_pso_script(self)
            

    def call_pso_script(self):
        """
        Calls the optimization script after geometry generation is complete.
        """
        if not self.error_tracking:
            StatusMessage.set_text(self, "message-id_01")
            try:
                self.thread = WorkerThread(lambda: OtimizationManager.start_pso(self), name="PsoThread")
                self.thread.finished_signal.connect(lambda: OtimizationManager.finish_otimization(self))
                self.thread.finished_signal.connect(lambda: OtimizationManager.clean_folder(self))
                self.thread.start()
            except Exception as e:
                OtimizationManager._handle_error(self, e, "Error at call_pso_script")
        else:
            StatusMessage.set_text(self, "geometry-error-main.py")
            OtimizationManager._handle_error(self, e, "Error at call_pso_script - id2")


    def start_pso(self):
        """
        Start the Particle Swarm Optimization (PSO) algorithm.
        Updates the optimization manager with the best position and score.
        """
        if not self.error_tracking:
            PsoManager.run_pso(self)


    def finish_otimization(self):
        """
        Finalizes the optimization process by calculating and formatting the
        duration of the optimization.
        """
        if not self.error_tracking:
            try:
                self.duration = (time.time()) - self.initial_time
                days, hours, minutes, seconds = self.duration // (24 * 3600), (self.duration % (24 * 3600)) // 3600, (self.duration % 3600) // 60, self.duration % 60
                self.formatted_duration = f"{int(days)} dias, {int(hours)}h, {int(minutes)}m e {int(seconds)}s"
                StatusMessage.set_text(self, "message-id_07")
            except Exception as e:
                OtimizationManager._handle_error(self, e, "Error at def finish_otimization")


    def clean_folder(self):
        """
        Cleans up temporary Abaqus-related files from the current directory.
        """
        if not self.error_tracking:
            try:
                current_directory = os.getcwd()
                for file in os.listdir(current_directory):
                    if file.startswith("abaqus") or file.startswith("save_abaqus") or file.endswith(".pyc"):
                        file_path = os.path.join(current_directory, file)
                        if os.path.isfile(file_path):  
                            os.remove(file_path)

                for folder in os.listdir(current_directory):
                    if folder == "__pycache__":
                        folder_path = os.path.join(current_directory, folder)
                        shutil.rmtree(folder_path)

            except Exception as e:
                OtimizationManager._handle_error(self, e, "Error at def clean_folder")


    def _handle_error(self, exception, stage):
        """
        Handles errors by logging them, updating error tracking, and sending a status message.
        """
        self.e = exception
        self.stage = stage
        self.error_tracking = True
        StatusMessage.set_text(self, "message-error")
        traceback.print_exc()

