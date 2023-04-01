de  volver  a importar  I


 producto de clase :
    constante = 0
    def  __init__ ( self , nombre , precio ):
        uno mismo __nombre = nombre
        uno mismo __precio = precio
 #adquiridor   
    def  get_nombre ( auto ):
        devolverse  a uno mismo . __nombre

    def  get_precio ( auto ):
        devolverse  a uno mismo . __precio
  #setter  
    def  set_nombre ( self , nombre ):
        uno mismo __nombre = nombre

    def  set_precio ( self , precio ):
        uno mismo __precio = precio
    def  calculariva ( auto ):
        yo = yo . __precio * 0.19
        iva = uno mismo . __precio + yo
        return  f" { self . __precio } tiene un iva de { i } total { iva } "

producto1 = producto ( "teclado" , 32000 )
producto2 = producto ( "ratón" , 10000 )
producto3 = producto ( "parlante" , 20000 )

imprimir ( producto1 . get_nombre ())
producto1 . set_nombre ( "televisor" )
imprimir ( producto1 . get_nombre ())

imprimir ( producto1 . obtener_precio ())
producto1 . set_precio ( 15000 )
imprimir ( producto1 . obtener_precio ())

imprimir ( producto1 . calculariva ())
imprimir ( producto1 )