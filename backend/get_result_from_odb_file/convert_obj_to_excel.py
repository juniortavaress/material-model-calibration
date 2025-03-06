import os
import alphashape
import pandas as pd
import numpy as np
from scipy.signal import find_peaks
from shapely.geometry import MultiPolygon
from openpyxl import load_workbook
from openpyxl.styles import Alignment
from backend.get_result_from_odb_file.createplt import createPlots
import os

class GetChipMeasure():
    def main_to_chip_results(self, file):
        """
        Main function to process OBJ files, calculate chip thickness statistics,
        and save results and plots.
        """
        # from file_utils import FileUtils
        # self.file = FileUtils()
        # self.file.create_folders(self, "temp-force")

        file_directory = self.obj_path
        output_directory = self.excel_files

        results, file_groups = [], {}
        GetChipMeasure.process_datas(self, file_directory, file_groups, output_directory, file)
        GetChipMeasure.calculate_results_and_save(self, file_groups, results, output_directory)
        

    def process_datas(self, file_directory, file_groups, output_directory, file):
        """
        Processes all OBJ files in the specified directory.

        Args:
            file_directory (str): Path to the directory containing OBJ files.
            file_groups (dict): Dictionary to store grouped file results.
        """
        for file_name in os.listdir(file_directory):
            if file_name.endswith('.obj'):
                base_name = '_'.join(file_name.split('_')[:-1])  
                file_path = os.path.join(file_directory, file_name)

                if base_name == file:
                    try: 
                        num_lines = GetChipMeasure.count_lines_until_empty(file_path)

                        
                        min_distances, peaks, valleys, lower_chip_side, upper_chip_side, left_segmented_chip_side, right_smooth_chip_side, points, absolute_minimum, absolute_maximum = GetChipMeasure.process_obj_file(file_path, num_lines, output_directory)


                        if base_name not in file_groups:
                            file_groups[base_name] = []
                        file_groups[base_name].append((file_name, absolute_minimum, absolute_maximum))

                        if "Frame50" in file_name or "Frame46" in file_name:
                            createPlots.create_plots(self, file_name, min_distances, peaks, valleys, lower_chip_side, upper_chip_side, left_segmented_chip_side, right_smooth_chip_side, points)

                    except Exception as e:
                        
                        # Print the error and the file that caused it
                        # print(f"Error processing file: {file_name}")
                        # print(f"Error details: {e}")
                        continue  # Skip this file and move to the next one

    def count_lines_until_empty(file_path):
        """
        Counts the number of non-empty lines in the file.

        Args:
            file_path (str): Path to the file to count lines.

        Returns:
            int: Number of non-empty lines before the first empty line.
        """
        count = 0
        with open(file_path, 'r') as file:
            for line in file:
                if not line.strip():
                    break
                count += 1
        return count


    def process_obj_file(file_path, num_lines, output_directory):
        """
        Processes a single OBJ file to calculate chip thickness statistics.

        Args:
            file_path (str): Path to the OBJ file.
            num_lines (int): Number of lines to read in the file.

        Returns:
            float: Average minimum chip thickness.
            float: Average maximum chip thickness.
        """
        points = GetChipMeasure.load_obj_points(file_path, num_lines)
        alpha_shape = GetChipMeasure.find_valid_alphashape(points)

        if alpha_shape is None or alpha_shape.is_empty:
            raise ValueError("AlphaShape is empty or invalid.")
    
        # Extract chip sides
        contour_points, ymin, ymax = GetChipMeasure.sort_contour_points(alpha_shape)
        lower_chip_side = GetChipMeasure.get_chip_side_01(contour_points, ymin) 
        upper_chip_side = GetChipMeasure.get_chip_side_02(contour_points, ymax, ymin) 
        left_segmented_chip_side = GetChipMeasure.get_chip_side_03(contour_points, lower_chip_side, upper_chip_side, ymin, ymax)
        right_smooth_chip_side = GetChipMeasure.get_chip_side_04(upper_chip_side, contour_points, lower_chip_side)

        # Calculate distances and statistics
        min_distances = GetChipMeasure.calculate_min_distances(left_segmented_chip_side, right_smooth_chip_side)
        peaks, _ = find_peaks(min_distances)
        valleys, _ = find_peaks(-min_distances)

        # print(file_path, peaks, valleys)

        if len(peaks) == 0:
            pass
            # print("No peaks were found in the distance data.")
        if len(valleys) == 0:
            pass
            # print("No valleys were found in the distance data.")

        absolute_maximum = np.max(min_distances[peaks]) * 1000
        absolut_minimum = np.min(min_distances[valleys]) * 1000
        return min_distances, peaks, valleys, lower_chip_side, upper_chip_side, left_segmented_chip_side, right_smooth_chip_side, points, absolut_minimum, absolute_maximum
        # return 0, 0, 0, 0, 0, 0, 0, 0, 0, 0


    def load_obj_points(file_path, num_lines):
        """
        Loads points from an OBJ file and filters them for further processing.

        Args:
            file_path (str): Path to the OBJ file.
            num_lines (int): Number of lines to read in the file.

        Returns:
            np.ndarray: Filtered 2D points.
        """
        arc = np.loadtxt(file_path, skiprows=2, max_rows=num_lines - 2, usecols=(1, 2, 3))

        # Mine
        # points = arc[arc[:, 2] == 0.02]
        points = arc[(arc[:, 2] >= 0.02*0.8) & (arc[:, 2] <= 0.02*1.2)]
        # points = points[(points[:, 1] >= 0.55) & (points[:, 1] <= 0.75)]
        points = points[(points[:, 1] >= 0.55)]

        # Severin
        # points = arc[arc[:, 2] == 0.02]
        # points = points[points[:, 1] >= 0.02]  # Filter some points because sometimes there were errors with alphashape
        # points = points[points[:, 1] <= 0.5]  # Filter some points because sometimes there were errors with alphashape
        return np.delete(points, 2, axis=1) 


    def sort_contour_points(alpha_shape):
        """
        Sorts the contour points from the alpha shape, ensuring correct order.

        Args:
            alpha_shape (Polygon): The alpha shape calculated from the points.

        Returns:
            np.ndarray: Sorted contour points.
            float: Minimum y-value in the contour points.
            float: Maximum y-value in the contour points.
        """
        contour_x, contour_y = alpha_shape.exterior.xy
        contour_points = np.column_stack((contour_x, contour_y))
        ymin = np.min(contour_points[:, 1])
        lower_y_points = contour_points[contour_points[:, 1] == ymin] 
        start_point = lower_y_points[np.argmax(lower_y_points[:, 0])] 
        start_index = np.where(np.all(contour_points == start_point, axis=1))[0][0]
        contour_points = np.roll(contour_points, -start_index, axis=0)  
        ymax = np.max(contour_y)
        return contour_points, ymin, ymax


    def find_valid_alphashape(points, alpha=150, step_size=0.005):
        """
        Finds a valid alpha shape for the given points.

        Args:
            points (np.ndarray): Array of 2D points.
            alpha (float): Alpha parameter for the alpha shape calculation.
            step_size (float): Increment to filter points if alpha shape fails.

        Returns:
            Polygon: Valid alpha shape.
        """
        iteration = 0
        while True:
            try:
                alpha_shape = alphashape.alphashape(points, alpha)
                if isinstance(alpha_shape, MultiPolygon):
                    raise AttributeError("Alphashape resulted in MultiPolygon.")
                return alpha_shape
            except AttributeError:
                iteration += 1
                xmin = np.min(points[:, 0])
                
                # Filter points that are greater than xmin + step_size
                points = points[points[:, 0] > xmin + step_size]
                if len(points) == 0:
                    raise ValueError("No more valid points avaliable.")


    def get_chip_side_01(contour_points, ymin):
        """
        Extracts the lower chip side.

        Args:
            contour_points (np.ndarray): Contour points of the alpha shape.
            ymin (float): Minimum y-value in the contour points.

        Returns:
            np.ndarray: Points representing the lower chip side.
        """
        return contour_points[contour_points[:, 1] == ymin]


    def get_chip_side_02(contour_points, ymax, ymin):
        """
        Extracts the upper chip side based on vertical and horizontal segments.

        Args:
            contour_points (np.ndarray): Contour points of the alpha shape.
            ymax (float): Maximum y-value in the contour points.

        Returns:
            np.ndarray: Points representing the upper chip side.
        """
        upper_chip_side = [] 
        vertical_line = GetChipMeasure.find_vertical_lines(contour_points)
        vertical_line = np.array(vertical_line, dtype=object).squeeze()

        horizontal_lines = GetChipMeasure.find_horizontal_lines(contour_points, ymin)

        # Determine the upper chip side based on vertical and horizontal segments
        if horizontal_lines:  # If horizontal lines are found
            # Select the horizontal line with the highest y-coordinate
            horizontal_lines = sorted(horizontal_lines, key=lambda line: np.max(line[:, 1]), reverse=True)
            horizontal_line = horizontal_lines[0]

            # Combine with vertical lines, if present
            if vertical_line.size > 0:
                upper_chip_side = np.vstack((vertical_line, horizontal_line))
            else:
                upper_chip_side = horizontal_line
        else:
            # Fallback: Only vertical lines or points at ymax
            if vertical_line.size > 0:
                upper_chip_side = vertical_line
            else:
                upper_chip_side = contour_points[contour_points[:, 1] == ymax]

        return upper_chip_side


    def get_chip_side_03(contour_points, lower_chip_side, upper_chip_side, ymin, ymax):
        """
        Extracts the left segmented chip side by connecting the lower and upper chip sides.

        Args:
            contour_points (np.ndarray): Contour points of the alpha shape.
            lower_chip_side (np.ndarray): Points of the lower chip side.
            upper_chip_side (np.ndarray): Points of the upper chip side.
            ymin (float): Minimum y-value in the contour points.
            ymax (float): Maximum y-value in the contour points.

        Returns:
            np.ndarray: Points representing the left segmented chip side.
        """
        left_segmented_chip_side = []
        lower_end_index = np.where(np.all(contour_points == lower_chip_side[-1], axis=1))[0][0]
        upper_start_index = np.where(np.all(contour_points == upper_chip_side[0], axis=1))[0][0]

        # Collect points between the lower and upper chip side
        for i in range(lower_end_index + 1, upper_start_index):
            point = contour_points[i]
            if ymin < point[1] < ymax:
                left_segmented_chip_side.append(point)

        # Close the left chip side by appending the start and end points
        left_segmented_chip_side.insert(0, lower_chip_side[-1])  # Append end of lower line
        left_segmented_chip_side = np.array(left_segmented_chip_side)
        return left_segmented_chip_side


    def get_chip_side_04(upper_chip_side, contour_points, lower_chip_side):
        """
        Extracts the right smooth chip side by connecting the upper and lower chip sides.

        Args:
            upper_chip_side (np.ndarray): Points of the upper chip side.
            contour_points (np.ndarray): Contour points of the alpha shape.
            lower_chip_side (np.ndarray): Points of the lower chip side.

        Returns:
            np.ndarray: Points representing the right smooth chip side.
        """
        # Append start and end points to close the right segment
        right_smooth_chip_side = []
        start_point = upper_chip_side[-1] 
        found_start = False

        # Collect points along the contour starting from the right segment
        for point in contour_points:
            if np.array_equal(point, start_point):
                found_start = True
            if found_start:
                right_smooth_chip_side.append(point)

        # Close the right segment by appending the start and end points
        right_smooth_chip_side.append(lower_chip_side[0])  # Append start of lower line
        right_smooth_chip_side = np.array(right_smooth_chip_side)
        return right_smooth_chip_side


    def find_vertical_lines(contour_points):
        """
        Identifies vertical lines in the contour points.

        Args:
            contour_points (np.ndarray): Contour points of the alpha shape.

        Returns:
            list: List of vertical lines, each represented as a list of points.
        """
        vertical_lines = []
        current_line = [contour_points[0]]

        for i in range(1, len(contour_points)):
            x1, y1 = contour_points[i - 1]
            x2, y2 = contour_points[i]

            # Check if the line remains vertical (same x-coordinate)
            if x1 == x2:
                current_line.append((x2, y2))
            else:
                # Check if the vertical line is long enough
                if len(current_line) >= 5:
                    vertical_lines.append(current_line)
                current_line = [(x2, y2)]  # Reset with the current point

        # Final check for the last segment
        if len(current_line) >= 5:
            vertical_lines.append(current_line)
        return vertical_lines

    # Function to find horizontal lines with at least 3 points (excluding ymin)
    def find_horizontal_lines(contour_points, ymin):
        horizontal_lines = []
        unique_y = np.unique(contour_points[:, 1])  # All unique y-coordinates

        for y in unique_y:
            if y != ymin:  # Exclude ymin
                horizontal_line = contour_points[contour_points[:, 1] == y]
                if len(horizontal_line) >= 3:  # At least 3 points required
                    horizontal_lines.append(horizontal_line)

        return horizontal_lines
    
    def calculate_min_distances(curve1, curve2):
        """
        Calculates the minimal distances between two curves.

        Args:
            curve1 (np.ndarray): Points of the first curve.
            curve2 (np.ndarray): Points of the second curve.

        Returns:
            np.ndarray: Minimal distances between the curves.
        """
        curve1 = np.array(curve1)
        curve2 = np.array(curve2)
        # Adjustment of the dimensions
        curve1_exp = np.expand_dims(curve1, axis=1)
        curve2_exp = np.expand_dims(curve2, axis=0)
        # Calculation of Euclidean distances
        distances = np.sqrt(np.sum((curve1_exp - curve2_exp) ** 2, axis=2))
        # Calculation of minimal distances and corresponding indices
        min_indices = np.argmin(distances, axis=1)
        min_distances = distances[np.arange(len(curve1)), min_indices]
        # Get the first and last point of curve2
        first_point = curve2[0]
        last_point = curve2[-1]
        
        # Filter out measurements involving the first or last point of curve2
        filtered_indices = [
            i for i, idx in enumerate(min_indices)
            if not (np.array_equal(curve2[idx], first_point) or np.array_equal(curve2[idx], last_point))
        ]
        
        # Return the filtered distances
        filtered_distances = min_distances[filtered_indices]
        
        return filtered_distances


    def calculate_results_and_save(self, file_groups, results, output_directory):
        """
        Calculates the results for all file groups and saves them to an Excel file.

        Args:
            file_groups (dict): Grouped file results.
            results (list): List to store results.
            output_directory (str): Path to the output directory.
        """
        for base_name, group_results in file_groups.items():
            group_results.sort(key=lambda x: int(x[0].split('_')[-1].replace('Frame', '').replace('.obj', '')))
            h = float(f"{base_name.split('h')[1].split('_g')[0]}")
            means_min = [r[1] for r in group_results]
            means_max = [r[2] for r in group_results]
            self.chip_datas[base_name] = {"Chip Compression Ratio (CCR)": np.mean(means_max)/h, "Chip Segmentatio Ratio (CSR)": np.mean(means_max)/np.mean(means_min)}

if __name__ == "__main__":
    chip = GetChipMeasure()
    chip.main_to_chip_results()