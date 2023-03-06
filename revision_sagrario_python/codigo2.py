# Usando la función para crear una lista de números pares
def funcion_pares(tam):
    return [i for i in range(0, tam*2, 2)]

print(funcion_pares(5))
#Respuesta: [0, 2, 4, 6, 8]

# Usando la función para crear una lista de números impares
def funcion_impares(tam):
    return [i for i in range(1, tam*2+1, 2)]

print(funcion_impares(5))
# Respuesta: [1, 3, 5, 7, 9]

# Usando la función para crear una lista de números al cuadrado
def funcion_cuadrado(tam):
    return [i**2 for i in range(tam)]

print(funcion_cuadrado(5))
# Output: [0, 1, 4, 9, 16]