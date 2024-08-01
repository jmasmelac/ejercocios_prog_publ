#seleccionar cualquier país y visualizar sus datos
#los datos en un diccionario

import random #la importo con el fin de randomize el país

import matplotlib.pyplot as plt #para gráfica los datos

import csv  #lector de csv

def lector_csv(path):
    with open(path,'r') as csv_file:
        lector=csv.DictReader(csv_file,delimiter=',')
        datos_dict = {fila['Country']: fila for fila in lector}
        return datos_dict

datos_=lector_csv('Python_proyects/{29}ver_datos_pais/data_pais.csv')

país_aleatorio = random.choice(list(datos_.keys()))# Seleccionar un país al azar
datos_país = datos_[país_aleatorio]
print(f'País seleccionado: {país_aleatorio}')
print(datos_país)

años = ['1970', '1980', '1990', '2000', '2010', '2015', '2020', '2022']# Extraer datos de población
población = [int(datos_país[f'{anio} Population']) for anio in años]

países = list(datos_.keys())#lista de países
porcentajes = [float(datos_[país]['World Population Percentage']) for país in países]

# Crear subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Gráfica evolución de la población
axs[0].plot(años, población, marker='o')
axs[0].set_title(f'Evolución de la población - {país_aleatorio}')
axs[0].set_xlabel('Año')
axs[0].set_ylabel('Población')
axs[0].grid(True)

# Gráfica población mundial en diagrama de pie
axs[1].pie(porcentajes, labels=países, autopct='%1.1f%%', startangle=140)
axs[1].set_title(f'Distribución del porcentaje de la población mundial - {país_aleatorio} - {float(datos_[país_aleatorio]['World Population Percentage'])}%')

# Ajustar layout
plt.tight_layout()
plt.show()

