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
                self.canvas = FigureCanvas(Figure(figsize=(12, 8)))  # Inicializa o canvas em branco

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
        filename = self.ui.combobox_file.currentText()
        type = self.ui.combobox_analysis_type.currentText()

        if filename != "None":
            try:
                if type == "Forces":
                    createPlots.plot_force_graphs(self, filename)
                elif type == "Temperature vs. Time":
                    createPlots.plot_temp_time_graph(self, filename)
                elif type == "Temperature vs. Penetration Depth":
                    createPlots.plot_temp_penetration_graph(self, filename)
                elif type == "Chip Format":
                    createPlots.plot_chip(self, filename)
            except:
                createPlots.canvas(self)
        else:
            createPlots.canvas(self)


    def plot_force_graphs(self, filename):
        """
        Generates and displays force-related graphs using Matplotlib.

        Args:
            filename (str): Name of the sheet in the Excel file.
        """
        matplotlib.use('QtAgg') 
        path = os.path.join(self.graph_folder, "forces_result.xlsx")
        df = pd.read_excel(path, sheet_name=filename[4:])
        
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


    def plot_temp_penetration_graph(self, filename):
        """
        Generates and displays temperature-related graphs using Matplotlib.

        Args:
            filename (str): Name of the sheet in the Excel file.
        """
        matplotlib.use('QtAgg')
        path = os.path.join(self.graph_folder, "temperature_result.xlsx")
        df = pd.read_excel(path, sheet_name=filename[4:])

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


    def plot_temp_time_graph(self, filename):
        """
        Generates and displays temperature vs time graph using Matplotlib.

        Args:
            filename (str): Name of the sheet in the Excel file containing the time-temperature data.
        """
        matplotlib.use('QtAgg')
        path = os.path.join(self.graph_folder, "temperature_result.xlsx")
        df = pd.read_excel(path, sheet_name=filename[4:])

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

  
    def plot_chip(self, filename):
        """
        Generates and displays the chip contour using Alpha Shape.

        Args:
            filename (str): Name of the sheet in the Excel file.
        """
        matplotlib.use('QtAgg') 
        path = os.path.join(self.graph_folder, "chip_shape.xlsx")
        df = pd.read_excel(path, sheet_name=filename[4:])

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


    def create_chip_img(self, file_path, min_distances, peaks, valleys, sides, points):
        """
        Creates images of chip shape and stores them in a folder.

        Args:
            file_path (str): Path to the input file.
            min_distances (list): List of minimum distances.
            peaks (list): List of peak points.
            valleys (list): List of valley points.
            sides (list): List of detected sides.
            points (array): Array of points representing the chip geometry.
        """
        matplotlib.use('Agg') 
        folder = os.path.join(self.chip_images, os.path.basename(file_path)[:-12])
        if not os.path.isdir(folder):
            os.makedirs(folder)

        graph_names = ["_thickness_profile.png", "_detected_sides.png", "_minimal_distances.png", "_measurement_lines.png"]
        for graph_name in graph_names:
            plt.figure(figsize=(10, 10))
            plt.title('Detected Chip Sides')
            plt.xlabel('X Coordinates [mm]')
            plt.ylabel('Y Coordinates [mm]')
            plt.grid()

            if graph_name == "_thickness_profile.png":
                createPlots.plot_trickness_profile(self, min_distances, peaks, valleys)
            elif graph_name == "_detected_sides.png":
                createPlots.plot_chip_geometry(self, points, sides)
            elif graph_name == "_minimal_distances.png":
                createPlots.plot_minimal_distances(self, min_distances)
            elif graph_name == "_measurement_lines.png":
                createPlots.plot_measurement_lines(self, sides, points)

            save_path = os.path.join(folder, os.path.basename(file_path)[-11:].replace('.obj', graph_name))
            plt.savefig(save_path)
            plt.close()  


    def plot_trickness_profile(self, min_distances, peaks, valleys):
        """
        Plots the thickness profile of the chip.

        Args:
            min_distances (list): List of minimum distances (thickness) at each point.
            peaks (list): List of peak indices in the thickness profile.
            valleys (list): List of valley indices in the thickness profile.
        """
        plt.plot(range(len(min_distances)), min_distances, '-', color='blue', linewidth=1.5, label='Chip Thickness')
        plt.plot(peaks, min_distances[peaks], 'ro', label='Maximal Thickness')  
        plt.plot(valleys, min_distances[valleys], 'go', label='Minimal Thickness') 
        ymax = np.max(min_distances)
        plt.ylim(0, ymax * 1.2)


    def plot_chip_geometry(self, points, sides):
        """
        Plots the geometry of the chip, showing the detected sides.

        Args:
            points (array): Points representing the chip geometry.
            sides (list): List of sides of the chip.
        """
        plt.axis('equal')
        plt.plot(points[:, 0], points[:, 1], 'b.', markersize=5, label='Points')
        plt.plot(sides[0][:, 0], sides[0][:, 1], 'c-', linewidth=2, label='Lower chip side')
        plt.plot(sides[1][:, 0], sides[1][:, 1], 'm-', linewidth=2, label='Upper chip side')
        plt.plot(sides[2][:, 0], sides[2][:, 1], 'r-', linewidth=2, label='Segmented chip side')
    

    def plot_minimal_distances(self, min_distances):
        """
        Plots the minimal distances of the chip.

        Args:
            min_distances (list): List of minimum distances between points.
        """
        plt.plot(range(len(min_distances)), min_distances, 'o-', color='blue', markersize=3, label='Minimal Distances')


    def plot_measurement_lines(self, sides, points):
        """
        Plots the measurement lines between sides of the chip.

        Args:
            sides (list): List of detected sides of the chip.
            points (array): Points representing the chip geometry.
        """
        left_points = np.array(sides[2])
        right_points = np.array(sides[3])

        # Interpolation of the middle points
        num_measurement_points = len(left_points)
        t = np.linspace(0, 1, len(left_points))
        middle_left_interp_x = np.interp(np.linspace(0, 1, num_measurement_points), t, left_points[:, 0])
        middle_left_interp_y = np.interp(np.linspace(0, 1, num_measurement_points), t, left_points[:, 1])
        middle_left_interp_points = np.column_stack((middle_left_interp_x, middle_left_interp_y))

        # Calculate the corresponding points on the right curve (minimal distance)
        curve1 = np.expand_dims(middle_left_interp_points, axis=1)
        curve2 = np.expand_dims(right_points, axis=0)
        distances = np.sqrt(np.sum((curve1 - curve2) ** 2, axis=2))
        min_indices = np.argmin(distances, axis=1)
        selected_right_points = right_points[min_indices]

        # Filter out lines that involve the first or last point of the right curve
        first_point = right_points[0]
        last_point = right_points[-1]
        filtered_lines = [(p1, p2) for p1, p2, idx in zip(middle_left_interp_points, selected_right_points, min_indices) if not (np.array_equal(p2, first_point) or np.array_equal(p2, last_point))]
        
        plt.axis('equal')
        plt.plot(points[:, 0], points[:, 1], 'b.', markersize=5, label='Points')
        plt.plot(left_points[:, 0], left_points[:, 1], 'r-', linewidth=2, label='Left Chip Side')
        plt.plot(right_points[:, 0], right_points[:, 1], 'g-', linewidth=2, label='Right Chip Side')

        # Draw only the filtered measurement lines
        for p1, p2 in filtered_lines:
            plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k--', linewidth=1)  # Draw connecting line


