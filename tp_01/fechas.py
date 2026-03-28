def ordena_fechas(f1, f2):
    anterior = f1
    posterior = f2

    anio1 = f1 % 10000
    dia1 = f1 // 1000000
    mes1 = f1 % 1000000 // 10000

    anio2 = f2 % 10000
    dia2 = f2 // 1000000
    mes2 = f2 % 1000000 // 10000

    if not es_fecha_valida(dia1, mes1, anio1) or not es_fecha_valida(dia2, mes2, anio2):
        print("Fecha invalida")
        return None, None
    # Versión conceptual
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

    # Version m'as a lo python comparando tuplas
    if (anio1, mes1, dia1) < (anio2, mes2, dia2):
        anterior = f1
        posterior = f2
    elif (anio1, mes1, dia1) > (anio2, mes2, dia2):
        anterior = f2
        posterior = f1
    else:
        print("Son la misma fecha")
    return anterior, posterior


def es_bisiesto(anio: int) -> bool:
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


def esta_dentro_del_rango(x: int, a: int, b: int) -> bool:
    return a <= x <= b


def es_fecha_valida(d: int, m: int, a: int) -> bool:
    mes_valido = esta_dentro_del_rango(m, 1, 12)
    dia_valido = esta_dentro_del_rango(d, 1, 31)
    anio_valido = esta_dentro_del_rango(a, 1900, 2100)

    if not (mes_valido and dia_valido and anio_valido):
        return False

    if m == 2:
        return d <= 28 + es_bisiesto(a)
    elif m in (4, 6, 9, 11):
        return d <= 30
    else:
        return True


def main():
    f1 = 27122027
    f2 = 27032026
    print(ordena_fechas(f1, f2))


if __name__ == "__main__":
    main()
