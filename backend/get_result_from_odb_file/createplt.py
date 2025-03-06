import os 
import numpy as np
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt

class createPlots:
    def create_plots(self, file_path, min_distances, peaks, valleys, lower_chip_side, upper_chip_side, left_segmented_chip_side, right_smooth_chip_side, points):

        folder = os.path.join(self.chip_images, os.path.basename(file_path)[:-12])
        if not os.path.isdir(folder):
            os.makedirs(folder)

        graph_names = ["_thickness_profile.png", "_detected_sides.png", "_minimal_distances.png", "_measurement_lines.png"]
        for graph_name in graph_names:
            createPlots.plot(self, graph_name, folder, file_path, min_distances, peaks, valleys, lower_chip_side, upper_chip_side, left_segmented_chip_side, right_smooth_chip_side, points)

        
    def plot_trickness_profile(self, min_distances, peaks, valleys):
        plt.plot(range(len(min_distances)), min_distances, '-', color='blue', linewidth=1.5, label='Chip Thickness')
        plt.plot(peaks, min_distances[peaks], 'ro', label='Maximal Thickness')  
        plt.plot(valleys, min_distances[valleys], 'go', label='Minimal Thickness') 
        ymax = np.max(min_distances)
        plt.ylim(0, ymax * 1.2)


    def plot_chip_geometry(self, points, lower_chip_side, upper_chip_side, left_segmented_chip_side, right_smooth_chip_side):
        plt.axis('equal')
        plt.plot(points[:, 0], points[:, 1], 'b.', markersize=5, label='Points')
        plt.plot(lower_chip_side[:, 0], lower_chip_side[:, 1], 'c-', linewidth=2, label='Lower chip side')
        plt.plot(upper_chip_side[:, 0], upper_chip_side[:, 1], 'm-', linewidth=2, label='Upper chip side')
        plt.plot(left_segmented_chip_side[:, 0], left_segmented_chip_side[:, 1], 'r-', linewidth=2, label='Segmented chip side')
    

    def plot_minimal_distances(self, min_distances):
        plt.plot(range(len(min_distances)), min_distances, 'o-', color='blue', markersize=3, label='Minimal Distances')


    def plot_measurement_lines(self, left_segmented_chip_side, right_smooth_chip_side, points):
        left_points = np.array(left_segmented_chip_side)
        right_points = np.array(right_smooth_chip_side)

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


    def plot(self, graph_name, folder, file_path, min_distances, peaks, valleys, lower_chip_side, upper_chip_side, left_segmented_chip_side, right_smooth_chip_side, points): 
        plt.figure(figsize=(10, 10))
        plt.title('Detected Chip Sides')
        plt.xlabel('X Coordinates [mm]')
        plt.ylabel('Y Coordinates [mm]')
        plt.grid()

        if graph_name == "_thickness_profile.png":
            createPlots.plot_trickness_profile(self, min_distances, peaks, valleys)
        elif graph_name == "_detected_sides.png":
            createPlots.plot_chip_geometry(self, points, lower_chip_side, upper_chip_side, left_segmented_chip_side, right_smooth_chip_side)
        elif graph_name == "_minimal_distances.png":
            createPlots.plot_minimal_distances(self, min_distances)
        elif graph_name == "_measurement_lines.png":
            createPlots.plot_measurement_lines(self, left_segmented_chip_side, right_smooth_chip_side, points)

        save_path = os.path.join(folder, os.path.basename(file_path)[-11:].replace('.obj', graph_name))
        plt.savefig(save_path)
        plt.close()
