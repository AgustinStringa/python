class ManejoArchivos:

    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def __enter__(self):
        print('estamos abriendo el archivo'.center(50, '-'))
        self.nombre = open(self.nombre, 'r', encoding='utf8')
        return self.nombre

    def __exit__(self, execption_type, exception_value, trace_back):
        print('closing the fucking file'.center(50, '-'))
        if self.nombre:
            self.nombre.close()


with ManejoArchivos('./Seccion 21/with.txt') as archivo:
    print(archivo.read())
