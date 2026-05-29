from io import open
from os import device_encoding, wait

"""
Una empresa almacena información de sus ventas diarias en un archivo de texto llamado ventas.txt.
Cada línea del archivo contiene los datos de una venta, separados por comas, con el siguiente formato:
<codigo_producto>,<descripcion>,<categoria>,<precio_unitario>,<cantidad_vendida>,<vendedor>
Por ejemplo:
A1023,Mouse Logitech M90,Periféricos,5200.50,3,Camila
"""


class Venta:
    def __init__(self, cp, desc, cat, pu, cv, vendedor) -> None:
        self.cp = cp
        self.desc = desc
        self.cat = cat
        self.pu = pu
        self.cv = cv
        self.vendedor = vendedor

    def monto_venta(self):
        return self.cv * self.pu

    def __repr__(self) -> str:
        return f"{self.desc}, {self.monto_venta()}"


class GestionVentas:
    def __init__(self) -> None:
        self.ventas: list[Venta] = []

    def leer_ventas(self, archivo):
        with open(archivo, "r") as ai:
            for cada_venta in ai:
                datos = cada_venta.strip().split(",")
                cp = datos[0]
                desc = datos[1]
                cat = datos[2]
                pu = float(datos[3])
                cv = int(datos[4])
                vendedor = datos[5]
                venta = Venta(cp, desc, cat, pu, cv, vendedor)
                self.ventas.append(venta)
        ai.close()

    def mostrar_ventas(self):
        for v in self.ventas:
            print(v)

    def total_ventas(self) -> float:
        total = 0
        for cada_venta in self.ventas:
            total += cada_venta.monto_venta()

        return total

    def vendedor_estrella(self):
        max_venta = self.ventas[0].monto_venta()
        max_vendedor = self.ventas[0].vendedor
        for v in self.ventas:
            if v.monto_venta() > max_venta:
                max_venta = v.monto_venta()
                max_vendedor = v.vendedor

        return max_venta, max_vendedor

    def ventas_por_vendedor_basica(self) -> dict[str, float]:
        ventas_vendedor: dict[str, float] = {}

        for cada_venta in self.ventas:
            if cada_venta.vendedor not in ventas_vendedor.keys():
                nuevo_valor = cada_venta.monto_venta()
            else:
                nuevo_valor = (
                    ventas_vendedor[cada_venta.vendedor] + cada_venta.monto_venta()
                )
            ventas_vendedor[cada_venta.vendedor] = nuevo_valor

        return ventas_vendedor

    def ventas_por_vendedor_con_get(self) -> dict[str, float]:
        ventas_vendedor: dict[str, float] = {}

        for venta in self.ventas:
            ventas_vendedor[venta.vendedor] = (
                ventas_vendedor.get(venta.vendedor, 0) + venta.monto_venta()
            )

        return ventas_vendedor

    def mostrar_ventas_por_vendedor(self):
        # vv = self.ventas_por_vendedor_basica()
        vv = self.ventas_por_vendedor_con_get()

        for vendedor, monto in vv.items():
            print(f"Vendedor: {vendedor}, Ventas Totales: {monto}")

    def cantidades_por_producto(self) -> dict[str, int]:
        aux: dict[str, int] = {}
        for cada_venta in self.ventas:
            if cada_venta.cp not in aux.keys():
                nuevo_valor = cada_venta.cv
            else:
                nuevo_valor = aux[cada_venta.cp] + cada_venta.cv
            aux.update({cada_venta.cp: nuevo_valor})

        return aux

    def producto_mas_vendido(self):
        aux = self.cantidades_por_producto()

        max_cv = list(aux.values())[0]

        for cp, cv in aux.items():
            if cv > max_cv:
                max_cv = cv

        mas_vendidos = []

        for cp, cv in aux.items():
            if cv == max_cv:
                mas_vendidos.append((cp, cv))

        return mas_vendidos


def main():
    gvi = GestionVentas()
    gvi.leer_ventas("ventas.txt")
    gvi.mostrar_ventas()
    print("Total de ventas", gvi.total_ventas())
    print("Vendedor estrella: ", gvi.vendedor_estrella())
    # print("Ventas por vendedor", gvi.ventas_por_vendedor())
    gvi.mostrar_ventas_por_vendedor()
    print(gvi.cantidades_por_producto())
    print(gvi.producto_mas_vendido())


if __name__ == "__main__":
    main()
