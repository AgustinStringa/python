from Producto import *


class Orden:

    contador_ordenes = 0

    def __init__(self, *productos):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos)
        # con list() convierto al tipo de lista el valor obtenido
        # similar a int()

    def add_product(self, producto_nuevo):
        if (isinstance(producto_nuevo, Producto)):
            self._productos.append(producto_nuevo)
        else:
            alerta = f'ALERT - no es posible agregar el producto "{producto_nuevo}"'
            print(
                alerta.center(100, '-'))

    def calc_precio(self):
        precio = float(0)
        contador = 0
        for e in self._productos:
            if(isinstance(e, Producto)):
                precio += e.precio
                contador += 1
        else:
            precio = float(precio)
            return(f'el precio de la orden es ${precio}')
            # La cantidad de productos es: {contador}

    def __str__(self):
        str_productos = f'\n'
        count = 0
        for e in self._productos:
            str_productos += f'{e.__str__()}\n'
            count += 1
        return f'[Numero de orden: {self._id_orden}, Precio: {self.calc_precio()}, Productos ({count} en total) :{str_productos}'


# if __name__ == '__main__':
