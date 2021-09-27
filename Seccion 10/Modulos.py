#from Coche import *
from Coche import Coche

print('creando objetos'.center(50, '='))
fiat_uno = Coche('fiat', 'crema')
fiat_uno.mostrar_detalles()

print('eliminando objetos'.center(50, '='))
del fiat_uno

fiat_uno.mostrar_detalles()
