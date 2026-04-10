import unittest
from nota import Nota


class NotaTest(unittest.TestCase):
    def test_oabtener_valor(self):
        nota = Nota(4)
        self.assertEqual(4, nota.valor)

    def test_es_mayor_que_4_esta_aprobada(self):
        nota = Nota(5)
        self.assertTrue(nota.aprobado())
