'''hacer una funcion que identifique cuales son numeros amigo'''

def sumadiv(num):
    sum = 0
    for i in range(1, num + 1):
        if num % i == 0:
            sum += i
    return sum

def perfectos(n):
    suma = sumadiv(n)
    if suma == 1:
        return "Si es numero primo"
    else:
        return "No es numero primo"


def amigo(x, y):
    sumx = sumadiv (x)
    sumy = sumadiv (y)
    if sumx == y and sumy == x:
        return "son amigo"
    else:
        return "son enemigos"
