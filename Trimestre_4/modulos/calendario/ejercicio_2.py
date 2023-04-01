importar  calendario
def  añ o_bisiesto () :
    a ñ o = int ( input ( 'Ingrese el valor del rango mínimo: ' ))
    a ñ o2 = int ( input ( 'Ingrese el valor del rango máximo:' ))
    para  i  en  rango ( a ñ o , a ñ o2 + 1 ):
        si  calendario . isleap ( i ) == Verdadero :
            print ( i , 'es un año bisiesto' )
        más :
            print ( i , 'No es un año bisiesto' )


añ o_bisiesto ( )