import os
import time
import shutil
import traceback
from frontend.aux_files.tracking_message_manager import ProcessStatusLogger

class AuxClass():
    
    def _handle_exception(self, exception: Exception, stage: str) -> None:
        """
        Handles and logs exceptions that occur during any simulation stage.
        
        Args:
            exception: The exception object raised.
            stage: Description of the stage where the error occurred.
        """
        self.e = exception
        self.stage = stage
        ProcessStatusLogger.set_log_to_ui(self, "message-error")
        error_message = traceback.format_exc()
        print(f"\n❌ Error during stage '{stage}':\n{error_message}")


    def finish_otimization(self) -> None:
        """
        Finalizes the optimization process by calculating the duration
        and updating the UI with the elapsed time.
        """
        if not self.main.error_tracking:
            try:
                self.duration = (time.time()) - self.initial_time
                days, hours, minutes, seconds = self.duration // (24 * 3600), (self.duration % (24 * 3600)) // 3600, (self.duration % 3600) // 60, self.duration % 60
                self.formatted_duration = f"{int(days)} dias, {int(hours)}h, {int(minutes)}m e {int(seconds)}s"
                ProcessStatusLogger.set_log_to_ui(self, "message-id_05")
            except Exception as e:
                self.main.error_tracking = True
                AuxClass._handle_exception(self, e, "Error at def finish_otimization")


    def clean_folder(self):
        """
        Removes temporary Abaqus and Python-generated files from the working directory,
        including .pyc files and __pycache__ folders.
        """
        if not self.main.error_tracking:
            try:
                cwd  = os.getcwd()
                
                for file in os.listdir(cwd):
                    if file.startswith("abaqus") or file.startswith("save_abaqus") or file.endswith(".pyc"):
                        file_path = os.path.join(cwd, file)
                        if os.path.isfile(file_path):  
                            os.remove(file_path)

                for folder in os.listdir(cwd):
                    if folder == "__pycache__":
                        folder_path = os.path.join(cwd, folder)
                        shutil.rmtree(folder_path)

            except Exception as e:
                self.main.error_tracking = True
                AuxClass._handle_exception(self, e, "Error at def clean_folder")    


   