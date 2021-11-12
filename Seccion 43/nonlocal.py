# la keyword nonlocal funciona como global, solo que dentro de contextos no globales, como funciones


def funcion_ext():
    var_local_ext = '1'

    def funcion_anidada():
        var_local_anidada = '2'

        nonlocal var_local_ext
        print(f'''local anidada: {var_local_anidada}
        local externa: {var_local_ext}
        ''')

        var_local_ext = 'nuevo valor dado por la function'

        print(f'''local anidada: {var_local_anidada}
        local externa: {var_local_ext}
        ''')
    funcion_anidada()


funcion_ext()
