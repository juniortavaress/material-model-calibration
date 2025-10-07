import os
import sys
import traceback
from abaqus import session
from abaqusConstants import ON
import displayGroupOdbToolset as dgo


class ChipGeometryExporter():
    """
    Extracts chip geometry from Abaqus ODB files and exports it as OBJ files.
    """

    def __init__(self):
        """
        Initializes environment variables and starts the ODB processing workflow.
        """
        self.obj_path = os.getenv("OBJ_DIRECTORY", ".")
        self.odb_file = os.getenv("ODB_FILE", "")
        self.log_file = os.path.join(os.getenv("LOG_DIRECTORY", "."), "debugg_chip.txt")

        self._log("=== Starting  Chip Geometry Extraction ===")
        self._process_odb()


    def _log(self, message, level=None):
        """
        Appends a message to the log file with optional severity.

        Args:
            message (str): Log message.
            level (str): Optional log level ('info' or 'error').
        """
        prefix = "[ERROR] " if level == "error" else ""
        with open(self.log_file, "a") as f:
            f.write(prefix + message + "\n")


    def _create_viewport(self, odb_path):
        """
        Creates and returns a new viewport for the specified ODB file.

        Args:
            odb_path (str): Full path to the ODB file.

        Returns:
            Viewport: Abaqus viewport object.
        """
        viewport = session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=200, height=100)
        viewport.makeCurrent()
        viewport.maximize()
        viewport.setValues(displayedObject=session.openOdb(name=odb_path))
        return viewport


    def _get_frames_to_analyze(self, odb_path):
        """
        Selects the last 5 frames (or fewer) from the last step of the analysis.

        Args:
            odb_path (str): Full path to the ODB file.

        Returns:
            tuple: Frame indices, step name, and assembly instances.
        """
        odb = session.odbs[odb_path]
        assembly = odb.rootAssembly.instances
        step_name = list(odb.steps.keys())[-1]
        step = odb.steps[step_name]
        total_frames = len(step.frames)
        frame_indices = range(max(0, total_frames - 5), total_frames)
        return frame_indices, step_name, assembly
    

    def _extract_frames(self, viewport, base_name, output_folder, odb_path):
        """
        Extracts chip geometry from selected frames and exports them as OBJ files.

        Args:
            viewport: Abaqus viewport object.
            base_name (str): Base name of the ODB file.
            odb_path (str): Full path to the ODB file.
            output_folder (str): Directory to save OBJ files.
        """
        frame_indices, step_name, assembly = self._get_frames_to_analyze(odb_path)
        for frame_index in frame_indices:
            obj_filename = base_name + '_Frame' + str(frame_index) + '.obj'
            obj_filepath = os.path.join(output_folder, obj_filename)

            try:
                viewport.odbDisplay.setFrame(step=step_name, frame=frame_index)
                viewport.odbDisplay.setValues(viewCutNames=('EVF_VOID',), viewCut=ON)
                all_instances = tuple(assembly.keys())
                leaf_all = dgo.LeafFromPartInstance(partInstanceName=all_instances)
                viewport.odbDisplay.displayGroup.remove(leaf=leaf_all)
            except Exception as e:
                self._log("Warning removing instances leaves:" + str(e), level="error")
                self._log(traceback.format_exc(), level="error")

            try:
                instance_items = assembly.items()
                chip_set_name  = list(instance_items[1][1].elementSets.keys())[0]
                element_set = '{0}.{1}'.format(instance_items[1][0], chip_set_name )
                leaf_chipset = dgo.LeafFromElementSets(elementSets=(element_set, ))
                viewport.odbDisplay.displayGroup.add(leaf=leaf_chipset)
                viewport.view.setValues(session.views['Front'])
            except Exception as e:
                self._log("Error adding chip set on view" + str(frame_index) + ":" + str(e), level="error")
                self._log(traceback.format_exc(), level="error")
                
            try:
                session.writeOBJFile(fileName=obj_filepath, canvasObjects=(viewport, ))
                self._log(" Saved OBJ: " + obj_filename)
            except Exception as e:
                self._log("Error generating OBJ for frame" + str(frame_index) + ":" + str(e), level="error")
                self._log(traceback.format_exc(), level="error")


    def _process_odb(self):
        """
        Processes the ODB file:
        - Opens the file
        - Creates a viewport
        - Extracts chip geometry from selected frames
        - Exports each frame as an OBJ file
        """
        base_name = os.path.splitext(os.path.basename(self.odb_file))[0]
        output_folder  = os.path.join(self.obj_path, base_name)

        self._log("Processing file: " + self.odb_file)

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        try:
            viewport  = self._create_viewport(self.odb_file)
        except Exception as e:
            self._log("Failed to open or display ODB: " + self.odb_file, level="error")
            self._log(traceback.format_exc(), level="error")
            
        try:
            self._extract_frames(viewport, base_name, output_folder, self.odb_file)
        except Exception as e:
            self._log("Failed to process ODB file: " + self.odb_file, level="error")
            self._log(traceback.format_exc(), level="error")
        finally:
            session.odbs[self.odb_file].close()


if __name__ == "__main__":
    ChipGeometryExporter()
    sys.exit()
