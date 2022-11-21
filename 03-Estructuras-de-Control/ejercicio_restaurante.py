""" Practica 01: Descuentos de un restaurante
Enunciado: un restaurante ofrece un descuento del 10% para consumo de hasta 
s/. 100.00 y un descuento del 20 % para consumos mayores y un 30% si el consumo
es mayor a 200.00.
 se aplica un impuesto del 19%. Determinar el monto del descuento, 
 el impuesto y el importe a pagar.

 Consumo (S/.)       Descuento (%)

Hasta 100                 10

Mayor a 100             20

Mayor a 200             30

Análisis: para la solución de este problema, se requiere que el usuario 
ingrese el consumo y el sistema verifica y calcula el monto del descuento,
el impuesto y el importe a pagar.

monto del descuento

impuesto

importe a pagar """

# Entrada 
consumo = float(input('Ingrese el consumo del cliente: '))

if consumo >= 0:
    #Proceso 
    if consumo <= 100:
        # Descuento de 10%
        dato_descuento = '10%'
        descuento = consumo * 0.10
    elif consumo > 100 and consumo <= 200:
        #Descuento de 20%
        dato_descuento = '20%'
        descuento = consumo * 0.20
    elif consumo > 200:
        #Descuento de 30%
        dato_descuento = '30%'
        descuento = consumo * 0.30

    monto_descuento = consumo - descuento
    igv = monto_descuento * 0.19 
    total_pagar = monto_descuento + igv

    #Salida de datos 
    print('='*30)
    print('----- FACTURA DE CONSUMO -----')
    print('Descuento que se aplica:', dato_descuento)
    print('='*30)
    print('Consumo: ', consumo)
    print('Descuento: ', descuento)
    print('Monto con descuento: ', monto_descuento)
    print('IGV: ', igv)
    print('Total a Pagar: ', total_pagar)
    print('='*30)

else:
    print('Error al Ingresar el consumo')
