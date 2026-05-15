from __future__ import annotations
from abc import ABC
# -----------------------------
# Ejercicio: Sistema de Biblioteca Virtual
# -----------------------------


# Clase base
class Material(ABC):
    def __init__(self, titulo: str, autor: str, anio: int):
        # Atributos privados
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio

    # Getters
    # def get_titulo(self) -> str:
    #     pass  # TODO: devolver el título
    #
    # def get_autor(self) -> str:
    #     pass  # TODO: devolver el autor
    #
    # def get_anio(self) -> int:
    #     pass  # TODO: devolver el año

    def __str__(self) -> str:
        return f"Título: {self.__titulo}, Autor: {self.__autor}, Año: {self.__anio}"

    def __repr__(self) -> str:
        return self.__str__()


# -----------------------------
# Subclases (Herencia)
# -----------------------------
class Libro(Material):
    def __init__(self, titulo: str, autor: str, anio: int, genero: str):
        super().__init__(titulo, autor, anio)
        self.__genero = genero

    def __str__(self) -> str:
        return f"Libro: {super().__str__()}, Genero: {self.__genero}"


class Revista(Material):
    def __init__(self, titulo: str, autor: str, anio: int, numero_edicion: int):
        super().__init__(titulo, autor, anio)
        self.__numero_edicion = numero_edicion

    def __str__(self) -> str:
        return (
            f"Revista: {super().__str__()}, Numero de edición: {self.__numero_edicion}"
        )


class DVD(Material):
    def __init__(self, titulo: str, autor: str, anio: int, duracion: int):
        super().__init__(titulo, autor, anio)
        self.__duracion = duracion

    def __str__(self) -> str:
        return f"DVD: {super().__str__()}, Duración: {self.__duracion}"


# -----------------------------
# Clase Usuario (Composición)
# -----------------------------
class Usuario:
    def __init__(self, nombre: str):
        self.__nombre: str = nombre
        self.__materiales_prestados: list[Material] = []  # lista de objetos Material

    def prestar(self, material: Material):
        self.__materiales_prestados.append(material)

    def devolver(self, material: Material):
        self.__materiales_prestados.remove(material)

    def listar_materiales(self) -> str:
        s = ""
        for m in self.__materiales_prestados:
            s = s + m.__str__() + "\n"

        return s

    def __str__(self) -> str:
        return f"Usuario: {self.__nombre}, Materiales prestados:\n{self.listar_materiales()}"


# -----------------------------
# Función polimórfica
# -----------------------------


# -----------------------------
# Programa principal
# -----------------------------


def main():
    # TODO: crear algunos libros, revistas y DVDs
    # TODO: crear usuarios
    # TODO: prestar materiales
    # TODO: listar materiales de cada usuario

    libro = Libro("El vado de los zorros", "Anna Starobinets", 2025, "Ficción")
    revista = Revista("Cifras", "Editorial Cuspide", 2026, 4678)
    dvd = DVD("Matilda", "Autor de Matilda", 1996, 2)
    luisito = Usuario("Luisito")

    luisito.prestar(libro)
    luisito.prestar(revista)
    luisito.prestar(dvd)

    print(luisito)

    luisito.devolver(libro)

    print(luisito)

    def mostrar_informacion(material: Material):
        print(material.__str__())

    mostrar_informacion(libro)
    mostrar_informacion(dvd)


if __name__ == "__main__":
    main()
