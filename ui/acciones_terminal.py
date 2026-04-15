import random
import time
import os
from core.poker import evaluar_jugada, ia_facil, ia_media, ia_inteligente
from core.visuals import *

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def gestionar_turno_poker(nombre, func_ia=None):
    limpiar()
    print(f"\n--- TURNO {nombre} ---")
    dados = [(random.randint(1, 6), 6) for _ in range(5)]
    animar_poker(dados)
    
    for lanz in range(2):
        limpiar()
        print(f"\n--- TURNO {nombre} ---")
        print(f"Lanzamiento {lanz + 1}/2")
        imprimir_poker(dados, mostrar_indices=True)
        
        if func_ia:
            print(f"\nLa IA está pensando su jugada...")
            time.sleep(1.5)
            idx = func_ia([d[0] for d in dados])
            if not idx: 
                print("La IA decide plantarse.")
                time.sleep(1)
                break
        else:
            acc = input("\n1. Relanzar | 2. Plantarse: ")
            if acc == "2": break
            try:
                entrada = input("Dados a cambiar (1-5 con espacio): ")
                idx = [int(i)-1 for i in entrada.split() if i.isdigit()]
            except: idx = []
            
        if idx:
            animar_poker(dados, idx)
            for i in idx: 
                if 0 <= i < 5:
                    dados[i] = (random.randint(1, 6), 6)
    
    res, pts = evaluar_jugada([d[0] for d in dados])
    limpiar()
    print(f"\n--- RESULTADO {nombre} ---")
    imprimir_poker(dados)
    print(f"JUGADA: {res}")
    time.sleep(2)
    return {"dados": dados, "texto": res, "puntos": pts}

def jugar_poker():
    while True:
        limpiar()
        print("\n--- PÓKER DE DADOS ---\n1. Humano vs IA\n2. Humano vs Humano\n3. Volver al menú principal")
        modo = input("Opción: ")
        if modo == "3": break
        if modo not in ["1", "2"]: continue
        
        func_ia = None
        if modo == "1":
            print("\n1. Fácil | 2. Media | 3. Difícil")
            dif = input("IA: ")
            func_ia = {"1": ia_facil, "2": ia_media}.get(dif, ia_inteligente)
            
        while True:
            res1 = gestionar_turno_poker("JUGADOR 1")
            print("\nPasando al turno del siguiente jugador...")
            time.sleep(1.5)
            
            res2 = gestionar_turno_poker("JUGADOR 2" + (" (IA)" if func_ia else ""), func_ia)
            
            limpiar()
            print("\n" + "="*40)
            print(f"JUGADOR 1: {res1['texto']}")
            imprimir_poker(res1['dados'])
            print(f"\nJUGADOR 2: {res2['texto']}")
            imprimir_poker(res2['dados'])
            
            if res1['puntos'] > res2['puntos']: print("\n¡GANA JUGADOR 1!")
            elif res2['puntos'] > res1['puntos']: print("\n¡GANA JUGADOR 2!")
            else: print("\n¡EMPATE!")
            print("="*40)

            print("\n1. Repetir | 2. Cambiar modo | 3. Volver al menú principal")
            f = input("Opción: ")
            if f == "1": continue
            if f == "2": break
            return

def eliminar_dados_cesta(cesta_grupos):
    colores = {4: "\033[93m", 6: "\033[92m", 8: "\033[94m", 10: "\033[91m", 12: "\033[95m", 20: "\033[33m", 100: "\033[96m"}
    reset = "\033[0m"
    
    while cesta_grupos:
        limpiar()
        mostrar_leyenda_rol()
        print("\n--- LISTA DE DADOS ---")
        for i, (tipo, cant) in enumerate(cesta_grupos):
            color = colores.get(tipo, reset)
            print(f"({i+1}) {color}{cant}d{tipo}{reset}", end="  ")
        
        try:
            sel = input("\n\nElegir dados o enter para relanzar: ")
            if not sel: return True
            
            idx = int(sel) - 1
            if 0 <= idx < len(cesta_grupos):
                tipo, cant = cesta_grupos[idx]
                quitar = int(input(f"¿Cuántos d{tipo} quieres quitar? (Disponibles {cant}): "))
                if quitar >= cant:
                    cesta_grupos.pop(idx)
                elif quitar > 0:
                    cesta_grupos[idx] = (tipo, cant - quitar)
                
                if not cesta_grupos: break
                
                cont = input("\n¿Quieres eliminar más dados antes de relanzar? (S/N): ").upper()
                if cont != "S": return True
        except: break
    return True

def mesa_de_rol():
    tipos = [4, 6, 8, 10, 12, 20, 100]
    cesta_grupos = [] 
    while True:
        limpiar()
        mostrar_leyenda_rol()
        texto_cesta = " + ".join([f"{cant}d{tipo}" for tipo, cant in cesta_grupos])
        print(f"\nCesta actual: {texto_cesta if texto_cesta else 'Vacía'}")
        print("-" * 30)
        print("L. LANZAR | C. LIMPIAR CESTA | E. ELIMINAR DADO | V. VOLVER AL MENÚ PRINCIPAL")
        
        opc = input("\nSeleccione dados o acción: ").upper()
        
        if opc == "V": break
        if opc == "C": cesta_grupos = []; continue
        if opc == "E": eliminar_dados_cesta(cesta_grupos); continue

        if opc == "L" and cesta_grupos:
            while True:
                limpiar()
                mostrar_leyenda_rol()
                dados_finales = []
                for tipo, cant in cesta_grupos:
                    for _ in range(cant): 
                        dados_finales.append((random.randint(1, tipo), tipo))
                
                animar_rol(dados_finales)
                limpiar()
                mostrar_leyenda_rol()
                print("\n--- RESULTADO DEL LANZAMIENTO ---")
                
                for i in range(0, len(dados_finales), 6):
                    grupo = dados_finales[i:i+6]
                    imprimir_rol(grupo)
                
                print("\n1. Relanzar | 2. Seleccionar dados | 3. Volver al menú principal")
                p = input("Opción: ")
                
                if p == "1":
                    resp = input("¿Quieres quitar algún dado antes de relanzar? (S/N): ").upper()
                    if resp == "S":
                        eliminar_dados_cesta(cesta_grupos)
                        if not cesta_grupos: break
                    continue
                if p == "2": cesta_grupos = []; break
                return
                
        elif opc.isdigit() and 1 <= int(opc) <= 7:
            tipo_sel = tipos[int(opc)-1]
            try:
                cant_sel = int(input(f"¿Cuántos d{tipo_sel} añadir?: "))
                if cant_sel > 0:
                    añadido = False
                    for i, (tipo, cant) in enumerate(cesta_grupos):
                        if tipo == tipo_sel:
                            resp = input(f"Ya hay d{tipo_sel}. ¿Sumar a los existentes? (S/N): ").upper()
                            if resp == "S":
                                cesta_grupos[i] = (tipo, cant + cant_sel)
                                añadido = True
                                break
                    if not añadido:
                        cesta_grupos.append((tipo_sel, cant_sel))
            except: pass

def ejecutar_opcion_terminal(opcion):
    if opcion == "1": jugar_poker()
    elif opcion == "2": mesa_de_rol()
    return opcion != "3"