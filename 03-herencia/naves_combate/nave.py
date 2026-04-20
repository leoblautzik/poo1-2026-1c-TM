from __future__ import annotations
from abc import ABC, abstractmethod


class Nave(ABC):
    def __init__(self, nombre, salud, danio) -> None:
        self.__nombre = nombre
        self.__salud = salud
        self.__danio = danio

    @abstractmethod
    def atacar(self, enemigo: Nave) -> None:
        pass

    @property
    def salud(self) -> int:
        return self.__salud

    @salud.setter
    def salud(self, nueva_salud):
        self.__salud = nueva_salud

    def recibir_danio(self, atacante: Nave):
        self.__salud -= atacante.__danio
        if self.__salud <= 0:
            self.__salud = 0

    def esta_destruida(self) -> bool:
        return self.__salud <= 0

    def estado(self) -> str:
        return f"Nave: {self.__nombre} -> salud: {self.__salud}"


class Caza(Nave):
    def __init__(self, nombre) -> None:
        super().__init__(nombre, 100, 15)

    def atacar(self, enemigo: Nave) -> None:
        enemigo.recibir_danio(self)


class Bombardero(Nave):
    def __init__(self, nombre) -> None:
        super().__init__(nombre, 150, 25)

    def atacar(self, enemigo: Nave) -> None:
        enemigo.recibir_danio(self)
        self.salud -= 5


class Crucero(Nave):
    def __init__(self, nombre) -> None:
        super().__init__(nombre, 300, 40)

    def atacar(self, enemigo: Nave) -> None:
        if self.salud > 50:
            enemigo.recibir_danio(self)


def main():
    c1 = Caza("Caza")
    c2 = Caza("X")

    print(c1.estado())
    print(c2.estado())

    c1.atacar(c2)

    print(c1.estado())
    print(c2.estado())


if __name__ == "__main__":
    main()
