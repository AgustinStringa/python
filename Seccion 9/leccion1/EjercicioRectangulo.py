b = float(input('introduce la base del rectangulo '))
h = float(input('introduce la altura del rectangulo '))


class Rectangulo:

    def __init__(self, b, h):
        self.b = b
        self.h = h

    def mostrarDetalles(self):
        print(
            f'La base del rectangulo es {self.b} y la altura del mismo es {self.h}')

    def getPerimetro(self):
        return((float(self.b)*2) + (float(self.h)*2))

    def getArea(self):
        return(float(self.b) * float(self.h))


rec1 = Rectangulo(b, h)
rec2 = Rectangulo(5, 10)

# operando con rec1
rec1.mostrarDetalles()
print(f'Perimetro: {rec1.getPerimetro()}')
print(f'Area: {rec1.getArea()}')

# operando con rec2
rec2.mostrarDetalles()
print(f'Perimetro: {rec2.getPerimetro()}')
print(f'Area: {rec2.getArea()}')
