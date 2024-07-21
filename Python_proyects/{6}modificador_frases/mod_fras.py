#modificador de frases 
frase=input("dame la frase que desees que modifique -> ")
print("la palabra python esta en la frase? ","python" in frase)                          #busca en un arreglo de caracteres
print("el numero de caracteres son: ",len(frase))                                        #tamaño de un arreglo
print("todo en mayúsculas ",frase.upper())                                               #pone todo en mayúscula
print("todo en minúsculas",frase.lower())                                                #pone todo en minúscula
print("empieza por mayúscula",frase.capitalize())                                        #empieza por mayúscula
print("cada palabra empieza en mayúscula", frase.title())                                #empieza por mayúscula todas las palabras
print("cuenta cuantas vees aparece la a",frase.count("a"))                               #cuenta cuantas veces aparece un carácter
print("presto cambio",frase.swapcase())                                                  #cambia mayúscula a minúscula y minúscula a mayúscula
print("empieza por 'el' ? ",frase.startswith("el"))                                      #verifica si una cadena de caracteres empieza por algo en especifico
print("termina por 'el' ? ",frase.endswith("el"))                                        #verifica si una cadena de caracteres termina por algo en especifico
print("la cosa mas asquerosa que vas a leer ",frase.replace('o','e'))                    #remplaza por lo que desees
print("el texto son dígitos? ",frase.isdigit())                                          #son dígitos?
splash=frase.split()
print("almacena las palabras en una lista ",splash)                                      #el split almacena una cadena de palabras por palabra