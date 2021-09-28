class Persona:

    def __init__(self, nombre, apellidos, edad):
        self._nombre = nombre
        self._apellidos = apellidos
        self._edad = edad

    # declaracion de atributos encapsulados _

    def mostrar_detalles(self):
        print(f'''
        Objeto: {self}
        Nombre: {self._nombre}
        Apellidos: {self._apellidos}
        Edad: {self._edad}
        ''')

    # sobreescribiendo el metodo __str__ de la clase object
    # este es el metodo que se "llama" cuando se realiza un :
    # print(object)
    def __str__(self) -> str:
        return f'Persona-> [ Nombre: {self._nombre}, Apellidos: {self._apellidos}, Edad: {self._edad}]'
