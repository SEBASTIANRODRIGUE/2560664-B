def  edad (): #Se crea una funcion la cual no consta de parametros
    try : #Se crea el try para la secuencia que se quiere evaluar
        tuedad = int ( input ( "introduce tu edad" )) #se crea una variable en la cual se va a almacenar la edad que introduzca el usuario, esta edad debera ser un numero, si no es asi, el pregoma no funcionara
        print ( f'tu edad es   { tuedad } ' ) #se imprime una cadena de letras y tambien se imprime la variable creada anteriormente
        #print('Tu edad es',tuedad)
    excepto  ValueError  as  e :    #se crea la excepcion "ValueError" por si el usuario ingresa un valor que no sea un numero ejecutar esta excepcion, ademas se le cambia el nombre por "e"
        print ( e ) #se imprime la variable "e" si se llega a cumplir la excepcion
        print ( "La edad debe ser un valor numerico..." ) #se imprime una cadna de letras por si se llega a cumplir la excepcion
        edad () #Se ejecutara siempre y cuando la excepcion se cumpla
    
edad () # terminación de la excepción