from abc import ABC, abstractmethod


class Cuenta(ABC):
    def __init__(self, dni: int) -> None:
        self.__dni: int = dni
        self._saldo: float = 0

    def depositar(self, monto: float) -> None:
        if monto <= 0:
            raise ValueError("Monoto inválido")
        self._saldo += monto

    @property
    def saldo(self) -> float:
        return self._saldo

    @property
    def dni(self) -> int:
        return self.__dni

    @abstractmethod
    def retirar(self, monto):
        pass

    @abstractmethod
    def dinero_disponible(self) -> float:
        pass


class CajaDeAhorro(Cuenta):
    def __init__(self, dni: int) -> None:
        super().__init__(dni)
        self.__reserva = 0

    def retirar(self, monto):
        if self.saldo < monto:
            raise ValueError("No te alcanza, jajajaja")
        self._saldo -= monto

    def reservar(self, monto):
        if self._saldo < monto:
            raise ValueError("Saldo insuficiente para reserva")
        self.__reserva += monto
        self._saldo -= monto

    def retirar_reservar(self, monto):
        if self.__reserva < monto:
            raise ValueError("Reserva insuficiente")
        self.__reserva -= monto
        self._saldo += monto

    def dinero_disponible(self) -> float:
        return self.saldo + self.__reserva
