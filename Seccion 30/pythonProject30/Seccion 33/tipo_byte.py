# un byte son 8 bits
# es el minimo elemento de memoria direccionable de una computadora

chars_en_byte = b'hi fucking world'
print(chars_en_byte)
print(type(chars_en_byte))
print(chars_en_byte[0]) # valor en ascii de la primera posicion de la cadena
print(chr(chars_en_byte[0])) # conversion de byte al caracter