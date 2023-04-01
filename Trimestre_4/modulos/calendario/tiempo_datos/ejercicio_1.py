importar  fecha y hora  como  d

por definición  navidad ():
    dia_presente =  d . fecha _ hoy ()
    dia_navidad = d . fecha ( dia_presente . año , 12 , 25 )
    si  dia_presente > dia_navidad :
        dia_navidad = d . fecha ( dia_presente . año + 1 , 12 , 25 )
        dia_faltante = ( dia_navidad - dia_presente ). días
        volver ( f'Faltan { dia_faltante } para navidad' )    
    más :
        dia_faltante = ( dia_navidad - dia_presente ). días
        volver ( f'Faltan { dia_faltante } para navidad' )
         
imprimir ( navidad ())