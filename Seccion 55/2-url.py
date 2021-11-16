from urllib import request
import pprint as pp

reqres = 'https://reqres.in/api/users/2'


pagina = request.urlopen(
    "http://www.scratchya.com.ar/pythonya/ejercicio336/pagina1.html")
datos = pagina.read()
datos_decodificados = datos.decode('utf-8')

print(datos_decodificados)
