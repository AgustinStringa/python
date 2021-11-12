variable_global = 'GLOBAL'


def funcion():
    # para evitar error se debe indicar cual es la variable global
    global variable_global

    print(f'La variable global es: {variable_global}')

    # de lo contrario, se considera esta como local, y se estaría llamando en la linea de arriba antes de ser definida
    variable_global = 'modificando valor de la global'

    print(f'La variable global es: {variable_global}')

    print(id(variable_global))


funcion()
