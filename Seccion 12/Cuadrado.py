from FiguraGeometrica import *
from Colores import *


class Cuadrado(FiguraGeometrica, Colores):
    def __init__(self, lado, nombre_color, hexa) -> None:

        FiguraGeometrica.__init__(self, lado, lado)
        Colores.__init__(self, nombre_color, hexa)

    def calcular_area(self):

        return f' Area del cuadrado: {self._altura * self._base}'

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Colores.__str__(self)}'


# si se quieren obtener atributos desde aqui
# aunque sería mala práctica, deberíamos llamarles por el nombre en sus clases padres

# print(asd._altura)  # esta linea se ejecuta correctamente a pesar de que el init de la clase cuadrado no tiene un atributo con el nombre _altura

# print(asd.calcular_area())
# print(asd.get_hexa())
