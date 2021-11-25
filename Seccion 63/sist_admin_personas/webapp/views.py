from django.http.response import HttpResponse
from django.shortcuts import render
import psycopg2
# Create your views here.


def iniciar_webapp(request):
    print(request)
    print(type(request))

    conn = psycopg2.connect(user='postgres', password='admin',
                            host="localhost", port="5432", database="test_db_python")

    with conn:
        with conn.cursor() as cursor:
            sql = 'SELECT * FROM persona '
            cursor.execute(sql)
            registros = cursor.fetchone()

            print(registros)

    return HttpResponse(f"""<html>
    <head></head>
    <body>
        <h1>Hola mundo desde django</h1>
        <table border>
        <tr>
            <td>{registros[0]}</td>
            <td>{registros[1]}</td>
            <td>{registros[2]}</td>
            <td>{registros[3]}</td>

        </tr>
        </table>
        
    </body>
    </html>""")


def farewell(request):
    print(f'la request es {request}')
    return HttpResponse(f"""<html>
    <head></head>
    <body>
        <i>so long and good night</i>
        
    </body>
    </html>""")
