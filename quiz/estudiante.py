#modulo del estudiante
class estudiante: 
    def __init__(self, nombre, edad, asignaturas):
        self.nombre = nombre
        self.edad= edad
        self. notas ={}
    def agregar_notas(self, asignatura , nota):
        self.notas[asignatura] = nota

    def obtener_promedio(self,asignatura,nota):
        self.nota[asignatura] = nota

    def obtener_promedio(self):
        if len(self.notas) ==0:
            return
        else:

            return sum(self.notas.values()) / len (self.notas)
    
    def consultar_profesor(self, profesor):
        profesor.consultar()
