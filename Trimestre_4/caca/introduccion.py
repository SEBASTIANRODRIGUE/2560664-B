class  Vehiculo :                                          #Definmos una clase la cual llamaremos "vehiculo"
    def  __init__ ( self , tipo ):                             #creamos una funcion donde se encuentra el constructor y tenemos un parametro
        uno mismo tipo = tipo                                   #crea una variable de instancia que guarda el argumento
    def  descripcion ( self ):                               #una funcion
        print ( 'Soy generico no tengo descripcion' , self . tipo ) #Imprime una cadena de texto, con el tipo
#v=Vehículo('Cualquier tipo')

    def  getTipo ( self ):                                   #crea una función para visualizar el tipo
        devolverse  a uno mismo . tipo                                 #retorna el tipo
        #retorno Vehiculo.tipo
    def  __str__ ( self ):                                   # se crea un metodo
        return  'Soy objeto de la clase Vehiculo'         # return una cadena

class  Herramienta :                                       #se crea otra clase llamada "herramienta"
    def  __init__ ( self , proposito ):                        #se crea el constructor y una funcion con sus parametros
        uno mismo __proposito = proposito                       #crea una variable de instancia que guarda el argumento
    def  getProposito ( self ):                              #
        devolverse  a uno mismo . __proposito
    def  __str__ ( uno mismo ):
        volver  'Soy objeto de la clase Herramienta'
clase  Terrestre ( Vehiculo , Herramienta ):
    def  __init__ ( self , tipo , propuesto ):
        Herramienta . __init__ ( auto , propuesto )
        vehiculo _ __init__ ( auto , tipo )        
    def  datos ( auto ):
        print ( 'Tipo: ' , super (). getTipo ())
        print ( 'Tipo: ' , super (). getProposito ())
    # def __str__(uno mismo):
    # return 'Soy objeto de la clase Terrestre'
               
t = Terrestre ( "terrestre" , "carga" )
t . datos ()
imprimir ( t . __str__ ())