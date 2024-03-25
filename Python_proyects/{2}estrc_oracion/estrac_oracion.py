#muestra un conjunto de caracteres provenientes de una frase
frase_=input("ingrese una frase: ")#la frase
pos_init=int(input("ingrese la poscicion donde empiesa a leer: "))#la poscicion inicial 
pos_fini=int(input("ingrese la poscicion donde termina de leer: "))#la poscicion final
print(frase_[pos_init-1:pos_fini])#resultado, le resto 1 por como se cuenta