def cont_palabras (texto_):
    texto_=texto_.lower()#pasa a minúscula
    import string # importa la librería de string
    texto_=texto_.translate(str.maketrans("", "", string.punctuation))# elimina los signos de puntuación
    palabras_ = texto_.split()#divide el texto en palabras
    conteo={}#el diccionario
    for palabra in palabras_:#contador de palabras
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    
    return conteo


texto_ejemplo = input("Dame el texto que deses que analice para ver la frecuencia de las palabras -> \n")
resultado = cont_palabras(texto_ejemplo)
print(resultado)