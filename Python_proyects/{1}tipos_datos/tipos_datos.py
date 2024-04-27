#variables numéricas
valor1 = 10
valor2 = 33
resultado=valor1+valor2
print("El resultado es : ",resultado)

valor1 -= 1
valor2 += 3
resultado=valor1+valor2
print("El resultado es : ",resultado)

#flotantes
float_1=3.33
float_2=6.66
print(float_1+float_2)
y=1.1+2.2               #ojo, con esta operación
print(y)
print(round(y,2))       #con la función round especificamos los decimales en un flotante y se puede operar

#caracteres y frases
Pablo= "Pablo angel"
miau="Mauricio guerrero"
print('el nombre del "maau" es ', miau)
print("el apodo de ",Pablo,"es el 'maricón'")
frase="el {} y el {} son dos pendejos que hacen videos en internet".format(Pablo,miau)
print(frase)
frase2=f"el {Pablo} y el {miau} se destacan por hacer pendejadas y hacer reír a la gente"
print(frase2)

#booleans
soltero=True
print("para la variable soltero ",type(soltero)," su valor es ",not soltero)

#listas
mi_lista = [1, 2, 3, 4, 5]

#tupla  elementos inmutables
mi_tupla = (1, 2, 3)

#conjuntos
mi_conjunto = {1, 2, 3}

#diccionario
mi_diccionario = {"nombre": "Juan", "edad": 30}

#transformar tipos
print(type(valor1)," ",type(Pablo), " ","pero yo quiero ver ",Pablo+" "+str(valor1))#le puse un espacio para leer mejor
print(f"el pendejo de {Pablo} tiene {valor1} años")
input_=input("dame un numero -> ")
print(type(input_))
input_10=int(input_)+10
print('le sume 10, y da ',input_10)