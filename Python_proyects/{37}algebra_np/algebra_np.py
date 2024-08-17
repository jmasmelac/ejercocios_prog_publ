import numpy as np

A=np.array([[1,3],[2,4]])
B=np.array([[5,7],[6,8]])

suma_=A+B
print(A,"\n")
print(B,"\n")

print("suma\n")
print(suma_,"\n")


multiplicación=np.dot(A,B)
print("\n multiplicación \n")
print(multiplicación)

determinante_A=np.linalg.det(A)
inversa_A=np.linalg.inv(A)
print("\n determinante A\n")
print(determinante_A)
print("\n inversa A\n")
print(inversa_A)

#resolver sistema de ecuaciones ojo 
#para este caso "Ax = b"
b=np.array([9,11])

x=np.linalg.solve(A,b)
print("\n la solución a la ecuación 'Ax = b' donde b es 9 y 11 es \n")
print(x)