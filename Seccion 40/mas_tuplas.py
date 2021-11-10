# swap
h = 'Hi'
b = 'Bye'

# pueden omitirse los parentesis, pero no deja de ser una tupla
(h, b) = (b, h)

print(f'''
h: {h}
b: {b}
''')

#


def minmax(elements):
    return min(elements), max(elements)


mi_min, mi_max = (minmax((3, 4, 5, 99, -12, 9823)))
print(f'''
mi_min= {mi_min}
mi_max= {mi_max}
''')

# retornar la suma de una tupla


def sumar(*elementos):
    return sum(elementos)


print(sumar(1, 5, 3, 1, 5, 8, 9))
