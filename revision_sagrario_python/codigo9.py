#Ejercicio 1
def is_even(x):
  return x % 2 == 0
numero = [1, 2, 3, 4, 5, 6]
listaN = []
for num in numero:
  if is_even(num):
    listaN.append(num)

print(listaN)  
# Respuetas: [2, 4, 6]

#Ejercicio 2
def multiplo(x, y):
  return x * y
numero = [1, 2, 3, 4, 5]
producto = numero[0]
for i in range(1, len(numero)):
  producto = multiplo(producto, numero[i])

print(producto)  
# Respuesta: 120

#Ejercicio 3
def cuadrado(x):
  return x**2
numero = [1, 2, 3, 4]
cuadrado_numero = []
for num in numero:
  cuadrado_numero.append(cuadrado(num))

print(cuadrado_numero)  
# Respuesta: [1, 4, 9, 16]
