def imprimir_mensaje(valor):
    # Usar un bucle if, elif y else para imprimir un mensaje diferente en función del valor de la variable
    if valor == 0:
        print("El valor es 0")
    elif valor == 1:
        print("El valor es 1")
    elif valor == -1:
        print("El valor es diferente de 0 y 1")

# Crear una variable
mi_valor =int(input('ingrese un numero: '))

# Usar la función para imprimir un mensaje en función del valor de la variable
imprimir_mensaje(mi_valor)



# def suma_impares(inicio, fin):
#     suma = 0
#     while inicio <= fin:
#         if inicio % 2 != 0:
#             suma += inicio
#         inicio += 1
#     return suma

# print(suma_impares(1, 10))
