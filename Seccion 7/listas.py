names = ['juan', 'delfina', 'carlos', 'maria']

for elemento in names:
    print(elemento)

print(names[-1])

# recorre desde el primer indice hasta el segundo, sin incluirle
# si el indice inicial es 0, puede omitirse, de esta forma
# print(names[:2])
print(names[0:2])

# recorre desde el indice indicado hasta el final
print(names[1:])

# add
names.append('alejandro')
print(names)
