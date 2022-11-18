'''Determinar cuales y cuantos numeros perfectos hay entre 1 y
1000?''''
#Para el numero en rango de 1 a 1000, creamos iy contador
para  n  en  rango ( 1 , 1000 + 1 ):
  yo = 1
  contador = 0
  while ( n > i ): #Mientras que el numero siga siendo mayor ai, solo se contaran los que cumplir la division aumenta 1 en el contador y la i
   si  n % i  == 0:
    contador += yo 
   yo += 1
  if  n == contador : #Si el contador tiene el mismo valor que el numero, el numero es perfecto
    print ( "El numero " , n , " es perfecto" )
