import math


def area_circulo(radio):
    return math.pi * pow(radio, 2)


def volumen_cilindro(radio_base, altura):
    return area_circulo(radio_base) * altura


def main():
    print(area_circulo(5))
    print("Volumen del cilindro de radio_base 4 y altura 8: ", volumen_cilindro(4, 8))


if __name__ == "__main__":
    main()
