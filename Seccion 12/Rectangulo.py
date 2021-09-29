from FiguraGeometrica import FiguraGeometrica
from Colores import Colores


class Rectangulo(FiguraGeometrica, Colores):
    def __init__(self, base, altura, nombre_color, hexadecimal) -> None:
        FiguraGeometrica.__init__(self, base, altura)
        Colores.__init__(self, nombre_color, hexadecimal)

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Colores.__str__(self)}'

    def calcular_area(self):
        return self._base * self._altura
