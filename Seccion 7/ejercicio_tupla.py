tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []
j = 0


for i in tupla:
    if(i < 5):
        lista.insert(j, i)
        j += 1

lista.sort()
print(lista)
