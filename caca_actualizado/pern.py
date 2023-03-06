class  Persona :                                      #Se define o crea la clase llamada persona
    def  __init__ ( self , nombre , documento ):            #Se define el método del constructor con sus parámetros
        uno mismo __nombre = nombre                        #Se define el atributo relacionando con el parametro nombre
        uno mismo __documento = documento                  #Se define el atributo relacionando con el parametro documento
        #print('Constructor Activado')        

    def  getNombre ( self ):                            #Se define el método getnombre para que realice el proceso con el nombre ingresado
        devolverse  a uno mismo . __nombre                        #Devuelve el atributo nombre para imprimirlo incluso estado privado

    def  getdocum ( self ):                             #Se define el metodo getdocum para que realice el proceso del numero de documento ingresado
        devolverse  a uno mismo . __documento                     #Devuelve el atributo documento para imprimirlo incluso estado privado
    def  setNombre ( self , nombre ):                     #Se define el metodo setNombre para que realice el proceso con el nombre ingresado/de momento no se llama
        uno mismo __nombre = nombre                        #Se define el atributo relacionando con el parametro nombre/de momento no se llama
    def  docum ( self , documento ):                      #Se define el método docum para que realice el proceso con el parametro documento
        uno mismo __documento = documento                  #Se define el atributo relacionando con el parametro documento
class  aprendiz ( Persona ):                            #Se define la herencia aprendiz determinando la relación con la clase padre persona
    def  __init__ ( self , nombre , documento , ficha ,):      #Se define el método del constructor con sus parámetros y uno nuevo que es ficha
        uno mismo __ficha = ficha                          #Se define el atributo relacionando con el parametro ficha
        persona _ __init__ ( self , nombre , documento )     #Se realiza un init para relacionar los parametros con la clase padre
    def  getficha ( self ):                             #Se define el metodo getficha para que realice el proceso del numero de ficha ingresado
        devolverse  a uno mismo . __ficha                         #Devuelve el atributo ficha para imprimirlo incluso estado privado
    def  gettodo ( self ):                              #Se define el método gettodo
        print ( "Documento:" , app . getdocum ())          #Se imprime el metodo getdocum con el objeto app
        print ( "Nombre:" , app . getNombre ())             #Se imprime el metodo getNombre con el objeto app
        print ( "Ficha:" , app . getficha ())             #Se imprime el metodo getficha con el objeto app
app = aprendiz ( "sebas" , 2560664 , 1032370694 )             #Se define el objeto
print ( app . gettodo ())                                #Se imprime el metodo gettodo para que llame los metodos de la clase padre desde la herencia aprendiz
