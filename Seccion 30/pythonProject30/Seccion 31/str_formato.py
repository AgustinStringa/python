"""
dando formato
%s -> para string
%d -> para integer
%.2f -> para flotante con 2 decimales

"""


nombre = 'Agustin'
edad = 22

mensaje = 'Hola, soy %s y tengo años' % (nombre,)
mensaje = 'Hola, soy %s y tengo %d años' % (nombre, edad)

print(mensaje)


