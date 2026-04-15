import time
import random
from core.utils import formatear_bloque

RESET = "\033[0m"
ROJO_POKER = "\033[91m"

def obtener_color_dado(caras, es_poker=False):
    if es_poker: return ROJO_POKER
    colores = {4: "\033[93m", 6: "\033[92m", 8: "\033[94m", 10: "\033[91m", 12: "\033[95m", 20: "\033[38;5;208m", 100: "\033[96m"}
    return colores.get(caras, "\033[97m")

def dibujo_poker(valor):
    puntos = {
        1: ["       ", "   •   ", "       "],
        2: [" •     ", "       ", "     • "],
        3: [" •     ", "   •   ", "     • "],
        4: [" •   • ", "       ", " •   • "],
        5: [" •   • ", "   •   ", " •   • "],
        6: [" •   • ", " •   • ", " •   • "]
    }
    p = puntos.get(valor, ["       ", f"  {str(valor).center(3)}  ", "       "])
    return [f"{ROJO_POKER}┌───────┐{RESET}", f"{ROJO_POKER}│{p[0]}│{RESET}", f"{ROJO_POKER}│{p[1]}│{RESET}", f"{ROJO_POKER}│{p[2]}│{RESET}", f"{ROJO_POKER}└───────┘{RESET}"]

def dibujo_rol(valor, caras):
    color = obtener_color_dado(caras)
    v = str(valor).center(3)
    return [f"{color}┌───────┐{RESET}", f"{color}│       │{RESET}", f"{color}│  {v}  │{RESET}", f"{color}│       │{RESET}", f"{color}└───────┘{RESET}"]

def imprimir_poker(dados, mostrar_indices=False):
    dibujos = [dibujo_poker(v) for v, c in dados]
    for f in range(5):
        print("".join([formatear_bloque(d[f], 12) for d in dibujos]))
    if mostrar_indices:
        print("".join([formatear_bloque(f"   ({i+1})", 12) for i in range(len(dados))]))
    print("")
    return 7 if mostrar_indices else 6

def imprimir_rol(dados):
    for i in range(0, len(dados), 6):
        grupo = dados[i:i+6]
        dibujos = [dibujo_rol(v, c) for v, c in grupo]
        for f in range(5):
            print("".join([formatear_bloque(d[f], 12) for d in dibujos]))
        print("")
    lineas = ((len(dados)-1)//6 + 1) * 6
    return lineas

def animar_poker(dados_actuales, indices=None):
    print("\033[?25l", end="")
    h = 0
    idx = indices if indices is not None else list(range(len(dados_actuales)))
    for _ in range(8):
        if h > 0: print(f"\033[{h}A", end="")
        temp = [(random.randint(1, 6) if i in idx else v, 6) for i, (v, c) in enumerate(dados_actuales)]
        h = imprimir_poker(temp)
        time.sleep(0.08)
    print("\033[?25h", end="")

def animar_rol(dados_cesta):
    print("\033[?25l", end="")
    h = 0
    for _ in range(8):
        if h > 0: print(f"\033[{h}A", end="")
        temp = [(random.randint(1, c), c) for v, c in dados_cesta]
        h = imprimir_rol(temp)
        time.sleep(0.08)
    print("\033[?25h", end="")

def mostrar_leyenda_rol():
    tipos = [4, 6, 8, 10, 12, 20, 100]
    leyenda = " ".join([f"{obtener_color_dado(t)}[ ({i+1}) d{t} ]{RESET}" for i, t in enumerate(tipos)])
    print(f"\n{leyenda}")