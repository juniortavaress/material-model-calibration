import os 
import alphashape
import matplotlib
import numpy as np
import pandas as pd
from PySide6.QtGui import QPixmap
from shapely.geometry import Polygon
from matplotlib.figure import Figure
from PySide6.QtWidgets import QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class ResultsPlotManager():
    """
    Class for generating and displaying plots related to forces and chip geometry.
    """
    def canvas(self, figure: Figure | None = None) -> None:
        """
        Creates and displays a Matplotlib canvas in the Qt interface.

        Args:
            figure (Figure | None): Optional Matplotlib figure. If None, a new figure is created.
        """
        if figure is None:
            return
        
        canvas = FigureCanvas(figure)
        canvas.setStyleSheet("background: transparent;")
        figure.patch.set_facecolor('none')

        ax = figure.add_subplot(111) if len(figure.get_axes()) == 0 else figure.get_axes()[0]
        ax.set_facecolor('none')

        layout = self.ui.frame_results_graph.layout()
        if layout is not None:
            for i in reversed(range(layout.count())):
                widget = layout.itemAt(i).widget()
                if widget is not None:
                    widget.deleteLater()
            layout.addWidget(canvas)

        self.canvas = canvas
        figure.tight_layout(pad=1)
        canvas.draw()


    def graphs_manager(self) -> None:
        """
        Manages the generation of different types of graphs based on the selected file and analysis type.

        Args:
            forces (dict): Force data.
            chip (dict): Chip geometry data.
            weights (dict): Weight parameters.
            supabase: Supabase client instance. 
            project_id (str): Project identifier.
        """      
        matplotlib.use('QtAgg') 
        type = self.ui.combobox_analysis_type.currentText()
        filename = self.ui.combobox_file.currentText()

        try:
            if type == "Convergence Analysis" and self.current_opt >= 2:
                # self.ui.combobox_file.setEnabled(False)
                # self.ui.combobox_file.setCurrentIndex(0)
                ResultsPlotManager.plot_convergence_analysis(self)
            else:
                # self.ui.combobox_file.setEnabled(True)
                if self.ui.combobox_file.currentIndex() == 0:
                    self.ui.combobox_file.setCurrentIndex(1)

            filename = self.ui.combobox_file.currentText()
            ResultsPlotManager.get_interface_value(self, filename)
                   
            if type == "Forces" and filename != "":
                print(" \n\n Forces")
                ResultsPlotManager.plot_force_graphs(self, filename)
            elif type == "Chip Format" and filename != "":
                ResultsPlotManager.plot_chip(self, filename)

        except Exception as e:
            import traceback
            print("❌ Error generating graph:")
            print(traceback.format_exc()) 
            # figure = Figure(figsize=(12, 8))
            # ResultsPlotManager.canvas(self, figure)


    def get_interface_value(self, filename: str) -> None:
        """
        Fetches simulation results from the database and updates the UI labels.

        Args:
            supabase: Supabase client instance.
            project_id (str): Project identifier.
            filename (str): Simulation filename.
        """
        if not filename or str(filename).strip().lower() == "none":
            for label in [self.ui.label_steady_fc, self.ui.label_steady_fn, self.ui.label_steady_ccr, self.ui.label_steady_csr]:
                label.setText("-")
        else:
            parts = filename.split("_")
            response = self.supabase.table("results")\
                .select("simulated_compression_ratio, simulated_segmentation_ratio, simulated_cutting_force, simulated_normal_force")\
                .eq("project_id", self.project_id)\
                .eq("iteration_number", parts[2])\
                .eq("parameter_set", parts[4])\
                .eq("condition_name", parts[0])\
                .execute()
        
            if response.data and len(response.data) > 0:
                row = response.data[0]
                self.ui.label_steady_fc.setText(str(row["simulated_cutting_force"]))
                self.ui.label_steady_fn.setText(str(row["simulated_normal_force"]))
                self.ui.label_steady_ccr.setText(str(row["simulated_compression_ratio"]))
                self.ui.label_steady_csr.setText(str(row["simulated_segmentation_ratio"]))


    def plot_force_graphs(self, filename: str) -> None:
        """
        Generates and displays force-related graphs using Matplotlib.

        Args:
            supabase: Supabase client instance.
            project_id (str): Project identifier.
            filename (str): Simulation filename.
        """
        print("TA AQUIII", filename)
        response = self.supabase.table("simulation_forces_results")\
            .select("time", "cutting_force", "normal_force")\
            .eq("project_id", self.project_id)\
            .eq("filename", filename)\
            .execute()
            
        if not response.data or len(response.data) == 0:
            print(f"❌ No data found for '{filename}' in project {self.project_id}")
            return

        data = response.data[0]
        time = data["time"]
        cutting = data["cutting_force"]
        normal = data["normal_force"]


        figure = Figure(figsize=(12, 8))
        ax = figure.add_subplot(111)
        ax.set_facecolor('none')
        ax.plot(time, cutting, label="Cutting Force Fc [N]", linewidth=1.5)
        ax.plot(time, normal, label="Normal Cutting Force FcN [N]", linewidth=1.5)
        ax.set_xlabel("Time t [ms]", fontsize=11)
        ax.set_ylabel("Force Component Fi [N]", fontsize=11)
        ax.legend(fontsize=11)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ResultsPlotManager.canvas(self, figure)

  
    def plot_chip(self, filename: str) -> None:
        """
        Generates and displays the chip contour using Alpha Shape.

        Args:
            supabase: Supabase client instance.
            project_id (str): Project identifier.
            filename (str): Simulation filename.
        """
        response = self.supabase.table("simulation_chip_results")\
            .select("x", "y")\
            .eq("project_id", self.project_id)\
            .eq("filename", filename)\
            .execute()
            
        if not response.data or len(response.data) == 0:
            print(f"❌ No data found for '{filename}' in project {self.project_id}")
            return

        data = response.data[0]
        x = data["x"]
        y = data["y"]
        pontos = list(zip(x, y))

        hull = alphashape.alphashape(pontos, alpha = 250)
        figure = Figure(figsize=(12, 8))
        ax = figure.add_subplot(111)

        if isinstance(hull, Polygon): 
            x, y = hull.exterior.xy
            ax.fill(x, y, color="blue", alpha=0.5, label="Corpo sólido")
            ax.plot(x, y, 'b-', linewidth=2)

        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.axis("equal")
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ResultsPlotManager.canvas(self, figure)


    def plot_convergence_analysis(self) -> None:
        """
        Generates and displays convergence analysis graph based on error metrics.

        Args:
            forces (bool): Whether to include force errors.
            chip (bool): Whether to include chip geometry errors.
            weights (list[float]): Weights for each error component.
            supabase: Supabase client instance.
            project_id (str): Project identifier.
        """
        response = self.supabase.table("results")\
            .select("iteration_number, parameter_set, error_fc, error_fn, error_ccr, error_csr")\
            .eq("project_id", self.project_id)\
            .execute()

        if not response.data or len(response.data) == 0:
            print(f"❌ Nenhum dado encontrado na tabela 'results' para o projeto {self.project_id}")
            return
        
        number_of_particles = len(set(item["parameter_set"] for item in response.data if "parameter_set" in item))
        df = pd.DataFrame(response.data)
        grouped = df.groupby(["iteration_number", "parameter_set"])

        dict_errors = {}
        for name, group in grouped:
            fc = fn = temp = ccr = csr = 0.0
            if self.forces:
                fc = pd.to_numeric(group["error_fc"], errors="coerce").abs().mean()
                fn = pd.to_numeric(group["error_fn"], errors="coerce").abs().mean()
            if self.chip:
                ccr = pd.to_numeric(group["error_ccr"], errors="coerce").abs().mean()
                csr = pd.to_numeric(group["error_csr"], errors="coerce").abs().mean()

            combined_error = (self.wfc * fc + self.wfn * fn + self.wccr * ccr + self.wcsr * csr)
            dict_errors[name] = {"error": round(combined_error * 100, 1)}  # em porcentagem

        lines = {}
        for keys, values in dict_errors.items():
            particle = keys[1]
            for error_type, error_value in values.items():
                if error_type not in lines:
                    lines[error_type] = {i: [] for i in range(1, number_of_particles + 1)}
                lines[error_type][particle].append(abs(error_value))

        min_values = {}
        for error_type, set_values in lines.items():
            all_values = [val for values in set_values.values() for val in values]
            min_values[error_type] = min(all_values)

        figure = Figure(figsize=(10, 6))
        ax = figure.add_subplot(111)
        ax.axhline(min_values['error'], color='gray', linestyle='--')
        ax.text(1, min_values['error'] - 2, f"{min_values['error']:.1f}%", va='bottom', ha='left', fontsize=10)
        n_points = len(next(iter(lines['error'].values())))
        ax.set_xticks(range(1, n_points + 1))
        ax.set_xlabel("Iteration Number")
        ax.set_ylabel("Average Error (%)")
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        for set_num in range(1, number_of_particles + 1):
            if set_num in lines['error']:
                y = lines['error'][set_num]
                x = np.arange(1, len(y) + 1)
                line = ax.plot(x, y, label=f"Set-{set_num:02d}")
                color = line[0].get_color()

                if len(y) >= 2:
                    coef = np.polyfit(x, y, 1)
                    trendline = np.polyval(coef, x)
                    ax.plot(x, trendline, linestyle='--', color=color, label=f"Set-{set_num:02d} (trendline)")

        all_y_values = [val for values in lines['error'].values() for val in values]
        max_y = max(all_y_values) if all_y_values else 1.0  # fallback seguro
        ax.set_ylim(bottom=0, top=max_y * 1.05)
        ax.legend()
        ResultsPlotManager.canvas(self, figure)


    def extract_otimization_info(self, command: str) -> None:
        """
        Handles export of graph image or data table based on the given command.

        Args:
            command (str): Either 'graph' to export image or 'data' to export CSV.
        """
        folder_to_save = QFileDialog.getExistingDirectory(self, "Select a folder to save the file: ")
        if command == 'graph':
            type = self.ui.combobox_analysis_type.currentText().lower().replace(" ", "_")
            file = self.ui.combobox_file.currentText().lower()
            pixmap = QPixmap(self.ui.frame_results_graph.size())
            self.ui.frame_results_graph.render(pixmap)
            filename = f"{folder_to_save}/graph_{type}.png" if not file or str(file).strip().lower() == "none" else f"{folder_to_save}/graph_{type}_{file}.png"
            pixmap.save(filename)
        elif command == 'data':
            response = self.supabase.table("results").select("*").eq("project_id", self.project_id).execute()
            if response.data:
                df = pd.DataFrame(response.data)
                df = df.dropna(axis=1, how='all')
                filename = os.path.join(folder_to_save, "resulst_export_project.csv")
                df.to_csv(filename, index=False)




    def _update_tracking_view(self):
        """
        Updates the UI based on the selected tracking or graph view.
        """
        if self.ui.combobox_tracking_graph.currentText() == "Code Tracking":
            self.ui.frame_tracking.show()
            self.ui.frame_results_graph.hide()
        
            self.ui.frame_graph_analysis.hide()
            self.ui.pushButton_extract_data.hide()
            self.ui.pushButton_extract_graph.hide()

            response = self.supabase.table("projects")\
                .select("logs")\
                .eq("project_name", self.project_name)\
                .execute()

            if response.data and response.data[0]["logs"]:
                logs = response.data[0]["logs"]
                self.ui.label_code_status.setText(logs)
            else:
                self.ui.label_code_status.setText("No logs available.")


        elif self.ui.combobox_tracking_graph.currentText() == "Graphs":
            self.ui.label_code_status.setText("")
            self.ui.frame_tracking.hide()
            self.ui.frame_results_graph.show()
            ResultsPlotManager.canvas(self)
            self.ui.frame_graph_analysis.show()
            self.ui.pushButton_extract_data.show()
            self.ui.pushButton_extract_graph.show()

        if self.ui.combobox_analysis_type.currentText() not in ["Forces", "Chip Format"]:
            self.ui.frame_forces_and_chip.hide()
        elif self.ui.combobox_tracking_graph.currentText() == "Graphs":
            self.ui.frame_forces_and_chip.show()
