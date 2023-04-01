importar  calendario
def  saber_mes ():
    a ñ o = int ( input ( 'Ingrese el año: ' ))
    mes = int ( input ( 'Ingrese el mes: ' ))
    si  mes <= 12 :
        imprimir ( calendario . mes ( a ñ o , mes ))
    más :
        print ( 'ERROR:Solo hay 12 meses' )
        saber_mes ()
saber_mes ()