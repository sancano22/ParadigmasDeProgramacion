from functools import reduce

def operacion(x,y,funcion):
    return funcion(x,y)

def suma(x,y):
    return x+y

def resta(x,y):
    return x-y

#print(operacion(5,1,resta))

integer=[1,2,3,4,5,6,7,8,9,10]
#salida=list(filter(lambda x:x%2==0, integer))
#salida=list(map(lambda x:x%2==0, integer))

salida=reduce(lambda a,b:a+b,integer)
print(salida)