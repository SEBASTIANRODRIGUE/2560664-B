importar  csv
con  open ( "archivos/sebastian_age_female.csv" , "r" ) como  sebastianmujer :

    csvReader = csv . lectora ( sebastianmujer )
    para  i  en  csvReader :
        imprimir ( "Índice:" [ 0 ])
        imprimir ( "Año:" [ 1 ])
        imprimir ( "Edad:" [ 2 ])
        imprimir ( "Nombre:" [ 3 ])
        imprimir ( "Película:" [ 4 ])