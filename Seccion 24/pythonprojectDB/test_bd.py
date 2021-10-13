import psycopg2
# en lugar de localhost, puede usarse 127.0.0.1
# print(conn)
try:
    conn = psycopg2.connect(user='postgres', password='admin', host="localhost", port="5432", database="test_db_python")

    with conn:
        with conn.cursor() as cursor:
            sql = 'SELECT nombre FROM persona WHERE id_persona = %s'
            placeholder_value = 2
            cursor.execute(sql, (placeholder_value, ))
            registros = cursor.fetchone()

            print(registros)
except Exception as e:
    print(e, type(e))
finally:
    cursor.close()
    conn.close()