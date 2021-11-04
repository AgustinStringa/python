cadena_string = 'Programación con Python'

cadena_bytes = cadena_string.encode('UTF-8')
print(cadena_bytes)

print(cadena_bytes.decode("UTF-8"))

# apuntan al mismo objeto en memoria
print(cadena_string.__str__)
print(cadena_bytes.decode().__str__)


print(id(cadena_bytes.decode()))
print(id(cadena_string))
