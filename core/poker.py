import random
from core.dados import tirar_varios_dados, tirar_dado

PUNTUACIONES = {
    "Nada": 1,
    "Escalera": 2,
    "Pareja": 3,
    "Doble pareja": 4,
    "Trio": 5,
    "Full": 6,
    "Poker": 7,
    "Re-poker": 8
}

def contar_valores(dados):
    conteo = {}
    for d in dados:
        conteo[d] = conteo.get(d, 0) + 1
    return conteo

def es_escalera(dados):
    ordenados = sorted(dados)
    return ordenados == [1, 2, 3, 4, 5] or ordenados == [2, 3, 4, 5, 6]

def evaluar_jugada(dados):
    conteo = contar_valores(dados)
    repeticiones = sorted(conteo.values(), reverse=True)

    if repeticiones == [5]:
        return ("Re-poker", PUNTUACIONES["Re-poker"])
    if repeticiones == [4, 1]:
        return ("Poker", PUNTUACIONES["Poker"])
    if repeticiones == [3, 2]:
        return ("Full", PUNTUACIONES["Full"])
    if repeticiones == [3, 1, 1]:
        return ("Trio", PUNTUACIONES["Trio"])
    if repeticiones == [2, 2, 1]:
        return ("Doble pareja", PUNTUACIONES["Doble pareja"])
    if repeticiones == [2, 1, 1, 1]:
        return ("Pareja", PUNTUACIONES["Pareja"])
    if es_escalera(dados):
        return ("Escalera", PUNTUACIONES["Escalera"])

    return ("Nada", PUNTUACIONES["Nada"])

def mostrar_dados(dados):
    print(" ".join(f"{i+1}:[{d}]" for i, d in enumerate(dados)))

def leer_indices():
    while True:
        entrada = input("Dados a relanzar (1-5, separados por espacio): ").strip()
        if not entrada: return []
        
        partes = entrada.split()
        if not all(p.isdigit() for p in partes):
            print("❌ Solo números")
            continue

        indices = [int(p) - 1 for p in partes]
        if not all(0 <= i < 5 for i in indices):
            print("❌ Valores entre 1 y 5")
            continue

        if len(indices) != len(set(indices)):
            print("❌ No repitas dados")
            continue
            
        return indices

def relanzar_dados(dados, indices):
    nuevos = dados.copy()
    for i in indices:
        if 0 <= i < len(dados):
            nuevos[i] = tirar_dado(6)
    return nuevos

def ia_facil():
    return [i for i in range(5) if random.choice([True, False])]

def ia_media(dados):
    conteo = contar_valores(dados)
    buenos = [n for n, c in conteo.items() if c >= 2]
    return [i for i, d in enumerate(dados) if d not in buenos]

def ia_inteligente(dados):
    conteo = contar_valores(dados)
    objetivo = max(conteo, key=conteo.get)
    return [i for i, d in enumerate(dados) if d != objetivo]

def jugar_turno(nombre="Jugador"):
    print(f"\n🎲 Turno de {nombre}")
    dados = tirar_varios_dados(5, 6)
    intentos = 2

    while intentos > 0:
        mostrar_dados(dados)
        if input("¿Relanzar? (s/n): ").strip().lower() not in ("s", "si"):
            break
        indices = leer_indices()
        dados = relanzar_dados(dados, indices)
        intentos -= 1

    mostrar_dados(dados)
    jugada, pts = evaluar_jugada(dados)
    print(f"{nombre} obtuvo: {jugada} ({pts} pts)")
    return pts

def turno_ia(nivel):
    print(f"\n🤖 Turno IA ({nivel})")
    dados = tirar_varios_dados(5, 6)
    intentos = 2

    while intentos > 0:
        if nivel == "facil": indices = ia_facil()
        elif nivel == "medio": indices = ia_media(dados)
        else: indices = ia_inteligente(dados)

        if not indices: break
        dados = relanzar_dados(dados, indices)
        intentos -= 1

    jugada, pts = evaluar_jugada(dados)
    print(f"La IA obtuvo: {jugada} ({pts} pts)")
    return pts

def modo_vs_ia():
    print("\n🤖 Selecciona dificultad:")
    print("1. Fácil\n2. Media\n3. Inteligente")
    op = input("Nivel: ").strip()
    nivel = {"1": "facil", "2": "medio", "3": "inteligente"}.get(op)

    if not nivel:
        print("❌ Nivel inválido")
        return

    pj = jugar_turno("Jugador")
    pi = turno_ia(nivel)

    if pj > pi: print("\n🏆 ¡Ganaste!")
    elif pi > pj: print("\n🤖 Gana la IA")
    else: print("\n🤝 Empate")

def modo_vs_jugador():
    p1 = jugar_turno("Jugador 1")
    p2 = jugar_turno("Jugador 2")

    if p1 > p2: print("\n🏆 Gana Jugador 1")
    elif p2 > p1: print("\n🏆 Gana Jugador 2")
    else: print("\n🤝 Empate")

def jugar_poker():
    print("\n" + "="*20)
    print("🎲 POKER DE DADOS")
    print("="*20)
    print("1. Jugador vs IA")
    print("2. Jugador vs Jugador")
    
    op = input("\nElige modo: ").strip()
    if op == "1":
        modo_vs_ia()
    elif op == "2":
        modo_vs_jugador()
    else:
        print("❌ Opción inválida")