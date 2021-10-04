from Periferico import Periferico


class Teclado(Periferico):
    count_keyboard = 0

    def __init__(self, tipo, marca) -> None:
        # uso el nombre de la clase para acceder a la variable de clase
        Teclado.count_keyboard += 1
        self.__id_teclado = Teclado.count_keyboard
        super().__init__(tipo, marca)

    def __str__(self):
        return f'Teclado [id: {self.__id_teclado}] {super().__str__()}'

# cod de prueba
# noga = Teclado('mecanico', 'noga')
# noga.tipo = "gamer"
# print(noga)
