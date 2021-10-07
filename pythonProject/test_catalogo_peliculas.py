print('Bienvenido al sistema de catalogo de peliculas'.center(100, '-'))
print('Estas son las acciones que puedes realizar:')
print(f'''
1) Agregar pelicula
2) listar películas
3) Eliminar catalogo de peliculas
4) salir
''')

n_cata = input('Introduce el nombre para un nuevo catalogo de peliculas ')

accion = ''

from Servicios.CatalogoPeliculas import CatalogoPeliculas

cat = CatalogoPeliculas(n_cata)

with open(cat.ruta, "a+", encoding="utf8") as archivo:
    while(accion != 4):
        try:
            accion = int(input('Escribe el numero de acción a realizar (1-4) '))
        except Exception as e:
            # print(f'error {e}')
            print('por favor introduce algun valor válido')
            continue

        if (accion >= 1 and accion <= 3):
            if(accion == 1):
                new_film = input('Introduce el nombre de la nueva película ')
                cat.add_pelicula(new_film)
                continue
            elif(accion == 2):
                cat.listar_peliculas()
                continue
            elif(accion == 3):
                archivo.close()
                cat.eliminar_catalogo()
                print(f'Programa finalizado, gracias por usar el sistema!'.center(75, '-'))
                break
        elif(accion != 4):
            print('el numero ingresado no corresponde a alguna accion')
            continue
    else:
        print('saliendo del programa'.center(50, '-'))