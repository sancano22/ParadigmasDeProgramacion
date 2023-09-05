import json
from datetime import datetime

format_data="%m/%d/%Y %H:%M:%S"

class Dato:
    def __init__(self,nombres,apellidos,genero,fechaNacimiento,email,carrera):
        self.fechaNacimiento=datetime.strptime(fechaNacimiento, format_data)
        self.nombres=nombres
        self.apellidos=apellidos
        self.genero=genero
        self.email=email
        self.carrera=carrera
    
    def calcularEdad(self):
        self.edad=datetime.now().year - self.fechaNacimiento.year
        return self.edad

if __name__=="__main__":
    archivo= open('data.json')
    dato=json.load(archivo)
    for i in range(0,len(dato)):
        datos=Dato(dato[i]["nombre"],dato[i]["apellidos"],
                   dato[i]["genero"],dato[i]["fechaNacimiento"],dato[i]["email"],dato[i]["carrera"])
        print(datos.calcularEdad())