import numpy as np

class StatusMessage:
    def set_text(self, message):
        """
        Responsible for displaying messages in the interface.
        """

        messages = []

        if message == "message-id_01":
            messages = ["<br>", "<b>STARTING OPTIMIZATION</b><br>"]
            messages.extend(["<b>==========================================</b>"])

        elif message == "message-id_02":
            messages = ["<br><br><b>ITERATION {0}</b>".format(self.count_iteration)]
            messages.extend(["<br>Editing .inp file"])

        elif message == "message-id_03":
            messages = ["<br>Running simulation"]

        elif message == "message-id_04":
            messages = ["<br>Collecting results from .odb file<br><br>"]

        elif message == "message-id_05":
            print("message", message)
            print(self.error)
            print(self.error_cutting_force)
            print(self.error_normal_force)
            print(self.error_CCR)
            print(self.error_CSR)
            print(self.best_parameters)

            try:
                messages.extend(["Best Result of Iteration<br>--------------------------<br>"])
                messages.extend(["Optimized Parameters: <br>"])
                messages.extend("<br>".join(["{0}: {1:.3f}".format(key, value) for key, value in self.best_parameters.items()]))
                messages.extend(["<br><br>Average Error: {0:.1f}%<br>".format(self.error * 100)])
                # messages.extend(["Average Error Temperature: {0:.1f}%<br>".format(self.error_temp * 100)])
                messages.extend(["Average Error Cutting Force: {0:.1f}%<br>".format(self.error_cutting_force * 100)])
                messages.extend(["Average Error Normal Force: {0:.1f}%<br>".format(self.error_normal_force * 100)])
                messages.extend(["Average Error Chip Compression Ratio: {0:.1f}%<br>".format(self.error_CCR * 100)])
                messages.extend(["Average Error Chip Segmentation Ratio: {0:.1f}%<br>".format(self.error_CSR * 100)])
                messages.extend(["<br><b>==========================================</b>"])
            except Exception as e:
                import traceback
                print("Erro na thread:", e)  # Exibe o erro no terminal
                traceback.print_exc()

        elif message == "message-id_06":
            messages = ["<br><br><b>BEST RESULT</b><br><br>"]
            messages.extend("Optimized Error: {0}".format(np.round(self.error, 2)))
            messages.extend(["<br>Number of Iterations: {0}".format(self.count_iteration - 1)])
            messages.extend(["<br>Number of Simulations: {0}".format((self.count_iteration - 1) * self.number_of_particles * self.cutting_conditions)])
            messages.extend(["<br><br>Optimized Parameters: <br>"])
            messages.extend("<br>".join(["-  {0}: {1:.3f}".format(key, value) for key, value in self.best_parameters.items()]))
            messages.extend(["<br><br><b>==========================================</b><br>"])

        elif message == "message-id_07":
            messages.extend(["Time running: {0}".format(self.formatted_duration)])

        elif message == "message-error":
            messages = ["<br><b>==========================================</b><br>"]
            messages.extend(["<b> --> There was a problem related with PSO Algorithm. </b><br>"])
            if self.stage:
                messages.extend(["<br> Stage: ", self.stage, "<br>"])
            messages.extend(["<br>", self.e, "<br>"])
            messages.extend(["<br><b>==========================================</b><br>"])

        if messages:
            # print("dentro do if", messages)
            [self.ui.label_code_status.setText(self.ui.label_code_status.text() + str(message)) for message in messages]
        else:
            print("Deu erro cumpadre")
