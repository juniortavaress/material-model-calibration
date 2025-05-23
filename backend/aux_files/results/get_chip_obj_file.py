import os
from abaqus import *
from abaqusConstants import *
from odbAccess import *
import displayGroupOdbToolset as dgo
import sys
import inspect
import traceback
import yaml

class GetChipMeasure():
    """
    Class to manage the extraction of chip data from ODB files and generate OBJ files.
    """
    def __init__(self):
        """
        Initialize the GetChipMeasure instance, process ODB files, and extract data.
        """
        self.software_config_path = os.path.join(os.getenv("SystemDrive", "C:") , "\MaterialOtimization", "config.yaml")
        with open(self.software_config_path, "r") as file:
            data = yaml.safe_load(file) 

        # Get and verify result directories.
        sys.path.append(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

        file_directory = data["odb_processing"]
        obj_directory = data["obj_path"]

        # Process ODB files
        self.process_odb(file_directory, obj_directory)


    def process_odb(self, file_directory, obj_directory):
        """
        Process each ODB file to extract chip data and generate OBJ files.

        Args:
            file_directory (str): Path to the directory containing ODB files.
            step_name (str): Name of the step to process.
            obj_directory (str): Path to the directory for saving OBJ files.
        """
        
        odb_files = [f for f in os.listdir(file_directory) if f.endswith('.odb')]

        for odb_file in odb_files:
            odb_file_path = os.path.join(file_directory, odb_file)

            # Open ODB
            try:
                view = session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=200, height=100)
                view.makeCurrent()
                view.maximize()
                view.setValues(displayedObject=session.openOdb(name=odb_file_path))
            except Exception as e:
                continue

            try:
                # Get the step and the total number of frames
                odb = session.odbs[odb_file_path]
                step_names = list(odb.steps.keys())
                step_name = step_names[-1]
                step = odb.steps[step_name]
                total_frames = len(step.frames)

                # Select the last 5 frames or fewer if total_frames < 5
                frame_indices = range(max(0, total_frames - 5), total_frames)

                for frame_index in frame_indices:
                    # frame = step.frames[frame_index]
                    obj_file_name = os.path.splitext(odb_file)[0] + '_Frame' + str(frame_index) + '.obj'
                    obj_file_path = os.path.join(obj_directory, obj_file_name)

                    # Activate section view
                    view.odbDisplay.setFrame(step=step_name, frame=frame_index)
                    view.odbDisplay.setValues(viewCutNames=('EVF_VOID',), viewCut=ON)

                    part_instances = list(odb.rootAssembly.instances.keys())

                    # Remove CHIPPLATE-1, TOOL-1 and EULERIAN-1
                    try:
                        leaf_chipplate = dgo.LeafFromPartInstance(partInstanceName=(str(part_instances[0]),))
                        view.odbDisplay.displayGroup.remove(leaf=leaf_chipplate)

                        leaf_tool = dgo.LeafFromPartInstance(partInstanceName=(str(part_instances[2]),))
                        view.odbDisplay.displayGroup.remove(leaf=leaf_tool)

                        leaf_eulerian = dgo.LeafFromPartInstance(partInstanceName=(str(part_instances[1]), ))
                        view.odbDisplay.displayGroup.remove(leaf=leaf_eulerian)
                    except Exception as e:
                        continue

                    # Add Chip Set, set Front View, and create OBJ
                    try:
                        eulerian_instance = odb.rootAssembly.instances.items()
                        chip_set = list(eulerian_instance[1][1].elementSets.keys())[0]
                        element_set = '{0}.{1}'.format(eulerian_instance[1][0], chip_set)
                        leaf_chipset = dgo.LeafFromElementSets(elementSets=(element_set, ))
                        view.odbDisplay.displayGroup.add(leaf=leaf_chipset)
                        view.view.setValues(session.views['Front'])
                        session.writeOBJFile(fileName=obj_file_path, canvasObjects=(view, ))
                    except Exception as e:
                        traceback.print_exc()

            except Exception as e:
                traceback.print_exc()
            finally:
                session.odbs[odb_file_path].close()


if __name__ == "__main__":
    GetChipMeasure()
    sys.exit()
