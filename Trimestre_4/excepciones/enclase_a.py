Try : #es la secuencia que se quiere evaluar
    #imprimir(1/1))
    raise  SyntaxError  #es el error que quiero generar
excepto  SyntaxError  as  e : #seutiliza la excepción para que se genere este error, además se utiliza como para cambiar el nombre de la excepción
    print ( e ) #se imprime el cambio de nombre de la excepcion
    print ( 'Cierra el parentesis' ) #se imprime la respuesta que queremos dar
    
prueba :
    #raise ZeroDivisionError
    imprimir ( 1 / 0 )
#excepto (ZeroDivisionError) como e:
excepto  ZeroDivisionError  como  zde :
    imprimir ( zde )
    #print('prueba de error')