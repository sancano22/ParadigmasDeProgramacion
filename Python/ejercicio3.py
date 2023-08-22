class FabricaTelefonos():
    def __init__(self, marca, *colores,**modelos):
        self.marca=marca
        self.colores=colores
        self.modelos=modelos

telefono=FabricaTelefonos("Samsung","Negro","Azul",m1=200,m2=100)
print(telefono.colores)
print(telefono.modelos)