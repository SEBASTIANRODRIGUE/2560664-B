
suma=0          #define una variable suma iniciando en cero
for i in range(10): #usa un bucle for para sumar los numeros de 0  al 7 inclusive a suma y lurgo imprime el resultado 
    
    if i>7: # el bucle for termina temprano si si es mayor que 7 debido a la instruccion brteak
        break 
suma=suma+i
    print("La suma con break ha sido:",suma)
for i in range(10): # luego, otro bucle for se utiliza para sumar los números del 0 al 9 (inclusive) a suma y se imprime el resultado.
    suma=suma+i
print("La suma sin break ha sido:",suma)


#En la primera parte del código, el bucle for termina temprano debido a la instrucción break, por lo que suma solo contiene la suma de los números del 0 al 6 (inclusive), que es 28.

#En la segunda parte del código, el bucle for se ejecuta completamente sin interrupción, sumando los números del 0 al 9 (inclusive) a suma. Entonces, el valor final de suma es la suma de los números del 0 al 9, que es 45.