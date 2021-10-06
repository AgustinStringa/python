with open('./Seccion 21/with.txt', 'w', encoding='utf8') as with_archivo:

    linea = ''
    for i in range(1, 11):
        ast = '*'*i + '\n'
        linea += ast
    else:
        with_archivo.write(linea)


with open('./Seccion 21/with.txt', 'r', encoding='utf8') as archivo:
    print(archivo.read())
