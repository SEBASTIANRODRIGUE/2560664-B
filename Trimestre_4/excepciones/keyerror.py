def  ErrordeLlave ():
    prueba :
        animal = input ( "Ingrese el tipo de animal: " )
        diccionario = { 'Mamifero' :[ 'Perro' , 'Gato' , 'León' ], 'Aves' :[ 'Loro' , 'Perico' , 'Paloma' ]}
        imprimir ( diccionario [ animal ])
    excepto  KeyError :
        print ( "KeyError: Llave no encontrada" )

ErrordeLlave ()