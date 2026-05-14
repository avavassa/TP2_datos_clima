

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


print("=== GISTEMP ===")
print(f"Anomalía promedio: {prom_g:.2f}°C")
print(f"Anomalía máxima:   {max_g:.2f}°C (año {anio_max_g})")
print(f"Anomalía mínima:   {min_g:.2f}°C (año {anio_min_g})")

print("
=== GCAG ===")
print(f"Anomalía promedio: {prom_c:.2f}°C")
print(f"Anomalía máxima:   {max_c:.2f}°C (año {anio_max_c})")
print(f"Anomalía mínima:   {min_c:.2f}°C (año {anio_min_c})")

# Guardamos los indicadores
with open("resultados/indicadores.txt", "w") as f:
    f.write("=== GISTEMP ===
")
    f.write(f"Anomalía promedio: {prom_g:.2f}°C
")
    f.write(f"Anomalía máxima:   {max_g:.2f}°C (año {anio_max_g})
")
    f.write(f"Anomalía mínima:   {min_g:.2f}°C (año {anio_min_g})
")
    f.write("
=== GCAG ===
")
    f.write(f"Anomalía promedio: {prom_c:.2f}°C
")
    f.write(f"Anomalía máxima:   {max_c:.2f}°C (año {anio_max_c})
")
    f.write(f"Anomalía mínima:   {min_c:.2f}°C (año {anio_min_c})
")
