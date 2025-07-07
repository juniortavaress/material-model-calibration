import numpy as np

from matplotlib.figure import Figure
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class GraphManager():
    def __init__(self):
        super(GraphManager, self).__init__()


    def canvas(self, figure=None):
        """
        Creates and displays a Matplotlib canvas in the Qt interface.

        Args:
            figure (matplotlib.figure.Figure, optional): A Matplotlib figure to be displayed. Defaults to None, which creates a blank canvas.
        """

        if figure is None:
            figure = Figure(figsize=(12, 8))

        new_canvas = FigureCanvas(figure)
        new_canvas.setStyleSheet("background: transparent;")
        new_canvas.figure.patch.set_facecolor('none')

        axes = new_canvas.figure.get_axes()
        if axes:
            ax = new_canvas.figure.get_axes()[0]
            ax.set_facecolor('none')


        # Adiciona o canvas ao layout
        layout = self.ui.plot_geometry_frame.layout()
        if layout is not None:
            for i in reversed(range(layout.count())):
                widget = layout.itemAt(i).widget()
                if widget is not None:
                    widget.deleteLater()

        layout.addWidget(new_canvas)
        new_canvas.draw()
        self.canvas = new_canvas

    def plot_3d_graph(self, geometry):
        """
        Generates and displays force-related graphs using Matplotlib.

        Args:
            filename (str): Name of the sheet in the Excel file.
        """

        # Create a new figure
        figure = Figure(figsize=(12, 8))
        ax = figure.add_subplot(111, projection='3d')
        ax.set_facecolor('none')

        if self.ui.tabWidget.currentIndex() == 3:
            partitions = sorted([float(self.ui.eulerianPartitionY1.text()), float(self.ui.eulerianPartitionY2.text()), float(self.ui.eulerianPartitionY3.text()), float(self.ui.eulerianPartitionY4.text())], reverse=True)[1]
            x = sorted([float(self.ui.eulerianPartitionX1.text()), float(self.ui.eulerianPartitionX2.text()), float(self.ui.eulerianPartitionX3.text()), float(self.ui.eulerianPartitionX4.text())])[2]
            self.ui.xTool.setText(str(x))
            self.ui.yTool.setText(str(partitions))
            self.xChipPlatePosition = x - float(self.ui.chipWidth.text()) - float(self.ui.fromTool.text())
            self.zChipPlatePosition = partitions + float(self.ui.overWorkpiece.text())

        # Geração das faces da geometria
        faces = GraphManager.call_faces(self, geometry, ax)
        alpha = 0.2 if geometry == 'Eulerian' else 1.0

        # Adiciona as faces ao gráfico 3D
        ax.add_collection3d(Poly3DCollection(faces, facecolors='#009c94', linewidths=1, edgecolors='white', alpha=alpha))

        GraphManager.axis_layout(self, geometry, ax, figure)

        # Customize axis appearance
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        GraphManager.canvas(self, figure)


    def axis_layout(self, geometry, axis, fig):
        if geometry == "ChipPlate":
            xlim = [0, float(self.ui.chipWidth.text())]
            ylim = [-0.1*float(self.ui.chipWidth.text()), 0.1*float(self.ui.chipWidth.text())]
            zlim = [-0.1*float(self.ui.chipWidth.text()), 0.1*float(self.ui.chipWidth.text())]
            elev, azim, boxAspect = [30, 40, [1, 1, 1]]

        elif geometry == "Eulerian":
            xlim = [-(float(self.ui.eulerianHeight.text())-float(self.ui.eulerianWidth.text()))/2, float(self.ui.eulerianWidth.text()) + (float(self.ui.eulerianHeight.text())-float(self.ui.eulerianWidth.text()))/2]
            ylim = [0, float(self.ui.eulerianHeight.text())]
            zlim = [0, float(self.ui.eulerianHeight.text())]
            elev, azim, boxAspect = [0, -90, [1, 1, 1]]

        elif geometry == "Tool":
            clearanceFaceDimension = float(self.ui.toolClearanceDimension.text())
            rakeFaceDimension = float(self.ui.toolRakeDimension.text())
            bottom_angle_rad = np.radians(float(self.ui.toolClearanceAngle.text()))
            space = (rakeFaceDimension*np.cos(bottom_angle_rad)-clearanceFaceDimension*np.cos(bottom_angle_rad))/2

            xlim = [-space, clearanceFaceDimension*np.cos(bottom_angle_rad)+space]
            ylim = [0, rakeFaceDimension*np.cos(bottom_angle_rad)]
            zlim = [-(rakeFaceDimension*np.cos(bottom_angle_rad)/10), (rakeFaceDimension*np.cos(bottom_angle_rad)/10)]
            elev, azim, boxAspect = [90, 270, [1, 1, 1]]

        elif geometry == "Assembly":
            xlim = [0.5, 6]
            ylim = [0.5, 6]
            zlim = [0.5, 6]
            elev, azim, boxAspect = [0, -90, [1, 1, 1]]

        axis.set_xlim(xlim)
        axis.set_ylim(ylim)
        axis.set_zlim(zlim)
        axis.set_axis_off()
        axis.view_init(elev=elev, azim=azim)
        axis.set_box_aspect(boxAspect)
        fig.tight_layout()


    def call_faces(self, geometry, ax):
        if geometry == 'Eulerian':
            faces = GraphManager.eulerian_and_chip_plate_datas(self, 'Eulerian', 0, 0, 0)
            GraphManager.create_eulerian_partition(self, ax)
        elif geometry == 'ChipPlate':
            faces = GraphManager.eulerian_and_chip_plate_datas(self, 'ChipPlate', 0, 0, 0)
        elif geometry == 'Tool':
            faces = GraphManager.tool_datas(self, geometry)
        elif geometry == 'Assembly':
            faces = GraphManager.eulerian_and_chip_plate_datas(self, 'Eulerian', 0, 0, 0)
            GraphManager.create_eulerian_partition(self, ax)
            ax.add_collection3d(Poly3DCollection(faces, facecolors='#48bca6', linewidths=0.8, edgecolors='black', alpha=0.2))
            faces = GraphManager.eulerian_and_chip_plate_datas(self, 'ChipPlate', self.xChipPlatePosition, 0, self.zChipPlatePosition)
            ax.add_collection3d(Poly3DCollection(faces, facecolors='black', linewidth=1, edgecolors='black', alpha=1))
            faces = GraphManager.tool_datas(self, geometry)
            ax.add_collection3d(Poly3DCollection(faces, facecolors='#01dcdc', linewidth=0.5, edgecolors='black', alpha=1))
        return faces


    def eulerian_and_chip_plate_datas(self, fig, x, y, z):
        geometry = [self.ui.chipWidth, self.ui.chipTrickness, self.ui.chipHeight] if fig == 'ChipPlate' else [self.ui.eulerianWidth, self.ui.eulerianTrickness, self.ui.eulerianHeight]
        vertices_combinations = [[0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4], [2, 3, 7, 6], [1, 2, 6, 5], [4, 7, 3, 0]]
        faces = GraphManager.geometry_datas(self, geometry, vertices_combinations, x, y, z, 0)
        return faces


    def geometry_datas(self, geometry, vertices_combinations, x, y, z, page):
        Width = float(geometry[0].text())
        Trickness = float(geometry[1].text())
        Height = float(geometry[2].text())
        vertices_position = [[0 + x, 0 + y, 0 + z], [Width + x, 0 + y, 0 + z],
                             [Width + x, Trickness + y, 0 + z], [0 + x, Trickness + y, 0 + z],
                             [0 + x, 0 + y, Height + z], [Width + x, 0 + y, Height + z],
                             [Width + x, Trickness + y, Height + z], [0 + x, Trickness + y, Height + z]]
        faces = GraphManager.get_faces(self, vertices_position, vertices_combinations)
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

        tool_faces = GraphManager.get_faces(self, tool_vertices, vertices_combinations)
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



