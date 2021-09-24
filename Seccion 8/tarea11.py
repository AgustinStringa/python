def multiplicar(*numeros):
    producto = 1
    for num in numeros:
        producto *= num
    else:
        return producto


print(multiplicar(1, 2, 3, 4, -5))
