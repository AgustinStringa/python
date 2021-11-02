class MiClase:

    '''
    INFO DE LA CLASE
    '''
    def __init__(self):
        '''
        INFO DEL INIT
        '''
        pass

    def mi_metodo(self, param1, param2):
        # si inserto parametros en la declaracion del metodo
        # y debajo escribo triple comilla simple
        # se agrega automaticamente la documentacion de dicho metodo
        '''
        :param param1:
        :param param2:
        :return:
        '''


# ahora que tenemos docstring en la clase podemos utilizar el metodo help() a datos de ese tipo
help(MiClase)
print(MiClase.__doc__)
print(MiClase.__init__.__doc__)
