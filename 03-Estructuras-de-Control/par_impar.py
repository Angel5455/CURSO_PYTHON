num = int(input("Ingrese un numero "))

if num != 0:
    if num > 0: 
        
        if num%2==0 :
            print("El numero", num, "es par positivo") 
        else :
            print("El numero", num, "es impar positivo")
    else: 
         if num%2==0 :
            print("El numero", num, "es par negativo") 
         else :
            print("El numero", num, "es impar negativo")

else: 
   print(f"El numero {num} es neutro")





