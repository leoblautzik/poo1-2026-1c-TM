from nota import Nota


class Cursada:
    def __init__(self, parcial1, parcial2) -> None:
        self.nota1 = Nota(parcial1)
        self.nota2 = Nota(parcial2)

    def promociona(self):
        return self.nota1.promociona() and self.nota2.promociona()

    def regulariza(self):
        return self.nota1.aprobado() and self.nota2.aprobado() and not self.promociona()

    def reprueba(self):
        return self.nota1.desaprobado() or self.nota2.desaprobado()

    def __str__(self) -> str:
        cursada = "regulariza"
        if self.promociona():
            cursada = "promocion"
        elif self.reprueba():
            cursada = "reprobada"
        return f"Parcial 1: {self.nota1}, Parcial 2: {self.nota2} Cursada: {cursada}"


def main():
    cursada_pablito = Cursada(2, 5)
    print(cursada_pablito)


if __name__ == "__main__":
    main()
