green_eyes = {'coldplay', 'yo', 'mariana'}
brown_eyes = {'juan', 'matias'}
menores = {'yo', 'juan'}
mayores = set()

# OPERACIONES DE CONJUNTO

print(f'Union entre ojos verdes y menores: {green_eyes.union(menores)}')
print(
    f'Interseccion entre ojos verdes y menores: {green_eyes.intersection(menores)}')

print(
    f'Interseccion entre ojos verdes y marrones: {green_eyes.intersection(brown_eyes)}')  # conjunto vacio

# asignando valores a mayores (vacio)
todos = green_eyes.union(brown_eyes)
mayores = set(todos.difference(menores))

print(f'mayores= {mayores}')
