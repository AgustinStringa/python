print('Bienvenido al sistema de catalogo de peliculas'.center(100, '-'))
print('Estas son las acciones que puedes realizar:')
print(f'''
1) Agregar pelicula
2) listar películas
3) Eliminar catalogo de peliculas
4) salir
''')

accion = ''

while(accion != 4):
    accion = int(input('Escribe el numero de acción a realizar (1-4) '))

    if (accion >= 1 and accion <= 3):
        if(accion == 1):
            pass
        elif(accion == 2):
            pass
        elif(accion == 3):
            pass
    else:
        print('el numero ingresado no corresponde a alguna accion')
        continue
else:
    print('saliendo del programa'.center(50, '-'))
