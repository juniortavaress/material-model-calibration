import os 
import matplotlib
import alphashape
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class createPlots():
    """
    Class for generating and displaying plots related to forces, temperature, and chip shape.
    """
    def canvas(self, figure=None):
        """
        Creates and displays a Matplotlib canvas in the Qt interface.

        Args:
            figure (matplotlib.figure.Figure, optional): A Matplotlib figure to be displayed. Defaults to None, which creates a blank canvas.
        """
        if figure:
            self.canvas = FigureCanvas(figure)

            self.canvas.setStyleSheet("background: transparent;")
            self.canvas.figure.patch.set_facecolor('none')
            ax = self.canvas.figure.get_axes()[0]
            ax.set_facecolor('none')

            layout = self.ui.frame_results_graph.layout()
            if layout is not None:
                # Limpando o layout antes de adicionar o novo gráfico
                for i in reversed(range(layout.count())):
                    widget = layout.itemAt(i).widget()
                    if widget is not None:
                        widget.deleteLater()

            layout.addWidget(self.canvas)
            self.canvas.figure.tight_layout(pad=1)

        else:
            if not hasattr(self, 'canvas'):
                self.canvas = FigureCanvas(Figure(figsize=(12, 8)))  

            # Clear Layout
            layout = self.ui.frame_results_graph.layout()
            if layout is not None:
                for i in reversed(range(layout.count())):
                    widget = layout.itemAt(i).widget()
                    if widget is not None:
                        widget.deleteLater()
        self.canvas.draw()


    def graphs_manager(self):
        """
        Manages the generation of different types of graphs based on the selected file and analysis type.
        """
        type = self.ui.combobox_analysis_type.currentText()
        filename = self.ui.combobox_file.currentText()

        try:
            if type == "Convergence Analysis":
                # self.ui.combobox_file.setCurrentIndex(0)
                self.ui.combobox_file.setEnabled(False)
                createPlots.plot_convergence_analysis(self)
            else:
                # self.ui.combobox_file.setCurrentIndex(1)
                self.ui.combobox_file.setEnabled(True)

            if filename != "None":
                sheet_name = filename[4:]

                if len(sheet_name) > 31:
                    sheet_name = sheet_name[:31]

                if type == "Forces":
                    createPlots.plot_force_graphs(self, sheet_name)
                elif type == "Temperature vs. Time":
                    createPlots.plot_temp_time_graph(self, sheet_name)
                elif type == "Temperature vs. Penetration Depth":
                    createPlots.plot_temp_penetration_graph(self, sheet_name)
                elif type == "Chip Format":
                    createPlots.plot_chip(self, sheet_name)
            else:
                createPlots.canvas(self)
        except:
            createPlots.canvas(self)



    def plot_force_graphs(self, sheet_name):
        """
        Generates and displays force-related graphs using Matplotlib.

        Args:
            filename (str): Name of the sheet in the Excel file.
        """

        matplotlib.use('QtAgg') 
        path = os.path.join(self.graph_folder, "forces_result.xlsx")
        df = pd.read_excel(path, sheet_name=sheet_name)
        
        # Create a new figure
        figure = Figure(figsize=(12, 8))
        ax = figure.add_subplot(111)
        ax.set_facecolor('none')

        # Plot the data on the graph
        ax.plot(df.iloc[:, 0], df.iloc[:, 1], label="Cutting Force Fc [N]", linewidth=1.5)
        ax.plot(df.iloc[:, 0], df.iloc[:, 2], label="Normal Cutting Force FcN [N]", linewidth=1.5)

        # Set title and labels
        ax.set_xlabel("Time t [ms]", fontsize=11)
        ax.set_ylabel("Force Component Fi [N]", fontsize=11)
        ax.legend(fontsize=11)

        # Customize axis appearance
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        createPlots.canvas(self, figure)


    def plot_temp_penetration_graph(self, sheet_name):
        """
        Generates and displays temperature-related graphs using Matplotlib.

        Args:
            filename (str): Name of the sheet in the Excel file.
        """
        matplotlib.use('QtAgg')
        path = os.path.join(self.graph_folder, "temperature_result.xlsx")
        df = pd.read_excel(path, sheet_name=sheet_name)

        # Create a new figure for Temperature vs. Penetration Depth
        figure = Figure(figsize=(12, 8))
        ax = figure.add_subplot(111)

        ax.plot(df.iloc[:, 0], df.iloc[:, 1], label="Temperature at the last frame", linewidth=1.5)
        ax.plot(df.iloc[:, 0], df.iloc[:, 2], label="Maximum temperature", linewidth=1.5)

        ax.set_xlabel("Penetration Depth [µm]", fontsize=11)
        ax.set_ylabel("Temperature T [°C]", fontsize=11)
        ax.legend(fontsize=11)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        # Create the canvas and add it to the UI
        createPlots.canvas(self, figure)


    def plot_temp_time_graph(self, sheet_name):
        """
        Generates and displays temperature vs time graph using Matplotlib.

        Args:
            filename (str): Name of the sheet in the Excel file containing the time-temperature data.
        """
        matplotlib.use('QtAgg')
        path = os.path.join(self.graph_folder, "temperature_result.xlsx")
        df = pd.read_excel(path, sheet_name=sheet_name)

        # Create the graph for Temperature at Node vs Time
        figure = Figure(figsize=(12, 8))
        ax = figure.add_subplot(111)
        ax.plot(df.iloc[:, 3], df.iloc[:, 4], label="Temperature at Node 1", linewidth=1.5)

        ax.set_xlabel("Time t [ms]", fontsize=11)
        ax.set_ylabel("Temperature at Node 1 [°C]", fontsize=11)
        ax.legend(fontsize=11)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        # Create the canvas and add it to the UI
        createPlots.canvas(self, figure)

  
    def plot_chip(self, sheet_name):
        """
        Generates and displays the chip contour using Alpha Shape.

        Args:
            filename (str): Name of the sheet in the Excel file.
        """
        matplotlib.use('QtAgg') 
        path = os.path.join(self.graph_folder, "chip_shape.xlsx")
        df = pd.read_excel(path, sheet_name=sheet_name)

        pontos = df[['X', 'Y']].values

        # Generate the closed contour
        hull = alphashape.alphashape(pontos, alpha = 250)

        # Plot chip contour
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
        createPlots.canvas(self, figure)


    def plot_convergence_analysis(self):
        matplotlib.use('QtAgg') 
        # self.excel_files = r"S:\Junior\abaqus-with-python\convergence_and_correlation_analysis\database"
        excel_results_path = os.path.join(self.excel_files, "datas.xlsx")
        df = pd.read_excel(excel_results_path)

        df.drop(columns=[col for col in df .columns if col.startswith("Par") and col != "Parameter Set"], inplace=True)
        grouped = df.groupby(["Iteration Number", "Parameter Set"])     
       
        dict_errors = {}
        fc = fn = temp = ccr = csr = 0.0
        for name, group in grouped:
            if self.forces:
                fc = pd.to_numeric(group["Error Fc"], errors="coerce").abs().mean()
                fn = pd.to_numeric(group["Error Fn"], errors="coerce").abs().mean()
            if self.temp:
                temp = pd.to_numeric(group["Error Fc"], errors="coerce").abs().mean()
                print('temp')
            if self.chip:
                ccr = pd.to_numeric(group["Error CCR"], errors="coerce").abs().mean()
                csr = pd.to_numeric(group["Error CSR"], errors="coerce").abs().mean()

            # Erro combinado com os pesos definidos  
            combined_error = self.weights[0] * fc + self.weights[1] * fn + self.weights[2] * temp + self.weights[3] * ccr + self.weights[4] * csr
            dict_errors[name] = {
                "error": round(combined_error * 100, 1),}# multiplicado por 100 para porcentagem}
        
        lines = {}
        for keys, values in dict_errors.items():
            particle = keys[1]
            for error_type, error_value in values.items():
                if error_type not in lines:
                    lines[error_type] = {i: [] for i in range(1, self.number_of_particles+1)}
                lines[error_type][particle].append(abs(error_value))

        min_values = {}
        for error_type, set_values in lines.items():
            all_values = [val for values in set_values.values() for val in values]
            min_values[error_type] = min(all_values)

        # Create plot
        figure = Figure(figsize=(10, 6))
        ax = figure.add_subplot(111)

        ax.axhline(min_values['error'], color='gray', linestyle='--')
        ax.text(1, min_values['error'] - 2, f"{min_values['error']:.1f}%", va='bottom', ha='left', fontsize=10)

        n_points = len(next(iter(lines['error'].values())))
        ax.set_xticks(range(1, n_points + 1))
        ax.set_ylim(bottom=0, top=100)
        ax.set_xlabel("Iteration Number")
        ax.set_ylabel("Average Error (%)")

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        for set_num in range(1, self.number_of_particles+1):
            if set_num in [1, 2, 3, 4, 5]:
                y = lines['error'][set_num]
                x = np.arange(1, len(y) + 1)
                line = ax.plot(x, y, label=f"Set-{set_num:02d}")
                color = line[0].get_color()
                
                if len(y) >= 2:
                    coef = np.polyfit(x, y, 1)
                    trendline = np.polyval(coef, x)
                    ax.plot(x, trendline, linestyle='--', color=color, label=f"Set-{set_num:02d} (trendline)")
        ax.legend()
        createPlots.canvas(self, figure)




