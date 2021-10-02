class Producto:
    contador_productos = 0

    def __init__(self, nombre, precio):
        self._nombre_producto = nombre
        self._precio_producto = precio
        Producto.contador_productos += 1
        self._id_producto = Producto.contador_productos

    def __str__(self):
        return f'[id: {self._id_producto} nombre: {self._nombre_producto}, precio: {self._precio_producto}]'

    @property
    def precio(self):
        return self._precio_producto


if __name__ == '__main__':
    mocovi = Producto('arroz', 25.5)
    manianita = Producto('yerba', 50)
    print(mocovi)
    print(manianita)
