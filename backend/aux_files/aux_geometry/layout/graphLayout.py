import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

class GraphLayout():
    def __init__(self):
        super(GraphLayout, self).__init__()

    # Create the plot areas and set up the canvas.
    def create_plot_areas(self, plot_area, type=None):
        fig, ax = plt.subplots()
        ax.axis(False)
        ax = fig.add_subplot(111, projection='3d') if type == '3d' else fig.add_subplot(111)
        ax.set_axis_off()
        fig.set_facecolor((182/255, 182/255, 182/255))
        ax.set_facecolor((182/255, 182/255, 182/255))
        canvas = FigureCanvas(fig)
        canvas.setGeometry(plot_area.contentsRect())
        canvas.setParent(plot_area)
        return ax, fig, canvas


    # Resize the canvas based on the current page
    def resize(self):
        page_mappings = {1: (self.canvas_geometry, self.ax_geometry, self.ui.plot)}
        page_index = self.ui.pages.currentIndex()

        if page_index in page_mappings:
            canvas, axis, plot_area = page_mappings[page_index]
            size = plot_area.size()
            canvas.setGeometry(0, 0, size.width(), size.height())
            axis.figure.tight_layout()
            canvas.draw()


    # Set up the axis limits, view, and aspect ratio for the current page.
    def axis_layout(self, geometry):
        if geometry == "ChipPlate":
            xlim = [0, float(self.ui.chipWidth.text())]
            ylim = [-0.1*float(self.ui.chipWidth.text()), 0.1*float(self.ui.chipWidth.text())]
            zlim = [-0.1*float(self.ui.chipWidth.text()), 0.1*float(self.ui.chipWidth.text())]
            elev, azim, boxAspect = [30, 40, [1, 1, 1]]
            axis, fig, canvas = [self.ax_geometry, self.fig_geometry, self.canvas_geometry]

        elif geometry == "Eulerian":
            xlim = [-(float(self.ui.eulerianHeight.text())-float(self.ui.eulerianWidth.text()))/2, float(self.ui.eulerianWidth.text()) + (float(self.ui.eulerianHeight.text())-float(self.ui.eulerianWidth.text()))/2]
            ylim = [0, float(self.ui.eulerianHeight.text())]
            zlim = [0, float(self.ui.eulerianHeight.text())]
            elev, azim, boxAspect = [0, -90, [1, 1, 1]]
            axis, fig, canvas = [self.ax_geometry, self.fig_geometry, self.canvas_geometry]

        elif geometry == "Tool":
            clearanceFaceDimension = float(self.ui.toolClearanceDimension.text())
            rakeFaceDimension = float(self.ui.toolRakeDimension.text())
            bottom_angle_rad = np.radians(float(self.ui.toolClearanceAngle.text()))
            space = (rakeFaceDimension*np.cos(bottom_angle_rad)-clearanceFaceDimension*np.cos(bottom_angle_rad))/2

            xlim = [-space, clearanceFaceDimension*np.cos(bottom_angle_rad)+space]
            ylim = [0, rakeFaceDimension*np.cos(bottom_angle_rad)]
            zlim = [-(rakeFaceDimension*np.cos(bottom_angle_rad)/10), (rakeFaceDimension*np.cos(bottom_angle_rad)/10)]
            elev, azim, boxAspect = [90, 270, [1, 1, 1]]
            axis, fig, canvas = [self.ax_geometry, self.fig_geometry, self.canvas_geometry]

        elif geometry == "Assembly":
            xlim = [0.5, 6]
            ylim = [0.5, 6]
            zlim = [0.5, 6]
            elev, azim, boxAspect = [0, -90, [1, 1, 1]]
            axis, fig, canvas = [self.ax_geometry, self.fig_geometry, self.canvas_geometry]

        axis.set_xlim(xlim)
        axis.set_ylim(ylim)
        axis.set_zlim(zlim)
        axis.set_axis_off()
        axis.view_init(elev=elev, azim=azim)
        axis.set_box_aspect(boxAspect)
        fig.tight_layout()
        canvas.draw()



