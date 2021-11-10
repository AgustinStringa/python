lista = [1, 2, 5, 3, 2, 6674, 234, 6783]
tupla = ('a', 'b', 'c', 'd', 'e', 'f')

conjunto_numeros = set(lista)
conjunto_letras = set(tupla)


# añadiendo tuplas a un set
conjunto_numeros.add((42, 69))  # agrega la tupla

conjunto_numeros.update({42, 69})  # agrega los valores individuales
conjunto_numeros.update({42, 69})  # agrega los valores individuales


print(conjunto_numeros)

# copiar un set
# copia poco profunda, se copian las referencias
copia_pocoprofunda = conjunto_numeros.copy()
copia_profunda = set(conjunto_numeros)

print(f'''
original: {id(conjunto_numeros)}
poco profunda: {id(copia_pocoprofunda)}
profunda: {id(copia_profunda)}
''')

print(conjunto_numeros is copia_profunda)
print(conjunto_numeros is copia_pocoprofunda)
