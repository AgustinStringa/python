class Usuario:

    def __init__(self, nombre=None,password=None, id_usuario=None):
        self._id_usuario = id_usuario
        self._username = nombre
        self._password = password

    """
    GETTERS Y SETTERS
    """
    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id):
        self._id_usuario = id

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, nombre):
        self._username = nombre

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, passw):
        self._password = passw

    def __str__(self):
        return f"""Username: {self._username}
Password: {self._password}
id: {self._id_usuario}
"""
