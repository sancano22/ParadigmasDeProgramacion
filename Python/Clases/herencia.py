class Animal():
    def __init__(self,nombre=""):
        self.nombre=nombre

    def hablar(self):
        print("Hola soy un animal")

class Perro(Animal):
    def __init__(self,nombre):
        super().__init__(nombre)
    def hablar(self):
        print("Hola soy un"+self.nombre)

perrito1=Perro("pepe")


