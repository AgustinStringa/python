class ExcepcionPersonalizada(Exception):
    def __init__(self, mensaje) -> None:
        self.message = mensaje
