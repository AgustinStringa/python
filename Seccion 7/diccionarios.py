from typing import Counter


diccionario1 = {
    'primero': 'enero',
    'segundo': 'febrero',
    'tercero': 'marzo'
}

for llave, valor in diccionario1.items():
    print(llave, valor)

for llave in diccionario1.keys():
    print(llave)

for valor in diccionario1.values():
    print(valor)

print('primero' in diccionario1)
