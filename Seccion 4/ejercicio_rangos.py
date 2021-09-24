valor = input('introduzca un valor ')
min = 0
max = 5


try:
    valor = int(valor)
    if(valor >= min and valor <= max):
        print(f'el valor {valor} se encuentra en el rango')
    else:
        print(f'el valor {valor} NO se encuentra en el rango')
except ValueError:
    print("debes introducir un valor numerico")
