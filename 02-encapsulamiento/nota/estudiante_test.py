import unittest

from estudiante import Estudiante


class EstudianteTest(unittest.TestCase):
    def test_aprobado_con_7(self):
        cacho = Estudiante("Cachito", 7)
        self.assertTrue(cacho.aprobado())
