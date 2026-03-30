import random

def tirar_dado(caras=6):
    return random.randint(1, caras)

def tirar_varios_dados(cantidad=5, caras=6):
    return [tirar_dado(caras) for _ in range(cantidad)]