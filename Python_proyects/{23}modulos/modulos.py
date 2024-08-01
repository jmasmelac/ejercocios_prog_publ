#los módulos son lo análogo al llamado de librerías,  estos se hace con la sentencia import

import sys
print(sys.path)#imprime las direcciones de los lugares donde se compila el proyecto, el .py, python3 la lib y package
#lista

import re   #librería de excreciones regulares
text = 'Mi numero de teléfono es 311 123 121, el código del país es 57, mi numero de la suerte 3'
result = re.findall('[0-9]+', text)
#Esta expresión regular busca lo indicado dentro de [ ] 
print(result)

import time     # librería de tiempo
timestamp = time.time() 
#hora actual en formato de computadora
print(timestamp) 
local = time.localtime()
#Indica la hora local
result = time.asctime(local) 
#Transforma el formato de hora
print(result)

import collections  #librería para manejar listas
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)
#Devuelve un diccionario con el número de veces que se repite un item dentro de un elemento (frecuencia)
print(counter)

import mi_libreria
def run():
    keys, values = mi_libreria.get_population()
    #print(keys.values)
    print(keys,values)

#si deseo compilar esto por aparte pero que la función si haga algo se hace lo siguiente
if __name__ == '__modulos__': #ojo con el nombre del archivo
    run()