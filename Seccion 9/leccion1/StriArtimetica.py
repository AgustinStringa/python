
class Aritmetica():
    """
    Clase aritmetica para realizar operaciones básicas
    """

    def __init__(self) -> None:
        pass

    def mostrar_operaciones(self):
        print('Para utilizar esta clase utilice los metodos: sumar(), restar(), multiplicar() y dividir()')

    def sumar(self, a, b):
        return f'Suma =  {(int(a) + int(b))}'

    def restar(self, a, b):
        return f'Resta =  {(int(a) - int(b))}'

    def multiplicar(self, a, b):
        return f'Multiplicacion =  {int(a) * int(b)}'

    def dividir(self, a, b):
        return f'Division =  {(int(a) / int(b))}'


stri1 = Aritmetica()
print(stri1.sumar(1, 6))
print(stri1.dividir(24, 6))
