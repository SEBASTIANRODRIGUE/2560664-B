# Ejercico 1:
def funcion(a, b):
    for i in range(b):
        for j in range(a):
            if i == j:
                print(i, j)
funcion(3, 3)
# Respuesta:
# 0 0
# 1 1
# 2 2

# Ejercicio 2:
def funcion(a, b):
    for i in range(b):
        for j in range(a):
            if (i + j) % 2 == 0:
                print(i, j)
funcion(3, 3)
# Respuesta:
# 0 0
# 0 2
# 1 1
# 2 0
# 2 2

# Ejercicio 3:
def funcion(a, b):
    for i in range(b):
        for j in range(a):
            if i > j:
                print(i, j)
funcion(3, 3)
# Respuesta:
# 1 0
# 2 0
# 2 1