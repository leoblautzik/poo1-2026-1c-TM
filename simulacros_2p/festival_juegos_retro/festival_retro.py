import csv


class LineaFormatoIncorrecto(Exception):
    pass


class Partida:
    def __init__(self, jugador, juego, nivel, minutos) -> None:
        self.jugador = jugador
        self.juego = juego
        self.nivel = nivel
        self.minutos = minutos

    def __repr__(self):
        return f"Jugador: {self.jugador}, juega: {self.juego}, nivel: {self.nivel}, durante: {self.minutos} minutos"


class FestivalRetro:
    def __init__(self, archivo) -> None:
        self.__partidas = []
        self.__cargar_partidas(archivo)

    def __cargar_partidas(self, archivo):
        try:
            with open(archivo, "r") as file:
                reader = csv.reader(file)
                next(reader)
                for linea in reader:
                    try:
                        if len(linea) != 4:
                            raise LineaFormatoIncorrecto
                        self.__partidas.append(
                            Partida(linea[0], linea[1], int(linea[2]), int(linea[3]))
                        )

                    except LineaFormatoIncorrecto:
                        print("Linea invalida")

                    except ValueError:
                        print("Valores no numéricos")
            file.close()

        except FileNotFoundError:
            print("Archivo no encontrado")

    def listar_partidas(self):
        for p in self.__partidas:
            print(p)

    def jugadores_registrados(self):
        jugadores = set()
        for p in self.__partidas:
            jugadores.add(p.jugador)

        return jugadores

    def juegos_por_jugador(self):
        jpj = {}

        for partida in self.__partidas:
            juegos = jpj.get(partida.jugador, set())
            juegos.add(partida.juego)
            jpj[partida.jugador] = juegos

        return jpj

    def minutos_por_jugador(self):
        mpj = {}

        for p in self.__partidas:
            minutos = mpj.get(p.jugador, 0)
            minutos += p.minutos
            mpj[p.jugador] = minutos

        return mpj

    def jugador_mas_dedicado(self):
        max_minutos = max(self.minutos_por_jugador().values())

        for jugador, minutos in self.minutos_por_jugador().items():
            if minutos == max_minutos:
                return (jugador, minutos)

        return None

    def maximo_nivel_por_juego(self):
        mnpj = {}

        for p in self.__partidas:
            nivel = mnpj.get(p.juego, 0)
            nivel = max(nivel, p.nivel)
            mnpj[p.juego] = nivel

        mnpj = list(tuple(mnpj.items()))
        mnpj.sort(key=lambda n: n[1], reverse=True)

        return mnpj


def main():

    festival = FestivalRetro("partidas.csv")
    festival.listar_partidas()
    print(
        f"\nJugadores registrados: {len(festival.jugadores_registrados())}\n{festival.jugadores_registrados()}\n"
    )
    print(f"\nJuegos por Jugador:\n{festival.juegos_por_jugador()}")
    print(f"\nMinutos por jugador:\n{festival.minutos_por_jugador()}")
    print(f"\nJugador mas dedicado: {festival.jugador_mas_dedicado()}")
    print(f"\nMaximo nivel por juego:\n{festival.maximo_nivel_por_juego()}")


if __name__ == "__main__":
    main()
