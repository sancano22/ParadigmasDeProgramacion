class Calculadora:
    def __init__(self):
        self.num1=int(input("Ingrese el valor 1:"))
        self.num2=int(input("Ingrese el valor 2:"))
    
    def operacion(self,operacion):
        if (operacion==1):
            self.resultado=self.num1+self.num2
        elif (operacion==2):
            self.resultado=self.num1-self.num2
        elif (operacion==3):
            self.resultado=self.num1*self.num2
        else:
            print("la opción que ha seleccionado no existe")
        return self.resultado
    
    def resultado(self, resultado):
        print("el resultado es:",resultado)
    
calculo=Calculadora()
calculo.resultado(calculo.operacion(1))