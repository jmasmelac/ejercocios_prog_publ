import numpy as np

array=np.array([10,20,30,40,50])
print(array[2])
print(array[-2])
print(array[0:2])#donde empieza y cuantos espacios recorre
print("\n")

print("arreglo de booleanos a partir de la comparación \n")
bool_index= array > 25
print(bool_index)
print(type(bool_index))
print("\n")

index_=[2,3,4,0]
print(array[index_])
print("\n")

array_=np.random.randint(1,10,size=(3,3))
print(array_)
print("\nposición 0,2 =",array_[0,2])
print("\ncorte de posición \n",array_[0:2,0:2])