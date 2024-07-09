
def calcular_area_rectángulo(ancho,alto):
    area=ancho*alto
    return area

def calcular_perímetro_rectángulo(ancho,alto):
    perímetro=2*ancho+2*alto
    return perímetro

def mostrar_resultados(area,perímetro):
    print('el area del rectángulo es',area)
    print('el perímetro del rectángulo es ',perímetro)

ancho=12
alto=10

area=calcular_area_rectángulo(ancho,alto)
perímetro=calcular_perímetro_rectángulo(ancho,alto)

mostrar_resultados(area,perímetro)

#otro tipo de funciones son las lambda

incremento=lambda x:x+1

print('\n prueba de funciones tipo lambda')
suma_=incremento(3)
print(suma_)

texto_simple=lambda name,last_name: f'Full name is {name} {last_name}'

texto_escrito=texto_simple('juan','masmela')
print(texto_escrito)

#las funciones pueden ser anidadas 
print('funciones anidadas')
def sumita_(x):
    return x+1

def sumota_(x,funct):
    return x + funct(x)

resultado=sumota_(2,sumita_)
print(resultado)