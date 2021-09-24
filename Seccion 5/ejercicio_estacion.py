mes = int(
    input('introduce el mes del año para obtener la estacion a la que corresponde (1-12) '))

estacion = None
if(not(mes < 1 or mes > 12)):

    if(mes == 1 or mes == 2):
        estacion = 'Verano'
    elif(mes == 3):
        estacion = 'Verano/otoño'
    elif(mes == 4 or mes == 5):
        estacion = 'Otoño'
    elif(mes == 6):
        estacion = 'Otoño/invierno'
    elif(mes == 7 or mes == 8):
        estacion = 'Invierno'
    elif(mes == 9):
        estacion = 'Invierno/primavera'
    elif(mes == 10 or mes == 11):
        estacion = 'Primavera'
    elif(mes == 12):
        estacion = 'Primavera/Verano'

    print(f'para el mes {mes} la estacion es {estacion}')
else:
    print('error con el numero introducido')
    exit(1)

print('esto no debería imprimirse en caso de fallar con el numero')
