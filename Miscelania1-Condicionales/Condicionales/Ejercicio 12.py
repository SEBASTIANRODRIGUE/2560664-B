"""Solicite la hora en formato horas, minutos y segundos. Imprima en pantalla la
hora que sera dentro de 1 segundo"""

h  =  int ( entrada ( "Horas = " ))
si  h  >= 0  y  h  <  12 :
    m  =  int ( entrada ( "Minutos = " ))
    si  m  >=  0  y  m  <  60 :
        s  =  int ( entrada ( "Segundos = " ))
        si  s  >=  0  y  s  <  60 :
            si  s + 1  ==  60 :
                s  =  "00"
                m  +=  1
            más : s  +=  1
            si  m  ==  60 :
                metro  =  "00"
                h  +=  1
            si  h  ==  12 :
                h  =  "00"
            
            imprimir ( h , m , s , sep = ":" )
            salir ()
imprimir ( "error" )