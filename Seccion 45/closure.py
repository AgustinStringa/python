"""
UNA FUNCION CLOSURE ES UNA QUE DEFINE UNA FUNCION INTERNA
ESA INTERNA A SU VEZ PUEDE ACCEDER A LAS VARIABLES DE LA "EXTERNA" Y SER RETORNADA
"""


def operacion(a, b):

    def sumar():
        return a+b

    return sumar


# para que sume es necesario agrear los ()
# esto debido a que operacion retorna la funcion sumar, no un llamado a la misma

# si quisiese eso, debería agregar () en el retorno de operacion y usar:
# print(operacion(5, 6))

print(operacion(5, 6)())
