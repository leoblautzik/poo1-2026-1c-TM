def invertir_cadena(cadena) -> str:
    # invertida = ""
    # for c in cadena:
    #     invertida = c + invertida
    # return invertida
    return cadena[::-1]


def main():
    cadena1 = "Anita lava la tina y el dinosaurio lava los platos"
    cadena2 = "El gato ninja come pizza mientras programa en pijama"

    print(invertir_cadena(cadena1))
    print(invertir_cadena(cadena2))


if __name__ == "__main__":
    main()
