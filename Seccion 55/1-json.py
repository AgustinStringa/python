from urllib.request import Request, urlopen
import json
import pprint as pp
# URL DE CONSULTA

URL = Request('http://globalmentoring.com.mx/api/personas.json')
# print(type(URL)) # <class 'urllib.request.Request'>

# SE AGREGA UN HEADER DE LECTURA EN HTML A LA CADENA URL QUE SE CREÓ

URL.add_header(
    'User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0')

# SE HACE LA CONEXIÓN YA CON EL HEADER

respuesta = urlopen(URL)

# print(respuesta) # htt.client.HTTPResponse object

# SE LEE EL CUERPO DE LA RESPUESTA

cuerpo_respuesta = respuesta.read()  # cadena en binario

json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))
pp.pprint(json_respuesta)  # se convierte en un diccionario
print(type(json_respuesta))

for e in json_respuesta['personas']:
    print(e)
