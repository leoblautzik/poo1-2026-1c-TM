import math


class Circulo:
    def __init__(self, radio: float):
        self.__radio = radio

    @property
    def radio(self):
        return self.__radio

    def area(self):
        return math.pi * pow(self.radio, 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

    def diametro(self):
        return 2 * self.radio

    def __repr__(self):
        return f"Soy un circulo de radio {self.radio}"


def main():
    radio = float(input("Ingrese el radio: "))
    c1 = Circulo(radio)
    print(c1)
    print("radio de c1: ", c1.radio)
    print(c1.area())
    print(c1.perimetro())


if __name__ == "__main__":
    main()
