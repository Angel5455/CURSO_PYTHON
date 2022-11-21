class Persona(object):
    def __init__(self, nombre):
        self.nombre = nombre

    def moverse(self):
        print(self.nombre, 'Ando Caminando')

class Atleta(Persona):

    def moverse(self):
        print(self.nombre,'Ando Corriendo')

class Ciclista(Persona):
    
    def moverse(self):
        print(self.nombre,'Ando moviendome en mi bicicleta')
