min = int(input('introduce el primer numero del rango '))
max = int(input('introduce el segundo numero del rango '))

while(min < max):
    if(min % 2 == 0):
        print(min)
        min += 1
        continue

    min += 1

else:
    print('fin de la iteracion')
