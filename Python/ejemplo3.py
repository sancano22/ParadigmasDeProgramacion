def voz_baja(texto):
    return texto.upper( ) + " !!"

def saludar(saludo,modo):
    saludo_formateado=modo(saludo)
    print ('*' *len(saludo_formateado))
    print(saludo_formateado)
    
gritando=voz_baja
saludar('Hola',gritando)
