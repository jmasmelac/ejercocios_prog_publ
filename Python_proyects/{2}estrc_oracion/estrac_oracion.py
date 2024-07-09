#muestra un conjunto de caracteres provenientes de una frase
frase_=input("ingrese una frase: ")#la frase
pos_init=int(input("ingrese la posición donde empieza a leer: "))#la posición inicial 
pos_fini=int(input("ingrese la posición donde termina de leer: "))#la posición final
print(frase_[pos_init-1:pos_fini])#resultado, le resto 1 por como se cuenta