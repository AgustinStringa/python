from Dominios.Pelicula import Pelicula
import os

class CatalogoPeliculas:

    ruta_archivos = ''

    def __init__(self, ruta):
        self.ruta = ruta

    def add_pelicula(self, pelicula):
        archivo = open(self.ruta, "a", encoding="utf8")
        archivo.write(f'\n {pelicula}')

    def listar_peliculas(self):
        archivo = open(self.ruta, "r", encoding="utf8")
        for e in archivo.readlines():
            print(e)

    def eliminar_catalogo(self):
        os.remove(self.ruta)


if __name__ == '__main__':
    peli2 = Pelicula('Agente 007')
    # print(peli2.nombre)

    cat = CatalogoPeliculas('catalogo1.txt')
    cat.add_pelicula('La guerra de los clones')
    cat.add_pelicula('mi villano favorito')
    cat.add_pelicula('ghost')
    cat.listar_peliculas()
