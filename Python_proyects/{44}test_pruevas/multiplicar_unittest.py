# Código a probar
def multiplicar(a, b):
    return a * b

# Pruebas unitarias
import unittest

class TestMultiplicacion(unittest.TestCase):
    
    def test_multiplicar_positivos(self):
        """Prueba: Multiplicación de dos números positivos"""
        self.assertEqual(multiplicar(3, 4), 12)  # 3 * 4 = 12
    
    def test_multiplicar_negativos(self):
        """Prueba: Multiplicación de dos números negativos"""
        self.assertEqual(multiplicar(-3, -4), 12)  # -3 * -4 = 12
    
    def test_multiplicar_cero(self):
        """Prueba: Multiplicación con cero"""
        self.assertEqual(multiplicar(0, 10), 0)  # 0 * 10 = 0

    def test_multiplicar_negativo_positivo(self):
        """Prueba: Multiplicación de un número negativo por uno positivo"""
        self.assertEqual(multiplicar(-3, 4), -12)

if __name__ == "__main__":
    unittest.main(verbosity=2)  # Activa el modo verbose
