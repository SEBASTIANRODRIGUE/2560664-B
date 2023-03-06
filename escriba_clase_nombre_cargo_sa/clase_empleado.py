#Escriba una clase Empleado que tenga como propiedades nombre, cargo, salario escriba metodos contructores, setters y getters escriba un método que permita calcular cuanto gana el empleado en una hora un método para saber cuanto recibe de incremento si el salario sube con el IPC. Si gana el mínimo se le aumenta el ipc + 3% Un método que reciba una cantidad de horas extras y calcule el salario incementando las extras. No puede hacer mas de dos horas diarias y trabaja de luenes a viernes. Valide


class Empleado:                                #Este código define una clase llamada "Empleado" 
    def __init__(self, nombre, cargo, salario): #proporciona algunos métodos para ello. El método " init " se utiliza para inicializar el objeto con 
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        
    def get_nombre(self):     #Los métodos "def" y "self" se utilizan para acceder y modificar las variables de instancia.
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_cargo(self):
        return self.cargo
    
    def set_cargo(self, cargo):
        self.cargo = cargo
    
    def get_salario(self):
        return self.salario
    
    def set_salario(self, salario):
        self.salario = salario
        
    def calcular_salario_hora(self):   #El método "calcular_salario_hora" calcula la tarifa horaria del empleado en función de su salario mensual.
        salario_hora = self.salario / 240  # se asume un promedio de 240 horas mensuales
        return salario_hora
    
    def calcular_incremento_ipc(self): #El método "calcular_incremento_ipc" calcula el incremento de salario en base al incremento del índice de 
        incremento = 0                  #precios  al consumidor (IPC). Si el salario del empleado es 1160000, el incremento se calcula sumando
                                         #el 3% y el 16.12% del salario; en caso contrario, se calcula sumando el 16.12% del salario.

        if self.salario == 1160000:  # se asume salario mínimo de 1160000
            incremento = (0.03 + 0.1612) * self.salario
        else:
            incremento = 0.1612 * self.salario  # se asume incremento del 16.12%
        return incremento
    
    def calcular_salario_horas_extras(self, horas_extras): #Finalmente, el método "calcular_salario_horas_extras" calcula el salario extra que reci
                                                            #recibe el empleado
                                                            #por trabajar horas extras. Si el empleado trabaja más de 2 horas extra, el número de horas se reduce a 2  y el salario se calcula como el doble de la tarifa por hora por las horas extra trabajadas.
        if horas_extras > 2:  # no puede hacer más de dos horas diarias
            horas_extras = 2
        salario_hora = self.calcular_salario_hora()
        salario_extra = salario_hora * 2 * horas_extras  # se asume pago del doble por horas extras
        return salario_extra
    







