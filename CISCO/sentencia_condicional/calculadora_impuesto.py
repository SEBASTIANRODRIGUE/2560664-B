#Si el ingreso del ciudadano no era superior a 85,528 pesos, el impuesto era igual al 18% del ingreso menos 556 pesos y 2 centavos (esta fue la llamada exención fiscal ).Si el ingreso era superior a esta cantidad, el impuesto era igual a 14,839 pesos y 2 centavos, más el 32% del excedente sobre 85,528 pesos. Tu tarea es escribir una calculadora de impuestos.Debe aceptar un valor de punto flotante: el ingreso.A continuación, debe imprimir el impuesto calculado, redondeado a pesos totales. Hay una función llamada round() que hará el redondeo por ti,


pago = float(input("Introduce el ingreso anual:"))

if pago<=85528 and pago>=3089:

   impuesto =(pago*18/100)-556.02

elif pago<3089:

   impuesto=0.

else:
    
    impuesto=14839.02+((pago-85528)*32/100)


impuesto = round(impuesto, 0)
print("El impuesto es:", impuesto, "pesos")