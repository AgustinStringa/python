from psycopg2 import pool
import logging as log

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
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    """
    UTILIZANDO POOL DE CONEXIONES
    """
    @classmethod
    def get_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host=cls._HOST, user=cls._USERNAME,
                                                      password=cls._PASSWORD, port=cls._DB_PORT,
                                                      database=cls._DATABASE)
                log.debug(f'Creacion de pool exitosa {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Error al obtener el pool {e}')
        else:
            return cls._pool

    @classmethod
    def get_connnection_pool(cls):
        conexion = cls.get_pool().getconn()
        log.debug(f'Objeto conexion creado correctamente {conexion}')
        return conexion

    @classmethod
    def liberar_conexion(cls, conexion):
        cls.get_pool().putconn(conexion)
        # el metodo .putconn() "pone" en el pool el objeto de conexion indicado por parametro
        log.debug(f'conexion {conexion} regresada al pool.')

    @classmethod
    def cerrar_conexiones(cls):
        cls.get_pool().closeall()

    """
    CODIGO PARA MANEJAR OBJETOS DE CONEXION DESDE ESTA CLASE
    """
    #_CONEXION = None
    #_CURSOR = None

    # @classmethod
    # def get_conexion(cls):
    #     if cls._CONEXION is None:
    #
    #         try:
    #             conn = psycopg2.connect(user=cls._USERNAME,
    #                                     password=cls._PASSWORD,
    #                                     host=cls._HOST,
    #                                     port=cls._DB_PORT,
    #                                     database=cls._DATABASE)
    #             cls._CONEXION = conn
    #             log.debug(f'conexion exitosa: {cls._CONEXION}')
    #             return cls._CONEXION
    #         except Exception as e:
    #             log.error(f'Ocurrio un error al obtener la conexion a la db {e}')
    #             sys.exit()
    #     else:
    #         return cls._CONEXION
    #
    # @classmethod
    # def get_cursor(cls):
    #     if cls._CURSOR is None:
    #
    #         try:
    #             cursor = cls.get_conexion().cursor()
    #             cls._CURSOR = cursor
    #             log.info(f'se abrió correctamente el cursor {cls._CURSOR}')
    #             return cls._CURSOR
    #         except Exception as e:
    #             log.error(f'Ocurrio un error al obtener el cursor {e}')
    #             sys.exit()
    #     else:
    #         return cls._CURSOR


if __name__ == "__main__":
    conexion1 = ConexionClase.get_connnection_pool()
    ConexionClase.liberar_conexion(conexion1)
    conexion2 = ConexionClase.get_connnection_pool()
    conexion3 = ConexionClase.get_connnection_pool()
    conexion4 = ConexionClase.get_connnection_pool()
    conexion5 = ConexionClase.get_connnection_pool()
    # conexion6 = ConexionClase.get_connnection_pool()
    # esta linea retornaría un error ya que el pool se vería exhausted

    ConexionClase.cerrar_conexiones()
    print(conexion3)

#     ConexionClase.get_cursor()
