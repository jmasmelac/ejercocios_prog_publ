# Paso 1: Definir la función
def calcular_cuadrado(numero):
    # Usamos assert para validar que la entrada sea un número no negativo.
    assert isinstance(numero, (int, float)), "El valor debe ser un número"  # Verifica que sea un número
    assert numero >= 0, "El número debe ser no negativo"  # Verifica que sea no negativo
    
    # Si las condiciones anteriores son válidas, se calcula el cuadrado.
    return numero ** 2

# Paso 2: Probar la función con datos válidos
resultado = calcular_cuadrado(4)  # Este debería funcionar correctamente
print(f"El cuadrado de 4 es: {resultado}")  # Salida esperada: El cuadrado de 4 es: 16

resultado = calcular_cuadrado(-1)
print(f"El cuadrado de -1 es: {resultado}")  # Salida esperada: Error: El número debe ser no negativo

# Paso 3: Probar la función con datos inválidos
try:
    resultado = calcular_cuadrado(-5)  # Esto debería generar un error de aserción
except AssertionError as e:
    print(f"Error: {e}")  # Salida esperada: Error: El número debe ser no negativo

# Paso 4: Probar con una entrada no numérica
try:
    resultado = calcular_cuadrado("texto")  # Esto también debería generar un error
except AssertionError as e:
    print(f"Error: {e}")  # Salida esperada: Error: El valor debe ser un número
