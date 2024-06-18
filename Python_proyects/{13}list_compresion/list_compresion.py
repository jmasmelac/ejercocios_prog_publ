#como se generan listas mas cortas y fáciles de leer

#forma clásica
números=[]
for element in range (1,10):
    números.append(element)
print(números)

#forma abreviada, el i puede ser cualquier variable

numbers_=[i for i in range(1,10)]
print(numbers_)

#otra forma para generar valores es operandolos en esa linea
numbers_=[i-3 for i in range(1,10)]
print(numbers_)

#para el caso de que se dese preguntar la forma tradicional es 

números=[]
for element in range (1,10):
    if element%2 == 0:
     números.append(element)
print(números)

#para la abreviación

numbers_=[i-3 for i in range(1,10) if i%2==0]
print(numbers_)

#caso
numbers = [35, 16, 10, 34, 37, 25]

even_numbers = []
for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)
print('v1 =>', even_numbers)

# Ahora usando List Comprehension 👇
even_numbers_v2 = [i for i in numbers if i%2==0]

print('v2 =>', even_numbers_v2)