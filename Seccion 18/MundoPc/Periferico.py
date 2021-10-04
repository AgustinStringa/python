class Periferico:
    def __init__(self, tipo, marca) -> None:
        self._tipo = tipo
        self._marca = marca

    def __str__(self):
        return f'[Tipo: {self._tipo}, Marca: {self._marca}]'

    """
    TIPO
    """
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    """
    MARCA
    """

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca


# codigo de prueba

# mouse = Periferico('mouse', 'hp')
# mouse.tipo = 'impresora'
# print(mouse.tipo)
# print(mouse)
