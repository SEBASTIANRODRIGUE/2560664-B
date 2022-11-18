import random
def sumlist (lista):
    sum = 0
    for i in lista:
        sum += i
    return sum

def llenarlista(lista):
    tam = round(random.randint(5, 15))
    for i in range(tam):
        lista.append(round(random.randrange(100)))
    return lista

list1 = []
list1 = llenarlista(list1)
print(list1)
print(sumlist(list1))




