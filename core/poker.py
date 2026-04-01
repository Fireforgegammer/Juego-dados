import random
import time
from core.dados import tirar_varios_dados, tirar_dado

PUNTUACIONES = {
    "Nada": 1, 
    "Pareja": 2,
    "Doble pareja": 3,
    "Trio": 4,
    "Escalera": 5,
    "Full": 6,
    "Poker": 7,
    "Re-poker": 8
}

COLORES = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m"]
RESET = "\033[0m"

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
    if repeticiones == [5]: return ("Re-poker", PUNTUACIONES["Re-poker"])
    if repeticiones == [4, 1]: return ("Poker", PUNTUACIONES["Poker"])
    if repeticiones == [3, 2]: return ("Full", PUNTUACIONES["Full"])
    if repeticiones == [3, 1, 1]: return ("Trio", PUNTUACIONES["Trio"])
    if repeticiones == [2, 2, 1]: return ("Doble pareja", PUNTUACIONES["Doble pareja"])
    if repeticiones == [2, 1, 1, 1]: return ("Pareja", PUNTUACIONES["Pareja"])
    if es_escalera(dados): return ("Escalera", PUNTUACIONES["Escalera"])
    return ("Nada", PUNTUACIONES["Nada"])

def dibujar_dado(valor, caras=6, indice=0):
    if caras != 6: return [f"[{valor}]", "       ", "       "]
    color = COLORES[indice % len(COLORES)]
    patrones = {
        1: ["       ", "   ●   ", "       "],
        2: [" ●     ", "       ", "     ● "],
        3: [" ●     ", "   ●   ", "     ● "],
        4: [" ●   ● ", "       ", " ●   ● "],
        5: [" ●   ● ", "   ●   ", " ●   ● "],
        6: [" ●   ● ", " ●   ● ", " ●   ● "]
    }
    p = patrones.get(valor, ["  ?    ", "       ", "       "])
    return [
        f"{color}┌───────┐{RESET}",
        f"{color}│{p[0]}│{RESET}",
        f"{color}│{p[1]}│{RESET}",
        f"{color}│{p[2]}│{RESET}",
        f"{color}└───────┘{RESET}"
    ]

def mostrar_dados(dados, caras=6):
    dibujos = [dibujar_dado(dados[i], caras, i) for i in range(len(dados))]
    linea_indices = ""
    for i in range(len(dados)): linea_indices += f"    {i+1}      "
    print(linea_indices)
    for fila in range(5):
        linea = ""
        for d in dibujos: linea += d[fila] + "  "
        print(linea)

def animar_tirada_dados(dados_actual, indices_a_cambiar=None):
    if indices_a_cambiar is None:
        indices_a_cambiar = list(range(len(dados_actual)))
    print("\033[?25l", end="") 
    for _ in range(10):
        temp_dados = list(dados_actual)
        for idx in indices_a_cambiar:
            temp_dados[idx] = random.randint(1, 6)
        mostrar_dados(temp_dados)
        time.sleep(0.08)
        print("\033[F" * 7) # Sube 7 líneas para limpiar
    print("\033[?25h", end="")

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
        if 0 <= i < len(dados): nuevos[i] = tirar_dado(6)
    return nuevos

def ia_facil(): return [i for i in range(5) if random.choice([True, False])]

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
        if intentos == 2: animar_tirada_dados(dados)
        mostrar_dados(dados)
        while True:
            resp = input("\n¿Relanzar? (s/n): ").strip().lower()
            if resp in ("s", "si", "n", "no"): break
            print("❌ Error: Introduce 's' o 'n'")
        if resp in ("n", "no"): break
        indices = leer_indices()
        if not indices: break
        animar_tirada_dados(dados, indices)
        dados = relanzar_dados(dados, indices)
        intentos -= 1
    
    # Imprimimos resultado final con espacio
    mostrar_dados(dados)
    jugada, pts = evaluar_jugada(dados)
    print(f"\n✨ {nombre} obtuvo: {jugada} ({pts} pts)\n")
    return pts

def turno_ia(nivel):
    print(f"\n🤖 Turno IA ({nivel})")
    dados = tirar_varios_dados(5, 6)
    intentos = 2
    animar_tirada_dados(dados)
    while intentos > 0:
        if nivel == "facil": indices = ia_facil()
        elif nivel == "medio": indices = ia_media(dados)
        else: indices = ia_inteligente(dados)
        if not indices: break
        animar_tirada_dados(dados, indices)
        dados = relanzar_dados(dados, indices)
        intentos -= 1
    
    # Añadimos espacio para que la IA no pise el menú
    mostrar_dados(dados)
    jugada, pts = evaluar_jugada(dados)
    print(f"\n🤖 La IA obtuvo: {jugada} ({pts} pts)\n")
    return pts

def modo_vs_ia():
    print("\n🤖 Selecciona dificultad:\n1. Fácil\n2. Media\n3. Inteligente")
    op = input("Nivel: ").strip()
    nivel = {"1": "facil", "2": "medio", "3": "inteligente"}.get(op)
    if not nivel: return
    pj = jugar_turno("Jugador")
    pi = turno_ia(nivel)
    if pj > pi: print("🏆 ¡Ganaste!")
    elif pi > pj: print("🤖 Gana la IA")
    else: print("🤝 Empate")
    input("\nPresiona Enter para volver al menú...")

def modo_vs_jugador():
    p1 = jugar_turno("Jugador 1")
    p2 = jugar_turno("Jugador 2")
    if p1 > p2: print("🏆 Gana Jugador 1")
    elif p2 > p1: print("🏆 Gana Jugador 2")
    else: print("🤝 Empate")
    input("\nPresiona Enter para volver al menú...")

def jugar_poker():
    print("\n" + "="*20 + "\n🎲 POKER DE DADOS\n" + "="*20)
    print("1. Jugador vs IA\n2. Jugador vs Jugador")
    op = input("\nElige modo: ").strip()
    if op == "1": modo_vs_ia()
    elif op == "2": modo_vs_jugador()