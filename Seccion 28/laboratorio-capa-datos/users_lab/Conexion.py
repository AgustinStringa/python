import psycopg2.extensions
from psycopg2 import pool
from logger import *

class Conexion:
    """ATRIBUTOS DE CLASE"""
    _DATABASE = "test_db_python"
    _USERNAME = "postgres"
    _PASSWORD = "admin"
    _DB_PORT = "5432"
    _HOST = "localhost"
    _MIN_CON = 1
    _MAX_CON = 3
    _POOL = None

    """METODOS DE CLASE"""
    @classmethod
    def get_pool(cls):
        if cls._POOL is None:
            try:
                cls._POOL = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host=cls._HOST, user=cls._USERNAME,
                                                      password=cls._PASSWORD, port=cls._DB_PORT,
                                                      database=cls._DATABASE)
                log.debug(f'Creacion de pool exitosa --> {cls._POOL}')
                return cls._POOL
            except Exception as e:
                log.error(f'Error al obtener el pool {e}')
        else:
            return cls._POOL

    @classmethod
    def get_conexion(cls):
        # se llama directamente a get_pool() ya que en caso de no existir lo crea
        try:
            conexion = cls.get_pool().getconn()
            log.info(f'objeto conexion creado correctamente  --> {conexion} ')
            return conexion
        except Exception as e:
            log.error(e)

    @classmethod
    def clear_conexion(cls, conn):
        if isinstance(conn, psycopg2.extensions.connection):
            cls.get_pool().putconn(conn)
            log.debug(f'Conexion {conn} liberada correctamente')
        else:
            log.warning('el objeto enviado no es de tipo conexion')

    @classmethod
    def close_conexion(cls):
        cls.get_pool().closeall()

if __name__ == '__main__':
    pass
