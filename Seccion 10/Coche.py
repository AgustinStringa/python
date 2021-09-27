class Coche:
    def __init__(self, marca, color) -> None:
        self._marca = marca
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    def __del__(self):
        print(f'Eliminando objeto {self.marca}')

    def mostrar_detalles(self):
        print(f'''marca: {self._marca} 
color: {self._color}
        ''')


if __name__ == 'main':
    # codigo a omitir en importaciones
    print(__name__)
