#Clase para donante que visitan el banco de sngre
class Donante:
        def __init__(self, cedula, nombre, apellido):
            """crea y devuelve una instancia de esta clase"""
            self.cedula = cedula
            self.nombre = nombre
            self.apellido = apellido
        
        # @property
        # def cedula(self):
        #     return self.__cedula
        
        # @cedula.setter
        # def cedula(self,cedula):
        #     self.__cedula = cedula

        def __str__(self):
            return f"{self.cedula} {self.nombre_completo}"

        #Metodos de clase, solo pueden ejecutarse haciendo referencia a la clase
        @classmethod
        def registrarse(cls, cedula, nombre, apellido):
            """Este es el metodo de registro"""
            nuevo_donante = cls(cedula, nombre.lower().capitalize(), apellido.lower().capitalize())
            return nuevo_donante
        
        @property
        def nombre_completo(self):
            """Devuelve nombre + " " + apellido"""
            return f"{self.nombre} {self.apellido}"

        def serializar(self):
            """Devuelve un diccionario con data del objeto """
            return {
                "cédula: ": self.cedula,
                "nombre: ": self.nombre,
                "apellido: ": self.apellido,
                "nombre_completo": self.nombre_completo
            }

class Perfil:
        def __init__(self, donante_cedula):
            self.donante_cedula = donante_cedula
            self.hepatitis = None
            self.VIH = None
            self.telefono = ""
            self.fecha_nacimiento = None
            self.email = ""
            self.RH_positivo =None
            self.sangre_tipo = ""

        @classmethod
        def crear(cls, donante_cedula):
            """crea y devuelve una instancia del perfil del donante"""
            return cls(donante_cedula)
        
        def actualizar_perfil(self, diccionario):
            """actualiza prop del perfil segun el contenido del dicc"""
            for (key, value) in diccionario.items():
                if hasattr(self,key):
                    self[key] = value
            return True


