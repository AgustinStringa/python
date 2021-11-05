titulo_centrado = "ESTE TITULO VA BIEN AL CENTRO"
longitud = len(titulo_centrado)
print(titulo_centrado.center(longitud+50, '='))
# + 50 -> 25 a cada lado


align_start = 'justify-content: start'
align_end = 'justify-content: end'
print(align_start.ljust(100))
print(align_end.rjust(100))


lorem = "orem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

print(lorem.replace(' ', '#=#'))
