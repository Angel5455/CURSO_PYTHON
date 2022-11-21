from persona import Persona

persona1 = Persona('Angel', 34)
persona1.__nombre = "Ramon"
print(persona1.__nombre); 
print(persona1)

print('='*25)
#Para modificar un objeto usamos el get y set en la clase Persona
persona1.set_nombre("Angel Ramon Paz")
print(persona1.get_nombre()); 
print(persona1); 