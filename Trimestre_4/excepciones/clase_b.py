valores  = ( 1 , 5 ) #se crea una tupla
#x,y=10,12
#imprimir(divmod(10,3))
try : #Se crea el try para la secuencia que se quiere evaluar
    q , r  =  divmod ( * valores ) #las variables toman el valor de la tupla, el * hace que cada variable se le asigna un valor y no la tupla en general, además se hace una división con el divmod
    #print('valor de q=',q)
    print ( f'q= { q } ' ) #se imprime la variable con su respectivo resultado
    print ( f'r= { r } ' ) #se imprime la variable con su respectivo resultado
excepto ( ZeroDivisionError , TypeError ) as  e : #esta la excepción por si llagan a dividir por 0 o ingresan un tipo de dato que no es, además se le cambia el nombre a la expcion por "e"
    print ( type ( e ), e ) #se imprime la variable "e", y se coloca el "type" para saber el tipo de dato que es
