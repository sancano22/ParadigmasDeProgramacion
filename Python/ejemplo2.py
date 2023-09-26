def voz_baja(texto):
    return texto.upper( ) + " !!"

gritando=voz_baja

dialogo =[( 'Hola', gritando),
          ('Por favor, no chilles, me duele la cabeza', None), 
          ('Perdona, ¿quieres una aspirina?', voz_baja)
        ]

for frase, modo in dialogo:
    if modo == None:
        print(frase)
    else:
        print(modo(frase))