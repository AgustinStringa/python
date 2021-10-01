class Producto:
    contador_productos = 0

    def __init__(self, nombre, precio):
        self._nombre_producto = nombre
        self._precio_producto = precio
        Producto.contador_productos += 1
        self._id_producto = Producto.contador_productos

    def __str__(self):
        return f'nombre_producto: {self._nombre_producto}, precio: {self._precio_producto}, id: {self._id_producto}'


mocovi = Producto('arroz', 25.5)
Manianita = Producto('yerba', 50)
