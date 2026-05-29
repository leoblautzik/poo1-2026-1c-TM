"""
============================================================
                    EJERCICIOS CON DICT
============================================================
"""


def contar_frecuencias(palabras: list[str]) -> dict[str, int]:
    """Recibe una lista de palabras y devuelve un diccionario donde
    las claves son palabras y los valores la cantidad de veces
    que aparece cada una.

    contar_frecuencias(["uno", "dos", "uno", "Uno", "java", "java", "UNO", "java", "java"]) ->
    {"uno": 4, "dos": 1, "java":4}
    """
    frecuencias: dict[str, int] = {}

    # for p in palabras:
    #     p = p.lower().strip()
    #     if p not in frecuencias.keys():
    #         nuevo_valor = 1
    #     else:
    #         nuevo_valor = frecuencias[p] + 1
    #
    #     frecuencias[p] = nuevo_valor

    for p in palabras:
        p = p.lower().strip()
        frecuencias[p] = frecuencias.get(p, 0) + 1

    return frecuencias


def palabra_mas_frecuente(dic: dict[str, int]) -> tuple[int, list[str]]:
    """devuelve la palabra con mayor frecuencia y su frecuencia.
    en caso de que haya empate, se debe retornar la frecuencia maxima y
    todas las palabras que se repiten ese numero de veces
    {"uno": 4, "dos": 1, "java": 4} -> (4, ["uno", "java"])
    """

    frec_max = 0
    palabras_mas_frecuentes = []

    for p, f in dic.items():
        if f > frec_max:
            frec_max = f

    for p, f in dic.items():
        if f == frec_max:
            palabras_mas_frecuentes.append(p)

    return (frec_max, palabras_mas_frecuentes)

    # return max(dic.items(), key=lambda item: item[1])


def invertir_diccionario(dic_in: dict[str, int]) -> dict[int, list[str]]:
    """Recibe un diccionario de palabra, frecuencia y devuelve un nuevo
    diccionario donde las claves son las frecuencias y los valores son
    listas de palabras con esa frecuencia."""

    salida: dict[int, list[str]] = {}

    for palabra, frecuencia in dic_in.items():
        salida.setdefault(frecuencia, []).append(palabra)

    return salida


def fusionar_diccionarios(dic1: dict[str, int], dic2: dict[str, int]) -> dict[str, int]:
    """Devuelve un nuevo diccionario que contiene todas las claves de ambos.
    Si una clave aparece en ambos, el valor debe ser la suma de los dos."""

    salida: dict[str, int] = {}

    for k, _ in dic1.items():
        salida[k] = dic1[k]

    for k, v in dic2.items():
        salida[k] = salida.get(k, 0) + v

    return salida


def filtrar_por_valor(dic: dict[str, int], minimo: int) -> dict[str, int]:
    """Devuelve un nuevo diccionario con solo las claves cuyo valor es mayor o
    igual que 'minimo'."""

    # TODO


def clave_mas_larga(dic: dict[str, str]) -> str:
    """Recibe un diccionario cuyas claves y valores son strings.
    Devuelve la clave con mayor longitud.
    Si el diccionario está vacío, devuelve cadena vacía."""

    if not dic:
        return ""

    # for k in dic.keys():
    #     if len(k) > len(salida):
    #         salida = k
    #
    # return salida
    return max(dic.keys(), key=len)

    # TODO


def main():
    entrada = {"hola": 2, "chau": 3, "si": 2}
    # esperado = {2: ["hola", "si"], 3: ["chau"]}
    salida = invertir_diccionario(entrada)
    print(salida)


if __name__ == "__main__":
    main()
