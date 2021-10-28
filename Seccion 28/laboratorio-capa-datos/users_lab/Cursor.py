from logger import *
from Conexion import Conexion

class Cursor:

    def __init__(self):
        self._conn = None
        self._cursor = None

    def __enter__(self):
        try:
            self._conn = Conexion.get_conexion()
            cursor = self._cursor = self._conn.cursor()
            return cursor
        except Exception as e:
            log.error(f'error al intentar crear el cursor')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            self._conn.rollback()
            log.error(f'Ha ocurrido un error, se cerrará la conexion {self._conn}')
        else:
            self._conn.commit()
            log.debug(f'Realizando commit a la DB {self._conn}')
            Conexion.clear_conexion(self._conn)

if __name__ == '__main__':

    with Cursor() as mycur:
      pass