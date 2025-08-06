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
        self.log_directory = os.getenv("LOG_DIRECTORY", ".")
        self.odb_processing = os.getenv("ODB_DIRECTORY", ".")
        self.obj_path = os.getenv("OBJ_DIRECTORY", ".")
        self.current_iteration = int(os.getenv("CUR_ITERATION"))

        self.log_file = os.path.join(self.log_directory, "debug_chip.txt")
        with open(self.log_file, "w") as f:
            f.write("=== Chip Extraction Log ===\n")
            f.write("ODB path: {}\n".format(self.odb_processing))
            f.write("OBJ path: {}\n".format(self.obj_path))
            f.write("Current Iteration: {}\n\n".format(self.current_iteration))

        self._log("=== Processing Files ===")
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


    def _create_viewport(self, odb_file_path):
        """
        Creates and returns a new viewport for the specified ODB file.

        Args:
            odb_file_path (str): Full path to the ODB file.

        Returns:
            viewport: Abaqus viewport object.
        """
        viewport = session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=200, height=100)
        viewport.makeCurrent()
        viewport.maximize()
        viewport.setValues(displayedObject=session.openOdb(name=odb_file_path))
        return viewport


    def _get_frames_to_analyze(self, odb_file_path):
        """
        Selects the last 5 frames (or fewer) from the last step of the analysis.

        Args:
            odb_file_path (str): Full path to the ODB file.

        Returns:
            tuple: frame indices, step name, and assembly instances.
        """
        odb = session.odbs[odb_file_path]
        assembly = odb.rootAssembly.instances
        step_name = list(odb.steps.keys())[-1]
        step = odb.steps[step_name]
        total_frames = len(step.frames)

        frame_indices = range(max(0, total_frames - 5), total_frames)
        return frame_indices, step_name, assembly
    

    def _extract_frames(self, view, odb_file, obj_file_folder, odb_file_path):
        """
        Extracts geometry data from the last frames of the simulation and exports it as OBJ files.

        This method performs the following steps for each selected frame:
        - Sets the current frame in the viewport.
        - Applies a view cut (e.g., EVF_VOID) to focus on the region of interest.
        - Removes all part instances from the display.
        - Adds only the chip element set back to the view.
        - Sets the view orientation and exports the current viewport to an OBJ file.

        Args:
            view: Abaqus viewport object displaying the current ODB.
            odb_file (str): The filename of the ODB being processed.
            obj_file_folder (str): Directory path where the generated OBJ files should be saved.
            odb_file_path (str): Full path to the ODB file on disk.
        """
        frame_indices, step_name, assembly = self._get_frames_to_analyze(odb_file_path)
        for frame_index in frame_indices:
            obj_file_name = os.path.splitext(odb_file)[0] + '_Frame' + str(frame_index) + '.obj'
            obj_file_path = os.path.join(obj_file_folder, obj_file_name)

            # Step 4.1: Set the current frame and activate void cut view
            view.odbDisplay.setFrame(step=step_name, frame=frame_index)
            view.odbDisplay.setValues(viewCutNames=('EVF_VOID',), viewCut=ON)

            # Step 4.2: Remove all part instances from the view
            try:
                all_instances = tuple(assembly.keys())
                leaf_all = dgo.LeafFromPartInstance(partInstanceName=all_instances)
                view.odbDisplay.displayGroup.remove(leaf=leaf_all)
            except Exception as e:
                self._log("Warning removing instances leaves:" + str(e), level="error")
                self._log(traceback.format_exc(), level="error")

            # Step 4.3: Add only the chip element set back to the view
            try:
                eulerian_instance = assembly.items()
                chip_set = list(eulerian_instance[1][1].elementSets.keys())[0]
                element_set = '{0}.{1}'.format(eulerian_instance[1][0], chip_set)
                leaf_chipset = dgo.LeafFromElementSets(elementSets=(element_set, ))
                view.odbDisplay.displayGroup.add(leaf=leaf_chipset)
                view.view.setValues(session.views['Front'])
            except Exception as e:
                self._log("Error adding chip set on view" + str(frame_index) + ":" + str(e), level="error")
                self._log(traceback.format_exc(), level="error")
                
            # Step 4.4: Export current viewport to OBJ
            try:
                session.writeOBJFile(fileName=obj_file_path, canvasObjects=(view, ))
                self._log(" Saved OBJ: " + obj_file_name)
            except Exception as e:
                self._log("Error generating OBJ for frame" + str(frame_index) + ":" + str(e), level="error")
                self._log(traceback.format_exc(), level="error")


    def _process_odb(self):
        """
        Processes all ODB files in the specified directory:
        - Opens each ODB
        - Selects last analysis step frames
        - Extracts chip elements
        - Exports them as OBJ files
        """
        # Step 1: List all ODB files in the directory
        try:
            iteration_str = "it_" + str(self.current_iteration).zfill(2)
            odb_files = [file for file in os.listdir(self.odb_processing) if file.endswith(".odb") and iteration_str in file]
        except Exception as e:
            self._log("Failed to list files in" + self.odb_processing + ":" + str(e), level="error")
            self._log(traceback.format_exc(), level="error")
            return
        
        # Step 2: Process each ODB file
        for i, odb_file in enumerate(odb_files):
            self._log(("\n" if i > 0 else "") + "File: " + odb_file)
            odb_file_path = os.path.join(self.odb_processing, odb_file)
            obj_file_folder = os.path.join(self.obj_path, os.path.splitext(odb_file)[0])
            if not os.path.exists(obj_file_folder):
                os.makedirs(obj_file_folder)

            # Step 3: Open the ODB and create a viewport
            try:
                view = self._create_viewport(odb_file_path)
            except Exception as e:
                self._log("Failed to open or display ODB: " + odb_file_path, level="error")
                self._log(traceback.format_exc(), level="error")
                continue

            # Step 4: Extract frames and begin per-frame OBJ export
            try:
                self._extract_frames(view, odb_file, obj_file_folder, odb_file_path)
            except Exception as e:
                self._log("Failed to process ODB file: " + odb_file, level="error")
                self._log(traceback.format_exc(), level="error")
            finally:
                session.odbs[odb_file_path].close()


if __name__ == "__main__":
    ChipGeometryExporter()
    sys.exit()
