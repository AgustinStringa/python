
def imprimirNumeros(num):
    if num == 1:
        return 1
    else:
        print(num)
        return imprimirNumeros(num-1)


print(imprimirNumeros(5))
