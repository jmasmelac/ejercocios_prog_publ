import functools
numbers=[1,2,3,4,5]
result=functools.reduce(lambda contador, item:contador+item,numbers)
#toma como argumento un conjunto de valores (lista, tupla, o cualquier iterable) y lo "reduce" a un único valor. dependerá de la función
#la función toma el primer argumento de la función lambda como el acumulador y segundo como el iterable
print(result)

# lo que esta pasando por detrás es lo siguiente:

def accu(contador_,item_):
    print(contador_,' cont')
    print(item_,' item')
    return contador_+item_

result2=functools.reduce(accu,numbers)
print(result2,' result2')