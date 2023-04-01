de  Clase  importación  *
importar  csv
listaapre = []
con  open ( "archivos/sebastian_age_female.csv" , "r" ) como  sebastianmujer :
    csvReader = csv . lectora ( sebastianmujer )
    para  y  en  csvReader :
        ob = Persona ( y [ 0 ], y [ 1 ], y [ 2 ], y [ 3 ], y [ 4 ])
        listaapre . agregar ( ob )

imprimir ( listaapre )        

para  apre  en  listaapre :
    imprimir ( apre . pelicula ())