class Usuario:
    def __init__(self, nombre, email, contraseña):
        self.nombre = nombre
        self.email = email
        self.__contraseña = contraseña

    def get_contraseña(self):
        return self.__contraseña

