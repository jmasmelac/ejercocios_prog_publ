import numpy as np
Survey_responses = np.array(["bueno", "excelente", "malo","bueno", "malo", "excelente","bueno", "bueno", "malo","excelente"] )

print("los elementos del conjunto son: \n ")
print(np.unique(Survey_responses))# muestra un arreglo con los elementos sin repetir
print("\n")

elementos_únicos,conteo=np.unique(Survey_responses,return_counts=True)
print(elementos_únicos)
print(conteo,"\n")

print("ojo con el siguiente error, se corrige creando copias")
array_x=np.arange(10)
copy_x=array_x[[1,2]]#la copia
view_y=array_x[1:3]
print(array_x)
print(view_y)
array_x[1:3]=[10,11]
print(array_x)
print(view_y)

print("\n")
array_x=np.arange(10)
print(array_x)
print(copy_x)
array_x[1:3]=[10,11]
print(array_x)
print(copy_x)