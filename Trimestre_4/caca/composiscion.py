class  Curso :   #Se crea la clase "Curso"
    def  __init__ ( self , titulo ): #Se crea el constructor con un parametro en la funcion
        uno mismo __titulo = titulo  #se asigna el parametro a la clase curso

    def  getTitulo ( self ): #Se crea una funcion para visualizar
        devolverse  a uno mismo . __titulo   #Retorna el atributo nombre de la clase

clase  Aprendiz :     #Se crea la clase "aprendiz"
    def  __init__ ( self , nombre ):   #Se crea el constructor con un parametro
        uno mismo __nombre = nombre  #se asigna el parametro a la clase curso
        uno mismo __cursos = []   #Se asigna una lista vacía para "cursos"

    def  agregarCurso ( self , nombreCursito ):   #Se crea una función para agregarcurso
        cursito = Curso ( nombreCursito )     #se asigna el parametro a la clase curso
        uno mismo __cursos . append ( cursito )   #se asigna el parametro a la clase curso

    def  getCursos ( self ):       #Se crea una funcion para visualizar
        devolverse  a uno mismo . __cursos   #Se devuelve el atributo nombre de la clase
    
ap = Aprendiz ( 'Sofia' )   #Se llama el metodo
ap . agregarCurso ( 'Python Basico' )   #Se utiliza el metodo
ap . agregarCurso ( 'Python Intermedio' ) #Se utiliza el metodo

para  c  en  ap . getCursos ():    #Se crea una para recuperar "getCursos"
    print ( c . getTitulo ())   #Se imprime la funcion "getTitulo"

del  ap     #Se elimina la variable "ap"