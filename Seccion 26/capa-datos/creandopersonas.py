import psycopg2 as db
con = db.connect(user="postgres", password="admin", host="localhost", port="5432", database="test_db_python")

class Persona:
    def __init__(self, id_persona, nombre, apellido, email):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def __str__(self):
        return f'''id_persona: {self._id_persona}
nombre: {self._nombre}
apellido: {self._apellido}
email: {self._email}
        '''

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

            with con:
                with con.cursor() as cursor:
                    sql = "SELECT * FROM persona WHERE id_persona = 1"
                    cursor.execute(sql)
                    result = cursor.fetchone()

                    propiedades = []
                    for e in result:
                        propiedades.append(e)

                    persona1 = Persona(propiedades[0], propiedades[1], propiedades[2], propiedades[3])

                    print(persona1)

if __name__ == "__main__":

    with con:
        with con.cursor() as cursor:
            sql = "SELECT * FROM persona "
            cursor.execute(sql)
            result = cursor.fetchall()

            # lista mayor contiene los datos traidos de la consulta, o sea, una lista de tuplas
            # losta objetos contendrá los objetos creados de la clase persona
            lista_mayor = []
            lista_objetos = []

            # llenando la lista de tuplas traidas de la db
            for e in result:
               lista_mayor.append(e)

            ind = 0
            max = len(lista_mayor)

            # creando objetos y añadiendolos a la lista de objetos
            for i in range(ind, max):
                persona_nueva = Persona(lista_mayor[i][0], lista_mayor[i][1], lista_mayor[i][2], lista_mayor[i][3])
                lista_objetos.append(persona_nueva)

            # utilizando metodo __str__ para mostrar que se crearon correctamente los objetos
            for persona in lista_objetos:
                print(persona)
                print(persona.nombre)

