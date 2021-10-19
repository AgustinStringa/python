import psycopg2
import logging as log
import sys

log.basicConfig(level=log.DEBUG, format='%(asctime)s: %(levelname)s [%(filename)s %(lineno)s %(message)s]',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.StreamHandler()
                ])


class ConexionClase:

    _DATABASE = "test_db_python"
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = 'localhost'
    _CONEXION = None
    _CURSOR = None

    @classmethod
    def get_conexion(cls):
        if cls._CONEXION is None:

            try:
                conn = psycopg2.connect(user=cls._USERNAME,
                                        password=cls._PASSWORD,
                                        host=cls._HOST,
                                        port=cls._DB_PORT,
                                        database=cls._DATABASE)
                cls._CONEXION = conn
                log.debug(f'conexion exitosa: {cls._CONEXION}')
                return cls._CONEXION
            except Exception as e:
                log.error(f'Ocurrio un error al obtener la conexion a la db {e}')
                sys.exit()
        else:
            return cls._CONEXION

    @classmethod
    def get_cursor(cls):
        if cls._CURSOR is None:

            try:
                cursor = cls.get_conexion().cursor()
                cls._CURSOR = cursor
                print(f'se abrió correctamente el cursor {cls._CURSOR}')
                return cls._CURSOR
            except Exception as e:
                log.error(f'Ocurrio un error al obtener el cursor {e}')
        else:
            return cls._CURSOR


ConexionClase.get_cursor()
