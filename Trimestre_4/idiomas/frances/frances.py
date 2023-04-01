# Aqui se cree un diccionario con las palabras y la traduccion a frances

word = input ( "Ingrese un instrumento" )

def  traducción ( palabra ):
    
    dictionary  = { "La guitarra" : "la guitarra" ,

"Le piano" : "el piano" ,

"La contrebasse" : "el contrabajo" ,

"La batería" : "la batería" ,

"Le saxofón" : "el saxofón" ,

"La trompeta" : "la trompeta" ,

"Le trombón" : "el trombón" ,

"Le violón" : "el violín"
}
    
#esta función sirve para buscar la palabra en el diccionario y su traducción. tambien sirve para mostrar cuantas palabras tienen en español e ingles
#y por ultimo muestra que tipo de palabra es
  
    si  palabra  en  el diccionario :
        
        traducir =  diccionario [ palabra ]
        
        palabra =  len ( palabra )
        palabrat  =  len ( traducir )
        
        tipo  =  "Sustantivo"
        
        
        volver ( "la palabra" , word , "traducida al español es" , traducir ,
        "la palabra" , word , "cuenta con" , palabra , "letras" ,
        "la palabra" , traducir , "cuenta con" , palabrat , "letras" ,
        traducir , "es un" , tipo )
    más :
        
        return  "La palabra no se encuentra en el diccionario."
