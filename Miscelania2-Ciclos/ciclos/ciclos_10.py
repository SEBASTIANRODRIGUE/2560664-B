'''4. Determinar cuales y cuantos números perfectos hay entre 1 y 1000?'''

#n = int(input("ingrese un numero: "))
'''s=0
for n in range(1, 1000):
    for i in range(1, n):
        if n % i == 0:
            s += i
            n == 0
    if s == n:
        print("el numero perfecto", n)
    else:
        print("el numero NO es perfecto", n)
    '''
for n in range(1, 1000):
   i = 1
   c = 0
   while( n > i):
      if n % i == 0:
        c += 1
      i += 1
   if n == c:
      print(n, "es un numero perfecto")