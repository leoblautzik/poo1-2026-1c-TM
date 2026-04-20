import unittest
from warnings import warn
from cuenta import CajaDeAhorro


class TestCuentasBancariasCajaDeAhorro(unittest.TestCase):
    def test_creacion(self):
        ca = CajaDeAhorro(12345678)
        self.assertEqual(0, ca.saldo)

    def test_depositar(self):
        ca = CajaDeAhorro(12345678)
        ca.depositar(100000.00)
        self.assertEqual(100000.00, ca.saldo)

    def test_retirar_todo(self):
        ca = CajaDeAhorro(12345678)
        ca.depositar(100000.00)
        ca.retirar(100000.00)
        self.assertEqual(0.00, ca.saldo)

    def test_retirar_no_alcanza(self):
        ca = CajaDeAhorro(12345678)
        ca.depositar(100000.00)

        with self.assertRaises(ValueError):
            ca.retirar(100001.00)

        self.assertEqual(100000, ca.saldo)


if __name__ == "__main__":
    unittest.main()
