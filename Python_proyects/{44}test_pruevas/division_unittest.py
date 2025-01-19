# Código a probar
def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

# Pruebas unitarias
import unittest

class TestDivisiones(unittest.TestCase):
    
    def test_dividir_positivos(self):
        """Prueba: División de dos números positivos"""
        self.assertEqual(dividir(10, 2), 5)  # 10 / 2 = 5

    def test_dividir_negativos(self):
        """Prueba: División de dos números negativos"""
        self.assertEqual(dividir(-10, -2), 5)  # -10 / -2 = 5

    def test_dividir_por_cero(self):
        """Prueba: División por cero debe generar un error"""
        with self.assertRaises(ValueError):  # Se espera un ValueError
            dividir(10, 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)  # Activar modo verbose