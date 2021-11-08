diccionario = {'em': 'emiliano', 'teac': 'silvina'}
term1, term2 = diccionario

numeros = [1, 2, 3]


def sumar(a, b, c):
    return a+b+c


print(sumar(*numeros))


def multiplicar(a, b, c):
    a = a*a
    b = b*b
    c = c*c
    return (a, b, c)


retorno1, retorno2, retorno3 = multiplicar(5, 10, 15)
print(*multiplicar(5, 18, 8273))

# unir listas
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [*list1, *list2]
print(list3)

# funciona igual para diccionarios, solo que con **

cadena = 'matias, agustin, alberto'
lista_str = [*cadena.split(',')]
print(lista_str)
