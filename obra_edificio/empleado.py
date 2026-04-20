class Empleado:
    def __init__(self, nombre, salario_base):
        self.__nombre = nombre
        self._salario_base = salario_base

    def bonificacion(self):
        return self._salario_base * 0.05

    def salario(self):
        return self._salario_base + self.bonificacion()

    def __str__(self) -> str:
        return f"Nombre: {self.__nombre}, salario: {self.salario()}"


class Gerente(Empleado):
    def __init__(self, nombre, salario_base, depto):
        super().__init__(nombre, salario_base)
        self.departamento = depto

    def bonificacion(self):
        return self._salario_base * 0.1


class Desarrollador(Empleado):
    def __init__(self, nombre, salario_base, lenguaje):
        super().__init__(nombre, salario_base)
        self.lenguaje = lenguaje

    def bonificacion(self):
        return self._salario_base * 0.07


def main():
    pedro = Empleado("Pedro", 100)
    juam = Gerente("Juan", 200, "Ventas")
    anita = Desarrollador("Ana", 500, "python")

    print(pedro)
    print(juam)
    print(anita)


if __name__ == "__main__":
    main()
