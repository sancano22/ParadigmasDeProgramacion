class Animales():
    def __init__(self, nombre):
        self.__nombre=nombre
        
    @property
    def nombre(self):
        return self.__nombre
    
class Perro(Animales):
    def __init__(self, nombre, sonido):
        super().__init__(nombre)
        self._sonido=sonido

perro=Perro("Ambar","Guaooo")
print (perro.nombre)