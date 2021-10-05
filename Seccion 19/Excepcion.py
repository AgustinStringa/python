from ExcepcionPersonalizada import ExcepcionPersonalizada
resultado = None


try:
    a = int(input('introduce el divisor '))
    b = int(input('introduce el divisor '))

    if (a == b):
        raise ExcepcionPersonalizada('ambos numeros son identicos')

    resultado = a/b
    print(resultado)
except ZeroDivisionError as zde:
    print(f'Error: "{zde}" {type(zde)}')
except TypeError as te:
    print(f'Error: "{te}" {type(te)}')
except Exception as e:
    print(f'Error: "{e}", {type(e)}')
else:
    print('no se arrojo excepcion alguna')
finally:
    print('termino la ejecucion del bloque try-except')


print('Next...')
