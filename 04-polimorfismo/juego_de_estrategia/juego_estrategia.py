from __future__ import annotations
from abc import ABC, abstractmethod


class RecibirAgua(ABC):
    @abstractmethod
    def recibir_racion_agua(self):
        pass


class Unidad(ABC):
    def __init__(self, posicion, salud, danio) -> None:
        self._posicion: int = posicion
        self._salud: int = salud
        self._danio: int = danio

    @abstractmethod
    def atacar(self, enemigo: Unidad):
        pass

    @abstractmethod
    def puede_atacar(self, enemigo: Unidad) -> bool:
        pass

    def distancia(self, enemigo: Unidad) -> int:
        return abs(self._posicion - enemigo._posicion)

    def esta_vivo(self) -> bool:
        return self._salud > 0

    def esta_muerto(self) -> bool:
        return self._salud <= 0

    def recibir_danio(self, enemigo: Unidad):
        self._salud -= enemigo._danio


class Soldado(Unidad, RecibirAgua):
    def __init__(self, posicion) -> None:
        super().__init__(posicion, 200, 10)
        self._energia = 100

    def puede_atacar(self, enemigo: Unidad):
        return (
            self != enemigo
            and self.esta_vivo()
            and self._energia >= 10
            and enemigo.esta_vivo()
            and self.distancia(enemigo) == 0
        )

    def atacar(self, enemigo):
        if self.puede_atacar(enemigo):
            enemigo.recibir_danio(self)
            self._energia -= 10

    def recibir_racion_agua(self):
        self._energia = 100


class Arquero(Unidad):
    def __init__(self, posicion) -> None:
        super().__init__(posicion, 50, 5)
        self._flechas = 20

    def puede_atacar(self, enemigo: Unidad):
        return (
            self != enemigo
            and self.esta_vivo()
            and self._flechas >= 1
            and enemigo.esta_vivo()
            and 2 <= self.distancia(enemigo) <= 5
        )

    def atacar(self, enemigo):
        if self.puede_atacar(enemigo):
            enemigo.recibir_danio(self)
            self._flechas -= 1

    def recargar_flechas(self):
        self._flechas += 6


class Caballero(Unidad):
    def __init__(self, posicion) -> None:
        super().__init__(posicion, 200, 50)
        self._caballo = Caballo()

    def puede_atacar(self, enemigo: Unidad):
        return (
            self != enemigo
            and self.esta_vivo()
            and not self._caballo.esta_rebelde()
            and enemigo.esta_vivo()
            and 1 <= self.distancia(enemigo) <= 2
        )

    def atacar(self, enemigo):
        if self.puede_atacar(enemigo):
            enemigo.recibir_danio(self)
            self._caballo.registrar_ataque()


class Caballo(RecibirAgua):
    def __init__(self) -> None:
        self.contador_ataques = 0

    def registrar_ataque(self):
        self.contador_ataques += 1

    def recibir_racion_agua(self):
        self.contador_ataques = 0

    def esta_rebelde(self) -> bool:
        return self.contador_ataques > 3


def main():
    rambo = Soldado(0)
    conan = Soldado(0)

    print(rambo.puede_atacar(conan))


if __name__ == "__main__":
    main()
