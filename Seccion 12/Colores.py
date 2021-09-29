class Colores:
    def __init__(self, nombre, hexadecimal) -> None:
        self._nombre_color = nombre
        self._hexadecimal = hexadecimal

    def get_hexa(self):
        return self._hexadecimal

    def __str__(self):
        return f'''Colores -> [nombre_color: "{self._nombre_color}"  hexadecimal: "{self._hexadecimal}"]'''

    """
    NOMBRE
    """
    @property
    def nombre(self):
        return self._nombre_color

    @nombre.setter
    def base(self, nombre):
        self._nombre_color = nombre

    """
    COD HEXADECIMAL #
    """
    @property
    def hexadecimal(self):
        return self._hexadecimal

    @hexadecimal.setter
    def hexadecimal(self, hexadecimal):
        self._hexadecimal = hexadecimal
