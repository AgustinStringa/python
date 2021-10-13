import psycopg2
try:
    conn = psycopg2.connect(user='postgres', password='admin', host="localhost", port="5432", database="test_db_python")

    print('SISTEMA CRUD EN POSTGRESQL Y PYTHON'.center(50, "-"))


    entrada = 0

    while(entrada != 5):
        print(f'''
        Acciones:
        1- Consultar registros
        2- Agregar registro
        3- Eliminar registro
        4- Actualizar registro
        5- salir
        ''')

        entrada = int(input('introduce el numero respectivo a la accion que quieres realizar '))

        if entrada >=1 and entrada <= 4:
            # consultando registros
            if entrada == 1:
                print('CONSULTAR REGISTRO'.center(50, "-"))

                consul = int(input(f'''
                consultar: 
                1- todas las columnas (tabla persona)
                2- nombres
                3- apellidos
                4- emails
                '''))
                if consul == 1:
                    sql = "SELECT * FROM persona"
                if consul == 2:
                    sql = "SELECT nombre FROM persona"
                if consul == 3:
                    sql = "SELECT apellido FROM persona"
                if consul == 4:
                    sql = "SELECT email FROM persona"

                try:
                    with conn:
                        with conn.cursor() as cursor:
                            cursor.execute(sql, )
                            registros = cursor.fetchall()
                            for e in registros:
                                print(e)
                except Exception as e:
                    print('ocurrió un error en la consulta ')
                    print(e, type(e))
                finally:
                    continue

            #agregando registro
            elif entrada == 2:
                print('AGREGAR REGISTRO'.center(50, "-"))

                try:
                    with conn:
                        with conn.cursor() as cursor:
                            nuevo_nombre = input("introduce el nombre para el nuevo registro ")
                            nuevo_apellido = input("introduce el apellido para el nuevo registro ")
                            nuevo_email = input("introduce el email para el nuevo registro ")

                            sql_insert = "INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)"
                            cursor.execute(sql_insert, (nuevo_nombre, nuevo_apellido, nuevo_email))
                except Exception as e:
                    print('ocurrio un error en la consulta')
                    print(e, type(e))
                finally:
                    print('Estos son los registros ahora'.center(50, "-"))
                    with conn.cursor() as cursor:
                        sql = "SELECT * FROM persona"
                        cursor.execute(sql)
                        registros = cursor.fetchall()
                        for e in registros:
                            print(e)
                    continue

            # eliminando registro
            elif entrada == 3:
                print('ELIMINAR REGISTRO'.center(50, "-"))

                try:
                    with conn:
                        with conn.cursor() as cursor:
                            sql = "SELECT * FROM persona"
                            cursor.execute(sql)
                            registros = cursor.fetchall()
                            print('estos son todos los registros ')
                            for e in registros:
                                print(e)
                            id_remove = input("introduce el id del registro a eliminar ")


                            nuevo_sql = "DELETE FROM persona WHERE id_persona = %s"
                            cursor.execute(nuevo_sql, id_remove)
                except Exception as e:
                        print(e, type(e))
                finally:
                        print('Estos son los registros ahora')
                        sql = "SELECT * FROM persona"
                        cursor.execute(sql)
                        registros = cursor.fetchall()
                        for e in registros:
                            print(registros)
                        continue

            elif entrada == 4:
                print('update')
                try:
                    with conn:
                        with conn.cursor() as cursor:
                            sql = "SELECT * FROM persona"
                            cursor.execute(sql)
                            registros = cursor.fetchall()
                            print('estos son todos los registros ')
                            for e in registros:
                                print(e)
                            #introducir id a updatear
                            id_updated = input("introduce el id del registro a actualizar ")

                            #introduciendo datos
                            nombre_updated = input('introduce el nombre actualizado ')
                            apellido_updated = input('introduce el apellido actualizado ')
                            email_updated = input('introduce el email actualizado ')

                            sql_updated = "UPDATE persona set nombre=%s, apellido=%s, email=%s WHERE id_persona = %s"
                            cursor.execute(sql_updated, (nombre_updated, apellido_updated, email_updated, id_updated))

                            print('ESTOS SON LOS REGISTROS AHORA'.center(50, '-'))

                            mostrar = "SELECT * FROM persona"
                            cursor.execute(mostrar)
                            registros_mostrar = cursor.fetchall()
                            for element in registros_mostrar:
                                print(element)
                except Exception as e:
                    print('error en el update')
                    print(e, type(e))
                finally:
                    continue




        else:
            if entrada == 5:
                print('bye')
            else:
                print('por favor introduce un número válido')
            continue
        #else si entrada no es >=1 y <=4
    else:
    #else de cuando termina el ciclo while
        #cuando no se cumple la condicion
        print('SALIENDO DEL SISTEMA'.center(50, "-"))


except Exception as e:
    print(e, type(e))
finally:
    cursor.close()
    conn.close()