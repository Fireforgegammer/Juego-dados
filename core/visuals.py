import time
import random
import os
from core.utils import formatear_bloque

RESET = "\033[0m"

def obtener_color_dado(caras):
    colores_por_caras = {
        4: "\033[91m",   
        6: "\033[92m",   
        8: "\033[93m",   
        10: "\033[94m",  
        12: "\033[96m",  
        20: "\033[95m",  
        100: "\033[97m" 
    }
    return colores_por_caras.get(caras, "\033[90m")

def mostrar_leyenda_colores(dados_en_pantalla):
    tipos_unicos = sorted(list(set([d[1] for d in dados_en_pantalla])))
    items = []
    for t in tipos_unicos:
        color = obtener_color_dado(t)
        items.append(f"{color}d{t}{RESET}")
    print(" | ".join(items))

def obtener_dibujo(valor, caras):
    color = obtener_color_dado(caras)
    v = str(valor).center(3)

    if caras == 4:
        return [f"  {color}▲{RESET}  ", f" {color}/{v}\\{RESET} ", f"{color}/_____\\{RESET}"]
    if caras == 8:
        return [f"  {color}▲{RESET}  ", f" {color}<{v}>{RESET} ", f"  {color}▼{RESET}  "]
    return [f"{color}┌───┐{RESET}", f"{color}│{v}│{RESET}", f"{color}└───┘{RESET}"]

def imprimir_grid(dados):
    if not dados:
        return 0
    
    mostrar_leyenda_colores(dados)
    
    ancho_consola = os.get_terminal_size().columns
    ancho_bloque = 11
    dados_por_fila = max(1, ancho_consola // ancho_bloque)
    lineas_totales = 1

    for i in range(0, len(dados), dados_por_fila):
        grupo = dados[i : i + dados_por_fila]
        dibujos = [obtener_dibujo(v, c) for v, c in grupo]
        for f in range(3):
            fila_texto = "".join(
                [formatear_bloque(d[f], ancho_bloque) for d in dibujos]
            )
            print(fila_texto)
            lineas_totales += 1
        print("")
        lineas_totales += 1
    return lineas_totales

def ejecutar_animacion_rol(dados_logica):
    print("\033[?25l", end="")
    h = 0
    for _ in range(10):
        if h > 0:
            print(f"\033[{h}F", end="")
        
        falsos = [(random.randint(1, c), c) for c in dados_logica]
        h = imprimir_grid(falsos)
        time.sleep(0.08)
    
    if h > 0:
        print(f"\033[{h}F", end="")
        for _ in range(h):
            print(" " * os.get_terminal_size().columns)
        print(f"\033[{h}F", end="", flush=True)
    
    print("\033[?25h", end="")