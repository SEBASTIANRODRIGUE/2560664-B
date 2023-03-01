#Suponemos que el primer valor es el más grande. Luego verificamos esta hipótesis con los dos valores restantes
# Se leen tres números
numero1 = int(input("Ingresa el primer número: "))   #int para introducir un numero entero
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))
numero_grande = numero1                            #Asumimos temporalmente que el primer número es el más grande

if numero2 > numero_grande:         # Comprobamos si el segundo número es más grande que el mayor número actual y actualiza el número más grande si es necesario.
    numero_grande = numero2

if numero3 > numero_grande:       # Comprobamos si el tercer número es más grande que el mayor número actual y actualiza el número más grande si es necesario.
    numero_grande= numero3

print("El número más grande es:", numero_grande) # Imprime el resultado.


