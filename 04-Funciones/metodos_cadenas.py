cadena = 'hola mundo'

print(cadena.upper()) 
print(cadena.lower())
print(cadena.capitalize())  
print(cadena.title()); 
print('Numero de o:', cadena.count('o'));

#reemplazar
palabra = 'Python'
print('Original:', palabra); 
palabra = palabra.replace('P', 'S'); 
print('Reemplazo:', palabra); 

#Borrar Espacios
palabra= "   Hola".strip()
print(palabra); 

palabra = "-----Hola-----".strip('-')
print(palabra); 

print(cadena.split()); 

palabra = 'Hola,mundo,desde,python'
print(palabra.split(','))

print(cadena.islower())
