num1 = int(input('Introduce el primer operando '))
num2 = int(input('Introduce el segundo operando '))


class Aritmetica():
    """
    Clase aritmetica para realizar operaciones básicas
    """

    def __init__(self, operandoA, operandoB) -> None:
        self.operandoA = operandoA
        self.operandoB = operandoB

    def mostrar_operaciones(self):
        print('Para utilizar esta clase utilice los metodos: sumar(), restar(), multiplicar() y dividir()')
        print(
            'Los operandos que se utilizaran son los enviados a la hora de crear el objeto')

    def sumar(self):
        return f'Suma =  {(int(self.operandoA) + int(self.operandoB))}'

    def restar(self):
        return f'Resta =  {(int(self.operandoA) - int(self.operandoB))}'

    def multiplicar(self):
        return f'Multiplicación =  {(int(self.operandoA) * int(self.operandoB))}'

    def dividir(self):
        return f'División =  {(int(self.operandoA) / int(self.operandoB))}'


clase1 = Aritmetica(num1, num2)

clase1.mostrar_operaciones()
print(clase1.sumar())
print(clase1.restar())
print(clase1.multiplicar())
print(clase1.dividir())
