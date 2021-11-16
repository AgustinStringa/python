
def funcion_decorador_a(funcion_a_decorar):
    def funcion_decorada_c():
        #print(f'Mandaste la funcion {funcion_a_decorar}')
        print(f'La funcion se ejecuta desde {funcion_decorador_a}')
        funcion_a_decorar()

    def otra_funcion():
        print('ESTA ES OTRA FUNCION')

    return funcion_decorada_c


@funcion_decorador_a
def mostrar_mensaje():
    print('Hello from mostrar_mensaje')


# print(f'Funcion decorador a: {funcion_decorador_a}')
# print(f'Funcion a decorador b: {mostrar_mensaje}')
# print(f'Funcion decorada c: {funcion_decorador_a(mostrar_mensaje)}')
# print('ejecutando funcion con decorador "B"'.center(100, '='))
mostrar_mensaje()
