try:
    archivo = open('./Seccion 20/prueba.txt', 'w', encoding='utf8')
    archivo.write('Agregando información al archivo')

    numeros = '\n'
    for i in range(0, 101):
        numeros += str(i) + '\n'

    archivo.write(numeros)
except Exception as e:
    print(f'error {e}, {type(e)}')
finally:
    archivo.close()
    txt = 'programa finalizado'
    print(txt.center(100, '-'))
