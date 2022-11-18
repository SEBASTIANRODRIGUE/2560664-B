'''escribe un programa que pida tre numeros y que escriba si los 3 numeros son iguales. si hay dos iguales o si los 3 son diferentes.
'''
def numeros(): 
    x = int(input("ingrede un numero"))
    y = int(input("ingrede un numero"))
    z = int(input("ingrede un numero"))

    if x == y == z:
        return "son iguales"
    elif x == y or x == z or y == z:
        return "hay dos numeros iguales"
    else:
        return "todos los numeros son diferentes"

print(numeros())