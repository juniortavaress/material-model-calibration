import matplotlib.pyplot as plt
import os

class ExcelUtils():
    @staticmethod
    def create_forces_graphs(df):
        """
        Generates and saves force-related graphs using Matplotlib.

        Args:
            df (pd.DataFrame): DataFrame containing the data for the charts.
            sheet_name (str): Name to be used for the saved image file.
        """
        sheet_name = "Forces"
        print("DF FORCES: ", df.head())
        # Criar a figura
        plt.figure(figsize=(8, 5))

        # Plotar os dados
        plt.plot(df.iloc[:, 0], df.iloc[:, 1], label="Cutting Force Fc [N]", linewidth=1.5)
        plt.plot(df.iloc[:, 0], df.iloc[:, 2], label="Normal Cutting Force FcN [N]", linewidth=1.5)

        # Configurar títulos e legendas
        plt.title(sheet_name, fontsize=14)
        plt.xlabel("Time t [ms]", fontsize=11)
        plt.ylabel("Force Component Fi [N]", fontsize=11)
        plt.legend(fontsize=11)
        plt.grid(True)

        # Salvar a imagem no diretório atual
        image_path = os.path.join(os.getcwd(), f"{sheet_name}.png")
        plt.savefig(image_path, dpi=300, bbox_inches="tight")

        # Fechar a figura para evitar consumo de memória
        plt.close()

        print(f"Graph saved as {image_path}")


    @staticmethod
    def create_temp_graps(df):
        """
        Generates and saves temperature-related graphs using Matplotlib.

        Args:
            df (pd.DataFrame): DataFrame containing the data for the charts.
            sheet_name (str): Name to be used for the saved image files.
        """
        print("DF TEMP: ", df.head())
        # Directory to save the images
        sheet_name = "Temp"
        save_path = os.getcwd()

        # Chart 1: Temperature vs. Penetration Depth
        plt.figure(figsize=(8, 5))
        plt.plot(df.iloc[:, 0], df.iloc[:, 1], label="Temperature at the last frame", linewidth=1.5)
        plt.plot(df.iloc[:, 0], df.iloc[:, 2], label="Maximum temperature", linewidth=1.5)

        plt.title(sheet_name, fontsize=14)
        plt.xlabel("Penetration Depth [µm]", fontsize=11)
        plt.ylabel("Temperature T [°C]", fontsize=11)
        plt.legend(fontsize=11)
        plt.grid(True)

        image_path1 = os.path.join(save_path, f"{sheet_name}_penetration_vs_temp.png")
        plt.savefig(image_path1, dpi=300, bbox_inches="tight")
        plt.close()

        # Chart 2: Temperature at Node vs. Time
        plt.figure(figsize=(8, 5))
        plt.plot(df.iloc[:, 3], df.iloc[:, 4], label="Temperature at Node 1", linewidth=1.5)

        plt.title(sheet_name, fontsize=14)
        plt.xlabel("Time t [ms]", fontsize=11)
        plt.ylabel("Temperature at Node 1 [°C]", fontsize=11)
        plt.legend(fontsize=11)
        plt.grid(True)

        image_path2 = os.path.join(save_path, f"{sheet_name}_time_vs_temp.png")
        plt.savefig(image_path2, dpi=300, bbox_inches="tight")
        plt.close()

        print(f"Graphs saved as {image_path1} and {image_path2}")
