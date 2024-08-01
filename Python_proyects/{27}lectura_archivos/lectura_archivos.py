# verificación de la ruta de trabajo
import os
print("Directorio de trabajo actual:", os.getcwd())

print("Archivos en el directorio:")
print(os.listdir())

# apertura de  archivos

#file=open('C:\\Users\\User\\Documents\\proyectos\\ejercicios_prog\\Python_proyects\\{27}lectura_archivos\\texto.txt')#funciona

file = open('Python_proyects/{27}lectura_archivos/texto.txt', 'r')#ojo donde se compila y a donde apunta el compilador al momento de ejecutar un script
#print(file.read())#lee todo
print("solo lee una linea", file.readline())#salta de linea en linea

for line in file:
    print (line)

file.close()

with open('Python_proyects/{27}lectura_archivos/texto.txt') as archivo:# apertura y cierre (with)
    for line in archivo:
        print(line)

#edición de archivos
