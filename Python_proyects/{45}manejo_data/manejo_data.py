print("Bienvenido al manejo de datos, variables y  en Python")
print("\n una variable en python almacena un objeto en ram")
print("\n ese valor se asigna a un espacio de memora donde esta el valor real")
edad=18
print("\n cuando yo asigno",edad," una vaariable esto solo es una referencia a la ubicacion real en memoria")
print("\n si yo cambio el valor de la variable esta se asigna a otra ubicacion en memoria")
print("\n miremos el id de la variable edad:",id(edad))
print("\n si asigno otro valor a la variable edad ->",edad+2)
edad=20
print("\n el id de la variable edad ahora es:",id(edad))
print("\n las variabels en python solo apuntan a una direccion, no al valor perce en ese espacio de memoria")
print("\n cuando se hace un cambio en una variable esta crea un valor en otra ubicacion de memoria")
print("\n si yo asigno una nueva variable el mismo valor , esta apuntara a la misma direccion")
otra_edad=edad
print("\n el id de la variable otra_edad es:",id(otra_edad))
print("\n python tiene una herramieta llamada garbage collector que se encarga de liberar espacio en memoria de variables no asignadas")
print("\n una variable es un nombre que referencia a un objeto en memoria")
# nombrar variables
print("\n las variables en python deben ser en minuscula separadas por un guion bajo")
print("\n mientras los nombres sean lo mas auto descriptivos mejor")
print("\n no poner simbolos especiales, ni empezar con numeros, ni las palabras reservadas")
# tipos de datos
print("\n los tipos de datos en python son:")
numero_ejemplo=10          # int
numero_flotante=10.5      # float   
texto_ejemplo="hola"      # str
booleano_ejemplo=True     # bool
print("\n - enteros (int) -> numeros sin decimales ",numero_ejemplo," ",type(numero_ejemplo))
print("\n - flotantes (float) -> numeros con decimales",numero_flotante," ",type(numero_flotante))
print("\n - cadenas de texto (str) -> texto entre comillas simples o dobles ",texto_ejemplo," ",type(texto_ejemplo)," estos son inmutables")
print("\n - booleanos (bool) -> True o False -> ",booleano_ejemplo," ",type(booleano_ejemplo))
print("\n  todo en python es un objeto, incluso los tipos de datos")
print("\n como todas las variables son objetos, podemos poner el . con al finalidad de usar los metodos corresponientes a ese tipo de dato")
