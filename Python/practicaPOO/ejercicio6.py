class Fabrica():
    def __init__(self, llantas, color, precio):
        self.llantas=llantas
        self.color=color
        self.precio=precio
class Carro(Fabrica):
    def datos(self):
        print("la cantidad de llantas es de:",self.llantas)
        print("El color del carro es", self.color)
class Moto(Fabrica):
    def datos(self):
        print("la cantidad de llantas es",self.llantas)
        print("El color del carro es", self.color)
moto=Moto(2,"negro",4000)
moto.datos()

