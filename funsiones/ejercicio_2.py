'''entrege la suma de los divisores de un numero'''

lista = 0

def sumadiv(num):
    sum = 0
    for i in range(1, num + 1):
        if num % i == 0:
            sum += i
    return sum



def perfectos(n):
    suma = sumadiv(n)
    if n == suma:
        print("es perfecto")
    else:
        print("No es perfecto")

print(perfectos(10))