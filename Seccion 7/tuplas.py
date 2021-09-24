equipos = ('barcelona', 'real madrid', 'sporting',
           'manchester', 'boca', 'river', 1, 55)

tupla_individual = ('atras',)

for i in equipos:
    print(i, end=' ')


# print(f'longitud {len(equipos)}')
# print(f'imprimir indice 1: {equipos[1]}')

# print(f'tupla individual: {tupla_individual}')
# print(f'longitud de la tupla individual{len(tupla_individual)}')

print(type(tupla_individual))

lista_individual = list(tupla_individual)
print(type(lista_individual))
tupla_individual = tuple(lista_individual)
print(type(tupla_individual))
