         #Primer ejercicio
def funcion (tupla,usuario):
    meses_año=('enero','febrero','marzo','abril','mayo','junio',
    'julio','agosto','septiembre','octubre','noviembre','diciembre')
    #usuario=int(input('ingresa un numero de mes: '))
    if usuario <len(meses_año):
        print('¡ERROR!')
    elif (usuario>=1 and usuario<=len(meses_año)): 
        print(meses_año[usuario-1])



        #Segundo ejercicio
def funcion(tupla,start,end):
     print(tupla[start:end])
transportes=('carro','bicicleta','moto','autobus','trasmilenio')
funcion(transportes,1,-1)

        #Tercer ejercicio
def funcion ():
    numero=(1,2,2,2,3,6,5,2,7,7,8,4,5,6,7,8,9)
    usuario=int(input('Que numero quieresver las veces que se encuentra repetidos: '))
    e=0
    for i in numero:
        if usuario == i:
            e+=1
    print('El numero',usuario,'esta',e,'veces repetido')
funcion()