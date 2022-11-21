nombre = 'angel'

def saludar():
    print('Hola desde la funcion saludar')
    print('Hola', nombre)

# funcion con parametros
def saludar2(nombre2):
    global nombre_completo
    nombre_completo = 'Angel Ramon Paz Lopez' 
    print('Hola desde la funcion2 saludar')
    print('Hola', nombre2)

saludar()
#llamando funcion con parametros
saludar2('Angel Ramon')
#llamando variable global creada en la funcion2
print('Hola desde fuera de la funcion2 saludar a', nombre_completo)


