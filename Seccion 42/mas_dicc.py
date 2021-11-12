from pprint import pprint as pp
nuevo_dicc = {'nombre': 'stri', 'generator': True, 'alumno': 'regular'}

print(nuevo_dicc['generator'])


# RECUPERANDO DATOS DE UN DICC
# produce una exception
# print(nuevo_dicc['apellido'])
# get no produce una exception
# get(llave-pedida, valor-por-defecto)
print(nuevo_dicc.get('apellido', 'no se encontró'))


# setdefault -> en caso de que no exista la crea con el valor default
# -> en caso de que sí, la retorna
print(
    nuevo_dicc.setdefault('nombres', 'valor default')
)
print(nuevo_dicc)


# pprint --> pretty print
# --> por default tiene muchos parametros como por ejemplo sort_dics=True
help(pp)

pp(nuevo_dicc, width=10, sort_dicts=False, compact=True)
