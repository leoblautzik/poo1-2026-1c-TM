import csv


class LineaFormatoIncorrecto(Exception):
    pass


class Visualizacion:
    def __init__(self, usuario, serie, episodio, duracion) -> None:
        self.usuario: str = usuario
        self.serie: str = serie
        self.episodio: int = episodio
        self.duracion: int = duracion


class Maraton:
    def __init__(self) -> None:
        self.visualizaciones: list[Visualizacion] = []

    def cargar_visualizaciones(self, archivo) -> None:
        contador_lineas_invalidas = 0
        try:
            with open(archivo, "r") as file:
                reader = csv.reader(file)
                for linea in reader:
                    try:
                        if len(linea) != 4:
                            raise LineaFormatoIncorrecto
                        usuario = linea[0]
                        serie = linea[1]
                        episodio = int(linea[2])
                        duracion = int(linea[3])
                        self.visualizaciones.append(
                            Visualizacion(usuario, serie, episodio, duracion)
                        )
                    except LineaFormatoIncorrecto:
                        contador_lineas_invalidas += 1
                        print("Linea mal formada")
                    except ValueError:
                        contador_lineas_invalidas += 1
                        print("Entero invalido")
            file.close()

        except FileNotFoundError:
            print("Archivo no encontrado")

    def usuarios_registrados(self) -> set[str]:
        usuarios = set()

        for v in self.visualizaciones:
            usuarios.add(v.usuario)

        return usuarios

    def series_por_usuario(self) -> dict[str, set]:
        aux: dict[str, set[str]] = {}

        for v in self.visualizaciones:
            series = aux.get(v.usuario, set())
            series.add(v.serie)
            aux[v.usuario] = series

        return aux

    def usuario_mas_activo(self) -> tuple:
        if len(self.visualizaciones) == 0:
            raise NotImplementedError

        aux: dict[str, int] = {}

        for v in self.visualizaciones:
            minutos = aux.get(v.usuario, 0)
            minutos += v.duracion
            aux[v.usuario] = minutos

        max_minutos = None
        for minutos in aux.values():
            if max_minutos is None or minutos > max_minutos:
                max_minutos = minutos

        max_usuarios = []
        for usuario, minutos in aux.items():
            if minutos == max_minutos:
                max_usuarios.append(usuario)

        return max_usuarios, max_minutos

        # usuario_max = max(aux.items(), key=lambda item: item[1])
        # return usuario_max

    def ranking_series(self):
        aux: dict[str, int] = {}

        for v in self.visualizaciones:
            cant_visualizaciones = aux.get(v.serie, 0)
            cant_visualizaciones += 1
            aux[v.serie] = cant_visualizaciones

        ordenados = []
        for k, v in aux.items():
            ordenados.append((k, v))

        ordenados.sort(reverse=True, key=lambda t: t[1])

        return ordenados[:3]

    def reporte(self, salida):

        with open(salida, "w") as file:
            usuarios = self.usuarios_registrados()
            file.write("Cantidad de usuarios registrados: " + str(len(usuarios)))
            file.write("\nUsuarios registrados\n")
            for u in usuarios:
                file.write(str(u) + "\n")

            series_por_usuario = self.series_por_usuario()
            file.write("\nSeries que vio cada usuario\n")
            for k, v in series_por_usuario.items():
                file.write(str(k) + " " + str(v) + "\n")

            file.write("\nUsuarios mas activos: \n")
            file.write(str(self.usuario_mas_activo()))

            file.write("\nRanking de series: \n")
            file.write(str(self.ranking_series()))

        file.close()


def main():
    ms = Maraton()
    ms.cargar_visualizaciones("maraton_series.csv")
    cant_usuarios = len(ms.usuarios_registrados())
    print("Cantidad de usuarios: ", cant_usuarios)
    print(ms.usuarios_registrados())
    print("series por usuario")
    print(ms.series_por_usuario())
    print(ms.usuario_mas_activo())
    print(ms.ranking_series())

    ms.reporte("reporte.txt")


if __name__ == "__main__":
    main()
