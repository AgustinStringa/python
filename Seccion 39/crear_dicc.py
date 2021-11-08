llaves = ['Nombre', 'Apellido', 'Edad']
valores = ['Agustin', 'Stringa', '19']

diccionario = dict(zip(llaves, valores))
print(diccionario)

diccionario.update(zip(['Edad'], [29]))
print(diccionario)
