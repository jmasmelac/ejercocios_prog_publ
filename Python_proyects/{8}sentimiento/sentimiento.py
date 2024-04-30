#ingresar una frase y analizar su sentimiento general
diccionario_sentimiento = {
    "amor": 1,
    "odio": -1,
    "feliz": 1,
    "triste": -1,
    "indiferente": 0,
    "maravilloso": 1,
    "horrible": -1,
    "increíble": 1,
    "pésimo": -1,
    "genial": 1,
    "terrible": -1,
    "extraordinario": 1,
    "deplorable": -1,
    "fantástico": 1,
    "lamentable": -1,
    "excelente": 1,
    "desastroso": -1,
    "impresionante": 1,
    "espantoso": -1,
    "fabuloso": 1,
    "nefasto": -1
}

frase=input("dame la frase que desees que verifique el sentimiento -> ")
frase=frase.lower()
palabras=frase.split()

sentiments = [] # lista donde se almacena los valores de los sentimientos

for palabra in palabras:
    if palabra in diccionario_sentimiento:
        sentiments.append(diccionario_sentimiento[palabra])

average_sentiment = sum(sentiments) / len(sentiments) # calcula el valor de sentimiento (un promedio)

print("El sentimiento promedio de la frase es: " + str(average_sentiment))