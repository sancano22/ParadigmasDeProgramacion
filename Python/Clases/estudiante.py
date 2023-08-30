class Estudiante():
    def __init__(self,rut="",nombre="",nota=0.0):
        self.__rut=rut
        self.__nombre=nombre
        self.__nota=nota
     
    def getRut(self):
       return self.__rut
    
    def setRut(self, rut):
        self.__rut=rut
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self,nombre):
        self.__nombre=nombre

    def getNota(self):
        return self.__nota
    
    def setNota(self,nota):
        self.__nota=nota

    def imprimirDato(self):
        print("El estudiante con código {}",self.rut)
    
    def calcularExamen(self):
        if(self.__nota>=5.0):
            print("No presenta examen")
        else:
            print("Presenta examen")
        
#fuera de la clase
estudiante1=Estudiante()
#datos del estudiante
estudiante1.setRut("12121-1")
estudiante1.setNombre("Pepito")
estudiante1.setNota(4.5)
estudiante1.calcularExamen()

ListaEstudiantes=[]
#ingresar muchos datos
for i in range (3):
    print("\nIngresando datos al estudiante {}".format((i+1)))
    estudiante=Estudiante()
    estudiante.setRut("12121-1")
    estudiante.setNombre("Pepito")
    estudiante.setNota(4.5)
    ListaEstudiantes.append(estudiante)

print(ListaEstudiantes[0].getNombre())