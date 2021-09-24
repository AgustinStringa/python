def listar(numero, *nombres, **bandas):

    for name in nombres:
        print(name)

    print(f'el numero introducido fue {numero}')

    for band in bandas:
        print(band)


listar(2, ('agustin', 'ignacio', 'silvana', 'alejandro'),
       ('foo', 'beatles', 'nirvana'))
