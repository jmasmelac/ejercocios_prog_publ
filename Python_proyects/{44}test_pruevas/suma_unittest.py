# Código a probar
def sumar(a, b):
    return a + b

# Prueba unitaria usando unittest
import unittest

class TestFunciones(unittest.TestCase):  # Creamos una clase que hereda de unittest.TestCase
    
    def test_sumar(self):
        # Probamos si la función sumar funciona correctamente
        self.assertEqual(sumar(2, 3), 5)  # 2 + 3 = 5
        self.assertEqual(sumar(-1, 1), 0)  # -1 + 1 = 0
        self.assertNotEqual(sumar(2, 2), 5)  # 2 + 2 != 5

# Ejecución de las pruebas
if __name__ == "__main__":
    unittest.main()
