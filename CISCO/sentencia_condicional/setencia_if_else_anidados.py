
#encuentran el número mayor de una serie de números y lo imprimen.

#Se leen dos números
numero1 = int(input("Ingresa el primer número: ")) 
numero2 = int(input("Ingresa el segundo número: "))
if numero1 > numero2:       #si el numero 1 es mayor que el numero2: entonces 
    numero_mas_grande = numero1  #el numero mas grande es = al numero 1
else:                            #de lo contrario 
    numero_mas_grande = numero2      #numero mas gande es = al numero 2

# Imprime el resultado
print("El número más grande es:", numero_mas_grande)