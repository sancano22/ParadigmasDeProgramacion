class A():
    def __init__(self, contador,cuenta):
        self._contador=contador
        self._cuenta=cuenta 

    def get_cuenta(self):
        return self._cuenta
    
    def get_contador(self):
        return self._contador
    
    def set_cuenta(self,cuenta):
        self._cuenta=cuenta

    
    def __del__(self):
        print("el objeto ha sido destruido")
    

a=A(20,10)
#a.set_cuenta(20)
#print(a.get_cuenta())
#print(a.get_contador())
a._cuenta=10
print(a.get_cuenta())