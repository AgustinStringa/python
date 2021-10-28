try:
    import psycopg2
    import psycopg2.extensions
    from Cursor import *
    from Usuario import Usuario
except Exception as e:
    print(f'{e}')
    print(psycopg2)

class UsuarioDAO:
    _SELECCIONAR = "SELECT * FROM usuario"
    _INSERTAR = "INSERT INTO usuario (username, password) VALUES (%s, %s)"
    _ACTUALIZAR = "UPDATE usuario SET username = %s, password = %s WHERE id_usuario = %s"
    _ELIMINAR = "DELETE FROM usuario WHERE id_usuario = %s"

    @classmethod
    def seleccionar(cls):
        with Cursor() as cursor:
            log.debug('Seleccionando usuarios')
            cursor.execute(cls._SELECCIONAR)
            regs = cursor.fetchall()
            lista_usuarios = []

            for e in regs:
                usuario_nuevo = Usuario(e[1], e[2], e[0])
                lista_usuarios.append(usuario_nuevo)
            else:
                return lista_usuarios

    @classmethod
    def insertar(cls, nuevo_usuario):
        with Cursor() as cursor:
            if(isinstance(nuevo_usuario, Usuario)):
                log.debug(f'Insertando usuario {nuevo_usuario}')
                # tambien se podria definir una tupla e incluir esta como segundo parametro
                # en lugar de crearla en el momento
                cursor.execute(cls._INSERTAR, (nuevo_usuario.username, nuevo_usuario.password))
                mod = cursor.rowcount
                return mod
            else:
                log.warning('El argumento enviado debe ser de class Usuario')

    @classmethod
    def actualizar(cls):
        with Cursor() as cursor:
            cursor.execute(cls._SELECCIONAR)
            regs = cursor.fetchall()
            print('REGISTROS'.center(50, '='))
            for e in regs:
                new_user = Usuario(e[1], e[2], e[0])
                print(new_user)

            id = input('introduce el id del registro a actualizar ')
            nuevo_nombre = input('Introduce el nuevo nombre ')
            nuevo_pass = input('Introduce el nuevo password ')
            cursor.execute(UsuarioDAO._ACTUALIZAR, (nuevo_nombre, nuevo_pass, id))
            mod = cursor.rowcount
            return mod

    @classmethod
    def eliminar(cls):
        with Cursor() as cursor:
            cursor.execute(cls._SELECCIONAR)
            regs = cursor.fetchall()
            print('REGISTROS'.center(50, '='))
            for e in regs:
                new_user = Usuario(e[2], e[1], e[0])
                print(new_user)

            id = input('introduce el id del registro a eliminar ')
            cursor.execute(UsuarioDAO._ELIMINAR, (id, ))
            mod = cursor.rowcount
            return mod

if __name__ == '__main__':

    def listar():
        for e in UsuarioDAO.seleccionar():
            print(e)

    def update():
        UsuarioDAO.actualizar()

    def eliminar():
        UsuarioDAO.eliminar()

    def insertar():
        emi = Usuario('emi', 'emi')
        UsuarioDAO.insertar(emi)

    listar()
    input('xxxx')