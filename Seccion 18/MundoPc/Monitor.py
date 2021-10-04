class Monitor:

    count_monitor = 0

    def __init__(self, marca, tam) -> None:
        self._marca = marca
        self._tam = tam
        Monitor.count_monitor += 1
        self.__id_monitor = Monitor.count_monitor

    def __str__(self) -> str:
        return f'Monitor [marca: {self._marca}, tamaño: {self._tam}, id: {self.__id_monitor}]'

    """
    MARCA
    """
    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    """
    TAMAÑO
    """
    @property
    def tam(self):
        return self._tam

    @tam.setter
    def tam(self, tam):
        self._tam = tam


# test code
if __name__ == '__main__':
    philco = Monitor('phlico', 32)
    print(philco)
