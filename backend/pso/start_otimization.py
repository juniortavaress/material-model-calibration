from frontend.aux_files.show_status_message import StatusMessage
from backend.aux_files.thread_manager import WorkerThread
from backend.pso.pso_manager import PsoManager
import time

class OtimizationManager:
    def main(self):
        if not self.error_tracking:
            OtimizationManager.call_pso_script(self)
            self.stage = None


    def call_pso_script(self):
        """
        Calls the optimization script after geometry generation is complete.
        """
        initial_time = time.time()
        if not self.error_tracking:
            try:
                self.e = 000
                StatusMessage.set_text(self, "message-id_01")
                self.thread = WorkerThread(lambda: OtimizationManager.start_pso(self), name="PsoThread")
                self.thread.finished_signal.connect(lambda: OtimizationManager.finish_otimization(self, initial_time))
                self.thread.start()
            except Exception as e:
                self.e = e
                self.stage = "Error at Call PSO"
                self.error_tracking = True
                StatusMessage.set_text(self, "message-error")
        else:
            StatusMessage.set_text(self, "geometry-error-main.py")


    def start_pso(self):
        """
        Start the Particle Swarm Optimization (PSO) algorithm.
        Updates the optimization manager with the best position and score.
        """

        if not self.error_tracking:
            # try:
            # PsoManager.run_pso(self)
            self.count_iteration, self.best_position, self.best_score = PsoManager.run_pso(self)

            # import numpy as np
            # best_position = np.round(best_position, 2)

            print('best position', self.best_position)
            # StatusMessage.set_text(self, "message-id_05")
            # except Exception as e:
            #     self.e = e
            #     self.stage = "start_pso"
            #     self.error_tracking = True
            #     StatusMessage.set_text(self, "message-error")


    def finish_otimization(self, initial_time):
        """
        Finalizes the optimization process by calculating and formatting the
        duration of the optimization.
        """
        if not self.error_tracking:
            try:
                self.duration = (time.time()) - initial_time
                days, hours, minutes, seconds = self.duration // (24 * 3600), (self.duration % (24 * 3600)) // 3600, (self.duration % 3600) // 60, self.duration % 60
                self.formatted_duration = f"{int(days)} dias, {int(hours)}h, {int(minutes)}m e {int(seconds)}s"
                StatusMessage.set_text(self, "message-id_06")
            except Exception as e:
                self.e = e
                self.stage = "finish_otimization"
                self.error_tracking = True
                StatusMessage.set_text(self, "message-error")
