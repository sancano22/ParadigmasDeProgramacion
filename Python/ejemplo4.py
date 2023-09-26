def crearEncriptador(clave):
    def encriptar(mensaje):
        return cesar(mensaje,clave)
    return encriptar

def cesar(texto, clave):
    if texto==texto.upper () : #PARA MAYUSCULAS
        abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    else:
        abc="abcdefghijklmnñopqrstuvwxyz" #PARA MINUSCULAS
    cifrad=""
    for c in texto:
        if c in abc:
            cifrad += abc[(abc.index(c)+clave)%(len(abc))]
        else:
             cifrad+=c  
    return cifrad 
valor=crearEncriptador(2)
print(valor("valor"))