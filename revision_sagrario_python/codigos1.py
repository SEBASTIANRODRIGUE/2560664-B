

a = 5 #las variables a,b,c si inicializan con los valosres enteros 
b = 5
c = 5
Rta = (a < b) and (b < c) or (not (a < b)) and (c < b) #La expresión (a < b)se evalúa como False, porque ay bambos son iguales a 5.
#La expresión (not (a < b))se evalúa como True, porque a < b es 
#La expresión (c < b)se evalúa como False, porque c y b ambos son iguales a 5.False.
#La expresión (a < b) and (b < c)es Falsa porque a < b es False
print(Rta)  

# respuesta: False

a = 7
b = 5
c = 3
rta = (a < b) and (b < c) or (not (a < b)) and (c < b)
print(rta) 
# respuesta: True

a = 3
b = 2
c = 1
rta = (a < b) or (b < c) and (not (a < b)) or (c < b)
#a,b(false) or (false)
#false
#print(rta) 
#respuesta: True