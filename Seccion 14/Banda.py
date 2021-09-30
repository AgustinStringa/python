class Banda:

    contador_bandas = 0

    def __init__(self, cant, gen) -> None:
        self._miembros = cant
        self._genero = gen
        Banda.contador_bandas += 1
        self._id_banda = Banda.contador_bandas

    def __str__(self) -> str:
        return f'[Cantidad de miembros: {self._miembros} , Genero: {self._genero}, idBanda: {self._id_banda}]'

    variable_clase = 'I\'m in the band'

    @staticmethod
    def descripcion():
        return f'Esto es un metodo estatico, relacionado con la class Banda. Una variable de clase es "{Banda.variable_clase}"'

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)


mcr = Banda(5, 'Pop punk')
blink = Banda(3, 'Skater')
foo = Banda(6, 'Post-Grunge')


# el contexto dinámico puede acceder al contexto estático
# no es necesario pasar el argumento cls, ya que al utilizar una instancia, ya tiene "asociada" su clase
# mcr.metodo_clase()


print(f'La cantidad de objetos creada es: {Banda.contador_bandas}')
