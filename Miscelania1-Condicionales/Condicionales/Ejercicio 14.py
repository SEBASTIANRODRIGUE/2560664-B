'''Solicite un Angulo al usuario en grados. Diga en que cuadrante esta. diga
además en que vuelta está sabiendo que cada 360 grados se completa una
vuelta a la circunferencia. Además diga el resultado en radianes.'''
#pedir el valor
Angulo = int ( input ( 'Ingrese el angulo en forma de grados: ' ))
Radianes = 3.1416 * Angulo / 180  #Ecuacion a radianes
vuelta = 0
#Definir la cantidad de vueltas
si  Angulo >= 360 :
    vuelta = Angulo // 360
    Angulo %= 360
    si  vuelta == 1 :
        print ( 'Se realizo' , vuelta , 'vuelta a la circunferencia' ) #Si es igual a 1, cambiar el mensaje para que tenga sentido
    más :
        print ( 'Se realizó' , vuelta , 'vuelta a la circunferencia' )
#Definir los rangos de los cuadrantes y la conversion ponerla
si  Angulo >= 0  y  Angulo <= 90 :
    print ( 'Cuadrante 1,' , Radianes , 'convertida a radianes' )
elif  Angulo > 90  y  Angulo <= 180 :
    print ( 'Cuadrante 2,' , Radianes , 'convertida a radianes' )
elif  Angulo > 180  y  Angulo <= 270 :
    print ( 'Cuadrante 3,' , Radianes , 'convertida a radianes' )
elif  Angulo > 270  y  Angulo <= 360 :
    print ( 'Cuadrante 4,' , Radianes , 'convertida a radianes' )
