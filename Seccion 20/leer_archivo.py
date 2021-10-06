try:
    file = open('./Seccion 20/prueba.txt', 'r', encoding='utf8')
    # print(file.read())

    # una vez que se ejecuta el metodo read, no queda mas nada por leer
    # .read() puede recibir por argumento la cantidad de caracteres a leer

    # leer caracteres

    def leer_caracteres():
        print(file.read(2))
        print(file.read(4))

    # leer lineas
    def leer_lineas():
        print(file.readline())
        print(file.readline())
        print(file.readline())

    # iterar archivo
    def iterar_file():
        for i in file:
            print(i)

    print(type(file.readlines()))


except Exception as e:
    print(f'error {e}, {type(e)}')
