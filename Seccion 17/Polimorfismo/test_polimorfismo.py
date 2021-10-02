from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto))


emp1 = Empleado('Ale', 90000)
# imprimir_detalles(emp1)

ger = Gerente('john', 150000, 'Sist')
# imprimir_detalles(ger)


if __name__ == '__main__':
    # codigo a omitir en importaciones
    print(__name__)
# a pesar de llamar un metodo declarado solo en la clase padre y heredado por la clase hija
# el resultado está declarado en la clase hija
# esto es debido a que detallar() recibe self como parametro e invoca a __str__
# como self apunta a un objeto de tipo Gerente, el __str__ que se invoca es el de la clase Gerente
    print(emp1.detallar())
    print(ger.detallar())
