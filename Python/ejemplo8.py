import random
import functools


superheroes = [
    {
        "nombre": "Batman",
        "editorial": "DC Comics",
        "alter_ego": "Bruce Wayne",
        "primera_aparicion": "Detective Comics #27"
    },
    {
        "nombre": "Superman",
        "editorial": "DC Comics",
        "alter_ego": "Kal-El",
        "primera_aparicion": "Action Comics #1"
    },
    {
        "nombre": "Spider Man",
        "editorial": "Marvel Comics",
        "alter_ego": "Peter Parker",
        "primera_aparicion": "Amazing Fantasy #15"
    },
    {
        "nombre": "Hulk",
        "editorial": "Marvel Comics",
        "alter_ego": "Bruce Banner",
        "primera_aparicion": "The Incredible Hulk #1"
    }
]

def anyadirPoder(superheroe):
    superheroe.update(poder=random.randint(0, 100))
    return superheroe

def contarMan(resultado, superheroe):
    if 'man' in superheroe['nombre'].lower():
        return resultado + 1
    else:
        return resultado

total = functools.reduce(contarMan, superheroes, 0)
superheroesPoder = map(anyadirPoder, superheroes)

print(total)
print(tuple(superheroesPoder))
