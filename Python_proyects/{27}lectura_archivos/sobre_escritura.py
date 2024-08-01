
with open('Python_proyects/{27}lectura_archivos/texto.txt','w+') as archivo:#este permiso remplaza el contenido del documento
    for line in archivo:
        print(line)
    archivo.write('hola yo te edite\n')
    archivo.write('hola yo te edite otra ves\n')