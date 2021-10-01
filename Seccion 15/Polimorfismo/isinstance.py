from Empleado import Empleado
from Gerente import Gerente
from test_polimorfismo import *

print(isinstance(emp1, Empleado))
print(isinstance(emp1, Gerente))

# print(isinstance(ger, Empleado))
# print(isinstance(ger, Empleado))

lista = [1, 2, 3, 4, 5, 6]
tupla = (1, 2, 3, 4, 5, 6)
elset = {1, 2, 3, 4, 5, 6}
print(isinstance(lista, object))
print(isinstance(tupla, object))
print(isinstance(elset, object))
