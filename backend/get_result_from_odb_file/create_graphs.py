import os 
import numpy as np
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt

class createPlots:
    def create_plots(self, file_path, min_distances, peaks, valleys, sides, points):
        # self.chip_images = r"S:\Junior\abaqus-with-python\otimization-scripts\new-version\material-model-calibration\Teste\chip_images"

        folder = os.path.join(self.chip_images, os.path.basename(file_path)[:-12])
        if not os.path.isdir(folder):
            os.makedirs(folder)

        graph_names = ["_thickness_profile.png", "_detected_sides.png", "_minimal_distances.png", "_measurement_lines.png"]
        for graph_name in graph_names:
            createPlots.plot(self, graph_name, folder, file_path, min_distances, peaks, valleys, sides, points)

        
    def plot_trickness_profile(self, min_distances, peaks, valleys):
        plt.plot(range(len(min_distances)), min_distances, '-', color='blue', linewidth=1.5, label='Chip Thickness')
        plt.plot(peaks, min_distances[peaks], 'ro', label='Maximal Thickness')  
        plt.plot(valleys, min_distances[valleys], 'go', label='Minimal Thickness') 
        ymax = np.max(min_distances)
        plt.ylim(0, ymax * 1.2)


    def plot_chip_geometry(self, points, sides):
        plt.axis('equal')
        plt.plot(points[:, 0], points[:, 1], 'b.', markersize=5, label='Points')
        plt.plot(sides[0][:, 0], sides[0][:, 1], 'c-', linewidth=2, label='Lower chip side')
        plt.plot(sides[1][:, 0], sides[1][:, 1], 'm-', linewidth=2, label='Upper chip side')
        plt.plot(sides[2][:, 0], sides[2][:, 1], 'r-', linewidth=2, label='Segmented chip side')
    

    def plot_minimal_distances(self, min_distances):
        plt.plot(range(len(min_distances)), min_distances, 'o-', color='blue', markersize=3, label='Minimal Distances')


    def plot_measurement_lines(self, sides, points):
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


    def plot(self, graph_name, folder, file_path, min_distances, peaks, valleys, sides, points): 
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


    @staticmethod
    def create_forces_graphs(df):
        """
        Generates and saves force-related graphs using Matplotlib.

        Args:
            df (pd.DataFrame): DataFrame containing the data for the charts.
            sheet_name (str): Name to be used for the saved image file.
        """
        sheet_name = "Forces"
        print("DF FORCES: ", df.head())
        # Criar a figura
        plt.figure(figsize=(8, 5))

        # Plotar os dados
        plt.plot(df.iloc[:, 0], df.iloc[:, 1], label="Cutting Force Fc [N]", linewidth=1.5)
        plt.plot(df.iloc[:, 0], df.iloc[:, 2], label="Normal Cutting Force FcN [N]", linewidth=1.5)

        # Configurar títulos e legendas
        plt.title(sheet_name, fontsize=14)
        plt.xlabel("Time t [ms]", fontsize=11)
        plt.ylabel("Force Component Fi [N]", fontsize=11)
        plt.legend(fontsize=11)
        plt.grid(True)

        # Salvar a imagem no diretório atual
        image_path = os.path.join(os.getcwd(), f"{sheet_name}.png")
        plt.savefig(image_path, dpi=300, bbox_inches="tight")

        # Fechar a figura para evitar consumo de memória
        plt.close()

        print(f"Graph saved as {image_path}")


    @staticmethod
    def create_temp_graps(df):
        """
        Generates and saves temperature-related graphs using Matplotlib.

        Args:
            df (pd.DataFrame): DataFrame containing the data for the charts.
            sheet_name (str): Name to be used for the saved image files.
        """
        print("DF TEMP: ", df.head())
        # Directory to save the images
        sheet_name = "Temp"
        save_path = os.getcwd()

        # Chart 1: Temperature vs. Penetration Depth
        plt.figure(figsize=(8, 5))
        plt.plot(df.iloc[:, 0], df.iloc[:, 1], label="Temperature at the last frame", linewidth=1.5)
        plt.plot(df.iloc[:, 0], df.iloc[:, 2], label="Maximum temperature", linewidth=1.5)

        plt.title(sheet_name, fontsize=14)
        plt.xlabel("Penetration Depth [µm]", fontsize=11)
        plt.ylabel("Temperature T [°C]", fontsize=11)
        plt.legend(fontsize=11)
        plt.grid(True)

        image_path1 = os.path.join(save_path, f"{sheet_name}_penetration_vs_temp.png")
        plt.savefig(image_path1, dpi=300, bbox_inches="tight")
        plt.close()

        # Chart 2: Temperature at Node vs. Time
        plt.figure(figsize=(8, 5))
        plt.plot(df.iloc[:, 3], df.iloc[:, 4], label="Temperature at Node 1", linewidth=1.5)

        plt.title(sheet_name, fontsize=14)
        plt.xlabel("Time t [ms]", fontsize=11)
        plt.ylabel("Temperature at Node 1 [°C]", fontsize=11)
        plt.legend(fontsize=11)
        plt.grid(True)

        image_path2 = os.path.join(save_path, f"{sheet_name}_time_vs_temp.png")
        plt.savefig(image_path2, dpi=300, bbox_inches="tight")
        plt.close()

        print(f"Graphs saved as {image_path1} and {image_path2}")