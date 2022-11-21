# Módulo de números de Fibonacci
def fibo(n):
    a, b = 0, 1
    while a < n: 
        print(a, end=' ') #imprimir en la misma linea con espacio
        a, b = b, a + b 
        
    print() #imprime un salto de linea
    print('Fin del Fibonacci')

def fibo2(n):
    resultado = []
    a, b = 0, 1
    while a < n: 
        resultado.append(a)
        a, b = b, a + b 
        
    return resultado


