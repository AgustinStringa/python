class Persona:
    def __init__(self, nombre, edad) -> None:
        self._nombre = nombre
        self._edad = edad

    def mostrar_detalles(self):
        print(f'{self._nombre, self._edad}')

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @edad.setter
    def edad(self, edad):
        self._edad = edad


stri = Persona('Agustin', 10)

stri.mostrar_detalles()
print(stri.nombre)
stri.edad = 19
print(stri.edad)
