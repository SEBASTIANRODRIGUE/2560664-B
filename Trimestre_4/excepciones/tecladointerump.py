def  interrupción ( ) :
    prueba :
        para  i  en   el rango ( 200000 ):
            imprimir ( yo )
    excepto  KeyboardInterrupt :
        print ( 'KeyboardInterrupt: Se ha detenido la ejecución del programa con el comando CTRL+C' )