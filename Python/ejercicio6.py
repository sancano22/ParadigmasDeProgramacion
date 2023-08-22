class Pez():
    def __init__(self):
        self._color=""
        self._tamanyo=""
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self,color):
        self._color=color
    
    @property
    def tamanyo(self):
        return self._tamanyo
    
    @tamanyo.setter
    def tamanyo(self,tamanyo):
        self._tamanyo=tamanyo
    
pez1=Pez()
print(pez1.color)
pez1.color="amarillo"
print(pez1.color)