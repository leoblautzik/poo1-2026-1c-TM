import csv


class CampeonatoMundial:
    def __init__(self) -> None:
        self.__partidos: dict[str, dict] = {}

    @property
    def partidos(self) -> dict[str, dict]:
        return self.__partidos

    def cargar_partidos(self, archivo_de_partidos):
        with open(archivo_de_partidos, "r") as file:
            lector = csv.reader(file)
            for partido in lector:
                k1 = partido[0]
                k2 = partido[2]
                datos_eq1 = self.partidos.get(
                    k1,
                    {
                        "jugados": 0,
                        "ganados": 0,
                        "empatados": 0,
                        "perdidos": 0,
                        "goles_favor": 0,
                        "goles_contra": 0,
                        "puntos": 0,
                    },
                )
                datos_eq2 = self.partidos.get(
                    k1,
                    {
                        "jugados": 0,
                        "ganados": 0,
                        "empatados": 0,
                        "perdidos": 0,
                        "goles_favor": 0,
                        "goles_contra": 0,
                        "puntos": 0,
                    },
                )
                ## paridos jugados
                datos_eq1["jugados"] += 1
                datos_eq2["jugados"] += 1
                ## partidos ganados
                if int(partido[1]) > int(partido[3]):
                    datos_eq1[1] += 1
                    datos_eq1[7] += 3
                    datos_eq2[3] += 1
                    datos_eq1[4] += int(partido[1]) - int(partido[3])
                    datos_eq2[5] += int(partido[3]) - int(partido[1])

                elif int(partido[3]) > int(partido[1]):
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

    def imprimir_tabla(self, tabla):
        with open(tabla, "w") as tabla:
            for seleccion, resultados in self.partidos.items():
                tabla.write(f"{seleccion} {resultados}\n")

    def campeon(self):
        puntos_max = max(self.partidos)

        print(puntos_max)


def main():
    mundial = CampeonatoMundial()
    mundial.cargar_partidos("partidos.csv")
    print(mundial.partidos)
    mundial.imprimir_tabla("tabla.txt")


if __name__ == "__main__":
    main()
