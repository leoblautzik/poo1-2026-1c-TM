import csv


class Visualizacion:
    def __init__(self, usuario, video, categoria, duracion) -> None:
        self.usuario = usuario
        self.video = video
        self.categoria = categoria
        self.duracion = duracion


class GestionVisualizaciones:
    def __init__(self, archivo) -> None:
        self.visualizaciones: list[Visualizacion] = []
        try:
            with open(archivo, "r") as file:
                reader = csv.reader(file)
                next(reader)
                for cada_linea in reader:
                    try:
                        self.visualizaciones.append(
                            Visualizacion(
                                cada_linea[0],
                                cada_linea[1],
                                cada_linea[2],
                                int(cada_linea[3]),
                            )
                        )
                    except ValueError:
                        print("Formato numérico erroneo")
            file.close()
        except FileNotFoundError:
            print("archivo no encontrado")

    def duracion_promedio(self) -> float:
        """Devuelve la duración promedio de las
        visualizaciones."""
        if len(self.visualizaciones) == 0:
            raise ValueError

        suma_d = 0

        for v in self.visualizaciones:
            suma_d += v.duracion

        return suma_d / len(self.visualizaciones)

    def videos_de_la_categoria(self, categoria) -> list[str]:
        """Devuelve una lista de videos de la categoría indicada,
        sin repetidos."""
        # Usamos un conjunto para evitar repetidos
        set_videos: set[str] = set()

        for v in self.visualizaciones:
            if v.categoria == categoria:
                set_videos.add(v.video)

        # convertimos el set en una lista para cumplir con la firma del método
        return list(set_videos)

    def usuarios_unicos(self) -> set[str]:
        """Devuelve el conjunto de usuarios registrados."""
        set_usuarios: set[str] = set()

        for v in self.visualizaciones:
            set_usuarios.add(v.usuario)

        return set_usuarios

    def minutos_por_usuario(self) -> dict[str, int]:
        """Devuelve un diccionario con el total de minutos
        visualizados por cada usuario."""
        dict_mxu: dict[str, int] = {}

        for v in self.visualizaciones:
            minutos = dict_mxu.get(v.usuario, 0)
            minutos += v.duracion
            dict_mxu[v.usuario] = minutos

        return dict_mxu

    def usuario_mas_activo(self) -> tuple[str, int]:
        """Devuelve una tupla (usuario, minutos) correspondiente
        al usuario con mayor tiempo acumulado."""
        dict_mxu = self.minutos_por_usuario()

        return max(dict_mxu.items(), key=lambda item: item[1])


def main():

    gv = GestionVisualizaciones("visualizaciones.csv")
    print(gv.duracion_promedio())
    print(gv.videos_de_la_categoria("Educación"))
    print(gv.usuarios_unicos())
    print(gv.minutos_por_usuario())
    print(gv.usuario_mas_activo())


if __name__ == "__main__":
    main()
