"""
Realizar un programa que conste de una clase llamada Estudiante,
que tenga como atributos el nombre y la nota del alumno.
Definir los métodos para inicializar sus atributos,
imprimirlos y mostrar un mensaje con el resultado de la nota
y si ha aprobado o no
"""

from nota import Nota


class Estudiante:
    def __init__(self, nombre: str, nota: int) -> None:
        self.__nombre: str = nombre
        self.__obj_nota: Nota = Nota(nota)

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        self.__nombre = nuevo_nombre

    @property
    def nota(self) -> int:
        return self.__obj_nota.valor

    @nota.setter
    def nota(self, nueva_nota: int) -> None:
        self.__obj_nota.valor = nueva_nota

    def recuperar(self, nueva_nota: int) -> None:
        self.__obj_nota.recuperar(nueva_nota)

    def aprobado(self) -> bool:
        return self.__obj_nota.aprobado()

    def promociona(self) -> bool:
        return self.__obj_nota.promociona()

    def desaprobado(self) -> bool:
        return self.__obj_nota.desaprobado()

    def __str__(self) -> str:
        return f"Alumno: {self.nombre}, {self.__obj_nota}"


pepito = Estudiante("pepito", 8)
luisito = Estudiante("Luis", 2)
susanita = Estudiante("Susana", 4)
print(pepito)
print(luisito)
print(susanita)
luisito.recuperar(4)
print(luisito)
