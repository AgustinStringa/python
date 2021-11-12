# las funciones son first class citizens

# asignar una funcion a una variable
# puedo acceder a la funcion suma desde otra variable
# no es lo mismo que asignar el resultado de una funcion a una variable

def suma(a, b):
    return a + b


funcion_sumar = suma
print(type(funcion_sumar))
print(funcion_sumar(2, 5))


# pasar funciones como argumentos a otras funciones

def operacion(operando1, operando2, ejecucion):
    return ejecucion(operando1, operando2)


print(operacion(2, 3, suma))
