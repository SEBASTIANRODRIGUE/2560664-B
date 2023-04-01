importar  csv
con  open ( "archivos/sebastian_age_female.csv" , "r"  ) como  sebastianhombre :

    csvReader = csv . lector ( sebastianhombre )
    para  i  en  csvReader :
        imprimir ( "Índice2:" [ 0 ])
        imprimir ( "Año2:" [ 1 ])
        imprimir ( "Edad2:" [ 2 ])
        imprimir ( "Nombre2:" [ 3 ])
        imprimir ( "Película2:" [ 4 ])