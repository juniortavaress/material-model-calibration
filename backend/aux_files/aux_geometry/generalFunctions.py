
import json
class AuxFunctions():
    def __init__(self):
        super(AuxFunctions, self).__init__()


    # Display a warning message in the provided label
    def warning(self, label_warning=None, message=None):
        if label_warning:
            label_warning.show
            label_warning.setText(message)
            QTimer.singleShot(3000, lambda: label_warning.setText(""))
            self.ui.saveButton.setEnabled(False)


    # Clean the specified folder and create it if it doesn't exist
    def clean_and_create_folder(self, path):
        try:
            for file in os.listdir(path):
                pathFile = os.path.join(path, file)
                os.remove(pathFile)
        except FileNotFoundError:
            os.makedirs(path)
        except PermissionError as e:
            print(f"Permission error: {e}. (AuxFiles\generalFunctions.py -> clean_and_create_folder)")


    # Save data to a JSON file
    def save_dict(pathName, data):
        with open(pathName, 'w') as json_file:
            json.dump(data, json_file, indent=4)






