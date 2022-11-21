#Dado un rango de números enteros, obtener la cantidad de números pares que contiene.

# Variables | Ingresar Datos.
numeroInicial = int(input('Número Inicial: '))
numeroFinal = int(input('Número Final: '))
i = 0
cantidadPares = 0

# Solución
i = numeroInicial + 1
while i < numeroFinal:
    if i % 2 == 0:
        cantidadPares += 1
    i += 1

# Mostrar Datos
print(f'CANTIDAD DE PARES: {cantidadPares}')