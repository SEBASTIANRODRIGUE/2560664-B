try: #bloque con las sentencias que quiere ejecutar
    #print(1/1))
    raise SyntaxError #raise se usa para indicar que se ha producido un error soobre el objeto de excepcion
#syntaxErro para saber si hay un comando mal escrito en la linea de codigo
except SyntaxError: #except 
    print('Cierra el parentesis')