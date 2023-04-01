palabra  =  "esdrújula"

si  len ( palabra ) <=  2 :
    imprimir ( "La palabra es aguda" )
elif  palabra [ - 1 ] en  "nNsS" :
    imprimir ( "La palabra es aguda" )
elif  palabra [ - 2 :] en [ "as" , "es" , "os" ]:
    imprimir ( "La palabra es grave" )
elif  palabra [ - 3 ] en  "aeiouáéíóú" :
    print ( "La palabra es esdrújula" )
más :
    print ( "La palabra es sobresdrújula" )