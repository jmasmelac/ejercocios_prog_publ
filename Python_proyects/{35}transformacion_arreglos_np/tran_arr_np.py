import numpy as np

matrix_=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix_)
print("\n")
print(matrix_.T)#el .t es la transpuesta
print("\n")

array_=np.arange(1,13)
redistribución_=array_.reshape(3,4)#3 filas 4 columnas
print(array_)
print(redistribución_)
print("\n")

al_revés_array=array_[::-1]
print(array_)
print(al_revés_array)
print("\n")

#flatering es el proceso de pasar de fila a columna

flat_matrix=matrix_.flatten()
print(flat_matrix)#paso de matrix a fila