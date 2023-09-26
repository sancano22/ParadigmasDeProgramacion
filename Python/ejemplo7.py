def multiplicar(a,b):
    return a*b

def multiplicar_por(f,n):
    return lambda y: f(n,y)

doblar=multiplicar_por(multiplicar,2)

print(doblar(10))
