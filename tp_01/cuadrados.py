"""Escribir una función que reciba una muestra de números en una lista
y devuelva otra lista con sus cuadrados"""


def cuadrados(muestra_de_numeros):
    numeros_al_cuadrado = []

    for n in muestra_de_numeros:
        numeros_al_cuadrado.append(pow(n, 2))

    return numeros_al_cuadrado


def main():
    numeros = [-1, 0, 8, -3]
    print(cuadrados(numeros))


if __name__ == "__main__":
    main()
