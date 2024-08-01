#ojo con la forma en la que se abren los archivos, puede incurrir en errores 

with open('Python_proyects/{27}lectura_archivos/texto.txt','r+') as archivo:
    for line in archivo:
        print(line)
    archivo.write('hola yo te edite\n')# tener en cuenta como queda el archivo después de la edición
    archivo.write('hola yo te edite otra ves\n')
