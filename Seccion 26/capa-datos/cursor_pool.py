from Conexion_clase import ConexionClase
import logging as log

class CursorPool:

    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        # crear la conexion y el cursor
        log.debug(f'Iniciando el metodo with __enter__')
        self._conexion = ConexionClase.get_connnection_pool()
        self._cursor = self._conexion.cursor()
        # esta ultima linea es la que hace que funcione el execute
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        log.debug(f'ejecutando __exit__')

        # se evalua si hay contenido en la excepcion, o sea, si ocurrio algun error
        if valor_excepcion:
            self._conexion.rollback()
            log.error(f'Error {tipo_excepcion} {detalle_excepcion}')
        else:
            self._conexion.commit()
            log.info(f'commit realizado a la Database')
        # realizar el commit y liberar la conexion

    """
    _cursor =  None

    @classmethod
    def get_cursor_pool(cls):
        if cls._cursor is None:
            conexion = ConexionClase.get_connnection_pool()
            cursor = conexion.cursor()
            cls._cursor = cursor
            log.debug(f'cursor: {cursor}')
            return cls._cursor
        else:
            return cls._cursor

    @classmethod
    def exec_query(cls, consulta="SELECT * FROM persona"):
        cls.get_cursor_pool().execute(consulta)
        regs = cls._cursor.fetchall()

        for e in regs:
            print(e)
    """

if __name__ == '__main__':

    with CursorPool() as my_cursor:
        print(CursorPool())
        print(my_cursor)
        my_cursor.execute('SELECT * FROM PERSONA')
        regs = my_cursor.fetchall()

        for e in regs:
            log.debug(e)