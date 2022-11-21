#Factorial de un numero
def factorial(n):
    print('valor inicial=>', n)
    if n > 1:
        n=n*factorial(n-1)
    print('valor final=>', n)
    return n

num = int(input('Ingrese un numero:'))

f = factorial(num)
print(f'El factorial de {num} es:', f)