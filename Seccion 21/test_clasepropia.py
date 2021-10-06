from ManejoArchivos import ManejoArchivos

with ManejoArchivos('./Seccion 21/with.txt') as archivo:
    print(archivo.read())
