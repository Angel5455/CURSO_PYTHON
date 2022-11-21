# Ingresar Datos / Lista
num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))
num4 = int(input('Número 4: '))
num5 = int(input('Número 5: '))
num6 = int(input('Número 6: '))

# Usando la función append()
lista1 = []
lista1.append(num1)
lista1.append(num2)
lista1.append(num3)

lista2 = []
lista2.append(num4)
lista2.append(num5)
lista2.append(num6)

#totalListas = lista1 + lista2
totalListas = []
lista1.extend(lista2)
totalListas.extend(lista1)
print(totalListas)

numeroPAR = 0
numeroIMPAR= 0

# Solución
for i in range(len(totalListas)):
    if totalListas[i] % 2 == 0:
        numeroPAR += 1
    else:
        numeroIMPAR += 1

    
# Mostrar Datos 
print('Número PARES: ', numeroPAR)
print('Número IMPARES: ', numeroIMPAR)