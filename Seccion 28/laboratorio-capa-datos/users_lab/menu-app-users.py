try:
    import psycopg2 as bs
    import logging as log

    log.basicConfig(level=log.DEBUG, format='%(asctime)s: %(levelname)s [%(filename)s %(lineno)s %(message)s]',
                    datefmt='%I:%M:%S %p',
                    handlers=[
                        log.StreamHandler()
                    ])

    print(f'''modulo {bs} importado correctamente
modulo {log} importado correctamente''')
    print(bs)
    print(log)
except Exception as e:
    print(e, type(e))
    input('....')


print(f"Bienvenido al sistema CRUD de usuarios con CAPA DE DATOS!".center(50, "="))
print(f'''
Selecciona una opcion
1 - Listar usuarios registrados
2 - Registrar un nuevo usuario
3 - Actualizar un usuario existente
4 - Eliminar un usuario
5- Salir del sistema
''')

entrada = 0
while entrada != 5:
    try:
        entrada = int(input('introduce una opcion '))
    except Exception as e:
        continue
    if (1 <= entrada <= 4):
        if entrada == 1:
            log.info(f'pulsaste {entrada}')
        elif entrada == 2:
            log.info(f'pulsaste {entrada}')
        elif entrada == 3:
            log.info(f'pulsaste {entrada}')

        elif entrada == 4:
            log.info(f'pulsaste {entrada}')
        elif (entrada == 5):
            continue
    else:
        continue
else:
    print("Saliendo del sistema!".center(50, "="))
    input("...")