# Ejercicio 1:
def multipo(tam,div): # es para una funcion
    for i in range(1, tam):#aqui es un bucle que comienza desde 1 hasta 19
        if(i%div==0):#si i que comienza desde 1 y lo divide 5 
            print(i,'es multipo de',div)
        else:
            print(i,'no es multiplo de',div)
multipo(20,5)#aqui lo que es tam =20 y div = 5
print('________________________')





# Ejercicio 2:
def numero(tam,div):
    for i in range(1, tam):
        if(i%div==0):
            print(i,'es multipo de',div)
        else:
            print(i,'no es multiplo de',div)
numero(30,4)
print('________________________')
# Ejercicio 3:
def numero(tam,div):
    for i in range(1, tam):
        if(i%div==0):
            print(i,'es multipo de',div)
        else:
            print(i,'no es multiplo de',div)
numero(50,7)