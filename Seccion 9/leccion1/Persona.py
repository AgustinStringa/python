
class Persona:

    def __init__(self, nombre, apellidos, edad, *terminos, **valores):
        self._nombre = nombre
        self._apellidos = apellidos
        self._edad = edad
        self.terminos = terminos
        self.valores = valores

    # declaracion de atributos encapsulados _

    def mostrar_detalles(self):
        print(f'''
        Objeto: {self}
        Nombre: {self._nombre}
        Apellidos: {self._apellidos}
        Edad: {self._edad}
        Terminos: {self.terminos}
        Valores: {self.valores}
        ''')


chabon1 = Persona('Agustin', 'Stringa', 18, '3467412255', 'San Martin 1763',
                  'Cruz Alta', 'Cordoba', m='manzana', p='pera', a='azul')
guy2 = Persona('Dave', 'grohl', 52)

# print(f'''
# Objeto: chabon1
# Nombre: {chabon1.nombre}
# Apellidos: {chabon1.apellidos}
# Edad: {chabon1.edad}
# ''')

# modificacion de atributos
chabon1._nombre = 'Ignacio'
chabon1._edad = 6

# print(f'''
# Objeto: chabon1
# Nombre: {chabon1.nombre}
# Apellidos: {chabon1.apellidos}
# Edad: {chabon1.edad}
# ''')

# obtener atributos
print(chabon1.__getattribute__('_nombre'))
print(guy2._nombre)


# utilizando metodos de instancia
chabon1.mostrar_detalles()
guy2.mostrar_detalles()

# otra forma de llamar al metodo
# aunque no es la recomendada, puede servir
Persona.mostrar_detalles(guy2)


# agregando atributos fuera de la declaracion de la clase

guy2.band = 'Foo Fighters'

print(guy2.band)
