from cursor_pool import CursorPool
import logging as log
from Conexion_clase import ConexionClase as Conexion
from Persona import Persona
import sys


class PersonaDAO:
    """"
    DATA ACCESS OBJECT
    CRUD
    """

    _SELECCIONAR = "SELECT * FROM persona"
    _ELIMINAR = "DELETE FROM persona WHERE id_persona = %s"
    _INSERTAR = "INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)"
    _ACTUALIZAR = "UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona = %s"

    @classmethod
    def seleccionar(cls, final=""):
        cadena = ''
        with CursorPool() as cursor:
            if (final):
                cadena = f"WHERE id_persona = {final}"
                nueva_consulta = f'{cls._SELECCIONAR} {cadena}'
                cursor.execute(nueva_consulta)
                registro = cursor.fetchone()
                persona_nueva = Persona(registro[0], registro[1], registro[2], registro[3])
                return persona_nueva
            else:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []
                for e in registros:
                    persona_nueva = Persona(e[0], e[1], e[2], e[3])
                    personas.append(persona_nueva)
                else:
                    return personas

    @classmethod
    def insertar(cls, persona):
        if isinstance(persona, Persona):
            log.debug(f'persona a insertar {persona}')
            try:
                with CursorPool() as cursor:
                    cursor.execute(cls._INSERTAR, (persona.nombre, persona.apellido, persona.email))
                    reg_modificados = cursor.rowcount
                    if reg_modificados > 0:
                        log.debug(f'objeto insertado {persona}')
                        log.debug(f'modificacion exitosa, {reg_modificados} agregados')
                    else:
                        log.warning('Por algun motivo no hubo modificaciones en la Base de Datos')

            except Exception as e:
                log.error(f'Error al insertar. Error: {e}')
                log.error('Saliendo del sistema'.center(50, '-'))
                sys.exit()
        else:
            log.error(f'Parametro introducido: {persona} no es válido para esta operacion')
            sys.exit()

    @classmethod
    def eliminar(cls, id):

        with CursorPool() as cursor:
            try:
                cursor.execute(cls._ELIMINAR, (id,))
                reg_modificados = cursor.rowcount
                if reg_modificados > 0:
                    log.debug(f'modificacion exitosa, {reg_modificados} eliminado/s')
                else:
                    log.warning(f'Es probable que el id ya se haya eliminado o que dicho id ({id}) no exista')
            except Exception as e:
                log.error(f'Error en la eliminación {e}')
                log.error('Saliendo del sistema'.center(50, '-'))
                sys.exit()

    @classmethod
    def actualizar(cls, persona):
        if isinstance(persona, Persona) and persona.id_persona is not None:
            try:
                with CursorPool() as cursor:
                    cursor.execute(cls._ACTUALIZAR,
                                   (persona.nombre, persona.apellido, persona.email, persona.id_persona))
                    mods = cursor.rowcount
                    if mods > 0:
                        log.debug(f'objeto actualizado {persona}')
                        log.debug(f'Modificacion exitosa, {mods} actualizado correctamente')
                    else:
                        log.warning(f'Es probable que el id ya se haya eliminado o que dicho id ({id}) no exista')
            except Exception as e:
                log.error(f'Ocurrio un error con el UPDATE {e}')
                sys.exit()
        else:
            log.error(f'parametro "{persona}" incorrecto para esta operacion. Se requiere un objeto de clase Persona')
            sys.exit()


if __name__ == "__main__":
    """
    probando seleccionar
    #for e in PersonaDAO.seleccionar():
    #    print(e)
    #    print('------------')    
    
    """

    """
    probando insertar
    #ojo a este codigo, crea registros duplicados

    #new_persona = Persona(69, 'emi', 'gonzalos', 'lalibertad@avanza')
    #PersonaDAO.insertar(new_persona)
    # PersonaDAO.insertar('alber', 'fernandez', 'alferdez@gato.com')

    #otra = Persona('silvia', 'aros','akjsdjakb@gkjbasj')
    #PersonaDAO.insertar(otra)    
    
    """

    """
    probando actualizar
    # PersonaDAO.actualizar('mariano', 'pratto', 'mpra@gmail.com', 16)

    #per_act = Persona('mariana', 'juga el coloso', 'mailfalso@mail.com', 16)
    #PersonaDAO.actualizar(per_act)    
    
    """

    """
    probando eliminar
    # PersonaDAO.eliminar(18)    
    """

