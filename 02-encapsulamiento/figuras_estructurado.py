import math


def area_circulo(radio):
    return math.pi * pow(radio, 2)


def area_cuadrado(lado):
    return pow(lado, 2)


def area_triangulo(base, altura):
    return base * altura / 2


def area_rectangulo(base, altura):
    return base * altura


def main():

    lado = int(input("Ingrese el valor del lado de un cuadrado -> "))
    print("El area del cuadrado es: ", area_cuadrado(lado))


if __name__ == "__main__":
    main()
