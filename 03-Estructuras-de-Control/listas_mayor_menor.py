#Ingrese 6 números en una lista y obtenga el número mayor y menor ingresado.

# Ingresar Datos / Lista
num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))
num4 = int(input('Número 4: '))
num5 = int(input('Número 5: '))
num6 = int(input('Número 6: '))

# Usando la función append()
numeros = []
numeros.append(num1)
numeros.append(num2)
numeros.append(num3)
numeros.append(num4)
numeros.append(num5)
numeros.append(num6)

# Solución
minimo = maximo = numeros[0]

for numeros in numeros:
    if numeros < minimo:
        minimo = numeros
    elif numeros > maximo:
        maximo = numeros 

# Mostrar Datos 
print("El mínimo es " + str(minimo)) 
print("El máximo es " + str(maximo))