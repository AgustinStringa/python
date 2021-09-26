alto = float(input('introduce el alto del cubo '))
largo = float(input('introduce el largo del cubo '))
profundo = float(input('introduce la profundidad del cubo '))


class Cubo:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def getVolume(self):
        return (f'El volumen del cubo es {self.x*self.y*self.z}')


cubito = Cubo(largo, alto, profundo)

print(cubito.getVolume())
