"""El módulo llamado os permite interactuar con tu sistema operativo usando Python
El módulo os te permite:
Obtener información sobre el sistema operativo.
Manejar procesos.
Operar en streams de E/S usando descriptores de archivos.
El módulo os te permite distinguir rápidamente el sistema operativo mediante el atributo name
posix: obtendrás este nombre si usas Unix.
nt: obtendrás este nombre si usas Windows.
java: obtendrás este nombre si tu código está escrito en Jython. """

importar  sistema operativo
#print(os.nombre)

#El módulo os proporciona una función llamada mkdir, la cual,te permite crear un directorio
#La función listdir devuelve una lista que contiene los nombres de los archivos y directorios que se encuentran en la ruta pasada como argumento.


#os.mkdir("mi_primer_directorio")
#imprimir(os.listdir())

#La función makedirs permite la creación recursiva de directorios, lo que significa que se crearán todos los directorios de la ruta.

#os.makedirs("mi_primer_directorio/mi_segundo_directorio")
#os.chdir("mi_primer_directorio")
#imprimir(os.listdir())
#Para moverte entre directorios, puedes usar una función llamada chdir, que cambia el directorio de trabajo actual a la ruta especificada.


#getcwd devuelve informacion sobre el directorio de trabajo actual

#os.chdir("mi_primer_directorio")
#imprimir(os.getcwd())
#os.chdir("mi_segundo_directorio")
#imprimir(os.getcwd())

#rmdir= función para eliminar un directorio SOLO
#removedirs= funcion para eliminar directorios y subdirectorios


#os.rmdir("mi_primer_directorio")
#imprimir(os.listdir())

#os.removedirs("mi_primer_directorio/mi_segundo_directorio")
#imprimir(os.listdir())


#Otra forma para crear un directorio
#valor_devuelto = os.system("mkdir mi_primer_directorio")
#imprimir(valor_devuelto)

#comprobacion si existe una carpeta o no

#if os.path.exists("carpeta1")==Verdadero:
# print("la carpeta ya existe")

#demás:
# os.mkdir("carpeta1")
# print("La carpeta fue creada con exito")    