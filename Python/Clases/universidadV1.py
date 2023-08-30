class Universidad():
    def __init__(self,Nombre):
        self.Nombre=Nombre

class Carrera():
    def carrera(self, carrera):
        self.carrera=carrera

class Estudiante(Universidad,Carrera):
    def datos(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        print("Mi nombre es {} soy estudiante de {} en la universidad de {} ".format(self.nombre,self.carrera, self.Nombre))

persona=Estudiante("PUCV")
persona.carrera("informática")
persona.datos("pepito",23)