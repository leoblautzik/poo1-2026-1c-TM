import csv
from functools import total_ordering


@total_ordering
class Equipo:
    def __init__(self, nombre, datos) -> None:
        self.nombre = nombre
        self.datos = datos

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, Equipo):
            return NotImplemented
        return self.datos[7] == value.datos[7] and self.datos[6] == value.datos[6]

    def __lt__(self, value: object, /) -> bool:
        if not isinstance(value, Equipo):
            return NotImplemented
        return (self.datos[7], self.datos[6]) < (value.datos[7], value.datos[6])


class CampeonatoMundial:
    def __init__(self) -> None:
        self.__partidos: dict[str, list[int]] = {}
        self.__tabla_posiciones: list[Equipo] = []

    @property
    def partidos(self) -> dict[str, list[int]]:
        return self.__partidos

    def cargar_partidos(self, archivo_de_partidos):
        with open(archivo_de_partidos, "r") as file:
            lector = csv.reader(file)
            for partido in lector:
                k1 = partido[0]
                k2 = partido[2]
                goles_k1 = int(partido[1])
                goles_k2 = int(partido[3])
                datos_eq1 = self.partidos.get(k1, [0, 0, 0, 0, 0, 0, 0, 0])
                datos_eq2 = self.partidos.get(k2, [0, 0, 0, 0, 0, 0, 0, 0])
                ## paridos jugados
                datos_eq1[0] += 1
                datos_eq2[0] += 1
                ## partidos ganados
                if goles_k1 > goles_k2:
                    datos_eq1[1] += 1
                    datos_eq1[7] += 3
                    datos_eq2[3] += 1
                    datos_eq1[4] += int(partido[1]) - int(partido[3])
                    datos_eq2[5] += int(partido[3]) - int(partido[1])

                elif goles_k2 > goles_k1:
                    datos_eq2[1] += 1
                    datos_eq1[7] += 3
                    datos_eq1[3] += 1
                    datos_eq2[4] += int(partido[1]) - int(partido[3])
                    datos_eq1[5] += int(partido[3]) - int(partido[1])
                else:
                    ## empatados
                    datos_eq1[2] += 1
                    datos_eq2[2] += 1
                    datos_eq1[7] += 1
                    datos_eq2[7] += 1
                datos_eq1[6] = datos_eq1[4] - datos_eq1[5]
                datos_eq2[6] = datos_eq1[4] - datos_eq1[5]
                self.partidos[k1] = datos_eq1
                self.partidos[k2] = datos_eq2
            file.close()

            # Cargamos la lista de equipos para ordenarla por la tabla de posiciones
            for seleccion, datos in self.partidos.items():
                self.__tabla_posiciones.append(Equipo(seleccion, datos))

            self.__tabla_posiciones.sort(reverse=True)

    def imprimir_tabla(self, tabla):
        with open(tabla, "w") as tabla:
            for seleccion in self.__tabla_posiciones:
                tabla.write(f"{seleccion.nombre} {seleccion.datos}\n")

    def campeon(self):
        max = 0
        campeon = ""

        for datos in self.partidos.values():
            if datos[7] > max:
                max = datos[7]

        for seleccion, datos in self.partidos.items():
            if datos[7] == max:
                campeon = seleccion

        print(campeon)


def main():
    mundial = CampeonatoMundial()
    mundial.cargar_partidos("partidos.csv")
    print(mundial.partidos)
    mundial.imprimir_tabla("tabla.txt")
    mundial.campeon()


if __name__ == "__main__":
    main()
