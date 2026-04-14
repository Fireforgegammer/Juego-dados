import random

def evaluar_jugada(dados):
    conteos = {x: dados.count(x) for x in set(dados)}
    valores = sorted(conteos.values(), reverse=True)
    
    if 5 in valores: return "Repóker", 80
    if 4 in valores: return "Póker", 70
    if 3 in valores and 2 in valores: return "Full House", 60
    if sorted(dados) in [[1,2,3,4,5], [2,3,4,5,6]]: return "Escalera", 50
    if 3 in valores: return "Trio", 40
    if valores.count(2) == 2: return "Doble pareja", 30
    if 2 in valores: return "Pareja", 20
    return "Carta Alta", 10

def ia_facil(dados=None):
    return random.sample(range(5), random.randint(1, 3))

def ia_media(dados):
    conteos = {x: dados.count(x) for x in set(dados)}
    mantener = [i for i, d in enumerate(dados) if conteos[d] >= 2]
    return [i for i in range(5) if i not in mantener]

def ia_inteligente(dados):
    jugada, pts = evaluar_jugada(dados)
    if pts >= 60: return []
    conteos = {x: dados.count(x) for x in set(dados)}
    max_repetido = max(conteos.values())
    valor_fuerte = [v for v, c in conteos.items() if c == max_repetido][0]
    return [i for i, d in enumerate(dados) if d != valor_fuerte]