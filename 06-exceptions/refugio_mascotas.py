"""
1. Clase Mascota
Atributos:
id (int)
nombre (str)
especie (str)
edad (int)
adoptado (bool)
Métodos:
marcar_adoptado(): cambia el estado a adoptado.
__str__(): devuelve una representación legible del animal.
"""


class BooleanError(Exception):
    pass


class Mascota:
    def __init__(
        self, id: int, nombre: str, especie: str, edad: int, adoptado: bool
    ) -> None:
        self.__id: int = id
        self.__nombre: str = nombre
        self.__especie: str = especie
        self.__edad: int = edad
        self.__adoptado: bool = adoptado

    def marcar_adoptado(self):
        self.__adoptado = True

    def __str__(self) -> str:
        return (
            f"Nombre: {self.__nombre}, edad: {self.__edad}, adoptado: {self.__adoptado}"
        )


class Refugio:
    def __init__(self) -> None:
        self.__mascotas: list[Mascota] = []

    def cargar_desde_archivo(self, ruta_al_archivo_de_mascotas: str):
        try:
            with open(ruta_al_archivo_de_mascotas, "r") as file:
                for cada_linea in file:
                    try:
                        cada_linea = cada_linea.strip()
                        datos = cada_linea.split(",")
                        id = int(datos[0])
                        nombre = datos[1]
                        especie = datos[2]
                        edad = int(datos[3])
                        adoptado = datos[4].strip()
                        if adoptado.lower() in ("true", "si"):
                            adoptado = True
                        elif adoptado.lower() in ("false", "no"):
                            adoptado = False
                        else:
                            raise BooleanError()
                        mascota = Mascota(id, nombre, especie, edad, adoptado)
                        self.__mascotas.append(mascota)
                    except ValueError:
                        print("Valor entero corrupto")
                    except BooleanError:
                        print("algo salio mal con los boolean")

                file.close()

        except FileNotFoundError:
            print("Archivo no encontrado")

    def mostrar_mascotas(self):
        for mascota in self.__mascotas:
            print(mascota)


def main():
    patitas = Refugio()
    archivo = input("Ingrese el nombre del archivo de mascotas: ")
    patitas.cargar_desde_archivo(archivo)
    # patitas.mostrar_mascotas()


if __name__ == "__main__":
    main()
