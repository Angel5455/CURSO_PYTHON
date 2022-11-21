#Ingrese 12 número en 3 listas (en cada lista con 4 números), 
# y obtenga la suma de cada lista.

# Ingresar Datos / Lista
num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))
num4 = int(input('Número 4: '))
num5 = int(input('Número 5: '))
num6 = int(input('Número 6: '))
num7 = int(input('Número 7: '))
num8 = int(input('Número 8: '))
num9 = int(input('Número 9: '))
num10 = int(input('Número 10: '))
num11 = int(input('Número 11: '))
num12 = int(input('Número 12: '))

# Usando la función append()
lista1 = []
lista1.append(num1)
lista1.append(num2)
lista1.append(num3)
lista1.append(num4)

lista2 = []
lista2.append(num5)
lista2.append(num6)
lista2.append(num7)
lista2.append(num8)

lista3 = []
lista3.append(num9)
lista3.append(num10)
lista3.append(num11)
lista3.append(num12)

suma1 = 0
suma2 = 0
suma3 = 0

# Solución

for numero in range(len(lista1)):
    suma1 += lista1[numero]
    suma2 += lista2[numero]
    suma3 += lista3[numero]
    
    

# Mostrar Datos 
print('Suma Lista 1: ', suma1)
print('Suma Lista 2: ', suma2)
print('Suma Lista 3: ', suma3)