import math


class RadioInvalidoException(Exception):
    pass


class Circulo:
    def __init__(self, radio: float):
        self.radio = radio

    @property
    def radio(self):
        return self.__radio

    @radio.setter
    def radio(self, nuevo_radio):
        if nuevo_radio <= 0:
            raise RadioInvalidoException("El radio no puede ser <= que cero")
        self.__radio = nuevo_radio

    def area(self):
        return math.pi * pow(self.radio, 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

    def diametro(self):
        return 2 * self.radio

    def __repr__(self):
        return f"Soy un circulo de radio {self.radio}"


def main():
    while True:
        try:
            radio = float(input("Ingrese el radio: "))
            c1 = Circulo(radio)
            print(c1)
            print("radio de c1: ", c1.radio)
            print(c1.area())
            print(c1.perimetro())
            print(c1.diametro())
            break

        except ValueError:
            print("El valor ingresado no es convertible a float")
        except RadioInvalidoException:
            print("El radio debe ser mayor que cero")
        finally:
            print("Pasaba por aqui...")


if __name__ == "__main__":
    main()
