clase  Producto ():
    __cont = 0
    suma = 0
    def  __init__ ( self , nombre , precio ):
        uno mismo __nombre  =  nombre
        uno mismo __precio  =  precio
        Producto . __cont += 1
        
    
    def  get_nombre ( auto ):
        devolverse  a uno mismo . __nombre
    def  set_nombre ( self , nombre ):
        uno mismo __nombre = nombre
    
    
    def  get_precio ( auto ):
        devolverse  a uno mismo . __precio
    def  set_precio ( self , precio ):
        uno mismo __precio  =  precio
    
     
    def  calcular_iva ( auto ):
        yo = yo . __precio * 0.19
        iva = uno mismo . __precio + yo
    
        
        return  f'Valor sin iva { self . __precio } tiene un iva de { i } total { iva } '
    
    def  contador ():
        volver  f'Se han creado { Producto . __cont } productos'
    


produc1 = Producto ( 'usb' , 3500 )
produc2 = Producto ( 'Nunca' , 100 )
produc3 = Producto ( 'computadora' , 500 )
produc4 = Producto ( 'teclado' , 500 )

     
imprimir ( produce1 . get_nombre ())
produce1 . set_nombre ( 'TV' )
imprimir ( produce1 . get_nombre ())


imprimir ( producir1 . obtener_precio ())
produce1 . set_precio ( 2000 )
imprimir ( producir1 . obtener_precio ())


imprimir ( produce1 . calcular_iva ())
imprimir ( produce2 . calcular_iva ())


imprimir ( Producto . contador ())