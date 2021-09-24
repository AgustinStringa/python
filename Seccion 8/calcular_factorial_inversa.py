entrada = int(input('introduce un numero para calcular su factorial '))


def calcularFactorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * calcularFactorial(numero-1)


print(f'el factorial de {entrada} es {calcularFactorial(entrada)}')
