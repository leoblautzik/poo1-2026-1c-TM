import unittest

from juego_estrategia import Soldado, Caballero


class TestJuegoDeEstrategia(unittest.TestCase):
    def test_puede_atacar(self):
        rambo = Soldado(0)
        conan = Soldado(0)
        self.assertTrue(rambo.puede_atacar(conan))
        self.assertTrue(conan.puede_atacar(rambo))
        self.assertFalse(conan.puede_atacar(conan))

    def test_atacar_hasta_quedarse_sin_energia(self):
        rambo = Soldado(0)
        conan = Soldado(0)
        for _ in range(10):
            rambo.atacar(conan)
        self.assertFalse(rambo.puede_atacar(conan))

    def test_atacar_hasta_matar(self):
        rambo = Soldado(0)
        conan = Soldado(0)
        for _ in range(10):
            rambo.atacar(conan)
        self.assertFalse(rambo.puede_atacar(conan))
        rambo.recibir_racion_agua()
        self.assertTrue(rambo.puede_atacar(conan))
        for _ in range(10):
            rambo.atacar(conan)
        self.assertTrue(conan.esta_muerto())

    def test_caballero_ataca_hasta_caballo_rebelde(self):
        lancelot = Caballero(1)
        rambo = Soldado(0)
        for _ in range(3):
            lancelot.atacar(rambo)
        self.assertFalse(lancelot.puede_atacar(rambo))
        self.assertTrue(lancelot._caballo.esta_rebelde())
        lancelot._caballo.recibir_racion_agua()
        self.assertFalse(lancelot._caballo.esta_rebelde())
        self.assertTrue(lancelot.puede_atacar(rambo))


if __name__ == "__main__":
    unittest.main()
