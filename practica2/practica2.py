import json
from datetime import datetime

format_data="%m/%d/%Y"

class Estudiante():
    def __init__(self, id,nombres,apellidos,genero, fechaNacimiento,rut, carrera,anyoAcademico,region,comuna):
          self.id=id
          self.nombres = nombres
          self.apelidos=apellidos
          self.genero=genero
          self.fechaNacimiento=datetime.strptime(fechaNacimiento, format_data)
          self.rut=rut
          self.carrera=carrera
          self.anyoAcademico=anyoAcademico
          self.region=region
          self.comuna=comuna
    
    def calculaEdad(self):
        self.edad=datetime.now().year - self.fechaNacimiento.year
        return self.edad

class Asignatura():
    def __init__(self, idEstudiante,codigo,nombre, notas):
        self.idEstudiante=idEstudiante
        self.codigo=codigo
        self.nombre=nombre
        self.notas=notas

    def calculaPromedio(self):
        promedio=0
        for i in range(0,len(self.notas)):
            promedio=promedio+self.notas[i]
        return (promedio/len(self.notas))



if __name__=="__main__":
    promedioEdadF=0
    promedioEdadM=0
    cantidadF=0
    cantidadM=0

    archivo= open('datos/estudiantes.json')
    dato=json.load(archivo)

    for i in range(0,len(dato)):
        datos=Estudiante(dato[i]["id"],dato[i]["nombres"],dato[i]["apellidos"],
                   dato[i]["genero"],dato[i]["fechaNacimiento"],dato[i]["rut"],dato[i]["carrera"],dato[i]["anyoAcademico"],dato[i]["region"],dato[i]["comuna"])
        #asignaturas
        archivoAsignatura= open('datos/asignaturas.json')
        datoAsignatura=json.load(archivoAsignatura)
        for j in range(0,len(datoAsignatura)):
           if(datoAsignatura[j]["idEstudiante"]==dato[i]["id"]):
                notas=Asignatura(datoAsignatura[j]["idEstudiante"],datoAsignatura[j]["codigo"],datoAsignatura[j]["nombre"],datoAsignatura[j]["notas"])
                print(notas.calculaPromedio())
        
        if(dato[i]["genero"]=="F"):
            cantidadF=cantidadF+1
            promedioEdadF=promedioEdadF+datos.calculaEdad()
        elif(dato[i]["genero"]=="M"):
            cantidadM=cantidadM+1
            promedioEdadM=promedioEdadM+datos.calculaEdad()

    print("el promedio de edad de genero Femenino es",promedioEdadF/cantidadF)
    print("el promedio de edad de genero Masculino es",promedioEdadF/cantidadM)
    
    
    
