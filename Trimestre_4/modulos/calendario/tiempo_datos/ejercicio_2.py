importar  fecha y hora  como  d


def  edad ( fecha_nacimiento , fecha_actual ):
    si  fecha_nacimiento  <  fecha_actual :
        edad = fecha_actual . año  -  fecha_nacimiento . año  - (( fecha_actual . mes , fecha_actual . día ) < ( fecha_nacimiento . mes , fecha_nacimiento . día ))
        print ( f'Esa persona, objeto o animal tiene { edad } años' )
    más :
        print ( 'No ha nacido' )

fecha_nac  =  d . fecha ( 2004 , 12 , 14 )
fecha_act = d . fecha _ hoy ()
edad ( fecha_nac , fecha_act )