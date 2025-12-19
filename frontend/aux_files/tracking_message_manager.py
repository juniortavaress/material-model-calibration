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
            messages = ["<br><b>ITERATION {0}</b>".format(self.main.current_opt)]
            messages.extend(["<br>Editing .inp file"])

        elif message == "message-id_03":
            messages = ["<br>Running simulation"]

        elif message == "message-id_04":
            messages = ["<br>Collecting results from .odb file<br><br>"]

        elif message == "message-id_05":
            messages.extend(["Time running: {0}".format(self.formatted_duration)])

        elif message == "message-id_06":
            messages = ["<br>Waiting for simulations"]

        elif message == "message-error":
            messages = ["<br><b>==========================================</b><br>"]
            messages.extend(["<b> --> There was a problem related with PSO Algorithm. </b><br>"])
            if self.stage:
                messages.extend(["<br> Stage: ", self.stage, "<br>"])
            messages.extend(["<br>", self.e, "<br>"])
            messages.extend(["<br><b>==========================================</b><br>"])


        new_message = "".join(str(m) for m in messages)

        if message == "message-id_01":
            ProcessStatusLogger.safe_set_text(self, self.main.ui.label_code_status, new_message)
            return

        request = self.main.supabase.table("projects").select("logs").eq("project_name", self.main.project_name)
        response = ProcessStatusLogger.safe_supabase_execute(self, request)

        if response is None or not response.data:
            existing_logs = ""
        else:
            existing_logs = response.data[0].get("logs", "") or ""

        new_logs = existing_logs + "\n" + new_message

        if message != "message-error":
            request_upd = self.main.supabase.table("projects").update({"logs": new_logs}).eq("project_name", self.main.project_name)
            ProcessStatusLogger.safe_supabase_execute(self, request_upd)

        ProcessStatusLogger.safe_set_text(self, self.main.ui.label_code_status, new_logs)


    def safe_set_text(self, widget, text):
        QMetaObject.invokeMethod(widget, "setText", Qt.QueuedConnection, Q_ARG(str, text))


    def safe_supabase_execute(self, request):
        """
        Executa requisições ao Supabase com tratamento de erros.
        Se o Supabase retornar HTML ou erro 500, retorna None.
        """
        try:
            response = request.execute()
        except Exception as e:
            # Se vier HTML (Cloudflare), identificar
            if "html" in str(e).lower():
                return None
            return None

        # Caso o Supabase retorne conteúdo inesperado
        if not hasattr(response, "data"):
            return None

        return response