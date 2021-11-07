# las listas de listas se manejan como matrices

lista1= [1,2,3,4,5,6,7,8]
lista2 = ['a', 'b', 'c', 'd', 'e']
lista3 = ['summer','winter', 'auttumn']

lista_listas = [lista1, lista2, lista3]
print(lista_listas)

print(lista_listas[0][0])

# con la key indicamos el criterio de orden
# en este caso, por la longitud de la lista
lista_listas.sort(key=len, reverse=True)
print(lista_listas)

lista3 = sorted(lista3)
print(lista3)

