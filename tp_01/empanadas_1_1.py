def main():
    cantidad = int(input("Cuantas empanadas: "))
    precio_unidad = 2000
    precio_docena = 20000

    docenas = cantidad // 12
    unidades = cantidad % 12

    total = docenas * precio_docena + unidades * precio_unidad
    print("Debe abonar: ", total)


if __name__ == "__main__":
    main()
