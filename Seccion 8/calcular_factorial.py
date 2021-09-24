numero = int(input('introduce un numero para calcular su factorial '))
fact = 1
for i in range(1, numero+1):
    mult = 1 * i
    fact = fact * mult
    print(fact)
