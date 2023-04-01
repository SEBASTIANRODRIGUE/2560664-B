clase  Ejemplo ():
    def  __init__ ( auto , var ):
        uno mismo __var = var
        print ( 'Constructor de métodos' )
    def  set_ejemplo ( self , var ):
        uno mismo __var = var
    def  get_ejemplo ( self ):
        devolverse  a uno mismo . __var
    
objeto = Ejemplo ( 'hola' )
imprimir ( objeto . get_ejemplo ())
objeto _ set_ejemplo ( 'chao' )
imprimir ( objeto . get_ejemplo ())



clase  Ejemplo2 ():
    __ lista = []
    def  __init__ ( auto , tele ):
        uno mismo __telefono = telefono
        Ejemplo2 . __lista . anexar ( self . __telefono )
    def  set_telefono ( self , tele ):
        uno mismo __telefono = telefono
    def  get_telefono ( self ):
        devolverse  a uno mismo . __telefono
    def  get_lista ():
        volver  Ejemplo2 . __lista
    
objeto2 = Ejemplo2 ( 321456887 )
objeto3 = Ejemplo2 ( 32148448 )


objeto3 . tele2 = 321554488


imprimir ( objeto2 . get_telefono ())
objeto2 . set_telefono ( 12345 )
imprimir ( objeto2 . get_telefono ())


imprimir ( Ejemplo2 . get_lista ())


imprimir ( objeto3 . tele2 )

imprimir ( objeto3 . tele2 )



imprimir ( objeto3 . __dict__ )
imprimir ( objeto2 . __dict__ )


clase  EjemploClase :
    atributo  =  1
    def  __init__ ( auto ):
        uno mismo atributo  =  1

m = ClaseEjemplo ()
imprimir ( hasattr ( m , 'attr' ))
imprimir ( hasattr ( EjemploClase , 'attri' ))
imprimir ( hasattr ( EjemploClase , 'accesorio' ))
