# Aqui se cree un diccionario con las palabras y la traduccion a ingles


x = input ( "Ingrese un instrumento" )

def  traducir_palabra ( x ):
    
    diccionario  = { "Acordeón" : "Acordeón" ,
 "gaita" : "gaita" ,
 "batería" : "Tambores" ,
 "chelo" : "violonchelo" ,
 "contrabajo" : "Contrabajo" ,
" flauta" : "flauta" ,
 "flauta dulce" : "Flauta dulce" ,
 "piano" : "piano" ,
 "Piano de cola" : "Piano de cola" ,
 "guitarra" : "guitarra" ,
 "pandereta"   : "pandereta" ,
 "trompeta"   : "Trompeta" ,
 "trombón"   : "trombón" ,
 "saxofón"   : "Saxofón" ,
 "guitarra acustica" : "Guitarra acustica" ,
 "guitarra electrica" ​​: "guitarra electrica" ​​,
 "bajo" : "Bajo o bajo" ,
 "maracas" : "maracas" ,
 "Guitarra" : "Guitarra" ,
 "órgano" : "Órgano" ,
 "armónica" : "Armónica" ,
 "maricón" : "fagot" ,
 "Bongó:" : "bongó" ,
 "clarinete" : " Clarinete" ,
 "platillos" : "Platillos " ,
 "castañuelas" : "Castañuelas" ,
 "violoncelo" : "violonchelo"
}
    
#esta función sirve para buscar la palabra en el diccionario y su traducción. tambien sirve para mostrar cuantas palabras tienen en español e ingles
#y por ultimo muestra que tipo de palabra es

    si  x  en  el diccionario :
        
        traducir =  diccionario [ x ]
        
        palabra =  len ( x )
        palabrat  =  len ( traducir )
        
        tipo  =  "Sustantivo"
        
        
        return ( "la palabra" , x , "traducida al idioma ingles es" , traducir ,
        "la palabra" , x , "cuenta con" , palabra , "letras" ,
        "la palabra" , traducir , "cuenta con" , palabrat , "letras" ,
        x , "es un" , tipo )
    más :
        
        return  "La palabra no se encuentra en el diccionario." #si se escribe una palabra que no este en el diccionario manda este mensaje
     
