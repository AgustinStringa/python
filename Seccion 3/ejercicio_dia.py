calificacion = input("Como estuvo tu dia del 1 al 10 ")

try:
    int(calificacion)
    calificacion = int(calificacion)
    if(calificacion > 0):
        if(calificacion < 3):
            print("mañana será otro día")
        else:
            if(calificacion < 6):
                print("tranqui, pudo ser peor")
            else:
                if(calificacion < 8):
                    print("joya rey, a seguir asi")
                else:
                    if(calificacion < 10):
                        print("Para tirar manteca al techo")
                    else:
                        if(calificacion >= 10):
                            print("estas re pasado de rosca")
    else:
        print("parece que tu dia fue muy malo")
except ValueError:
    print(f"debes introducir un valor numérico entre 1 y 10")
