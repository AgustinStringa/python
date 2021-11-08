# print(dir(__builtins__))
# help(zip)


mi_lista = [1, 2, 3, 4, 5]
mi_tupla = ('a', 'e', 'i', 'o', 'u')
mi_dicc = {'ar': 'argentina', 'br': 'brasil',
           'ch': 'chile', 'mx': 'mexico', 'es': 'españa'}

mezcla = zip(mi_lista, mi_tupla)
print(list(mezcla))
print(list(mezcla))
print(tuple(mezcla))
print(tuple(zip(mi_lista, mi_tupla)))

"""
zip genera un iterable. Por defecto puede recorrerse con un for
si se imprime, muestra un objeto de clase zip.
Para "desempaquetarle", es necesario pasarlo como param al constructor list()
una vez que se leen o se consumen, se altera el estado del objeto zip
por tanto puede que sea neceseario volver a crearle
"""

# si cuando se unen iterables el len() de uno es mayor al de otros
# la union se realiza la cantidad de veces == al len() del menor
# un zip de iterables len(4) len(3) y len(5) genera 3 "posiciones"

# definiendo un set y "mezclando"
conjunto = {28, 928, 137, 491}
letras = ('a', 'e', 'i', 'o', 'u')
zipeado = zip(conjunto, letras)
print(list(zipeado))
