# ahora la funcion interna es una lambda
# se trabaja igual y no se definen los params en la misma, los toma del entorno local

def operar(a, b):

    return lambda: a - b


print(operar(5, 9)())
