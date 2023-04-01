import  csv    #Importamos el archivo "csv"
diccio = [      #Se crea un diccionario
    { 'name' : 'Alice' , 'age' : 18 },         #Dentro de ese diciionaroi se encuentra otro diccionario con los datos
    { 'nombre' : 'Bob' , 'edad' : 19 },        
    { 'nombre' : 'Juan' , 'edad' : 17 }
]
header = [ 'nombre' , 'edad' ]      #Una variable con otro diccionario y sus datos

with  open ( 'archivos/people.csv' , 'w' ) as  csvfile :    #La ruta del archivo con su cambio de nombre
    escritor = csv . DictWriter ( csvfile , fieldnames = header )    #Se crea una variable local que va a almacenar lo que va a ir en la primera columna
    escritor _ writeheader ()            #Se utiliza la variable con un metodo para crear la cabecera del archivo
    escritor _ writerows ( diccio )       #Se utiliza la variable con un metodo para escribir lo demas del diccionario
