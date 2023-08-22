class Carro:
    def __init__(self, color):
        self.set_color(color)

    def set_color(self, color):
        if color=="amarillo":
            self._color=color
        else:
            self._color="negro"
    @property   
    def get_color(self):
        return self._color
    
a=Carro("amarillo")
print(a.get_color)