## los conjuntos se denotan con set , recordar que sus elementos no se repiten
set_countries = {'col','mex','bol','mex'}
print(set_countries)
print(type(set_countries))

set_numbers = {1,2,4,5,1}
print(set_numbers)

set_tipes = {1,'hola',True,13.3}## varios tipos de datos
print(set_tipes)

set_from_string =set('hola')
print(set_from_string)##imprime cada carácter

set_de_tupla = set(('abc','cbd','hij','abc'))
print(set_de_tupla)

numero_=[1,2,3,4,5,6,7,8,9,1,2,3]
set_numero_=set(numero_)
print(set_numero_)

## para modificarlos

##tamaños
print(len(set_countries))

##preguntar si esta
print('col'in set_countries)

#añadir
set_countries.add('pe')
set_countries.add('pe')##se añadió a drede
print(set_countries)

#actualizar

set_countries.update({'arg','sal','bol'})
print(set_countries)

#eliminar

set_countries.remove('sal')
print(set_countries)

set_countries.discard('mex')
print(set_countries)

set_de_tupla.clear()#limpia todo el conjunto
print(set_de_tupla)
print(len(set_de_tupla))

#operaciones entre conjuntos

set_a={'a','b','c','d'}
set_b={1,2,3,4,'d'}

set_c=set_a.union(set_b)#union
print(set_c)
print(set_a | set_b)

set_c=set_a.intersection(set_b)#intersección
print(set_c)
print(set_a & set_b)

set_c=set_a.difference(set_b)#diferencia
print(set_c)
print(set_a - set_b)

set_c=set_a.symmetric_difference(set_b)#diferencia simétrica
print(set_c)
print(set_a ^ set_b)