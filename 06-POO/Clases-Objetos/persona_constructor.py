class Persona_constructor:
    #Atributos

    #constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad 


    #Metodos
    def mostrar_datos(self):
        print('Nombre:', self.nombre)
        print('Edad:', self.edad)

    #Delvolver el estado de un objeto
    def __str__(self):
        return f'Nombre {self.nombre} \n Edad: {self.edad}'