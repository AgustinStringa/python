class Pelicula:

    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre


if __name__ == '__main__':
    peli = Pelicula('Indiana Jones')
    print(peli.nombre)
