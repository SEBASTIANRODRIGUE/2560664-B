importar  calendario
def  dia_semana ():
    a ñ o =  int ( input ( 'Ingrese el año: ' ))
    mes =  int ( input ( 'Ingrese el mes: ' ))
    dia =  int ( input ( 'Ingrese el dia: ' ))
    si  mes <= 12  y  dia  <= 31 :
        v = calendario . día de la semana ( año , mes , dia )
        si  v  ==  0 :
            imprimir ( 'El día es Lunes' )
        elif  v  ==  1 :
            imprimir ( 'El día es Martes' )
        elif  v  ==  2 :
            imprimir ( 'El dia es Miercoles' )
        elif  v  ==  3 :
            imprimir ( 'El día es Jueves' )
        elif  v  ==  4 :
            imprimir ( 'El día es Viernes' )
        elif  v  ==  5 :
            imprimir ( 'El día es Sabado' )
        elif  v  ==  6 :
            imprimir ( 'El día es Domingo' )
    más :
        print ( 'ERROR:Solo hay 12 meses y máximo 31 dias en algunos meses' )
        dia_semana ()