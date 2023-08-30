class Universidad():
    def universidad(self,Nombre):
        self.Nombre=Nombre

class Carrera():
    def carrera(self, carrera):
        self.carrera=carrera

class Estudiante(Universidad,Carrera):
    def __init__(self, universidad, carrera,nombre,edad):
        super().universidad(universidad)
        super().carrera(carrera)
        self.nombre=nombre
        self.edad=edad
        print("Mi nombre es {} soy estudiante de {} en la universidad de {} ".format(self.nombre,self.carrera, self.Nombre))

persona=Estudiante("PUCV","Informática","pepito",23)


