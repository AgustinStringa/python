from Persona import Persona


class Empleado(Persona):
    def __init__(self, nombre, apellidos, edad, sueldo, empresa):
        super().__init__(nombre, apellidos, edad)
        self._nombre = nombre
        self._apellidos = apellidos
        self._edad = edad
        self._sueldo = sueldo
        self._empresa = empresa

    def __str__(self) -> str:
        return f'Empleado-> [Sueldo: {self._sueldo}, Empresa: {self._empresa}] {super().__str__()} ]'


# peon = Empleado('Juan', 'Perez', 29, 80000, 'Globant')
# print(peon._sueldo)
# print(peon._empresa)
