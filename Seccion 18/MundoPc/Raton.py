from Periferico import Periferico


class Raton(Periferico):
    count_mouse = 0

    def __init__(self, tipo, marca) -> None:
        # uso el nombre de la clase para acceder a la variable de clase
        Raton.count_mouse += 1
        self.__id_raton = Raton.count_mouse
        super().__init__(tipo, marca)

    def __str__(self):
        return f'Raton [id: {self.__id_raton}] {super().__str__()}'


# test code
# gamer = Raton('normal', 'genius')
# print(gamer)
