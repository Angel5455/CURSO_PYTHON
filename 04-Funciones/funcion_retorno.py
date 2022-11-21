def saludar():
    return 'Hola Mundo desde la funcion'

def saludar2():
    global nombre 
    nombre = 'angel'
    edad = 24
    return 'Hola Mundo desde la funcion', nombre, edad

print(saludar())

#utilizando variables
valor = saludar()
print('utilizando variables', valor)

valor2 = saludar2()
#obtendremos una tupla
print("resultado de funcion saludar2", valor2)
#mostrar por separado los valores de la tupla
print('-'*50)
saludo, nombre, edad = saludar2()
print(saludo); 
print('nombre', nombre)
print('edad', edad)