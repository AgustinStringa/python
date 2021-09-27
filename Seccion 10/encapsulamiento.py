class Persona:
    def __init__(self, nombre, edad) -> None:
        self.__nombre = nombre
        self.__edad = edad

    def mostrar_detalles(self):
        print(f'{self.__nombre, self.__edad}')


stri = Persona('Agustin', 10)
stri.mostrar_detalles()

stri.__nombre = 'asd'
stri.mostrar_detalles()

# estableciendo __ antes del nombre del atributo se restringe el acceso desde fuera de la clase
