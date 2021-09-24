edad = input('introduce tu año de nacimiento ')
edad = int(edad)
actual = 2021

result = actual - edad
veintes = (result >= 20) and (result < 30)
treintas = (result >= 30) and (result < 40)

if(veintes or treintas):
    if(veintes):
        print(f'tienes {result} estás entre los 20\'s')
    elif(treintas):
        print(f'tienes {result} estás entre los 30\'s')
    #print(f'estas entre los 20\'s y 30\'s, tienes {result}')
else:
    if(result < 20):
        print(f"tienes menos que 20, tienes {result}")
    else:
        print(f"tienes más de 40, tienes {result}")
