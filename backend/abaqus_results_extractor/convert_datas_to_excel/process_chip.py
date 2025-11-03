import os
import logging
import alphashape
import numpy as np
from scipy.signal import find_peaks

from shapely.geometry import Polygon, MultiPolygon
from backend.abaqus_results_extractor.convert_datas_to_excel.chip_datas import ManagerChipDatasAndImage

class ChipProcessor():
    def __init__(self, main):
        self.main = main
        self.file_groups = {}
        self.results_summary = {}

        
    def process_file(self, filename: str) -> dict:
        """
        Process all OBJ files within a given simulation folder.

        For each OBJ file, computes chip thickness statistics, groups results,
        generates plots for specific frames, and saves points data to an Excel file.

        Args:
            filename (str): Name of the simulation folder inside obj_input_dir.

        Returns:
            dict: A dictionary grouping processed file results.
        """
        create_image_and_datas = True
        obj_folder = os.path.join(self.main.obj_path, filename)
 
        for file in os.listdir(obj_folder):
            file_path = os.path.join(obj_folder, file)
            base_name = '_'.join(file.split('_')[:-1])    
            chip_info = self._process_obj_file(file_path, base_name)

            if chip_info == {}:
                self.results_summary[base_name] = {"Chip Compression Ratio (CCR)": 1, "Chip Segmentatio Ratio (CSR)": 1}
            else:
                self._calculate_results_and_save()
            
            # Create and save chip figure and datas
            if create_image_and_datas and len(chip_info.get("min_distances", [])) > 0 and len(chip_info.get("peaks", [])) > 0 and len(chip_info.get("valleys", [])) > 0 and len(chip_info.get("sides", [])) > 0:
                create_image_and_datas = ManagerChipDatasAndImage.get_datas_and_figures(self, base_name, file, chip_info["min_distances"], chip_info["peaks"], chip_info["valleys"], chip_info["sides"], chip_info["points"])
            return self.results_summary


    def _process_obj_file(self, file_path: str, base_name: str) -> dict:
        """
            Processes a single .OBJ file containing 2D chip geometry to extract relevant geometric statistics.

            Main steps:
                1. Count the number of non-empty lines in the file.
                2. Load 2D points representing the chip geometry and construct an alpha shape (concave hull) to outline the chip.
                3. Identify and separate the chip sides based on the shape.
                4. Compute local chip thickness and detect peaks and valleys in the thickness profile.
                5. Calculate the absolute minimum and maximum thickness values (in microns).
                6. Save statistics for this file group, if both min and max values exist.
                7. Calculate CSR and CCR.

            Args:
                file_path (str): Full path to the .OBJ file.
                base_name (str): A unique identifier used to group file statistics.

            Returns:
                tuple: (
                    min_distances (np.ndarray): Array of local thickness values,
                    peaks (np.ndarray): Indices of detected peaks (local maxima),
                    valleys (np.ndarray): Indices of detected valleys (local minima),
                    sides (list): List of arrays for the four chip sides,
                    points (np.ndarray): Original 2D points loaded from the .OBJ file
                )
        """
        # STEP 1 
        num_lines = self._count_lines_until_empty(file_path)

        # STEP 2
        points = self._load_obj_points(file_path, num_lines)
        alpha_shape = self._find_valid_alphashape(points)

        if alpha_shape is None or alpha_shape.is_empty:
            logging.error("Pontos inválidos ou insuficientes no arquivo: %s", file_path)
            return {} 
    
        # STEP 3 
        contour_points, ymin, ymax = self._sort_contour_points(alpha_shape)
        lower_chip_side = contour_points[contour_points[:, 1] == ymin]
        upper_chip_side = self._get_chip_side_02(contour_points, ymax, ymin) 
        left_segmented_chip_side = self._get_chip_side_03(contour_points, lower_chip_side, upper_chip_side, ymin, ymax)
        right_smooth_chip_side = self._get_chip_side_04(upper_chip_side, contour_points, lower_chip_side)
        sides = [lower_chip_side, upper_chip_side, left_segmented_chip_side, right_smooth_chip_side]

        # STEP 4
        min_distances = self._calculate_min_distances(left_segmented_chip_side, right_smooth_chip_side)
        peaks, _ = find_peaks(min_distances)
        valleys, _ = find_peaks(-min_distances)

        # STEP 5
        absolute_maximum = np.max(min_distances[peaks]) * 1000  if len(peaks) > 0 else None
        absolut_minimum = np.min(min_distances[valleys]) * 1000  if len(valleys) > 0 else None
        
        # STEP 6
        if base_name not in self.file_groups:
            self.file_groups[base_name] = []

        if absolut_minimum and absolute_maximum:
            self.file_groups[base_name].append((file_path, absolut_minimum, absolute_maximum))

        return {"min_distances": min_distances, "peaks": peaks, "valleys": valleys, "sides": sides, "points": points, "absolute_minimum": absolut_minimum, "absolute_maximum": absolute_maximum, }
    

    @staticmethod
    def _count_lines_until_empty(file_path: str) -> int:
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


    @staticmethod
    def _load_obj_points(file_path: str, num_lines: int) -> np.ndarray:
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


    @staticmethod
    def _find_valid_alphashape(points: np.ndarray, alpha: float = 150, step_size: float = 0.005) -> Polygon:
        """
        Attempts to compute a valid alpha shape (concave hull) for the given 2D points.
        If the resulting shape is a MultiPolygon (invalid for this context), it filters 
        points incrementally by removing those with the smallest x-values until a valid 
        single Polygon is found or no points remain.

        Args:
            points (np.ndarray): Array of 2D points.
            alpha (float, optional): Alpha parameter controlling the concavity of the shape. Defaults to 150.
            step_size (float, optional): Incremental threshold to filter points on the x-axis when invalid shape occurs. Defaults to 0.005.

        Returns:
            Polygon: Valid alpha shape polygon.

        Raises:
            ValueError: If no valid alpha shape can be found after filtering all points.
        """
        iteration = 0
        while True:
            try:
                logging.disable(logging.WARNING) # Silence warnings temporarily
                alpha_shape = alphashape.alphashape(points, alpha)
                logging.disable(logging.NOTSET) # Re-enable logging
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
                
                
    @staticmethod
    def _sort_contour_points(alpha_shape: Polygon) -> tuple[np.ndarray, float, float]:
        """
        Sorts the contour points from the alpha shape's exterior ring, ensuring the correct 
        order and identifies the minimum and maximum y-values.

        Args:
            alpha_shape (Polygon): The alpha shape polygon.

        Returns:
            tuple:
                np.ndarray: Sorted contour points as Nx2 array.
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


    @staticmethod
    def _get_chip_side_02(contour_points: np.ndarray, ymax: float, ymin: float) -> np.ndarray:
        """
        Extracts the upper chip side from contour points using vertical and horizontal segments.

        Args:
            contour_points (np.ndarray): Nx2 array of contour points.
            ymax (float): Maximum y-value in contour points.
            ymin (float): Minimum y-value in contour points.

        Returns:
            np.ndarray: Points representing the upper chip side.
        """
        upper_chip_side = [] 
        vertical_line = ChipProcessor._find_vertical_lines(contour_points)
        vertical_line = np.array(vertical_line, dtype=object).squeeze()
        horizontal_lines = ChipProcessor._find_horizontal_lines(contour_points, ymin)

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
            pass
            # traceback.print_exc()
        return upper_chip_side


    @staticmethod
    def _get_chip_side_03(contour_points: np.ndarray, lower_chip_side: np.ndarray, upper_chip_side: np.ndarray, ymin: float, ymax: float) -> np.ndarray:
        """
        Extracts the left segmented chip side by connecting the lower and upper chip sides.

        Args:
            contour_points (np.ndarray): Nx2 array of contour points.
            lower_chip_side (np.ndarray): Points of the lower chip side.
            upper_chip_side (np.ndarray): Points of the upper chip side.
            ymin (float): Minimum y-value in contour points.
            ymax (float): Maximum y-value in contour points.

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


    @staticmethod
    def _get_chip_side_04(upper_chip_side: np.ndarray,contour_points: np.ndarray,lower_chip_side: np.ndarray) -> np.ndarray:
        """
        Extracts the right smooth chip side by connecting the upper and lower chip sides.

        Args:
            upper_chip_side (np.ndarray): Points of the upper chip side.
            contour_points (np.ndarray): Nx2 array of contour points.
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


    @staticmethod
    def _find_vertical_lines(contour_points: np.ndarray) -> np.ndarray:
        """
        Identifies vertical lines in the contour points.

        Args:
            contour_points (np.ndarray): Nx2 array of contour points.

        Returns:
            list or np.ndarray: List of vertical lines, each represented as an array of points.
                                If vertical lines exist, returns a vertically stacked np.ndarray of all points.
                                Otherwise, returns an empty list.
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


    @staticmethod
    def _find_horizontal_lines(contour_points: np.ndarray, ymin: float) -> np.ndarray:
        """
        Identifies horizontal lines in the contour points excluding the minimum y-value line.

        Args:
            contour_points (np.ndarray): Nx2 array of contour points.
            ymin (float): Minimum y-value in contour points to exclude.

        Returns:
            List[np.ndarray]: List of horizontal lines, each as an array of points with the same y-value.
        """
        horizontal_lines = []
        unique_y = np.unique(contour_points[:, 1])  # All unique y-coordinates

        for y in unique_y:
            if y != ymin:  # Exclude ymin
                horizontal_line = contour_points[contour_points[:, 1] == y]
                if len(horizontal_line) >= 3:  # At least 3 points required
                    horizontal_lines.append(horizontal_line)
        return horizontal_lines
    

    @staticmethod
    def _calculate_min_distances(curve1: np.ndarray, curve2: np.ndarray) -> np.ndarray:
        """
        Calculates the minimal Euclidean distances from each point in curve1 
        to the closest point in curve2, excluding distances involving the 
        first or last points of curve2.

        Args:
            curve1 (np.ndarray): Array of points representing the first curve.
            curve2 (np.ndarray): Array of points representing the second curve.

        Returns:
            np.ndarray: Array of minimal distances for each point in curve1, 
                        filtered to exclude those matching the first or last point of curve2.
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


    def _calculate_results_and_save(self):
        """
        Calculates the Chip Compression Ratio (CCR) and Chip Segmentation Ratio (CSR)
        for each file group based on the loaded project information, then stores the
        results in the instance attribute `results_summary`.

        Returns:
            Dict[str, Dict[str, Optional[float]]]: Dictionary where keys are base file names 
            and values are dictionaries containing CCR and CSR metrics (which can be None).
        """
        response = self.main.supabase.table("conditions").select("*").eq("project_id", self.main.project_id).execute()
        db_conditions = {}
        if response.data:
            for cond in response.data:
                db_conditions[cond["name"]] = cond
        
        for base_name, group_results in self.file_groups.items():
            cond = base_name.split("_")[1]

            if cond in db_conditions:
                h = float(db_conditions[cond].get("deepcuth", 0))

            means_min = [frame_info[1] for frame_info in group_results if frame_info[1] is not None]
            means_max = [frame_info[2] for frame_info in group_results if frame_info[2] is not None]

            # If no value is found, set the averages to 0 to avoid generating an error.
            if means_max and means_min and np.mean(means_min) != 0:
                CCR = np.mean(means_max)/h
                CSR = np.mean(means_max)/np.mean(means_min)
            elif means_max and (not means_min or np.mean(means_min)) != 0:
                CCR = np.mean(means_max)/h
                CSR = 1
            else:
                CCR = 1
                CSR = 1

            self.results_summary[base_name] = {"Chip Compression Ratio (CCR)": CCR, "Chip Segmentatio Ratio (CSR)": CSR}

