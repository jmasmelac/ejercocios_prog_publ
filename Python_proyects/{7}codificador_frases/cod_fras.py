'''
Escribe un programa en Python que solicite al usuario ingresar un párrafo de texto. Luego, el programa debe realizar lo siguiente:

Contar el número de palabras en el párrafo.
Contar el número de veces que aparece la palabra "Python" en el párrafo.
Verificar si el párrafo comienza con la palabra "El".
Verificar si el párrafo termina con la palabra "mundo".
Convertir todas las palabras del párrafo a minúsculas.
Reemplazar todas las apariciones de "Python" por "Java" en el párrafo.
Mostrar el resultado de cada una de estas operaciones al usuario.
'''
frase=input("dame el párrafo que desees que modifique -> ")
print("en el párrafo hay ",frase.count(" ")+1," palabras")#se puede hacer con split()

print("el párrafo empieza por 'el'? ",frase.startswith("el"))
print("el párrafo termina por 'mundo'? ",frase.endswith("mundo"))
print("el párrafo en minúscula es: ",frase.lower())
print("el nuevo párrafo es: ",frase.replace('python','java'))
#El programador de python tiene que cambiar el mundo