import unittest
from nota import Nota


class NotaTest(unittest.TestCase):
    def test_obtener_valor(self):
        nota1 = Nota(4)
        self.assertEqual(4, nota1.valor)

    def test_aprobado_con_4(self):
        nota = Nota(4)
        self.assertTrue(nota.aprobado())

    def test_promociona_con_7(self):
        nota_p = Nota(7)
        self.assertTrue(nota_p.promociona())

    def test_no_promociona_con_6(self):
        nota_p = Nota(6)
        self.assertFalse(nota_p.promociona())

    def test_reprobado_con_3(self):
        nota_3 = Nota(3)
        self.assertTrue(nota_3.desaprobado())
        self.assertFalse(nota_3.aprobado())

    def test_tiene_4_recupera_con_2(self):
        nota = Nota(4)
        nota.recuperar(2)
        self.assertEqual(4, nota.valor)
        self.assertTrue(nota.aprobado)
        self.assertFalse(nota.promociona())

    def test_tiene_2_recupera_con_8(self):
        nota = Nota(2)
        nota.recuperar(8)
        self.assertEqual(8, nota.valor)
        self.assertTrue(nota.aprobado)
        self.assertTrue(nota.promociona())
