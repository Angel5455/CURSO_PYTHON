def suma(a, b):
    global n1, n2
    n1 = a 
    n2 = b

    suma = a  + b 
    return suma

def multi(a=None, b=None):
    global n1, n2
    n1 = a 
    n2 = b
    if a==None or b==None:
        print("Error: Debes enviar numeros en la funcion")
        return 

   

    multiplicacion = a  * b 
    return multiplicacion

resultado = suma(5,2)
print(f"La suma de dos numeros {n1} y {n2} es {resultado}")

resultado2 = multi()
print(f"La multiplicacion de dos numeros {n1} y {n2} es {resultado2}")