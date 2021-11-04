cadena = "HOLA \" MUNDO"

print(cadena)

mensaje = "el caracter de escape en python es \\"
print(mensaje)


# raw string
# los raw string ignoran los saltos de lineas o caracteres de escape
raw = r'cadena \ \n con muchas cosas' \
      r'\b, esto se va a imprimir tambien'
print(raw)

print('================')

msg = 'sometimes' \
    \
      ' i wish' \
      ' someone ' \
       'out there will find me'

print(msg)

# cuando escribo cualquier tipo de string, la barra fuera de las comillas indica que la cadena continua en la linea siguiente