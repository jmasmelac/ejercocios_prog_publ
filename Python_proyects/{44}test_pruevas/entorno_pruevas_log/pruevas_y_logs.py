# Importamos el módulo `unittest` para escribir y ejecutar pruebas unitarias
import unittest

# Importamos el módulo `logging` para generar archivos de registro (logs)
import logging

# Configuración del sistema de logs:
# - `filename`: Nombre del archivo donde se guardarán los logs (test_log.log).
# - `level`: Nivel de los mensajes a registrar (INFO y superiores).
# - `format`: Formato del mensaje log, que incluye la hora, nivel y mensaje.
logging.basicConfig(filename="test_log.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Definimos la función `suma`, que toma dos argumentos (a y b) y retorna su suma
def suma(a, b):
    return a + b

# Definimos una clase de pruebas unitarias que hereda de `unittest.TestCase`
class TestSuma(unittest.TestCase):
    
    # Método de prueba para la suma de números positivos
    def test_suma_positivos(self):
        # Ejecutamos la función `suma` con los valores 3 y 4
        resultado = suma(3, 4)
        # Comprobamos que el resultado sea igual a 7
        self.assertEqual(resultado, 7)
        # Registramos en el log que esta prueba pasó
        logging.info("Prueba suma de positivos: PASSED")
    
    # Método de prueba para la suma de números negativos
    def test_suma_negativos(self):
        # Ejecutamos la función `suma` con los valores -3 y -4
        resultado = suma(-3, -4)
        # Comprobamos que el resultado sea igual a -7
        self.assertEqual(resultado, -7)
        # Registramos en el log que esta prueba pasó
        logging.info("Prueba suma de negativos: PASSED")
    
    # Método de prueba para un caso que debería fallar
    def test_suma_error(self):
        # Ejecutamos la función `suma` con los valores 2 y 2
        resultado = suma(2, 2)
        # Intentamos verificar que el resultado sea igual a 5
        # (Esto generará un error porque 2 + 2 es igual a 4)
        try:
            self.assertEqual(resultado, 5)
        except AssertionError as e:  # Capturamos la excepción generada
            # Registramos en el log que esta prueba falló, con detalles del error
            logging.error("Prueba suma con error: FAILED - %s", e)

# Punto de entrada principal del script
# Si este archivo se ejecuta directamente, se ejecutan las pruebas unitarias
if __name__ == "__main__":
    unittest.main()  # Ejecuta todas las pruebas definidas en la clase TestSuma

