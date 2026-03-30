class Cuadrado:
    def __init__(self, lado, color):
        self.__lado = lado
        self.__color = color

    def lado(self):
        return self.__lado

    def color(self):
        return self.__color

    def area(self):
        return pow(self.__lado, 2)

    def set_lado(self, nuevo_lado):
        self.__lado = nuevo_lado

    def set_color(self, nuevo_color):
        self.__color = nuevo_color

    def __str__(self) -> str:
        return f"Cuadrado de Lado: {self.lado()}, color: {self.color()}, area: {self.area()} "


class Rectangulo:
    def __init__(self, base, altura, color) -> None:
        self.__base = base
        self.__altura = altura
        self.__color = color

    def base(self):
        return self.__base

    def altura(self):
        return self.__altura

    def color(self):
        return self.__color

    def area(self):
        return self.__base * self.__altura

    def set_base(self, nueva_base):
        self.__base = nueva_base

    def set_altura(self, nueva_altura):
        self.__altura = nueva_altura

    def __str__(self) -> str:
        return f"Rectangulo de area: {self.area()}"


def main():
    cua_1 = Cuadrado(3, "Rojo")
    cua_2 = Cuadrado(9, "Azul")

    print(cua_1.lado(), cua_1.area(), cua_1.color())
    print(cua_1)
    print(cua_2)

    cua_2.set_lado(6)

    print(cua_2)

    re_1 = Rectangulo(2, 4, "Azul")
    re_2 = Rectangulo(8, 5, "Verde")

    print(re_1)
    print(re_2)


if __name__ == "__main__":
    main()
