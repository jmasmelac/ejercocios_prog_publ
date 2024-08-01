# los iterables clásicos
for i in range(1,11):
    print('iterable clásico',i)

rango=range(1,11)
print('rango',rango)

iterable_=iter(range(1,11))
print('rango',iterable_)#imprime la dirección de memoria donde se almacenan los valores de la iteración
print(next(iterable_))#la función next toma un valor del rango y lo imprime, en este caso el primero
print(next(iterable_))# si se ejecuta lo mismo el next continua con los elementos de forma secuencial
#si se sigue iterando hasta el final del rango genera un error