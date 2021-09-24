print('TIENDA DE LIBROS')
nombre = input('introduce el nombre del libro ')
isbn = input('introduce el isbn del libro ')
precio = float(input('introduce el precio (coma flotante) '))
envio = input('el envío es gratis? True/False ')


# al castear una cadena a tipo booleano de la forma
# bool() dará True si contiene algo distinto de vacío
# y False en caso contrario
# por tanto la conversion debe realizarse de otra forma

if envio == 'True':
    envio = True
elif envio == 'False':
    envio = 'el valor del envio es $50.0'
else:
    envio = 'error en el envío, debes introducir "True" o "False"'


print("-----------------INFORMACION DEL LIBRO-----------------")

print(f'''
nombre: {nombre}
isbn: {isbn}
precio: {precio}
envio gratis: {envio}
''')
