# Ejercicio 1:
def funcion(dictionary,key,value):
    if key not in dictionary.keys():
        dictionary[key]=value
        print('No exite')
    else:
        print('Existe')
di={'gato':'cat','perro':'dog','caballo':'horse'}
funcion(di, 'fruta', 'manzana')

# Ejercicio 2:
def obtener_valor(diccionario,key, clave):
    if clave in diccionario.keys():
        print('no existe')
    else:
        print('existe')
de={'color':'blanco','gato':'cat','black':'amarrilo'}
obtener_valor(de,'rojo','red')

# Ejercicio 3:
def obtener_valor(diccionario,key, clave):
    if clave in diccionario.keys():
        print('existe')
    else:
        print('existe')
de={'caballo':'negro','perro':'blanco','azul':'blue'}
obtener_valor(de,'blanco','white')