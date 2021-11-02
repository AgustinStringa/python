# utilizando split
# split corta la cadena cuando encuentre el caracter pasado por argumento
songs = ' aneurysm  ,   lithium, about a girl,  in bloom , drain you  ,  on a plain'
lista_songs = []

#el valor por defecto cuando se llama split() es el caracter vacio

for e in songs.split(','):
    # strip es como trim de javascript
    e = e.strip()
    lista_songs.append(e)
else:
    print(lista_songs)

# utilizando join
# join agrega en cada uno de los elementos de un iterable la cadena a la cual se esta aplicando el metodo
cadena = ' =.= '.join(lista_songs)
print(cadena)

#cuando se utiliza el metodo join solo se aplica a cadenas
# si se maneja otro tipo de datos, es necesario convertirlos
