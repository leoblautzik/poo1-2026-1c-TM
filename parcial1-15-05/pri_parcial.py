from abc import ABC, abstractmethod


class Mision:
    def __init__(self, nombre, dificultad) -> None:
        self.nombre = nombre
        self.dificultad = dificultad


class Agente(ABC):
    def __init__(self, alias: str, energia: int, nivel_hackeo: int) -> None:
        self.__alias = alias
        self.energia = energia
        if nivel_hackeo < 1 or nivel_hackeo > 10:
            raise ValueError("En nivel de hackeo debe estar entre 1 y 10")
        self.__nivel_hackeo = nivel_hackeo

    @property
    def energia(self):
        return self.__energia

    @energia.setter
    def energia(self, energia_inicial):
        if energia_inicial < 0:
            raise ValueError("La energía no puede ser negativa")
        self.__energia = energia_inicial

    @property
    def nivel_hackeo(self):
        return self.__nivel_hackeo

    @property
    def alias(self):
        return self.__alias

    @abstractmethod
    def ejecutar_mision(self, mision: Mision) -> bool:
        pass

    @abstractmethod
    def poder_hackeo(self) -> int:
        pass

    def recargar_energia(self, mas_energia):
        self.energia += mas_energia


class Cracker(Agente):
    def poder_hackeo(self):
        return self.nivel_hackeo * 2

    def ejecutar_mision(self, mision: Mision) -> bool:
        if self.energia >= 25 and self.poder_hackeo() >= mision.dificultad:
            self.energia -= 25
            return True
        else:
            return False


class IngenieroSocial(Agente):
    def poder_hackeo(self):
        return self.nivel_hackeo + 5

    def ejecutar_mision(self, mision: Mision) -> bool:
        if self.energia >= 10 and self.poder_hackeo() >= mision.dificultad:
            self.energia -= 10
            return True
        else:
            return False


class IAAutonoma(Agente):
    def poder_hackeo(self):
        return self.nivel_hackeo * 3

    def ejecutar_mision(self, mision: Mision) -> bool:
        if self.energia < 15:
            self.recargar_energia(15 - self.energia)
        if self.energia >= 15 and self.poder_hackeo() >= mision.dificultad:
            self.energia -= 15
            return True
        else:
            return False


class Operativo:
    def ejecutar_operativo(self, agentes, misiones):
        cant_misiones_exitosas = 0
        for i in range(len(agentes)):
            ag = agentes[i]
            mi = misiones[i]

            if ag.ejecutar_mision(mi):
                cant_misiones_exitosas += 1
                print(f"Agente: {ag.alias}, Mision: {mi.nombre}: Exitosa")

        print(
            f"Se cumplieron con éxito {cant_misiones_exitosas} de {len(misiones)} misiones"
        )


def main():
    agentes = [
        Cracker("Alpha", 200, 10),
        IngenieroSocial("Zeus", 100, 5),
        IAAutonoma("Socsi", 50, 2),
    ]
    misiones = [
        Mision("Casa de la moneda", 13),
        Mision("CIA", 20),
        Mision("Microsoft", 5),
    ]

    xxx = Operativo()
    xxx.ejecutar_operativo(agentes, misiones)


if __name__ == "__main__":
    main()
