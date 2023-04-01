#- De una cadena diga cuantas vocales tiene, cuantas consonantes, cuantas vocales con tilde y cuantos caracteres especiales.
def  contar_vocales ( cadena ):
	contador  =  0
	para  letra  en  cadena :
		si  letra . inferior () en  "aeiou" "áéíóú" :
			contador  +=  1
	volver  contador

def  es_vocal ( letra ):
    volver  letra  en  "aeiou"

      

cadena  =  "Hola mundo"
cadena_minuscula  =  cadena . inferior ()
cantidad  =  contar_vocales ( cadena )
print ( f"En la cadena ' { cadena } '' hay { cantidad } vocales" )
cantidad_consonantes  =  0
para  letra  en  cadena_minuscula :
    si  letra . isalpha () y  no  es_vocal ( letra ):
        cantidad_consonantes  +=  1
print ( f"En la cadena ' { cadena } ' hay { cantidad_consonantes } consonantes" )