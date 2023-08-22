class Estudiante():
    def __init__(self,rut,nombre,nota):
        self.__rut=rut
        self.nombre=nombre
        self.nota=nota
    
    def imprimirDato(self):
        print("El estudiante con código {}",self.rut)
    
    def calcularExamen(self):

        if(self.nota>=5.0):
            print("No presenta examen")
        else:
            print("Presenta examen")
        
#fuera de la clase
estudiante1=Estudiante("112121-1","pepito perez",4.5)
estudiante1.calcularExamen()