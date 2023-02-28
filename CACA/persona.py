class Persona:                 #esta linea de código define una clase llamada Persona
    def __init__(self,nombre):# El método " init " es un constructor que se llama cuando se crea un objeto de la clase "Persona" y establece el valor del atributo "nombre" al valor que se proporciona como argumento al constructor
        self.__nombre=nombre #esta linea nos dice el parametro 'nombre'
        print('Activando constructor') #imprime una cadena

    def getNombre(self):   # El método getNombre devuelve el valor del atributo __nombre y el método setNombre establece un nuevo valor para el atributo __nombre.
        return self.__nombre #no lo enten di
    
    def setNombre(self, nombre): #no lo entendi
        self.__nombre=nombre #no

    def metodo(self): # no 
        print('Soy un método') #imprime un mensaje "Activando constructor" cuando se llama.



ob=Persona('Ana')  #en esta linea se crea una  instancia de la clase Persona llamada ob con el valor 'Ana' como argumento del constructor
print(ob.getNombre()) # en esta linea vemos el  método getNombre en el objeto ob imprime el valor del atributo __nombre, que es 'Ana'.
ob.setNombre('Maria') #aqui se llama al método setNombre en el objeto ob con el valor 'Maria' como argumento, lo que cambia el valor del atributo __nombrea 'Maria'
print(ob.getNombre()) #esta linea llama el método getNombre de nuevo en el objeto ob y se imprime el valor del atributo __nombre, que es 'Maria'.


#ob.metodo()
#print(type(ob))
