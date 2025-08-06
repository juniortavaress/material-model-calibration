import os
import time
import shutil
import traceback
from typing import Optional
from frontend.aux_files.show_status_message import StatusMessage

class AuxClass():
    def handle_error(self, exception: Exception, stage: str) -> None:
        """
        Handles runtime errors during the optimization process by:
        - Marking the error state
        - Logging the error traceback to file
        - Updating the UI with a status message

        Args:
            exception (Exception): The exception instance that was raised.
            stage (str): The name or description of the stage where the error occurred.
        """
        self.error_tracking = True
        self.stage = stage
        self.e = exception
        
        # Update UI
        StatusMessage.set_text(self, "message-error")

        # Get full traceback as string
        error_message = traceback.format_exc()

        # Log error using the logging utility
        AuxClass.log(self, f"Error during stage '{stage}':\n{error_message}", level="error")


    def log(self, message: str, level: Optional[str] = None) -> None:
        """
        Appends a message to the log file with optional severity.

        Args:
            message (str): Log message.
            level (str): Optional log level ('info' or 'error').
        """

        prefix = "[ERROR] " if level == "error" else ""
        with open(self.log_file, "a") as f:
            f.write(prefix + message + "\n")


    def finish_otimization(self) -> None:
        """
        Finalizes the optimization process by calculating the duration
        and updating the UI with the elapsed time.
        """
        if not self.error_tracking:
            try:
                self.duration = (time.time()) - self.initial_time
                days, hours, minutes, seconds = self.duration // (24 * 3600), (self.duration % (24 * 3600)) // 3600, (self.duration % 3600) // 60, self.duration % 60
                self.formatted_duration = f"{int(days)} dias, {int(hours)}h, {int(minutes)}m e {int(seconds)}s"
                StatusMessage.set_text(self, "message-id_07")
            except Exception as e:
                AuxClass.handle_error(self, e, "Error at def finish_otimization")


    def clean_folder(self):
        """
        Removes temporary Abaqus and Python-generated files from the working directory,
        including .pyc files and __pycache__ folders.
        """
        if not self.error_tracking:
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
                AuxClass.handle_error(self, e, "Error at def clean_folder")