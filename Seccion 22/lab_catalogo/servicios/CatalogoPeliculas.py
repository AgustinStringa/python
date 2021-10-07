# from dominios.Pelicula import Pelicula


class CatalogoPeliculas:

    ruta_archivo = ''

    def __init__(self, ruta) -> None:
        self._ruta = ruta

    def agregar_pelicula(self, pelicula):
        archivo = open(self._ruta, 'a', encoding='utf8')
        archivo.write(f'\n{pelicula}\n')

    def listar_peliculas(self):
        archivo = open(self._ruta, 'a', encoding='utf8')
        for e in archivo.readlines():
            print(e)

    def eliminar_catalogo(self):
        # import os
        # os.remove(self._ruta)
        pass


# test code
if __name__ == '__main__':
    cat1 = CatalogoPeliculas('catalogo1.txt')
