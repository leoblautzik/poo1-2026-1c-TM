class ObraEdificio:
    """
    Escribir el código de una clase denominada ObraEdificio, con las siguientes características.
    Cada objeto de esta clase deberá tener información acerca de la superficie total a cimentar de una obra,
    y de la superficie que ya ha sido cimentada (en , sin decimales). Existirán los siguientes métodos:
    * Constructor: en la creación se fijará el área total a cimentar para este edificio
    * cimentando: recibirá un número indicando los metros de superficie que se están cimentando en ese momento.
    Si la suma de la superficie previamente cimentada más la que se supone que se está cimentando ahora,
    es mayor que la superficie total a cimentar, se escribirá un mensaje de error, y no se modificara nada.
    En caso contrario, se acumulara la cantidad de metros que se están cimentando con los que ya se habían cimentado antes.
    * restaPorCimentar: devolverá los metros que faltan por cimentar para alcanzar la superficie total
    * terminado: devolverá verdadero si la superficie cimentada ya es igual a la superficie total a cimentar
    """

    def __init__(self, superficie: int) -> None:
        self.__sup_a_cimentar: int = superficie
        self.__ya_cimentados: int = 0

    def cimentando(self, mts_cimentando: int) -> None:
        if mts_cimentando > self.resta_por_cimentar():
            raise RuntimeError("Exedido")
        self.__ya_cimentados += mts_cimentando

    def resta_por_cimentar(self) -> int:
        return self.__sup_a_cimentar - self.__ya_cimentados

    def terminado(self) -> bool:
        return self.resta_por_cimentar() == 0


def main():
    pass


if __name__ == "__main__":
    main()
