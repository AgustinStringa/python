def calculadora(a, b):

    def sumar(a, b):
        return float(a)+float(b)

    print(f'Suma: {sumar(a, b)}')

    def restar(a, b):
        return a-b

    print(f'Resta: {restar(a, b)}')

    def mult(a, b):
        return a*b

    print(f'Multiplicacion: {mult(a, b)}')


num1 = float(input('Introduce el primer numero para la calculadora '))
num2 = float(input('introduce el segundo numero para la calculador '))

calculadora(num1, num2)
