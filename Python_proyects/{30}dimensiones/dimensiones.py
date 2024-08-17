import numpy as np

escalar=np.array(42)
print(type(escalar))
print(escalar)
print("escalar")

vector = np.array([30,29,35,31,33,36,42]) 
print(vector)
print("vector")

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]]) 
print(matrix)
print("matrix")

tensor = np.array([[1,2],[3,4],[5,6],[7,8]]) 
print(tensor)#los tensores son multi dimensionales
print("tensor")

array_arange = np.arange(10) 
print(array_arange)
print("vector de 10 elementos")

eye_matrix = np.eye(6) 
print(eye_matrix)
print("matrix identidad")

diag = np.diag([1,2,3,4,5,6,7]) 
print(diag)
print("matrix diagonal")

random = np.random.random((2,3)) 
print(random)
print("matrix random")