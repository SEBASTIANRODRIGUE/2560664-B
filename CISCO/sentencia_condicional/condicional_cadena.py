#Escribe un programa que utilice el concepto de ejecución condicional, tome una cadena como entrada y que:Imprima el enunciado "Si, ¡El ESPATIFILIO! es la mejor planta de todos los tiempos!" en la pantalla si la cadena ingresada es "ESPATIFILIO".Imprima "No, ¡quiero un gran ESPATIFILIO!" si la cadena ingresada es "espatifilo".Imprima "¡ESPATIFILIO!, ¡No [entrada]!" de lo contrario. Nota: [entrada] es la cadena que se toma como entrada.

cadena = input("Ingrese una cadena:") #variable cadena
if cadena == "ESPATIFILIO":            #si cadena == se compara ESPATIFILIO: ENTONCES
    print("Si, ¡El ESPATIFILIO! es la mejor planta de todos los tiempos!") #imprima si
elif cadena == "espatifilo":             # de lo contrario cadena == se compara espatifilo: entonces
    print("No, ¡quiero un gran ESPATIFILIO!") #imprima no quiero un gran...
else:
    print("¡ESPATIFILIO!, ¡No " + cadena + "!")