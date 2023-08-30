class Pez():
    #constructor
    def __init__(self,color,tamanyo):
        self.__color=color
        self.__tamanyo=tamanyo

   #get y set 
    
    def getColor(self):
        return self.__color
    
    def setColor(self,color):
        self.__color=color

    def getTamanyo(self):
        return self.__tamanyo

    def setTamanyo(self,tamanyo):
        self.__tamanyo=tamanyo

    def __del__(self):
        print("Destruir el objeto")

    
    #comportamientos 
    def nadar(self):
        print ("El pez nada")
    
    def comer(self):
        print("El pez duerme")

pececito1=Pez("rojo","pequeño")
print(pececito1.getColor)
pececito1.nadar()
