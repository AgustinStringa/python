# el unpacking es como el destructuring en js
numeros = 1,2,3

num1,num2, _ = numeros

print(num1, num2)

lista_bandas = ['foo fighters', 'nirvana', 'the cranberries', 'meat muppets', 'pearl jam', 'soundgarden', 'queen', 'penultima', 'ultima']

band1, band2, *resto, penult, ult = lista_bandas

print(f'''
band1: {band1}
band2: {band2}
*resto: {resto} clase del resto: {type(resto)}
penult: {penult}
ult: {ult}''')

# al igual que se aplica en listas, se aplica en tuplas


# el unpacking puede utilizarse tambien con el retorno de funciones
def return_many(numero, letra):
    numero = numero * numero
    letra = numero*str(letra)
    return numero, letra


mi_numero, mi_letra = return_many(4, 's')
print(mi_numero, mi_letra)
