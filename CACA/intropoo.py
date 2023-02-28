#NO tipado
x=10 #las dos primeras líneas de código asignan valores en conflicto a la variable x, por lo que la segunda asignación sobrescribirá la primera. En concreto, x=10 asigna el valor entero 10 a x, mientras que x=[]asigna una lista vacía a x. Como resultado, después de que se ejecuten estas dos líneas, el valor de x será una lista vacía.
x=[]
cad='Amo la programación' #esta línea asigna un valor de cadena 'Amo la programación'a la variable cad.
print(type(cad)) #esta línea usa la type()función para imprimir el tipo de cad, que es strpara "cadena".
print(len(cad)) #esta línea usa la len()función para imprimir la longitud de cad, que es 20 (contando espacios).
print(cad.capitalize()) #esta línea usa el capitalize()método para poner en mayúscula la primera letra de cad, lo que hace que la cadena 'Amo la programación'se convierta en 'Amo la programación'.
