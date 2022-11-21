"""
Dado un rango de números enteros, obtener la cantidad de 
números enteros que contiene.

"""
# Variables | Ingresar Datos.
numeroInicial = int(input('Número Inicial: '))
numeroFinal = int(input('Número Final: '))
i = 0
contador = 0

# Solución
i = numeroInicial + 1
while i < numeroFinal:
    contador += 1
    i += 1

# Mostrar Datos
print(f'CANTIDAD: {contador}')