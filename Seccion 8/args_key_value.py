def listar1(**terminos):
    for k, v in terminos.items():
        print(f'Llave: {k}, Value: {v}')


listar1(a='agustin', b='ballena', c='cancion', d='diccionario')


def listar2(terminos):
    for k, v in terminos.items():
        print(k, v)


diccionario = {
    'a': 'agustin',
    'b': 'ballena',
    'c': 'cancion',
    'd': 'dinosaurio'
}
listar2((diccionario))
