contador = 0


def show_count():
    print(f'Contador= {contador}')


def increase_count(v):
    global contador
    contador += v


show_count()
increase_count(25)
increase_count(2)
show_count()
