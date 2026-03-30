import random

def tirar_dado(caras=6):
    return random.randint(1, caras)

def tirar_varios_dados(cantidad=5, caras=6):
    return [tirar_dado(caras) for _ in range(cantidad)]

def tirar_rol(cantidad, caras):
    tiradas = tirar_varios_dados(cantidad, caras)
    return tiradas, sum(tiradas)