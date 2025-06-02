from backend.aux_files.aux_geometry.layout.graphLayout import GraphLayout

class AuxFunctions():
    def __init__(self):
        super(AuxFunctions, self).__init__()

    # Change the page view based on the provided page name
    def change_page_number(self, page):
        self.setMinimumSize(1500, 850)
        self.ui.pages.setCurrentIndex(page)
        GraphLayout.resize(self) if page != 0 else None

        if page == 1:
            self.ui.saveButton.setEnabled(False)
            self.ui.iterationButton.setEnabled(False)
            [self.ui.tabWidget.setTabIcon(value, QIcon()) for value in [0, 1, 2, 3]]


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


    # Open a dictionary or pickle file based on the provided type
    def open_dict(type, path):
        try:
            if type == 'plk':
                with open(path, 'rb') as f:
                    data = pickle.load(f)
            elif type == 'dict':
                with open(path, 'r') as file:
                    data = json.load(file)
            return data
        except FileNotFoundError as e:
            print(f"File {path} not found. (Results/resultsDatas.py -> get_graph")
            raise e


    # Save data to a JSON file
    def save_dict(pathName, data):
        with open(pathName, 'w') as json_file:
            json.dump(data, json_file, indent=4)


    # Manage threading for input simulation and results processing
    def thread_manager_for_inp_simulation_and_results(self, argument):
        self.worker = WorkerThread(self, self.ui, argument)

        # Checks if the thread is already running and stops it if necessary
        if self.thread and self.thread.isRunning():
            self.thread.quit()
            self.thread.wait()

        # Starts a new thread and connects relevant signals
        self.thread = QThread()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.thread_manager)
        self.thread.finished.connect(self.thread.quit)
        self.thread.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()


    # Clear the plot area and update the canvas
    def clean_plot_area(self, ax, canvas):
        try:
            ax.clear()
            ax.axis(False)
            canvas.draw()
        except Exception as e:
            print(f"Error clearing graph: {e} (Results/resultsDatas.py -> get_graph")





