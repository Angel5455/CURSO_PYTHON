from io import open
from os import path

def escribir_archivo():
    archivo = open('texto.txt','w')
    archivo.write('Hola Mundo de Python')
    archivo.close()

def leer_archivo():
    if path.isfile('texto.txt'):
        archivo = open('texto.txt', 'r')
        #textos = archivo.read()
        #Para leer el contenido y colocarlo en una lista
        textos = archivo.readlines()
        archivo.close()

        print(textos)
    else: 
        print('No existe el archivo')

def agregar_datos():
    if path.isfile('texto.txt'):
        archivo = open('texto.txt', 'a')
        archivo.write('\nHola Angel')
        archivo.close()

    else:
        print('No existe el archivo')


def modificar_datos():
    if path.isfile('texto.txt'):
        archivo = open('texto.txt', 'r+')
        texto = archivo.readlines()
        print(texto)
        texto[1] = 'Hola Angel Ramon\n'
        #archivo.write('\nHola Juan')
        print(texto)
        archivo.seek(0) #Colocar el puntero al inicio
        archivo.writelines(texto) #Para reescribir el contenido del archivo
        archivo.close()
        print(texto)

    else:
        print('No existe el archivo')

#Elimina todo el contenido del archivo
def eliminar_datos():
    archivo = open('texto.txt', 'w')
    archivo.close()

#Elimina datos por rangos o individual 
def eliminar_datos2():
    archivo = open('texto.txt', 'r+')
    texto = archivo.readlines()
    archivo.seek(0)
    archivo.truncate()
    archivo.writelines(texto[0:2])
    

eliminar_datos2()