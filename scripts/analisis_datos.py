import urllib.request
import pandas as pd
import matplotlib.pyplot as plt

# Descarga el dataset directamente desde DataHub para garantizar la reproducibilidad
# del análisis sin depender de archivos locales que podrían no estar disponibles

urllib.request.urlretrieve(
    "https://pkgstore.datahub.io/core/global-temp/annual_csv/data/a26b154688b061cdd04f1df36e4408be/annual_csv.csv",
    "datos/dataset.csv")
print("Dataset descargado correctamente")

# Carga el dataset
# Usamos try-except para dar un mensaje claro al usuario si el archivo no existe
# y en ese caso se termina el programa con exit()

try:
    df = pd.read_csv("datos/dataset.csv")
    print("Dataset cargado correctamente")
except FileNotFoundError:
    print(f"Error: No se encontró el archivo en la ruta especificada.")
    print("Asegurate de que el archivo CSV esté dentro de la carpeta 'datos'.")
    exit()

# El dataset contiene dos fuentes independientes que miden la misma variable
# Las separamos para comparar ambas series sin mezclar datos de origen diferente

df_gistemp = df[df["Source"] == "GISTEMP"].sort_values("Year")
df_gcag = df[df["Source"] == "GCAG"].sort_values("Year")

# Los valores de "Mean" representan anomalías respecto al promedio 1951-1980,
# no temperaturas absolutas. Un valor positivo indica que ese año fue más
# cálido que el período de referencia.

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

print("\n=== GCAG ===")
print(f"Anomalía promedio: {prom_c:.2f}°C")
print(f"Anomalía máxima:   {max_c:.2f}°C (año {anio_max_c})")
print(f"Anomalía mínima:   {min_c:.2f}°C (año {anio_min_c})")

# Guardamos los indicadores en un archivo de texto para que queden disponibles
# en /resultados sin necesidad de volver a ejecutar el script
   

with open("resultados/indicadores.txt", "w") as f:
    f.write("=== GISTEMP ===\n")
    f.write(f"Anomalía promedio: {prom_g:.2f}°C\n")
    f.write(f"Anomalía máxima:   {max_g:.2f}°C (año {anio_max_g})\n")
    f.write(f"Anomalía mínima:   {min_g:.2f}°C (año {anio_min_g})\n")
    f.write("\n=== GCAG ===\n")
    f.write(f"Anomalía promedio: {prom_c:.2f}°C\n")
    f.write(f"Anomalía máxima:   {max_c:.2f}°C (año {anio_max_c})\n")
    f.write(f"Anomalía mínima:   {min_c:.2f}°C (año {anio_min_c})\n")


# Graficamos ambas fuentes en el mismo eje para facilitar la comparación visual.
# La línea punteada en y=0 marca el promedio de referencia histórico
# lo que permite ver claramente las anomalías.

plt.figure(figsize=(12, 5))
plt.plot(df_gistemp["Year"], df_gistemp["Mean"], color="steelblue", linewidth=1.5, label="GISTEMP")
plt.plot(df_gcag["Year"], df_gcag["Mean"], color="coral", linewidth=1.5, label="GCAG")
plt.axhline(0, color="gray", linestyle="--", linewidth=0.8)
plt.title("Evolución de la anomalía de temperatura global")
plt.xlabel("Año")
plt.ylabel("Anomalía de temperatura (°C)")
plt.legend()
plt.tight_layout()
plt.savefig("resultados/grafico_temperatura.png")
plt.show()
print("Gráfico guardado en /resultados")
