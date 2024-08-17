import numpy as np

months = np.array(['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio','Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])
product_A = np.array([150, 200, 250, 300, 220, 210, 180, 190, 230, 240, 280, 300])
product_B = np.array([180, 210, 230, 250, 270, 260, 240, 250, 270, 290, 310, 330])
product_C = np.array([200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420])
# se necesita ver todos los aspectos como:
# ventas de cada producto total
media_A = np.mean(product_A)
suma_A = np.sum(product_A)
media_B = np.mean(product_B)
suma_B = np.sum(product_B)
media_C = np.mean(product_C)
suma_C = np.sum(product_C)

media_A=round(media_A,3)
media_B=round(media_B,3)
media_C=round(media_C,3)

print(f"Media de ventas Producto A: {media_A}")
print(f"Suma de ventas Producto A: {suma_A}")
print(f"Media de ventas Producto B: {media_B}")
print(f"Suma de ventas Producto B: {suma_B}")
print(f"Media de ventas Producto C: {media_C}")
print(f"Suma de ventas Producto C: {suma_C}","\n")

#distribución por meses

total_ventas_por_mes = product_A+product_B+product_C
print(f"el total de ventas de los meses es {total_ventas_por_mes}")

promedio_ventas_productos = np.array([media_A, media_B, media_C])
print("el promedio de ventas por productos es ",promedio_ventas_productos)

encontrar_posición = lambda valor, array: np.where(array == valor)[0][0] if valor in array else None
valor_mayor_ventas = max(total_ventas_por_mes)
valor_menor_ventas = min(total_ventas_por_mes)
pos_mes_mas_ventas=encontrar_posición(valor_mayor_ventas,total_ventas_por_mes)
pos_mes_menos_ventas=encontrar_posición(valor_menor_ventas,total_ventas_por_mes)


print("el mes con mayor ventas es :",months[pos_mes_mas_ventas],"\n","el mes con menor ventas es :",months[pos_mes_menos_ventas])
#operaciones con numpy

print("\n")

ventas_matrix = np.array([product_A, product_B, product_C])
ventas_reshaped = ventas_matrix.reshape(3, 4, 3)# arreglo tridimensional
ventas_transposed = ventas_matrix.T

print("Ventas Matrix:\n", ventas_matrix)
print("Ventas Transposed:\n", ventas_transposed)
print("Ventas Reshaped (3, 4, 3):\n", ventas_reshaped)# arreglo tridimensional


print("\n")
# Invertir arrays y aplanar matrices
ventas_inverted = ventas_matrix[:, ::-1]
ventas_flattened = ventas_matrix.flatten()

print("Ventas Invertidas:\n", ventas_inverted)
print("Ventas Aplanadas:\n", ventas_flattened)

print("\n")
# elementos únicos y sus conteos
unique_ventas, counts_ventas = np.unique(ventas_flattened, return_counts=True)
print("Elementos únicos en las ventas:", unique_ventas)
print("Conteos de elementos únicos en las ventas:", counts_ventas)

# Indexation y slicing
# Seleccionar ventas del primer trimestre
ventas_primer_trimestre = ventas_matrix[:, :3]
print("Ventas del primer trimestre:\n", ventas_primer_trimestre)

# Indexación booleana para seleccionar meses con ventas totales superiores a 800
meses_altas_ventas = months[total_ventas_por_mes > 800]
ventas_altas = total_ventas_por_mes[total_ventas_por_mes > 800]
print("Meses con ventas totales superiores a 800:", meses_altas_ventas)
print("Ventas totales superiores a 800:", ventas_altas)

# Selección avanzada
indices = [0, 2, 4, 6, 8, 10]
ventas_indices_seleccionados = ventas_matrix[:, indices]
print("Ventas en meses seleccionados:\n", ventas_indices_seleccionados)