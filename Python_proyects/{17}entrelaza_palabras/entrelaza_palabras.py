#este código entrelaza dos cadenas de caracteres (no se si ese es el nombre adecuado para esta operación)
#en que consiste: tomar dos cadenas de caracteres y hacer el siguiente ejercicio
#mesa
#paloma
#mpeaslaoma  <-- esta palabra surge de la sobre posición de la primera palabra con la segunda

palabra_1_=input("dame la primera palabra a entrelazar: \n ")
palabra_2_=input("dame la segunda palabra a entrelazar: \n ")
cont=1

tamaño=min(len(palabra_1_),len(palabra_2_))

palabra_1_=palabra_1_.lower()
palabra_2_=palabra_2_.lower()
palabra_3_=''

for i in range(tamaño):
    palabra_3_+=palabra_1_[i]+palabra_2_[i]

palabra_3_=palabra_3_+palabra_1_[tamaño:]+palabra_2_[tamaño:]#los dos puntos son para indicar que en esa posición en adelante se siguen poniendo caracteres

print(palabra_1_)
print(palabra_2_)
print(palabra_3_)
