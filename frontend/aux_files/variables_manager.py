class ManagerVariables:
    """Class responsible for managing and printing variables."""

    def print_paths(self):
        """Prints the variables of the main class"""
        if len(self.__dict__) > 10:
            print("\n===========================")
            print("\nVARIABLES MAIN CLASS\n")

            for attr, value in list(self.__dict__.items())[10:]:
                print(f"{attr}: {value}")

            print("\n===========================\n")
