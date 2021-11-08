mi_lista = [1, 2, 3, 4, 5]
mi_tupla = ('a', 'e', 'i', 'o', 'u')
mi_dicc = {'ar': 'argentina', 'br': 'brasil',
           'ch': 'chile', 'mx': 'mexico', 'es': 'españa'}
bases = {'x', 'y', 'z'}

varios_iterables = zip(mi_lista, mi_tupla, mi_dicc, bases)


# iteracion en paralelo

for numero, vocal, inic, value, base in zip(mi_lista, mi_tupla, mi_dicc.keys(), mi_dicc.values(), bases):
    print(f'''
    numero: {numero}
    vocal: {vocal}
    inic: {inic}
    value: {value}
    base: {base}
    ''')

nueva_lista = []
for numero, vocal, inic, value, base in zip(mi_lista, mi_tupla, mi_dicc.keys(), mi_dicc.values(), bases):
    nueva_lista.append(f'{numero}-{vocal}-{inic}-{value}-{base}')
else:
    print(nueva_lista)
