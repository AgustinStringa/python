class Vehiculo:
    def __init__(self, color, ruedas) -> None:
        self._color = color
        self._ruedas = ruedas

    def __str__(self) -> str:
        return f'Vehiculo -> [color: {self._color}, ruedas: {self._ruedas}]'

    @property
    def color(self):
        return self._color

    @property
    def ruedas(self):
        return self._ruedas

    @color.setter
    def color(self, color):
        self._color = color

    @ruedas.setter
    def ruedas(self, ruedas):
        self._ruedas = ruedas


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo) -> None:
        super().__init__(color, ruedas)
        self._color = color
        self._ruedas = ruedas
        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    def __str__(self) -> str:
        return f'Bicicleta ->[tipo: {self._tipo}] {super().__str__()}'


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad) -> None:
        super().__init__(color, ruedas)
        self._color = color
        self._ruedas = ruedas
        self._velocidad = velocidad

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

    def __str__(self) -> str:
        return f'Coche -> [velocidad : {self._velocidad} ] {super().__str__()}'


# bici
olmo = Bicicleta('amarilla', '2', 'bmx')
# print(olmo.color)
# olmo.color = 'azul'
# olmo.tipo = 'mountain'
# print(olmo)

# Coche
fiat = Coche('crema', '4', '130km/h')
