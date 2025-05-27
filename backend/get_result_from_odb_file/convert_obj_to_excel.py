import os
import yaml
import traceback
import alphashape
import numpy as np
import pandas as pd
from scipy.signal import find_peaks
from shapely.geometry import MultiPolygon
from backend.get_result_from_odb_file.create_graphs import createPlots

class GetChipMeasure():
    def main_to_chip_results(self, filename):
        """
        Main function to process OBJ files, calculate chip thickness statistics,
        and save results and plots.
        """
        file_groups = {}
        file_directory = self.obj_path
        file_groups = GetChipMeasure.process_datas(self, file_directory, file_groups, filename)
        GetChipMeasure.calculate_results_and_save(self, file_groups)
        

    def process_datas(self, file_directory, file_groups, filename):
        """
        Processes all OBJ files in the specified directory.

        Args:
            file_directory (str): Path to the directory containing OBJ files.
            file_groups (dict): Dictionary to store grouped file results.
        """
        save_datas = True
        for file in os.listdir(file_directory):
            if file.endswith('.obj') and file.startswith(filename):
                base_name = '_'.join(file.split('_')[:-1])  
                file_path = os.path.join(file_directory, file)

                try: 
                    num_lines = GetChipMeasure.count_lines_until_empty(file_path)
                    min_distances, peaks, valleys, sides, points, absolute_minimum, absolute_maximum = GetChipMeasure.process_obj_file(file_path, num_lines)

                    if base_name not in file_groups:
                        file_groups[base_name] = []
                    file_groups[base_name].append((file, absolute_minimum, absolute_maximum))

                    if "Frame50" in file or "Frame46" in file:
                        createPlots.create_chip_img(self, file, min_distances, peaks, valleys, sides, points)
                    
                    if save_datas:
                        df_points = pd.DataFrame(points, columns=["X", "Y"])
                        output_excel_path = os.path.join(self.graph_folder, "chip_shape.xlsx")

                        sheet_name = base_name[4:]
                        if len(sheet_name) > 31:
                            sheet_name = sheet_name[:31]

                        if os.path.exists(output_excel_path):
                            with pd.ExcelWriter(output_excel_path, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                                df_points.to_excel(writer, sheet_name=sheet_name, index=False)
                        else:
                            df_points.to_excel(output_excel_path, sheet_name=sheet_name, index=False, engine="openpyxl")

                        save_datas = False
                        
                except Exception as e:
                    traceback.print_exc()
                    continue 
        return file_groups


    def count_lines_until_empty(file_path):
        """
        Counts the number of non-empty lines in the file.

        Args:
            file_path (str): Path to the file to count lines.

        Returns:
            int: Number of lines with vertices information
        """
        count = 0
        with open(file_path, 'r') as file:
            for line in file:
                if not line.strip():
                    break
                count += 1
        return count


    def process_obj_file(file_path, num_lines):
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
        lower_chip_side = contour_points[contour_points[:, 1] == ymin]
        upper_chip_side = GetChipMeasure.get_chip_side_02(contour_points, ymax, ymin) 
        left_segmented_chip_side = GetChipMeasure.get_chip_side_03(contour_points, lower_chip_side, upper_chip_side, ymin, ymax)
        right_smooth_chip_side = GetChipMeasure.get_chip_side_04(upper_chip_side, contour_points, lower_chip_side)
        sides = [lower_chip_side, upper_chip_side, left_segmented_chip_side, right_smooth_chip_side]

        # Calculate distances and statistics
        min_distances = GetChipMeasure.calculate_min_distances(left_segmented_chip_side, right_smooth_chip_side)
        peaks, _ = find_peaks(min_distances)
        valleys, _ = find_peaks(-min_distances)

        if len(peaks) > 0:
            absolute_maximum = np.max(min_distances[peaks]) * 1000
        else:
            absolute_maximum = 0
           
        if len(valleys) > 0:
            absolut_minimum = np.min(min_distances[valleys]) * 1000
        else:
            absolut_minimum = 0      
        
        return min_distances, peaks, valleys, sides, points, absolut_minimum, absolute_maximum


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

        y_min = np.min(arc[:, 1])
        y_max = np.max(arc[:, 1])
        z_min = np.min(arc[:, 2])
        z_max = np.max(arc[:, 2])
        y_lim_min = 1.03 * y_min if y_min > 0 else 0
        
        points = arc[(arc[:, 2] >= 0.7 * z_min) & (arc[:, 2] <= 1.3 * z_max)]
        points = points[(points[:, 1] >= y_lim_min) & (points[:, 1] <= 0.97 * y_max)]
        
        return np.delete(points, 2, axis=1) 


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
        if np.sum(contour_points[:, 1] == ymin) < 2: 
            ymin = np.unique(contour_points[:, 1])[1]

        ymax = np.max(contour_y)
        if np.sum(contour_points[:, 1] == ymax) < 2: 
            ymax = np.unique(contour_points[:, 1])[-2]
            
        lower_y_points = contour_points[contour_points[:, 1] == ymin] 
        start_point = lower_y_points[np.argmax(lower_y_points[:, 0])] 
        start_index = np.where(np.all(contour_points == start_point, axis=1))[0][0]
        contour_points = np.roll(contour_points, - start_index, axis=0)  
        return contour_points, ymin, ymax


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

        try:
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
        except:
            traceback.print_exc()
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
            if abs(x1 - x2) < 1e-5:
                current_line.append((x2, y2))
            else:
                # Check if the vertical line is long enough
                if len(current_line) >= 5:
                    vertical_lines.append(np.array(current_line))
                current_line = [(x2, y2)]

        # Final check for the last segment
        if len(current_line) >= 5:
            vertical_lines.append(np.array(current_line))
        
        if vertical_lines:
            return np.vstack(vertical_lines)
        return vertical_lines


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
        filtered_indices = [i for i, idx in enumerate(min_indices) if not (np.array_equal(curve2[idx], first_point) or np.array_equal(curve2[idx], last_point))]
        filtered_distances = min_distances[filtered_indices]
        return filtered_distances


    def calculate_results_and_save(self, file_groups):
        """
        Calculates the results for all file groups and saves them to an Excel file.

        Args:
            file_groups (dict): Grouped file results.
            results (list): List to store results.
            output_directory (str): Path to the output directory.
        """
        for base_name, group_results in file_groups.items():
            cond = base_name.split("_")[1]

            with open(self.project_infos_path, "r", encoding="utf-8") as file:
                data = yaml.safe_load(file)
            for condition in data.get("3. Conditions", {}).values():
                if condition["Cutting Properties"]["name"] == cond:
                    h = int(condition["Cutting Properties"]["deepCuth"])
                    break  

            # h = float(f"{base_name.split('h')[1].split('_g')[0]}")
            means_min = [frame_info[1] for frame_info in group_results]
            means_max = [frame_info[2] for frame_info in group_results]

        # If no value is found, set the averages to 0 to avoid generating an error.
        if not means_min or not means_max:
            CCR = 1
            CSR = 1
        else:
            CCR = np.mean(means_max)/h
            CSR = np.mean(means_max)/np.mean(means_min)


        self.chip_datas[base_name] = {"Chip Compression Ratio (CCR)": CCR, "Chip Segmentatio Ratio (CSR)": CSR}

