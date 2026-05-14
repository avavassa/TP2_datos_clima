

import urllib.request
import pandas as pd
import matplotlib.pyplot as plt

# Importar dataset

urllib.request.urlretrieve(
    "https://pkgstore.datahub.io/core/global-temp/annual_csv/data/a26b154688b061cdd04f1df36e4408be/annual_csv.csv",
    "datos/dataset.csv")
print("Dataset descargado correctamente")

# Cargamos el dataset

try:
    df = pd.read_csv("datos/dataset.csv")
    print("Dataset cargado correctamente")
except FileNotFoundError:
    print(f"Error: No se encontró el archivo en la ruta especificada.")
    print("Asegurate de que el archivo CSV esté dentro de la carpeta 'datos'.")
    exit()
