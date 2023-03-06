# Ejercicio 1:
def clasificacion_numero(num):
  if num > 0:
    return "positivo"
  elif num < 0:
    return "negativo"
  else:
    return "zero"
print(clasificacion_numero(5))  
print(clasificacion_numero(-3)) 
print(clasificacion_numero(0))  

# Ejercicio 2:
def numero_maxino(num1, num2):
  if num1 > num2:
    return num1
  else:
    return num2
print(numero_maxino(5, 10))  
print(numero_maxino(3, 3))   
print(numero_maxino(-2, 1))  

# Ejercicio 3:
def is_leap_year(year):
  if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    return True
  else:
    return False
print(is_leap_year(2000))  
print(is_leap_year(2020))  
print(is_leap_year(2100))  