from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado


class Computadora:
    # contador
    count_pc = 0

    def aumentar_count_pc():
        Computadora.count_pc += 1
        return Computadora.count_pc
    # validaciones de objetos

    def validar_monitor(monitor):
        if (isinstance(monitor, Monitor)):
            return True
        else:
            return False

    def validar_teclado(teclado):
        if (isinstance(teclado, Teclado)):
            return True
        else:
            return False

    def validar_raton(raton):
        if (isinstance(raton, Raton)):
            return True
        else:
            return False

    # metodos
    def __init__(self, nombre, monitor, teclado, raton) -> None:
        self._nombre = nombre
        if Computadora.validar_monitor(monitor):
            self._monitor = monitor
        if Computadora.validar_teclado(teclado):
            self._teclado = teclado
        if Computadora.validar_raton(raton):
            self._raton = raton
        self.__id_pc = Computadora.aumentar_count_pc()

    def __str__(self) -> str:
        return f'''{self._nombre}, id:[{self.__id_pc}]
        {self._monitor}
        {self._teclado}
        {self._raton}
        '''

    # atributos

    """
    NOMBRE
    """
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    """
    MONITOR
    """

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    """
    TECLADO
    """
    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    """
    RATON
    """

    @property
    def raton(self):
        return self._raton

    @raton.setter
    def raton(self, raton):
        self._raton = raton


# if (__name__ == '__main__'):
philco = Monitor('phlico', 32)
noga = Teclado('mecanico', 'noga')
gamer = Raton('normal', 'genius')

dell = Computadora('dell', philco, noga, gamer)
mac = Computadora('mac', philco, noga, gamer)
conectar_igualdad = Computadora('conectar_igualdad', philco, noga, gamer)

# print(mac)
# print(conectar_igualdad)
