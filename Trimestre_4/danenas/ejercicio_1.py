## Cuantas letras del abecedario estan en la cadena, si estan repetidas cuentela solo una vez

print ( "Ejercio" )
print ( "Caracteres repetidos" )

cadena  =  str ( input ( "Digite la cadena: " ))
contador  =  0

para  letra  en  cadena :
    para  i  en  letra :
        si  letra  == ( letra ):
            contador  +=  1
imprimir ( contador )