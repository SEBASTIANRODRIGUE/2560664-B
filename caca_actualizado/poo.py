class  Persona :                             #Se define o se crea la clase perosna
    def  __init__ ( self , nombre ):             #Se crea el metodo constructor con el parametro nombre
        uno mismo __nombre = nombre               #Se define el atributo relacionando con el parametro nombre
        #print('Constructor Activado')        

    def  getNombre ( self ):                   #Se define el metodo getnombre
        devolverse  a uno mismo . __nombre               #Devuelve el atributo nombre para saber el nombre incluso estado privado

    def  setNombre ( self , nombre ):            #Se define el metodo setnombre con el parametro nombre
        uno mismo __nombre = nombre               #Se relaciona el atributo con el parametro para agregar otor nombre

ob = Persona ( 'Maria' )                        #Determina el objeto con su determinada clase
print ( ob . getNombre ())                      #Se imprime el mensaje con la invocación de la función getnombre
ob . setNombre ( 'Ana' )                        #Se invoca la función setnombre referente al objeto ob
print ( ob . getNombre ())                      #Se imprime el mensaje con la invocación de la función getnombre
#imprimir(tipo(ob))