class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def detalle_persona(self):
        print( f'Nombre: {self.nombre} \nEdad: {self.edad}' )

    def __str__(self):
        return f'Nombre: {self.nombre} \nEdad: {self.edad}'

#Clase cliente que heredad de Persona
class Cliente(Persona):
    pass

#Usando la funcion super
# Clase Empleado que hereda de Persona
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        #Sin super seria:
        #Persona.__init__(self, nombre, edad)
        self.sueldo = sueldo

    def detalle_empleado(self):
        super().detalle_persona()
        #Sin super seria:
        #Persona.detalle_persona(self)
        print('Sueldo:',self.sueldo)

    def __str__(self):
        return super().__str__() + f'\nSueldo: {self.sueldo}'
        #Sin super seria:
        #return Persona.__str__(self) + f'\nSueldo: {self.sueldo}'
