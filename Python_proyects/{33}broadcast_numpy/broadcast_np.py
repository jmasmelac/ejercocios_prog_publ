import numpy as np

precios=np.array([100,200,300])
descuento=np.array([0.1])
ap_descuento=precios*descuento
print(ap_descuento)
print("\n")

precios2=np.random.randint(100,500,size=(3,3))
print(precios2)
print("\n suma por fila")
costo_mas=np.array([1,2,3])
precios_final=precios2+costo_mas
print(precios_final)
print("\n")

array=np.array([1,2,3,4,5])
print(np.all(array>0))#verifica todos   
print(np.any(array>5))#verifica alguno
print("\n")

array_a=np.array([1,2,3])
array_b=np.array([4,5,6])
concatenar_=np.concatenate((array_a,array_b))
print(concatenar_)
print("stack vertical")
stacked_=np.stack((array_a,array_b))
print(stacked_)
stacked_h=np.hstack((array_a,array_b))
print(stacked_h)

split_array=np.split(stacked_h,3)
print(split_array)