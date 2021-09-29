from FiguraGeometrica import FiguraGeometrica
from Colores import Colores
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('creacion de objeto cuadrado'.center(50, '-'))
lado = int(input('introduce el valor del lado '))
nombre_color_cua = input('introduce el nombre del color ')
hexa_cua = input('introduce el codigo hexadecimal del color ')

cuadrado1 = Cuadrado(lado, nombre_color_cua, hexa_cua)
print(cuadrado1)

print('creacion de objeto rectangulo'.center(50, '-'))

base = int(input('introduce el valor de la base '))
alt = int(input('introduce el valor de la altura '))
nombre_color_rec = input('introduce el nombre del color ')
hexa_rec = input('introduce el codigo hexadecimal del color ')
rectangulo1 = Rectangulo(base, alt, nombre_color_rec, hexa_rec)
print(rectangulo1)
