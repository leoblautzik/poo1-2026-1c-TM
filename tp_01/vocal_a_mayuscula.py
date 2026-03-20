"""
Escribir un programa que pida al usuario que
introduzca una frase en la consola y una vocal,
y después muestre por pantalla la misma frase,
pero con la vocal introducida en mayúscula
"""


def vocal_a_may(frase: str, vocal: str) -> str:
    return frase.replace(vocal, vocal.upper())


def main():

    cadena2 = "El gato ninja come pizza mientras programa en pijama"
    print(vocal_a_may(cadena2, "e"))


if __name__ == "__main__":
    main()
