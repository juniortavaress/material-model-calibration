import numpy as np
from PySide6.QtCore import QMetaObject, Qt
from PySide6.QtCore import Q_ARG

class ProcessStatusLogger:
    """
    Class responsible for managing and displaying status messages during
    the PSO optimization and simulation processes.
    """

    def set_log_to_ui(self, message: str) -> None:
        """
        Updates the UI with a message corresponding to a predefined message ID.

        Parameters:
            message (str): The message ID used to determine what content to display.
        """
        messages = []

        if message == "message-id_01":
            messages = ["<br>", "<b>STARTING OPTIMIZATION</b><br>"]
            messages.extend(["<b>==========================================</b>"])

        elif message == "message-id_02":
            messages = ["<br><br><b>ITERATION {0}</b>".format(self.main.current_opt)]
            messages.extend(["<br>Editing .inp file"])

        elif message == "message-id_03":
            messages = ["<br>Running simulation"]

        elif message == "message-id_04":
            messages = ["<br>Collecting results from .odb file<br><br>"]

        elif message == "message-id_05":
            messages.extend(["Time running: {0}".format(self.formatted_duration)])

        elif message == "message-error":
            messages = ["<br><b>==========================================</b><br>"]
            messages.extend(["<b> --> There was a problem related with PSO Algorithm. </b><br>"])
            if self.stage:
                messages.extend(["<br> Stage: ", self.stage, "<br>"])
            messages.extend(["<br>", self.e, "<br>"])
            messages.extend(["<br><b>==========================================</b><br>"])

        # Update the UI label with the constructed message
        if messages:
            existing_logs = ""
            if message != "message-id_01":
                response = self.main.supabase.table("projects").select("logs").eq("project_name", self.main.project_name).execute()
                existing_logs = response.data[0]["logs"] if response.data and response.data[0]["logs"] else ""

            new_logs = existing_logs + "\n" + "".join(str(m) for m in messages)
            self.main.supabase.table("projects").update({"logs": new_logs}).eq("project_name", self.main.project_name).execute()
            # self.main.ui.label_code_status.setText(new_logs)
            ProcessStatusLogger.safe_set_text(self, self.main.ui.label_code_status, new_logs)

    def safe_set_text(self, widget, text):
        QMetaObject.invokeMethod(widget, "setText", Qt.QueuedConnection, Q_ARG(str, text))
