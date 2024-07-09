#el map sirve para transformar elementos de un arreglo y convertirlos en otro valor y almacenarlo en otro arreglo
números=[1,2,3,4,5]
números2=[]

#forma clásica
for i in números:
    números2.append(i*2)

print(números)
print(números2)

#uso del map

números2=list(map(lambda u:u*2,números))#el map solo se visualiza como una dirección de memoria, para verlo como una lista se pasa a una 

print(números2)

#uso con diccionarios

items =[
    {'product': 'shirt',
    'price':120},
    {'product': 'pants',
    'price':160},
    {'product': 'jacket',
    'price':205}
]

precios=list(map(lambda i:i['price'],items))
print(precios)

#añadir impuestos 

def add_impuestos(item):#función que calcula los impuestos
    #new_item=item.copy()  #esto arregla la modificación del original, creando otra variable
    item['taxes']=item['price']*0.19
    return item

new_tabla=list(map(add_impuestos,items))
print(new_tabla)
print(items)#importante, el map también modifico el original