#Obtener la suma de pares e impares de los primeros N números enteros positivos.

# Variables | Ingresar Datos.
valor = int(input('Número: '))
valor += 1

numeroImpar = 0
numeroPAR = 0

# Solución
for numero in range(1, valor):
    if numero % 2 == 0:
        numeroPAR = numeroPAR + numero
    elif not(numero % 2 == 0):
        numeroImpar = numeroImpar + numero

# Mostrar Datos
print(f'SUMA PARES: {numeroPAR}')
print(f'SUMA IMPARES: {numeroImpar}')