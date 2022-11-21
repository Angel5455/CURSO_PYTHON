
# Argumentos por posicion *args
# Argumentos por nombres **kwargs

def sumar(*args, **kwargs):
    suma = 0
    for n in args:
        suma+=n
    return suma, kwargs 

resultado, datos = sumar(1,2,3, nombre='Angel Paz', edad=34)
print ('La suma es:', resultado)
print ('Datos:', datos)
print('-'*60)
print ('DATOS')
print('-'*60)
nombre= datos['nombre']
edad= datos['edad'] 
print('nombre:', nombre)
print('edad:', edad)