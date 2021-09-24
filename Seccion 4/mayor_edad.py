edadMayoria = 18
try:
    edad = input('introduce tu edad')
    int(edad)
    edad = int(edad)
    if(edad > 0):
        if(edad >= edadMayoria):
            print(f'eres mayor de edad, tienes {edad} años')
        else:
            print(f'no eres mayor de edad')
    else:
        print(f'no estamos seguros de que {edad} sea tu edad')
except ValueError:
    print(f"no estamos seguros de '{edad}' que esa sea tu edad")
