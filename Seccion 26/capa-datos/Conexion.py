import psycopg2

class Conexion:
    def __init__(self, DATABASE, USERNAME="postgres", PASSWORD="admin", DB_PORT="5432", HOST="localhost"):
        self._DATABASE = DATABASE
        self._USERNAME = USERNAME
        self._PASSWORD = PASSWORD
        self._DB_PORT = DB_PORT
        self._HOST = HOST
        self._CONEXION = psycopg2.connect(user=self._USERNAME,
                                          password=self._PASSWORD,
                                          host=self._HOST,
                                          port=self._DB_PORT,
                                          database=self._DATABASE )
        self._CURSOR = self._CONEXION.cursor()



    def get_conexion(self):
        return self._CONEXION


    def get_cursor(self):
        return self._CURSOR


    def cerrar(cls):
        cls._CONEXION.close()
        return f'conexion cerrada exitosamente'


if __name__ == '__main__':

    nueva = Conexion('test_db_python', 'postgres', 'admin', '5432', 'localhost')

    sql = "SELECT * FROM persona"
    nueva.get_cursor().execute(sql)

    regs = nueva.get_cursor().fetchall()

    for e in regs:
        print(e)
