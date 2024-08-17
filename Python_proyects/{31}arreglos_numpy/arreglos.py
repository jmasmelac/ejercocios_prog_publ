import numpy as np

array=np.array([[1,2,3],[4,5,6]])
print("indica las dimensiones: ",array.ndim)
print("indica el tamaño de cada dimension: ",array.shape)
print("indica el tipo de dato de la matrix: ",array.dtype)

z=np.array(3,dtype=np.uint8)
print("entero de 8 bits ",z,"\n")

double_array=np.array([1,2,3],dtype='d')
print("se pasaron a flotantes: \n",double_array,"\n")

z=z.astype(np.float16)
print("se paso a float ",z,"\n")

sum=np.sum(array)
print("suma del array ",sum,"\n")

mean=np.mean(array)
print("media del array ",mean,"\n")

std=np.std(array)
print("desviación estándar del array",std,"\n")