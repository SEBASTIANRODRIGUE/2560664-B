##Escriba una clase Empleado que tenga como propiedades nombre, cargo, salario escriba metodos contructores, setters y getters escriba un método que permita calcular cuanto gana el empleado en una hora un método para saber cuanto recibe de incremento si el salario sube con el IPC. Si gana el mínimo se le aumenta el ipc + 3% Un método que reciba una cantidad de horas extras y calcule el salario incementando las extras. No puede hacer mas de dos horas diarias y trabaja de luenes a viernes. Valide



class Empleado:                                  #Este código define una clase llamada "Empleado" 
    def __init__(self, nombre, cargo, salario):  #proporciona algunos métodos para ello. El método " init " se utiliza para inicializar el objeto con
        self.nombre = nombre                      #nombre, cargo y salario del empleado.
        self.cargo = cargo
        self.salario = salario

    def set_nombre(self, nombre):             #Los métodos "def" y "self" se utilizan para acceder y modificar las variables de instancia.
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_cargo(self, cargo):
        self.cargo = cargo

    def get_cargo(self):
        return self.cargo

    def set_salario(self, salario):
        self.salario = salario

    def get_salario(self):
        return self.salario

    def calcular_salario_hora(self):       ##El método "calcular_salario_hora" calcula la tarifa horaria del empleado en función de su salario 
        salario_hora = self.salario / 240  # mensual
        return salario_hora                #se considera que trabaja 8 horas diarias durante 30 días
                                           # se asume un promedio de 240 horas mensuales

    def calcular_incremento_ipc(self, ipc):
        if self.salario == 1160000:  # salario mínimo en Colombia en 2023 = 1160000
            incremento = ipc + 0.03  #El método "calcular_incremento_ipc" calcula el incremento de salario en base al incremento del índice de 
                                      #precios  al consumidor (IPC). Si el salario del empleado es 1160000, el incremento se calcula sumando
        else:                         #el 3% y el 13.12% del salario; en caso contrario, se calcula sumando el 13.12% del salario. 
            incremento = ipc
        nuevo_salario = self.salario * (1 + incremento) #1 es la hora de incremento
        incremento_total = nuevo_salario - self.salario
        return incremento_total

    def calcular_salario_con_horas_extra(self, horas_extra):
        if horas_extra > 2:
            return "No se puede trabajar más de 2 horas extra diarias."
        else:
            salario_hora = self.calcular_salario_hora()
            salario_extra = horas_extra * salario_hora * 1.25  # se considera un recargo del 25% por hora extra de acuerdo al salario salario mínimo 
            salario_total = self.salario + salario_extra       #salario mínimo en Colombia en 2023
            return salario_total

# ejemplo de uso
empleado1 = Empleado("sebastian rodriguez", "programador", 2000000)
salario_hora = empleado1.calcular_salario_hora()
incremento_total = empleado1.calcular_incremento_ipc(0.1312)  # se considera un IPC del 13.12%
salario_con_horas_extra = empleado1.calcular_salario_con_horas_extra(2)

print(f"El salario por hora de {empleado1.get_nombre()} es de ${salario_hora:.2f}.")
print(f"El incremento total del salario de {empleado1.get_nombre()} es de ${incremento_total:.2f}.")
print(f"El salario de {empleado1.get_nombre()} con 2 horas extra es de ${salario_con_horas_extra:.2f}.")
