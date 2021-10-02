from Producto import *
from Orden import *

mocovi = Producto('arroz', 25.5)
manianita = Producto('yerba', 50)
mineral = Producto('agua', 15)
my_or = Orden(mocovi, manianita)
my_or.add_product(mineral)
my_or.add_product(mocovi)

print(my_or)


orden2 = Orden(mocovi, mocovi, mocovi)
print(orden2)
