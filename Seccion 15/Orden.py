class Orden:

    contador_ordenes = 0

    def __init__(self, *productos):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._productos = productos

    def __str__(self):
        return f'Numero de orden: {self._id_orden}, Productos :[{self._productos}]'
