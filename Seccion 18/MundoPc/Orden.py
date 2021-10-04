from Computadora import *


class Order:
    # id orden
    count_orden = 0

    def aumentar_count_orden():
        Order.count_orden += 1
        return Order.count_orden

    def __init__(self, *computadoras) -> None:
        self.__id_orden = Order.aumentar_count_orden()
        self._computadoras = list()
        for e in computadoras:
            if(isinstance(e, Computadora)):
                self._computadoras.append(e)
            else:
                print(f'Error al intentar agregar {e} como elemento')

    def add_pc(self, pc):
        if(isinstance(pc, Computadora)):
            self._computadoras.append(pc)
    ####

    def print_pcs(self):
        text_pc = '\n'
        for e in self._computadoras:
            text_pc += e.__str__() + '\n'
        else:
            return text_pc

    def __str__(self):
        return f'''Orden {self.__id_orden}, computadoras:
{self.print_pcs()}
        '''


order1 = Order(dell, mac)
order1.add_pc(mac)

print(order1)

order2 = Order(conectar_igualdad, conectar_igualdad, conectar_igualdad)
order2.add_pc(mac)
print(order2)
