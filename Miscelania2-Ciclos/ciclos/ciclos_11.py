from tkinter import N
n = int(input("ingrese un numero: "))
s = 0
n -= 1
while n > 0:
    s += n**3
    n -= 1
print(n) 
