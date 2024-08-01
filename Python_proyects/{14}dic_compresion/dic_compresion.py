#compresión de diccionarios

#forma clásica

dict={}
for i in range(1,10):
    dict[i]=i*2
print(dict)

import random
países=['col','bol','pru','gua','hon','sal']
población={}
for país in países:
    población[país]=random.randint(1,100)
print(población)

#forma abreviada

dict_2={i:i*2 for i in range(1,10)}
print(dict_2)

población_v2={país:random.randint(1,100) for país in países}
print(población_v2)

nombres={'calo','flor','rita','obdulio'}
edades={33,44,24,29}
print(list(zip(nombres,edades)))#la función zip se usa para iterar tuplas
dic_3={nombres:edades for (nombres,edades)in zip(nombres,edades)}
print(dic_3)

#para poner condiciones 

result={país:población for (país,población)in población_v2.items()if población>20}
print(result)


texto='hola mundo soy juan y me gusta el limon'
print(texto)
vocales={c:c.upper() for c in texto if c in 'aeiou'}
print (vocales)
vocales_num={c:texto.count(c) for c in texto if c in 'aeiou'}#cuenta el numero de vocales
print(vocales_num)