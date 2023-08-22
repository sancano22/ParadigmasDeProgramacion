class Animales():
    def habla(self):
        print ("el animal habla")

class Perro(Animales):
    pass
    #def habla(self):
        #print("el perror habla")

c=Animales()
c.habla()

d=Perro()
d.habla()