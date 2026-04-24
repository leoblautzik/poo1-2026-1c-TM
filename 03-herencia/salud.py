from abc import ABC, abstractmethod


class ProfesionalSalud(ABC):
    def __init__(
        self, nombre: str, dni: int, salario_base: float, anios_experiencia: int
    ) -> None:
        self._nombre = nombre
        self._dni = dni
        self._salario_base = salario_base
        self._anios_experiencia = anios_experiencia

    @abstractmethod
    def plus(self) -> float:
        pass

    def __str__(self) -> str:
        return f"{self._nombre}, Salario Base: {self._salario_base}, Plus Anual: {self.plus()}"

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, ProfesionalSalud):
            return NotImplemented
        return self._salario_base + self.plus() == value._salario_base + value.plus()

    def __lt__(self, value: object) -> bool:
        if not isinstance(value, ProfesionalSalud):
            return NotImplemented
        return self._salario_base + self.plus() < value._salario_base + value.plus()


class Medico(ProfesionalSalud):
    def plus(self) -> float:
        return self._anios_experiencia * self._salario_base * 0.08


class Enfermero(ProfesionalSalud):
    def plus(self) -> float:
        return self._anios_experiencia * self._salario_base * 0.06


class Cirujano(Medico):
    def plus(self):
        """
        un cirujano cobra el mismo plus que un Medico mas un salario base
        """
        return super().plus() + self._salario_base


class Clinica:
    def __init__(self, profesionales: list[ProfesionalSalud]) -> None:
        self.__profesionales: list[ProfesionalSalud] = profesionales

    def listar_profesionales(self):
        for p in self.__profesionales:
            print(p)

    def listar_profesionales_ordenados(self):
        ordenada = sorted(self.__profesionales)
        for p in ordenada:
            print(p)


def main():
    tortazo = Medico("Dr. Tazo", 123456, 1000000, 10)
    fermin = Enfermero("Camilla", 234567, 1000000, 10)

    camino_al_cielo = Clinica(
        [
            tortazo,
            fermin,
            Enfermero("Lucas", 2345678, 300000, 3),
            Cirujano("Carnicer", 333445566, 2000000, 1),
        ]
    )
    camino_al_cielo.listar_profesionales()
    print("----------------------------------")
    camino_al_cielo.listar_profesionales_ordenados()

    print("----------------------------------")
    camino_al_cielo.listar_profesionales()


if __name__ == "__main__":
    main()
