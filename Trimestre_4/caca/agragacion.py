clase  aprendiz : #Definimos la clase aprendiz
    def  __init__ ( self , nombre ): #Creamos el constructor con un parámetro el cual es "nombre"
        uno mismo __nombre = nombre   #se asigna el parametro a la clase aprendiz
        uno mismo __cursos = []   #Se asigna una lista vacía al parámetro
    def  agregarCurso ( self , nombreCurso ): #Se crea una funcion con un parametro
        uno mismo __cursos . append ( nombreCurso ) #se va a agregar el parametro a la lista vacia
    def  verCursos ( self ): #Se crea una funcion para visualizar los cursos
        devolverse  a uno mismo . __cursos   #retorna el atributo nombre de la clase

class  Curso :        #Se crea otra clase llamada "curso"
    def  __init__ ( self , nombreCurso ):    #Se crea el constructor y la funcion tiene un parametro
        uno mismo __nombreCurso = nombreCurso  #se asigna el parametro a la clase curso

    def  getNombreCurso ( self ):   #Se crea una funcion para visualizar
        devolverse  a uno mismo . __nombreCurso  #Retorna el atributo nombre de la clase
    
ob = Aprendiz ( 'Miguel' )   #Se crea una variable para asignarle el nombre aprendiz
c1 = Curso ( 'Python Basico' ) #Se crea una variable para asignarsela al curso
c2 = Curso ( 'Python Intermedio' ) #Se crea una variable para asignarsela al curso
c3 = Curso ( 'Java Basico' ) #Se crea una variable para asignarsela al curso

ob . agregarCurso ( c1 ) #Se llama al metodo
ob . agregarCurso ( c2 ) #Se llama al metodo
ob . agregarCurso ( c3 ) #Se llama el metodo

para  cursor  en  ob . verCursos ():   #Se crea un for para recorrer la funcion "vercursos"
    print ( curso . getNombreCurso ()) #Se imprime la funcion "getNombreCurso"

del  ob  #Se elimina la variable "ob"
#imprimir(ob)
print ( '.....' , c1 . getNombreCurso ()) #Se imprime la funcion "getNombreCurso"