from typing import Iterable


letras = ['z', 'a', 'l']
numeros = [4, 89, 2]
letras.sort()
numeros.sort()

print(dir(__builtins__))
# print(sorted(zip(letras, numeros)))
# print(sorted(zip(numeros, letras)))
print(list(zip(numeros, letras)))
