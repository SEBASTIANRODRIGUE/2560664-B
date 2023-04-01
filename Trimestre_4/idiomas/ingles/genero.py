
#Diccionario de ingles a español

word = input ( "Ingrese un instrumento" )

def  traducir_palabra ( palabra ):
    
    diccionario  = { "Acordeón" : "acordeón" ,
 "Gaita" : "gaita" ,
 "Drums" : "batería" ,
 "violonchelo" : "chelo" ,
 "Contrabajo" : "contrabajo" ,
"Flauta" : "flauta" ,
 "Flauta Dulce" : "flauta dulce" ,
 "Piano" : "piano" ,
 "Piano de cola" : "Piano de cola" ,
 "Guitarra" : "guitarra" ,
 "Pandereta"   : "pandereta" ,
 "Trompeta"   : "trompeta" ,
 "trombón"   : "trombón" ,
 "Saxofón"   : "saxofón" ,
 "Guitarra acústica" : "guitarra acústica" ,
 "Guitarra eléctrica" ​​: "guitarra eléctrica" ​​,
 "Bajo o bajo" : "bajo" ,
 "Maracas" : "maracas" ,
 "Guitarra" : "Guitarra" ,
 "Órgano" : "órgano" ,
 "armónica" : "armónica" ,
 "Fagot" : "maricón" ,
 "Bongó:" : "bongó" ,
 "Teclado" : "teclado" ,
 "clarinete" : "clarinete" ,
 "Platillos" : "platillos " ,
 "Castañuelas" : "castañuelas" ,
 "violonchelo" : "violoncelo"
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
     
#imprimir(traducir_palabra(palabra))
 