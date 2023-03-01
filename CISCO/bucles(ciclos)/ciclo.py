# Se leen tres números para saber cual es el mas grande e imprimirlo
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

# Verifica cuál de los números es el mayor
# y pásalo a la variable largest_number
    
numero_grande= max(numero1, numero2, numero3) # funcion max()es el numero mas grande,  Verifica cuál de los números es el mayor y lo pása a la variable numero_grande

print("El número más grande es:", numero_grande)


# Se leen tres números para saber cual es el mas pequeño con funcion min() e imprimirlo
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

# Verifica cuál de los números es el menor
# y pásalo a la variable pequeño_numero
    
numero_pequeño= min(numero1, numero2, numero3) # funcion min()es el numero mas pequeño,  Verifica cuál de los números es el menor y lo pása a la variable numero_pequeño

print("El número más pequeño es:", numero_pequeño)