class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def info(self):
        print(f"La marca del vehiculo es: {self.marca}")


class Auto(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)  # Se invoca constructor de la superclase
        self.modelo = modelo

    def info(self):
        super().info()  # Se invoca método de la superclase
        print(f"El modelo es: {self.modelo}")


class Moto(Vehiculo):
    def __init__(self, marca, cilindrada):
        super().__init__(marca)  # Se invoca constructor de la superclase
        self.cilindrada = cilindrada

    def info(self):
        super().info()  # Se invoca método de la superclase
        print(f"La cilindrada es: {self.cilindrada}")


def main():
    auto = Auto("Fiat", "600")
    auto.info()
    moto = Moto("Honda", 1000)
    moto.info()


if __name__ == "__main__":
    main()
