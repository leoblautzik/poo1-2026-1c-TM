import unittest


from banco import Banco, CuentaCorriente, CajaDeAhorro


class TestCuentas(unittest.TestCase):
    def setUp(self):
        self.banco = Banco()
        self.caja = self.banco.abrirCajaDeAhorro(123)
        self.cc = self.banco.abrirCuentaCorriente(456, 1000)

    # -------------------------
    # CREACIÓN
    # -------------------------
    def test_creacion_caja_ahorro(self):
        self.assertEqual(self.caja.getSaldo(), 0)
        self.assertEqual(self.caja.dineroDisponible(), 0)

    def test_creacion_cuenta_corriente(self):
        self.assertEqual(self.cc.getSaldo(), 0)
        self.assertEqual(self.cc.dineroDisponible(), 1000)

    # -------------------------
    # DEPÓSITOS
    # -------------------------
    def test_deposito(self):
        self.caja.depositar(500)
        self.assertEqual(self.caja.getSaldo(), 500)

    def test_deposito_negativo(self):
        with self.assertRaises(Exception):
            self.caja.depositar(-100)

    # -------------------------
    # EXTRACCIONES
    # -------------------------
    def test_extraccion_caja_ok(self):
        self.caja.depositar(500)
        self.caja.retirar(200)
        self.assertEqual(self.caja.getSaldo(), 300)

    def test_extraccion_caja_sin_fondos(self):
        self.caja.depositar(100)
        with self.assertRaises(Exception):
            self.caja.retirar(200)

    def test_extraccion_cc_con_descubierto(self):
        self.cc.retirar(500)
        self.assertEqual(self.cc.getSaldo(), -500)

    def test_extraccion_cc_supera_descubierto(self):
        with self.assertRaises(Exception):
            self.cc.retirar(1500)

    # -------------------------
    # RESERVA (Caja de ahorro)
    # -------------------------
    def test_reserva_agregar(self):
        self.caja.depositar(1000)
        self.caja.agregar_reserva(300)

        self.assertEqual(self.caja.getSaldo(), 700)
        self.assertEqual(self.caja.dineroDisponible(), 1000)

    def test_reserva_quitar(self):
        self.caja.depositar(1000)
        self.caja.agregar_reserva(300)
        self.caja.quitar_reserva(200)

        self.assertEqual(self.caja.getSaldo(), 900)

    def test_reserva_insuficiente(self):
        self.caja.depositar(100)
        with self.assertRaises(Exception):
            self.caja.agregar_reserva(200)

    # -------------------------
    # DINERO DISPONIBLE
    # -------------------------
    def test_dinero_disponible_caja(self):
        self.caja.depositar(1000)
        self.caja.agregar_reserva(400)

        self.assertEqual(self.caja.dineroDisponible(), 1000)

    def test_dinero_disponible_cc(self):
        self.cc.retirar(300)
        self.assertEqual(self.cc.dineroDisponible(), 700)

    # -------------------------
    # TRANSFERENCIAS
    # -------------------------
    def test_transferencia_ok(self):
        self.caja.depositar(1000)
        self.caja.transferir(self.cc, 300)

        self.assertEqual(self.caja.getSaldo(), 700)
        self.assertEqual(self.cc.getSaldo(), 300)

    def test_transferencia_sin_fondos(self):
        with self.assertRaises(Exception):
            self.caja.transferir(self.cc, 100)

    # -------------------------
    # toString / str
    # -------------------------
    def test_to_string(self):
        s = str(self.caja)
        self.assertIn("123", s)

    # -------------------------
    # BANCO
    # -------------------------
    def test_total_descubierto(self):
        self.cc.retirar(500)
        self.assertEqual(self.banco.totalSaldoEnDescubierto(), -500)

    def test_total_descubierto_multiple(self):
        cc2 = self.banco.abrirCuentaCorriente(789, 1000)
        self.cc.retirar(300)
        cc2.retirar(200)

        self.assertEqual(self.banco.totalSaldoEnDescubierto(), -500)

    def test_listar_cuentas_ordenadas(self):
        self.caja.depositar(500)
        self.cc.retirar(200)

        cuentas = self.banco.listarCuentas()

        saldos = [c.getSaldo() for c in cuentas]
        self.assertEqual(saldos, sorted(saldos))


if __name__ == "__main__":
    unittest.main()
