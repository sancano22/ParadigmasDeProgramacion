class Marino():
    def hablar(self):
        print("Hola soy marino")

class Pulpo(Marino):
    def hablar(self):
        print("Hola soy un pulpo")

class Foca(Marino):
    def __init__(self, mensaje):
        self.mensaje=mensaje
    def hablar(self):
        print(self.mensaje)

pulpito=Pulpo()
pulpito.hablar()

foca=Foca("Hola soy una foca")
foca.hablar()