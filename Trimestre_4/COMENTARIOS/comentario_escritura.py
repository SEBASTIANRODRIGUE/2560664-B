import  csv     #Se importa el archivo "csv"
header = [ 'Fruta' , 'Precio' ]     #Se crea una variable que va a contener un diccionario
filas = [[ 'Apple' , 1200 ],        #Se crea otra variable con un diccionario
      [ 'Baya' , 2000 ],
      [ 'Limón' , 1000 ],
      [ 'Melón' , 3000 ],
      [ 'Uvas' , 4000 ],
      [ 'Pera' , 2000 ]]

with  open ( 'archivos/example.csv' , 'w' ) as  csvfile :     #La ruta del archivo con su cambio de nombre
    csvwriter = csv . escritor ( csvfile )      #se cfea una variable que va hacer igual al archivo que importamos con un metodo para escribir en el archivo de xsv
    escritor csv . writerow ( header )     #Se utiliza la variable con un metodo para escribir la primera fila
    escritor csv . writerows ( rows )    #Se utiliza la variable con un metodo para escribir lo demas