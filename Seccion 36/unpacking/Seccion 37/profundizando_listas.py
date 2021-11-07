pop_punk = ['sum41', 'simple plan', 'blink182', 'nofx']
artistas = 'deryck mark mike billy'.split()
# sumar listas
print(pop_punk + artistas) # genera una lista, pero no modifica las 2 anteriores
#extender listas
pop_punk.extend(artistas) # modifica la lista a la cual se le aplica el metodo
print(pop_punk)

for i in range(0, len(pop_punk)):
    if i == pop_punk.index('sum41'):
        print(pop_punk[i])

# reverse debe aplicarse a una lista
# modifica la misma
pop_punk.reverse()
print(pop_punk)

# sort ordena ascendentemente
pop_punk.sort()
print(pop_punk)

# ordenando al reves
# pop_punk.sort(reverse=True)
print(pop_punk)

# valores minimos y maximos
print(min(pop_punk), max(pop_punk))

# copiar una lista
nueva = pop_punk.copy()
nueva.remove('nofx')
print(nueva)