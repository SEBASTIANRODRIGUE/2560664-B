de  aprendiz  import  *
desde  curso  importar  *

ap = Aprendiz ( '2560664B' , 'SEBAS RODRIGUEZ' , 123456 )
c1 = Curso ( 'Python Intermedio' , 200 )
c2 = Curso ( 'Python Avanzado' , 200 )
#print(c1.getNombre())
ap . agregar Curso ( c1 )
ap . agregar Curso ( c2 )

para  el curso  en  ap . getCursos ():
    imprimir ( curso . obtenerNombre ())