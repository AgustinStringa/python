from Empleado import Empleado


class Gerente(Empleado):
    def __init__(self, nombre, sueldo, depto) -> None:
        super().__init__(nombre, sueldo)
        self.depto = depto

    def __str__(self) -> str:
        return f'Gerente Departamento: "{self.depto}" {super().__str__()}'
