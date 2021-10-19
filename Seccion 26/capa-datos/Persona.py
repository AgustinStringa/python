import logging as log
import psycopg2 as db

con = db.connect(user="postgres", password="admin", host="localhost", port="5432", database="test_db_python")

log.basicConfig(level= log.DEBUG, format='%(asctime)s: %(levelname)s [%(filename)s %(lineno)s %(message)s]',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.StreamHandler()
                ])


class Persona:
    def __init__(self, nombre, apellido, email, id_persona =None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def __str__(self):
        return f'''id_persona: {self._id_persona}
nombre: {self._nombre}
apellido: {self._apellido}
email: {self._email}'''

    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email


if __name__ == "__main__":

    una_persona = Persona(00, 'armando', 'bancos', 'elviolado,@gmail.com')
    log.debug(una_persona)
    if (2<1):
        with con:
            with con.cursor() as cursor:
                sql = "SELECT * FROM persona WHERE id_persona = 1"
                cursor.execute(sql)
                result = cursor.fetchone()

                propiedades = []
                for e in result:
                    propiedades.append(e)



                persona1 = Persona(propiedades[0], propiedades[1],propiedades[2],propiedades[3])

                print(persona1)


