from io import open


class LeerNombres:
    def __init__(self) -> None:
        self.nombres = []

    def leer_nombres(self, mi_archivo: str):
        with open(mi_archivo, "r") as archinom:
            for nombre in archinom:
                self.nombres.append(nombre.strip())
        archinom.close()

    def contar_nombres(self) -> int:
        return len(self.nombres)

    def nombres_mas_largos(self) -> list[str]:
        mas_largo = self.nombres[0]
        lista_largos = []
        l_max = len(mas_largo)
        for n in self.nombres:
            if len(n) > len(mas_largo):
                mas_largo = n
                l_max = len(mas_largo)
        for n in self.nombres:
            if len(n) == l_max:
                lista_largos.append(n)

        return lista_largos

    def filtrar_compienzan_con(self, letra: str):
        lista_nombres = []
        for n in self.nombres:
            if n[0].lower() == letra.lower():
                lista_nombres.append(n)

        return lista_nombres, len(lista_nombres)

    def filtrar_contienen(self, subcadena: str):
        lista_nombres = []
        subcadena.lower()
        for n in self.nombres:
            if subcadena in n.lower():
                lista_nombres.append(n)

        return lista_nombres, len(lista_nombres)

    def escribir_ordenado(self, archivo):
        lista_ordenada = sorted(self.nombres)
        with open(archivo, "w") as a:
            for n in lista_ordenada:
                a.write(n + "\n")
        a.close()


def main():
    ln = LeerNombres()
    ln.leer_nombres("nombres.txt")
    print(f"Hay {ln.contar_nombres()} nombres")
    print(f"Los nombres mas largos son: {ln.nombres_mas_largos()}")
    print("Los nombres que empiezan con M son:")
    print(ln.filtrar_compienzan_con("M"))

    subcadena = "ana"
    print(f"Los nombres que contienen {subcadena} son:")
    print(ln.filtrar_contienen(subcadena))

    ln.escribir_ordenado("ordenados.txt")


if __name__ == "__main__":
    main()
