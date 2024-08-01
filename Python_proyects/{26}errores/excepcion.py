try: # el try except es una sentencia para saltarse errores
    print(0/0)
except ZeroDivisionError as error:
    print("error")

try: # 
    assert 1!=1, "uno no es igual a uno"
except AssertionError as error:
    print("error")


edad=10
try: # 
    if edad<18:
        raise Exception("no se permiten menores de edad")
except Exception as error:
    print("error")

print("dentro del try se pueden poner mas de un error y en los except el criterio del error")

def my_divide(a, b):
   # Escribe tu solución 👇
   try:
      result = a / b
      
   except ZeroDivisionError as error:
      result='No se puede dividir por 0'
   return result
    
response = my_divide(10, 2)
print(response) # 5

response = my_divide(10, 0)
print(response) # No se puede dividir por 0