# ABC - Abstract Base Class

# ABC es la clase como tal y abstractmethod es un decorador, como @property
from abc import ABC, abstractmethod

# la clase extiende de la clase ABC


class FiguraGeometrica(ABC):

    def _validar(self, valor):
        return True if valor > 0 else False

    def __init__(self, base, altura) -> None:

        if self._validar(base):
            self._base = base
        else:
            print('Valor de base incorrecto')
        if self._validar(altura):
            self._altura = altura
        else:
            print('valor de altura incorrecto')

    def __str__(self):
        return f'''Figura Geometrica -> [Base: {self._base} Altura: {self._altura}]'''

    @abstractmethod
    def calcular_area(self):
        pass

    """
    BASE
    """
    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        if self._validar(base):
            self._base = base
        else:
            print('valor de base incorrecto')

    """
    ALTURA
    """
    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        if self._validar(altura):
            self._altura = altura
        else:
            print('valor altura incorrecto ')
