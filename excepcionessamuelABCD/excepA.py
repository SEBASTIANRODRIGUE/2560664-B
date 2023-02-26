try:                   #1) Inicio del bloque de codigo para ejecutar las excepciones raise ZeroDivisionError
    #print(1/1))
    raise SyntaxError  # 2) Se utiliza para generar el error de la manera que decidimos
except SyntaxError:    # 3) Se escribe la excepción con su debido tipo de error que se quiere resaltar para su ejecución 
    print('Cierre el parentesis') # 4) Se imprime el mensaje

