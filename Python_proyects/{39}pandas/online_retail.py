#datos tomados de https://www.kaggle.com/datasets/tunguz/online-retail 

import pandas as pd
ruta_archivo=r"Python_proyects\{39}pandas\Online_Retail.csv"
data_tienda=pd.read_csv(ruta_archivo,encoding='latin-1') #archivo CSV contiene caracteres que no pueden ser decodificados usando la codificación UTF-8.
print(data_tienda)
print(type(data_tienda))

"""
caso Excel
data_Excel = pd.read_excel(path)
"""
"""
caso json
data_json = pd.read_json(path)
"""

#exploración de los datos

columnas_nombres=data_tienda.columns #nombres de columnas
print(columnas_nombres)
# data_tienda.head()
# data_tienda.tail()

numero_filas,numero_columnas=data_tienda.shape
print("\nNumero de filas ",numero_filas," numero de columnas ",numero_columnas,"\n")

#para el caso de que desee ver mas especifico los datos de una columna 

ventas_diarias=data_tienda['Quantity']
print(ventas_diarias," \n ")

summary_=data_tienda.describe()
print(summary_," \n ")

valor_media=data_tienda.Quantity.mean()
print("el valor de la media Quantity es ",round(valor_media,3))

valor_mediana=data_tienda.Quantity.median()
print("el valor de la mediana Quantity es ",valor_mediana)

valor_suma=data_tienda.Quantity.sum()
print("el valor total Quantity es ",valor_suma)

valor_conteo_=data_tienda.Quantity.count()
print("el valor del conteo Quantity es ",valor_conteo_,"\n")

# para el caso de querer identificar filas en el conjunto de datos
# iloc y loc

primera_fila=data_tienda.iloc[0]
print(primera_fila)

primeras_filas=data_tienda.iloc[:5]
print(primeras_filas)

algunas_filas=data_tienda.iloc[:3,:2]
print(algunas_filas)

#limpieza de datos

missing_data=data_tienda.isna()
print(missing_data)# si el dato no esta disponible da true

contador_missing_data=data_tienda.isna().sum()
print(contador_missing_data)

#para este caso faltan datos en CustomerID y en Description 
"""
#esto elimina las filas con los datos faltantes
datos_perdidos= data_tienda.dropna()
print(datos_perdidos)
"""
#otra opción es rellenar los datos faltantes, esto se hace con
"""
# esto rellena los datos null vacíos,
relleno_datos_zero=data_tienda.fillna(0)
print(relleno_datos_zero)
"""
# con esto relleno lo que falta con 0 y lo cuento
relleno_datos_zero=data_tienda.fillna(0)
contador_datos_zero=relleno_datos_zero.isna().sum()
print(contador_datos_zero)
"""
en datos numéricos se puede rellenar con la media para no afectar la estadística

mean_unit_price = data_tienda['Unit-Price'].mean()
retail_data_filled_mean = data_tienda ['UnitPrice'].fillna(mean_unit_price)
print(retail_data_filled_mean)

"""
# lo siguiente son las operaciones en columnas