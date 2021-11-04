import urllib.request
from urllib.request import urlopen
import re
# print(urlopen) -> es una funcion

numeros = []
for e in range(1,21):
    numeros.append(str(e))
else:
    print(numeros)


req = urllib.request.Request('http://globalmentoring.com.mx/recursos/GlobalMentoring.txt',
                             headers={
                                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})

with urlopen(req) as mensaje:
    with open('archivo_numeros.txt', 'a', encoding='utf-8') as file_numbers:
        """
        for linea in mensaje.readlines():
            strr = linea.decode('utf-8')
            if re.search(r'\d', strr):
                file_numbers.write(strr)
        """


    contenido = mensaje.read()
    contenido_decodificado = contenido.decode('utf-8')
    print(contenido_decodificado.count('Universidad'))
    print('python'.lower() in contenido_decodificado.lower())

    # variable.startswith('asd')
    # variable.endswith('asd')


with open('nuevo_archivo.txt', 'a', encoding='utf-8') as archivo:
    #archivo.write(contenido_decodificado)
    #archivo.write('\nContenido leido desde la web')
    pass


