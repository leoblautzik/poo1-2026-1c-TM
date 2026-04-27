from abc import ABC
import math
from typing import final


class Figura(ABC):
    def __init__(self, area: float) -> None:
        self.__area = area

    @final
    def get_area(self) -> float:
        return self.__area

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Figura):
            raise NotImplementedError
        return self.get_area() == value.get_area()

    def __lt__(self, value: object) -> bool:
        if not isinstance(value, Figura):
            raise NotImplementedError
        return self.get_area() < value.get_area()


class Triangulo(Figura):
    def __init__(self, base, altura) -> None:
        super().__init__(base * altura / 2)


class Rectangulo(Figura):
    def __init__(self, base, altura) -> None:
        super().__init__(base * altura)


class Cuadrado(Rectangulo):
    def __init__(self, lado) -> None:
        super().__init__(lado, lado)


class Elipse(Figura):
    def __init__(self, radio_mayor, radio_menor) -> None:
        super().__init__(math.pi * radio_mayor * radio_menor)


class Circulo(Elipse):
    def __init__(self, radio) -> None:
        super().__init__(radio, radio)


def main():
    circulito = Circulo(5)
    triangulito = Triangulo(2, 5)
    elipse = Elipse(2, 6)
    rectangulito = Rectangulo(2, 5)
    cuadradito = Cuadrado(6)

    figuras = [circulito, triangulito, elipse, rectangulito, cuadradito]
    figuras.sort(reverse=True)

    for f in figuras:
        print(f.get_area())


if __name__ == "__main__":
    main()
