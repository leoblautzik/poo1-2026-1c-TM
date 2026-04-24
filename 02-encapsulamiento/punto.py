from functools import total_ordering
import math


@total_ordering
class Punto:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def distancia_al_origen(self) -> float:
        return math.hypot(self.x, self.y)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Punto):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return self.__str__()

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Punto):
            return NotImplemented
        return (self.x, self.y) < (other.x, other.y)


def main():
    p1 = Punto(1, 1)
    p5 = Punto(1, 1)
    p2 = Punto(-1, 1)
    p3 = Punto(-1, -1)
    p4 = Punto(1, -1)
    print(p1)
    print(p5.__str__())

    print(p1 == p5)
    print(p1 >= p5)
    print(p1.__eq__(p5))
    # p1.equals(p2)

    print(p1 < p2, "falso")
    print(p2 <= p1, "verdadero")
    print(p1 > p2, "verdadero")
    print(p2 > p1, "falso")

    puntos = [p1, p2, p3, p4, p5]

    puntos.sort()
    print(puntos)


if __name__ == "__main__":
    main()
