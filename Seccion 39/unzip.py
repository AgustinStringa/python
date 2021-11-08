# IMPORTANTE
# EL METODO LIST() RECIBE UN SOLO ARGUMENTO

mi_lista = [1, 2, 3, 4, 5]
mi_tupla = ('a', 'e', 'i', 'o', 'u')
mi_dicc = {'ar': 'argentina', 'br': 'brasil',
           'ch': 'chile', 'mx': 'mexico', 'es': 'españa'}

mezcla = zip(mi_lista, mi_tupla, mi_dicc.keys(), mi_dicc.values())

# desempaquetado completo --> print(list(zip(*list(mezcla))))


uno, dos, tres, cuatro = zip(*list(mezcla))

"""
list(mezcla) -> me genera una lista con tuplas [(,) , (,) , (,) ]
el unpacking me da por resultado cada una de estas (1,a,ar,argentina) (2,e,br,brasil) () ()}
si hago sobre eso un zip, alinea los indices y el resultado ahora es : (1,2,3,4,5) (a,e,i,o,u)
solo resta asignar uno de estos a cada variable
uno, dos ,tres, cuatro = zip(*list(mezcla))
"""
