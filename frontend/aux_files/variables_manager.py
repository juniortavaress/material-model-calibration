import os
import yaml
from PySide6.QtWidgets import QFileDialog


class ManagerVariables:
    def print_paths(self):
        if len(self.__dict__) > 10:
            print("\n===========================\nVARIABLES MAIN CLASS\n")
            for attr, value in list(self.__dict__.items())[10:]:
                print(f"{attr}: {value}")
            print("\n===========================\n")
