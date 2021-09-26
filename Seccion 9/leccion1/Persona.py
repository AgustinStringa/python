
class Persona:

    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def mostrar_detalles(self):
        print(f'''
        Objeto: {self}
        Nombre: {self.nombre}
        Apellidos: {self.apellidos}
        Edad: {self.edad}
        ''')


chabon1 = Persona('Agustin', 'Stringa', 18)
guy2 = Persona('Dave', 'grohl', 52)

# print(f'''
# Objeto: chabon1
# Nombre: {chabon1.nombre}
# Apellidos: {chabon1.apellidos}
# Edad: {chabon1.edad}
# ''')

# modificacion de atributos
chabon1.nombre = 'Ignacio'
chabon1.edad = 6

# print(f'''
# Objeto: chabon1
# Nombre: {chabon1.nombre}
# Apellidos: {chabon1.apellidos}
# Edad: {chabon1.edad}
# ''')

# obtener atributos
print(chabon1.__getattribute__('nombre'))
print(guy2.nombre)


# utilizando metodos de instancia
chabon1.mostrar_detalles()
guy2.mostrar_detalles()

# otra forma de llamar al metodo
# aunque no es la recomendada, puede servir
Persona.mostrar_detalles(guy2)


# agregando atributos fuera de la declaracion de la clase

guy2.band = 'Foo Fighters'

print(guy2.band)
