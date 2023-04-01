def  try_syntax ( numerador , denominador ): #se crea una funcion en la cual hay dos parametros
    try : #Se crea el try para la secuencia que se quiere evaluar
        resultado  =  numerador  /  denominador   #Se hace la operacion con los valores que tenemos como parametro de la funcion
        print ( f"In the try block: { numerator } / { denotor } " , result ) #se imprime la cadena que esta entre comillas y tambien la division que se va a ejecutar dependiendo de los datos que tengamos de parametro
        #quiero ver el resultado de la operacion en el print RPTA: Se hace la operacion antes del print y se llama la variable en el print
        resultado  =  numerador  /  denominador  #Se hace la operacion con los valores que tenemos como parametro de la funcion
    excepto  ZeroDivisionError  as  zde : #Se coloca la excepción "ZeroDivisionError" por si un parámetro llega a hacer cero, además se cambia el nombre de la función por "zde"
        print ( zde ) #se imprime la variable con nombre "zde"
    else : #ssse coloca un else por si no es necesario utilizar la excepcion y asi pueda imprimir lo de la siguiente linea
        print ( 'El resultado es:' , resultado ) #se imprime una cadena de letras y la variable "resultado"
        return  result  #el retorno de la funcion con la variable que ejecuta la operacion de la funcion
    finalmente : #se utiliza como una sentencia de finalizacion del programa
        print ( 'Exiting' ) #se imprime una cadena de texto
        #return "Fallo por cero"
#imprimir(intentar_sintaxis(12, 4))
print ( try_syntax ( 11 , 5 )) #se imprime la función con su respectivo resultado, además le damos los parámetros para realizar la función