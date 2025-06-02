
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class FacesGenerator():
    def __init__(self):
        super(FacesGenerator, self).__init__()

    def call_faces(self, geometry):
        if geometry == 'Eulerian':
            faces = FacesGenerator.eulerian_and_chip_plate_datas(self, 'Eulerian', 0, 0, 0)
            FacesGenerator.create_eulerian_partition(self, self.ax_geometry)
        elif geometry == 'ChipPlate':
            faces = FacesGenerator.eulerian_and_chip_plate_datas(self, 'ChipPlate', 0, 0, 0)
        elif geometry == 'Tool':
            faces = FacesGenerator.tool_datas(self, geometry)
        elif geometry == 'Assembly':
            faces = FacesGenerator.eulerian_and_chip_plate_datas(self, 'Eulerian', 0, 0, 0)
            FacesGenerator.create_eulerian_partition(self, self.ax_geometry)
            self.ax_geometry.add_collection3d(Poly3DCollection(faces, facecolors='#48bca6', linewidths=0.8, edgecolors='black', alpha=0.2))
            faces = FacesGenerator.eulerian_and_chip_plate_datas(self, 'ChipPlate', self.xChipPlatePosition, 0, self.zChipPlatePosition)
            self.ax_geometry.add_collection3d(Poly3DCollection(faces, facecolors='black', linewidth=1, edgecolors='black', alpha=1))
            faces = FacesGenerator.tool_datas(self, geometry)
            self.ax_geometry.add_collection3d(Poly3DCollection(faces, facecolors='#01dcdc', linewidth=0.5, edgecolors='black', alpha=1))
        return faces


    def eulerian_and_chip_plate_datas(self, fig, x, y, z):
        geometry = [self.ui.chipWidth, self.ui.chipTrickness, self.ui.chipHeight] if fig == 'ChipPlate' else [self.ui.eulerianWidth, self.ui.eulerianTrickness, self.ui.eulerianHeight]
        vertices_combinations = [[0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4], [2, 3, 7, 6], [1, 2, 6, 5], [4, 7, 3, 0]]
        faces = FacesGenerator.geometry_datas(self, geometry, vertices_combinations, x, y, z, 0)
        return faces


    def geometry_datas(self, geometry, vertices_combinations, x, y, z, page):
        Width = float(geometry[0].text())
        Trickness = float(geometry[1].text())
        Height = float(geometry[2].text())
        vertices_position = [[0 + x, 0 + y, 0 + z], [Width + x, 0 + y, 0 + z],
                             [Width + x, Trickness + y, 0 + z], [0 + x, Trickness + y, 0 + z],
                             [0 + x, 0 + y, Height + z], [Width + x, 0 + y, Height + z],
                             [Width + x, Trickness + y, Height + z], [0 + x, Trickness + y, Height + z]]
        faces = FacesGenerator.get_faces(self, vertices_position, vertices_combinations)
        return faces


    def tool_datas(self, page):
        clearanceFaceDimension = float(self.ui.toolClearanceDimension.text())
        rakeFaceDimension = float(self.ui.toolRakeDimension.text())
        Trickness = float(self.ui.toolTrickness.text())
        left_angle_rad = np.radians(float(self.ui.toolRakeAngle.text()))
        bottom_angle_rad = np.radians(float(self.ui.toolClearanceAngle.text()))

        vertices_combinations = [[0, 1, 3, 2], [4, 5, 7, 6], [0, 1, 5, 4], [2, 3, 6, 7], [0, 2, 6, 4], [1, 3, 7, 5]]

        if page == "Tool":
            tool_vertices = [[0, 0, 0],[0, 0, Trickness],
                        [clearanceFaceDimension*np.cos(bottom_angle_rad), clearanceFaceDimension*np.sin(bottom_angle_rad), 0],
                        [clearanceFaceDimension*np.cos(bottom_angle_rad), clearanceFaceDimension*np.sin(bottom_angle_rad), Trickness],
                        [rakeFaceDimension*np.sin(left_angle_rad), rakeFaceDimension*np.cos(left_angle_rad), 0],
                        [rakeFaceDimension*np.sin(left_angle_rad), rakeFaceDimension*np.cos(left_angle_rad), Trickness],
                        [clearanceFaceDimension*np.cos(bottom_angle_rad), rakeFaceDimension*np.cos(left_angle_rad), 0],
                        [clearanceFaceDimension*np.cos(bottom_angle_rad), rakeFaceDimension*np.cos(left_angle_rad), Trickness]]
        else:
            x = sorted([float(self.ui.eulerianPartitionX1.text()), float(self.ui.eulerianPartitionX2.text()), float(self.ui.eulerianPartitionX3.text()), float(self.ui.eulerianPartitionX4.text())])[2]
            z = sorted([float(self.ui.eulerianPartitionY1.text()), float(self.ui.eulerianPartitionY2.text()), float(self.ui.eulerianPartitionY3.text()), float(self.ui.eulerianPartitionY4.text())], reverse=True)[1]
            feed = float(self.ui.feed.text())
            tool_vertices = [
                [0 + x, 0, 0 + z - feed],
                [0 + x, Trickness, 0 + z - feed],
                [clearanceFaceDimension * np.cos(bottom_angle_rad) + x, 0, clearanceFaceDimension * np.sin(bottom_angle_rad) + z - feed],
                [clearanceFaceDimension * np.cos(bottom_angle_rad) + x, Trickness, clearanceFaceDimension * np.sin(bottom_angle_rad) + z - feed],
                [rakeFaceDimension * np.sin(left_angle_rad) + x, 0, rakeFaceDimension * np.cos(left_angle_rad) + z - feed],
                [rakeFaceDimension * np.sin(left_angle_rad) + x, Trickness, rakeFaceDimension * np.cos(left_angle_rad) + z - feed],
                [clearanceFaceDimension * np.cos(bottom_angle_rad) + x, 0, rakeFaceDimension * np.cos(left_angle_rad) + z - feed],
                [clearanceFaceDimension * np.cos(bottom_angle_rad) + x, Trickness, rakeFaceDimension * np.cos(left_angle_rad) + z - feed]]

        tool_faces = FacesGenerator.get_faces(self, tool_vertices, vertices_combinations)
        return tool_faces


    def get_faces(self, vertices, vertex_combinations):
        faces = []
        for vertex_set in vertex_combinations:
            face = [vertices[j] for j in vertex_set]
            faces.append(face)
        return faces


    def create_eulerian_partition(self, axis):
        x_values = [float(self.ui.eulerianPartitionX1.text()), float(self.ui.eulerianPartitionX2.text()), float(self.ui.eulerianPartitionX3.text()), float(self.ui.eulerianPartitionX4.text())]
        y_values = [float(self.ui.eulerianPartitionY1.text()), float(self.ui.eulerianPartitionY2.text()), float(self.ui.eulerianPartitionY3.text()), float(self.ui.eulerianPartitionY4.text())]

        for x_val in x_values:
            axis.plot([x_val, x_val], [0, 0], [0, float(self.ui.eulerianHeight.text())], 'w-')
            axis.plot([x_val, x_val], [float(self.ui.eulerianTrickness.text()), float(self.ui.eulerianTrickness.text())], [0, float(self.ui.eulerianHeight.text())], 'w-')
            axis.plot([x_val, x_val], [0, float(self.ui.eulerianTrickness.text())], [0, 0], 'w-')
            axis.plot([x_val, x_val], [0, float(self.ui.eulerianTrickness.text())], [float(self.ui.eulerianHeight.text()), float(self.ui.eulerianHeight.text())], 'w-')

        for y_val in y_values:
            axis.plot([0, 0], [0, float(self.ui.eulerianTrickness.text())], [y_val, y_val], 'w-')
            axis.plot([float(self.ui.eulerianWidth.text()), float(self.ui.eulerianWidth.text())], [0, float(self.ui.eulerianTrickness.text())], [y_val, y_val], 'w-')
            axis.plot([0, float(self.ui.eulerianWidth.text())], [0, 0], [y_val, y_val], 'w-')
            axis.plot([0, float(self.ui.eulerianWidth.text())], [float(self.ui.eulerianTrickness.text()), float(self.ui.eulerianTrickness.text())], [y_val, y_val], 'w-')












