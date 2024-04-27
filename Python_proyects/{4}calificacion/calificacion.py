#en función de la calificación se asigna una letra correspondiente
calificación_=int(input("Ingrese el valor de su calificación 0-100 -> "))
if calificación_<101 and calificación_> 89:
    print("su calificación es A")
elif calificación_<90 and calificación_ > 79:
    print("su calificación es B")
elif calificación_<80 and calificación_ > 69:
    print("su calificación es C")
elif calificación_<70:
    print("Reprobó, su calificación es F")
else:
    print("dato no valido")