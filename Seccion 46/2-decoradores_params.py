
def FUNCION_A(FUNCION_B):
    def FUNCION_C(*args, **kwargs):
        print('codigo antes de ejecutar'.center(100, '='))
        return FUNCION_B(*args, **kwargs)
    return FUNCION_C


@FUNCION_A
def FUNCION_B(uno, dos):
    return uno + dos


print(FUNCION_B(1, 4))
