import time
import random
import os
from core.utils import formatear_bloque

COLORES = {4: "\033[91m", 6: "\033[92m", 8: "\033[93m", 10: "\033[94m", 12: "\033[96m", 20: "\033[95m", 100: "\033[97m"}
RESET = "\033[0m"

def obtener_dibujo(valor, caras):
    c = COLORES.get(caras, RESET)
    v = str(valor).center(3)
    
    if caras == 4:
        return [
            f"   {c}▲{RESET}  ",
            f"  {c}/{v}\\{RESET} ",
            f" {c}/_____\\{RESET}"
        ]
    if caras == 8:
        return [
            f"  {c}▲{RESET}   ",
            f" {c}<{v}>{RESET}  ",
            f"  {c}▼{RESET}   "
        ]
    return [
        f"{c}┌───┐{RESET}",
        f"{c}│{v}│{RESET}",
        f"{c}└───┘{RESET}"
    ]

def imprimir_grid(dados):
    if not dados: return 0
    ancho_consola = os.get_terminal_size().columns
    ancho_bloque = 11 
    dados_por_fila = max(1, ancho_consola // ancho_bloque)
    lineas_totales = 0

    for i in range(0, len(dados), dados_por_fila):
        grupo = dados[i : i + dados_por_fila]
        dibujos = [obtener_dibujo(v, c) for v, c in grupo]
        for f in range(3):
            fila_texto = "".join([formatear_bloque(d[f], ancho_bloque) for d in dibujos])
            print(fila_texto)
            lineas_totales += 1
        print("")
        lineas_totales += 1
    return lineas_totales

def ejecutar_animacion_rol(dados_logica):
    print("\033[?25l", end="")
    h = 0
    for _ in range(12):
        if h > 0: print(f"\033[{h}A\r", end="")
        falsos = [(random.randint(1, c), c) for c in dados_logica]
        h = imprimir_grid(falsos)
        time.sleep(0.06)
    
    print(f"\033[{h}A\r", end="")
    for _ in range(h): print(" " * os.get_terminal_size().columns)
    print(f"\033[{h}A\r", end="", flush=True)
    print("\033[?25h", end="")