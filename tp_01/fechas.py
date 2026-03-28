def ordena_fechas(f1, f2):
    anterior = f1
    posterior = f2

    anio1 = f1 % 10000
    dia1 = f1 // 1000000
    mes1 = f1 % 1000000 // 10000

    anio2 = f2 % 10000
    dia2 = f2 // 1000000
    mes2 = f2 % 1000000 // 10000

    # if anio1 != anio2:
    #     if anio1 < anio2:
    #         anterior = f1
    #         posterior = f2
    #     else:
    #         anterior = f2
    #         posterior = f1
    # else:
    #     if mes1 != mes2:
    #         if mes1 < mes2:
    #             anterior = f1
    #             posterior = f2
    #         else:
    #             anterior = f2
    #             posterior = f1
    #     else:
    #         if dia1 != dia2:
    #             if dia1 < dia2:
    #                 anterior = f1
    #                 posterior = f2
    #             else:
    #                 anterior = f2
    #                 posterior = f1
    #
    #         else:
    #             print("Son la misma fecha")

    if (anio1, mes1, dia1) < (anio2, mes2, dia2):
        anterior = f1
        posterior = f2
    elif (anio1, mes1, dia1) > (anio2, mes2, dia2):
        anterior = f2
        posterior = f1
    else:
        print("Son la misma fecha")
    return anterior, posterior


def main():
    f1 = 27032027
    f2 = 27032026
    print(ordena_fechas(f1, f2))


if __name__ == "__main__":
    main()
