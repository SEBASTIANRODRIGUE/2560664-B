""""class Persona: #Se define la clase la cual se llama "persona"
    def __init__(self,nombre): #se crea una funcion con sus parametros ademas tambien se encuentra el constructor
        self.__nombre=nombre #se asigna el parametro a la clase persona
        #print('Constructor Activado')        
    def getNombre(self): #se crea una funcion para visualizar
        return self.__nombre #Retorna el atributo nombre de la clase
    def setNombre(self,nombre): #Se crea una funcion con sus parametros
        self.__nombre=nombre # se asigna el arametro a la clase persona
ob=Persona('Maria') #Se llama el metodo
print(ob.getNombre()) # Se utiliza el metodo
ob.setNombre('Ana') #Se llama el metodo
print(ob.getNombre()) #Se utiliza el metodo
#imprimir(tipo(ob)) """ ""

class  Persona :                   #se define la clase
    def  __init__ ( self , nombre ):   #funcion con parametros incluyendo el constructor
        uno mismo __nombre = nombre     #se crea una funcion con sus parametros ademas tambien se encuentra el constructor
        #print('Constructor Activado')        

    def  getNombre ( self ):   #se crea una funcion para visualizar
        devolverse  a uno mismo . __nombre  #Retorna el atributo nombre de la clase

    def  setNombre ( self , nombre ): #Se crea una función con sus parámetros
        uno mismo __nombre = nombre    #se asigna el parametro a la clase persona

ob = Persona ( 'Michael' )   #Se llama el metodo
print ( ob . getNombre ())    # Se utilla el metodo
ob . setNombre ( 'Julian' )    #Se llama el metodo
print ( "Segundo Nombre" , ob . getNombre ()) #Se utiliza el metodo


class  Aprendiz ( Persona ):      #Se define la clase con un argumento o una subclase
    def  __init__ ( self , nombre , ficha ):   #Se crea una función con sus parámetros respectivos
        persona _ __init__ ( self , nombre ) #Toma el metodo constructor de la clase
        uno mismo __ficha = ficha     #se asigna el parametro a la clase

    def  getFicha ( self ):        #se crea una funcion para visualizar
        devolverse  a uno mismo . __ficha     #Retorna el atributo nombre de la clase

app = Aprendiz ( 'Michael' , 2560664 )   #Se llama el metodo
print ( app . getFicha ())             #Se utiliza el metodo
         

class  Documento ( Persona ):         #Se define la clase con un argumento o una subclase
    def  __init__ ( self , nombre , documento ):    #Se crea una función con sus parámetros respectivos
        persona _ __init__ ( self , nombre )        #Toma el metodo constructor de la clase
        uno mismo __documento = documento            #se asigna el parametro a la clase

    def  getDocumento ( self ):           #se crea una funcion para visualizar
        devolverse  a uno mismo . __documento       #Retorna el atributo nombre de la clase

    def  setDocumento ( self , documento ):   #Se crea una función con sus parámetros
        uno mismo __documento = documento       #se asigna el arametro a la clase persona

asd = Documento ( "documento" , 107123546 )      #Se llama el metodo
print ( asd . getDocumento ())                 #Se utiliza ele metodo
asd . setDocumento ( "23456327" )         #Se llama el metodo
print ( "segundo documento" , asd . getDocumento ())   #Se utiliza el metodo