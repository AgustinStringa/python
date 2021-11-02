try:
    import psycopg2
    import logger
    import sys
    from UsuarioDAO import UsuarioDAO
    from logger import *
    from Conexion import Conexion
    from Cursor import Cursor
    from Usuario import Usuario
    # quizas importar todo desde Conexion

except Exception as e:
    print(e, type(e))
    input('....')


print(f"Bienvenido al sistema CRUD de usuarios con CAPA DE DATOS!".center(50, "="))


entrada = 0
while entrada != 5:
    try:
        print(f'''Selecciona una opcion
    1 - Listar usuarios registrados
    2 - Registrar un nuevo usuario
    3 - Actualizar un usuario existente
    4 - Eliminar un usuario
    5- Salir del sistema
    ''')
        entrada = int(input('introduce una opcion '))
    except Exception as e:
        continue

    if (1 <= entrada <= 4):

    # Listar
        if entrada == 1:
            try:
                for user in UsuarioDAO.seleccionar():
                    print(user)
            except Exception as e:
                log.error(e, type(e))
    # Insertar
        elif entrada == 2:
            try:
                print('Preparate para insertar un nuevo usuario')
                nombre_insert = input('Introduce el nombre del nuevo usuario ')
                pass_insert = input('Introduce el password del nuevo usuario ')
                user_insert = Usuario(nombre=nombre_insert, password=pass_insert)

                if UsuarioDAO.insertar(user_insert) > 0:
                    print('insertado correctamente')
                else:
                    print('no insertado')

            except Exception as e:
                log.error(e, type(e))
    # Actualizar
        elif entrada == 3:
            try:
                if UsuarioDAO.actualizar() > 0:
                    print(f'Registro actualizado correctamente')
                else:
                    print('Por algún motivo no se ha actualizado registro alguno, intentalo de nuevo :(')
            except Exception as e:
                print(f'error {e, type(e)}')

    # Eliminar
        elif entrada == 4:
            if UsuarioDAO.eliminar() > 0:
                print(f' se ha eliminado correctamente el registro ')
            else:
                print(f'Por algun motivo no se ha eliminado el registro, intentalo de nuevo ')
        elif (entrada == 5):
            continue
    else:
        continue
else:
    print("Saliendo del sistema!".center(50, "="))
    input("...")
    sys.exit()