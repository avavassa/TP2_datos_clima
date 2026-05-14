

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


# Separamos las fuentes
df_gistemp = df[df["Source"] == "GISTEMP"].sort_values("Year")
df_gcag = df[df["Source"] == "GCAG"].sort_values("Year")

# Indicadores GISTEMP
prom_g = df_gistemp["Mean"].mean()
max_g = df_gistemp["Mean"].max()
min_g = df_gistemp["Mean"].min()
anio_max_g = df_gistemp.loc[df_gistemp["Mean"].idxmax(), "Year"]
anio_min_g = df_gistemp.loc[df_gistemp["Mean"].idxmin(), "Year"]

# Indicadores GCAG
prom_c = df_gcag["Mean"].mean()
max_c = df_gcag["Mean"].max()
min_c = df_gcag["Mean"].min()
anio_max_c = df_gcag.loc[df_gcag["Mean"].idxmax(), "Year"]
anio_min_c = df_gcag.loc[df_gcag["Mean"].idxmin(), "Year"]

