from persona_constructor import Persona_constructor

persona1 = Persona_constructor('Angel Ramon Paz', 34)
persona1.mostrar_datos(); 

print('='*25)

persona2 = Persona_constructor('Ramon Bertilio Paz', 32)
persona2.mostrar_datos(); 

print('Agregar Apellido')
persona2.nombre = 'Ramon Bertilio Paz Lopez'
persona2.mostrar_datos(); 

print(persona1); #Se debe crear un metodo __str__ para que imprima el objeto de manera correcta
#y no solo se visualice el estado en la memoria