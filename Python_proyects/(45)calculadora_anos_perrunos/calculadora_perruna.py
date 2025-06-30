"""
código clásico de como se convierten años perrunos a años humanos.
"""
#dar la bienvenida al usuario
print("Bienvenido a la calculadora de años perrunos")
#validar las unidades de tiempo de la edad del perro
while True:
    unidad_tiempo = input("¿Qué unidad de tiempo quieres usar? (años escribe a / meses escribe m): ").strip().lower()# el strip() elimina los espacios al principio y al final de la cadena, y lower() convierte la cadena a minúsculas
    if unidad_tiempo in ['a', 'm']:
        break
    else:
        print("Unidad de tiempo no válida. Por favor, escribe 'a' para años o 'm' para meses.")

#validar la edad del perro
edad_perro = int(input("¿Cuántos años o meses tiene tu perro? "))
#convertir la edad del perro a años
if unidad_tiempo == 'm':
    edad_perro = edad_perro / 12  # convertir meses a años

#calcular la edad del perro en años humanos
match edad_perro:
    case x if x <= 0:
        print("La edad del perro no puede ser menor o igual a 0.")
    case x if x <= 1:
        edad_humana=edad_perro * 15 # primer año de vida del perro equivale a 15 años humanos
    case x if x <= 2:
        edad_humana = 15 + (edad_perro - 1) * 9 # segundo año de vida del perro equivale a 9 años humanos
    case x if x <= 3:
        edad_humana = 15 + 9 + (edad_perro - 2) * 5 # tercer año de vida del perro equivale a 5 años humanos
    case x if x > 3:
        edad_humana = 15 + 9 + 5 + (edad_perro - 3) * 4 # a partir del cuarto año de vida del perro, cada año equivale a 4 años humanos
# mostrar resultado si la edad es valida
if edad_perro > 0:
    print(f"La edad de tu perro en años humanos es: {edad_humana:.2f} años")  # .2f para mostrar dos decimales, el f en el print indica que es una cadena formateada (texto)