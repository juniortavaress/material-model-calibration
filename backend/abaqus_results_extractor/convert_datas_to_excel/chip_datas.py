import os 
import matplotlib
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

class ManagerChipDatasAndImage():
    """
    Class for generating and displaying plots related to forces, temperature, and chip shape.
    """
    def get_datas_and_figures(self, base_name, file_path, min_distances, peaks, valleys, sides, points):
        ManagerChipDatasAndImage.save_chip_datas(self, base_name, points)
        ManagerChipDatasAndImage.create_chip_img(self, file_path, min_distances, peaks, valleys, sides, points)
        return False

    def save_chip_datas(self, base_name, points):
        df_points = pd.DataFrame(points, columns=["X", "Y"])
        output_excel_path = os.path.join(self.output_excel_dir, "chip_shape.xlsx")

        sheet_name = base_name[4:]
        if len(sheet_name) > 31:
            sheet_name = sheet_name[:31]

        if os.path.exists(output_excel_path):
            with pd.ExcelWriter(output_excel_path, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                df_points.to_excel(writer, sheet_name=sheet_name, index=False)
        else:
            df_points.to_excel(output_excel_path, sheet_name=sheet_name, index=False, engine="openpyxl")


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
            try:
                plt.figure(figsize=(10, 10))
                plt.title('Detected Chip Sides')
                plt.xlabel('X Coordinates [mm]')
                plt.ylabel('Y Coordinates [mm]')
                plt.grid()

                if graph_name == "_thickness_profile.png":
                    ManagerChipDatasAndImage.plot_trickness_profile(self, min_distances, peaks, valleys)
                elif graph_name == "_detected_sides.png":
                    ManagerChipDatasAndImage.plot_chip_geometry(self, points, sides)
                elif graph_name == "_minimal_distances.png":
                    ManagerChipDatasAndImage.plot_minimal_distances(self, min_distances)
                elif graph_name == "_measurement_lines.png":
                    ManagerChipDatasAndImage.plot_measurement_lines(self, sides, points)

                save_path = os.path.join(folder, os.path.basename(file_path)[-11:].replace('.obj', graph_name))
                plt.savefig(save_path)
                plt.close()  
            except:
                pass
                # print("Nao foi possivel criar o grafico")


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


