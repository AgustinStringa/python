a = input('introduce el primer numero ')
b = input('introduce el segundo numero ')

try:
    a = int(a)
    b = int(b)

    if(not(a == b)):
        if(a > b):
            print(f"{a}, el primer numero introducido es mayor al segundo, {b}")
        else:
            print(f"{a}, el primer numero introducido,  es menor al segundo  {b}")
    else:
        print('los numeros introducidos son iguales')
except ValueError:
    print('debes introducir un valor numérico')
