import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import random
import time
from core.dados import tirar_varios_dados, tirar_dado
from core.poker import evaluar_jugada, ia_inteligente, ia_media, ia_facil

DICE_IMAGES = {}

def load_assets():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    assets_path = os.path.join(project_root, "ui", "assets")
    
    for i in range(1, 7):
        img_path = os.path.join(assets_path, f"dado_{i}.png")
        if os.path.exists(img_path):
            try:
                img = Image.open(img_path).convert("RGBA")
                img = img.resize((100, 100), Image.Resampling.LANCZOS)
                DICE_IMAGES[i] = ImageTk.PhotoImage(img)
            except:
                pass

def animar_dados(labels, iteracion, dados_finales, callback, seleccionados=None):
    if seleccionados is None:
        seleccionados = [True] * len(labels)
        
    if iteracion > 0:
        for i, lbl in enumerate(labels):
            if seleccionados[i]:
                cara_temp = random.randint(1, 6)
                if cara_temp in DICE_IMAGES:
                    lbl.config(image=DICE_IMAGES[cara_temp], text="")
                else:
                    lbl.config(text=f"[{cara_temp}]")
        labels[0].after(50, lambda: animar_dados(labels, iteracion - 1, dados_finales, callback, seleccionados))
    else:
        for i, lbl in enumerate(labels):
            if seleccionados[i]:
                if dados_finales[i] in DICE_IMAGES:
                    lbl.config(image=DICE_IMAGES[dados_finales[i]], text="")
                else:
                    lbl.config(text=f"[{dados_finales[i]}]")
        callback()

def mostrar_resultado_final(root, dados_p1, dados_p2, nombre_p2="Jugador 2"):
    for widget in root.winfo_children():
        widget.destroy()

    jugada1, pts1 = evaluar_jugada(dados_p1)
    jugada2, pts2 = evaluar_jugada(dados_p2)

    tk.Label(root, text="CUADRO DE HONOR", font=("Helvetica", 24, "bold"), fg="#2c3e50").pack(pady=20)
    
    main_frame = tk.Frame(root, bg="#f0f0f0")
    main_frame.pack(fill="both", expand=True, padx=40)

    f1 = tk.LabelFrame(main_frame, text="JUGADOR 1", font=("Arial", 12, "bold"), padx=15, pady=10, bg="white")
    f1.pack(fill="x", pady=10)
    d_frame1 = tk.Frame(f1, bg="white")
    d_frame1.pack()
    for d in dados_p1:
        img = DICE_IMAGES.get(d)
        if img: tk.Label(d_frame1, image=img, bg="white").pack(side=tk.LEFT, padx=5)
        else: tk.Label(d_frame1, text=f"[{d}]", font=("Arial", 18), bg="white").pack(side=tk.LEFT, padx=5)
    tk.Label(f1, text=jugada1, font=("Arial", 16, "bold"), fg="#2980b9", bg="white").pack()

    f2 = tk.LabelFrame(main_frame, text=nombre_p2.upper(), font=("Arial", 12, "bold"), padx=15, pady=10, bg="white")
    f2.pack(fill="x", pady=10)
    d_frame2 = tk.Frame(f2, bg="white")
    d_frame2.pack()
    for d in dados_p2:
        img = DICE_IMAGES.get(d)
        if img: tk.Label(d_frame2, image=img, bg="white").pack(side=tk.LEFT, padx=5)
        else: tk.Label(d_frame2, text=f"[{d}]", font=("Arial", 18), bg="white").pack(side=tk.LEFT, padx=5)
    tk.Label(f2, text=jugada2, font=("Arial", 16, "bold"), fg="#c0392b", bg="white").pack()

    if pts1 > pts2: res, color = "¡VICTORIA JUGADOR 1!", "#27ae60"
    elif pts2 > pts1: res, color = f"¡VICTORIA {nombre_p2.upper()}!", "#e74c3c"
    else: res, color = "EMPATE", "#7f8c8d"

    tk.Label(root, text=res, font=("Helvetica", 28, "bold"), fg=color).pack(pady=15)
    tk.Button(root, text="VOLVER AL MENÚ", font=("Arial", 13, "bold"), command=lambda: volver_al_inicio(root), 
              bg="#2c3e50", fg="white", width=25, pady=15, cursor="hand2").pack(pady=10)

def volver_al_inicio(root):
    from main import mostrar_menu
    mostrar_menu(root)

def iniciar_fase_jugador(root, callback_final, titulo_jugador, mano_rival=None):
    for widget in root.winfo_children():
        widget.destroy()
    
    if mano_rival:
        panel_rival = tk.LabelFrame(root, text="MANO A SUPERAR (JUGADOR 1)", font=("Arial", 10, "bold"), bg="#ecf0f1")
        panel_rival.pack(fill="x", padx=40, pady=10)
        d_rival_frame = tk.Frame(panel_rival, bg="#ecf0f1")
        d_rival_frame.pack(pady=5)
        for d in mano_rival:
            img = DICE_IMAGES.get(d)
            if img: tk.Label(d_rival_frame, image=img, bg="#ecf0f1").pack(side=tk.LEFT, padx=2)
            else: tk.Label(d_rival_frame, text=f"[{d}]", bg="#ecf0f1").pack(side=tk.LEFT, padx=2)

    estado = {"dados": tirar_varios_dados(5, 6), "intentos": 2}
    selecciones = [tk.BooleanVar() for _ in range(5)]
    
    tk.Label(root, text=titulo_jugador, font=("Helvetica", 22, "bold")).pack(pady=10)
    info_intentos = tk.Label(root, text=f"Relanzamientos restantes: {estado['intentos']}", font=("Arial", 12), fg="#e67e22")
    info_intentos.pack()

    cont = tk.Frame(root)
    cont.pack(pady=20)
    
    labels = []
    for i in range(5):
        f = tk.Frame(cont, padx=15)
        f.pack(side=tk.LEFT)
        l = tk.Label(f)
        l.pack()
        labels.append(l)
        tk.Checkbutton(f, variable=selecciones[i], cursor="hand2").pack(pady=5)

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    btn_relanzar = tk.Button(btn_frame, text="RELANZAR SELECCIONADOS", state="disabled", font=("Arial", 12, "bold"), 
                            bg="#2980b9", fg="white", padx=20, pady=10)
    btn_relanzar.pack(side=tk.LEFT, padx=10)

    btn_plantarse = tk.Button(btn_frame, text="PLANTARSE", state="disabled", font=("Arial", 12, "bold"), 
                             bg="#27ae60", fg="white", padx=20, pady=10)
    btn_plantarse.pack(side=tk.LEFT, padx=10)

    def terminar_turno():
        callback_final(estado["dados"])

    def ejecutar_relanzamiento():
        if estado["intentos"] > 0:
            indices = [i for i, v in enumerate(selecciones) if v.get()]
            if not indices:
                messagebox.showinfo("Atención", "Selecciona dados para cambiar.")
                return
            mask = [s.get() for s in selecciones]
            for i in indices:
                estado["dados"][i] = tirar_dado(6)
                selecciones[i].set(False)
            estado["intentos"] -= 1
            info_intentos.config(text=f"Relanzamientos restantes: {estado['intentos']}")
            btn_relanzar.config(state="disabled")
            btn_plantarse.config(state="disabled")
            animar_dados(labels, 15, estado["dados"], habilitar_botones, seleccionados=mask)
            if estado["intentos"] == 0:
                root.after(1200, terminar_turno)

    def habilitar_botones():
        if estado["intentos"] > 0:
            btn_relanzar.config(state="normal", command=ejecutar_relanzamiento)
            btn_plantarse.config(state="normal", command=terminar_turno)
        else:
            btn_relanzar.config(text="SIN INTENTOS", state="disabled")

    animar_dados(labels, 15, estado["dados"], habilitar_botones)

def comenzar_pvp(root):
    def final_jugador1(dados_p1):
        messagebox.showinfo("Turno terminado", "Turno del Jugador 2")
        iniciar_fase_jugador(root, lambda d2: mostrar_resultado_final(root, dados_p1, d2, "Jugador 2"), "TURNO JUGADOR 2", mano_rival=dados_p1)
    
    iniciar_fase_jugador(root, final_jugador1, "TURNO JUGADOR 1")

def comenzar_partida_ia(root, nivel_ia):
    for widget in root.winfo_children():
        widget.destroy()
    load_assets()
    estado = {"dados": tirar_varios_dados(5, 6), "intentos": 2}
    selecciones = [tk.BooleanVar() for _ in range(5)]
    tk.Label(root, text="TU TURNO", font=("Helvetica", 22, "bold")).pack(pady=10)
    info_intentos = tk.Label(root, text=f"Relanzamientos restantes: {estado['intentos']}", font=("Arial", 12), fg="#e67e22")
    info_intentos.pack()
    cont = tk.Frame(root); cont.pack(pady=30)
    labels = []
    for i in range(5):
        f = tk.Frame(cont, padx=15); f.pack(side=tk.LEFT)
        l = tk.Label(f); l.pack(); labels.append(l)
        tk.Checkbutton(f, variable=selecciones[i], cursor="hand2").pack(pady=5)
    btn_frame = tk.Frame(root); btn_frame.pack(pady=10)
    btn_relanzar = tk.Button(btn_frame, text="RELANZAR SELECCIONADOS", state="disabled", font=("Arial", 12, "bold"), bg="#2980b9", fg="white", padx=20, pady=10); btn_relanzar.pack(side=tk.LEFT, padx=10)
    btn_plantarse = tk.Button(btn_frame, text="PLANTARSE", state="disabled", font=("Arial", 12, "bold"), bg="#27ae60", fg="white", padx=20, pady=10); btn_plantarse.pack(side=tk.LEFT, padx=10)

    def preparar_interfaz_ia():
        for widget in root.winfo_children(): widget.destroy()
        lbl_status = tk.Label(root, text="TURNO DE LA IA", font=("Helvetica", 18, "bold"))
        lbl_status.pack(pady=10)
        panel = tk.Frame(root, bg="#f0f0f0"); panel.pack(fill="both", expand=True, padx=40)
        f_p1 = tk.LabelFrame(panel, text="TU MANO FINAL", font=("Arial", 10, "bold"), bg="white"); f_p1.pack(fill="x", pady=10)
        d_p1_frame = tk.Frame(f_p1, bg="white"); d_p1_frame.pack(pady=5)
        for d in estado["dados"]:
            tk.Label(d_p1_frame, image=DICE_IMAGES[d], bg="white").pack(side=tk.LEFT, padx=5)
        f_ia = tk.LabelFrame(panel, text=f"IA ({nivel_ia})", font=("Arial", 10, "bold"), bg="white"); f_ia.pack(fill="x", pady=10)
        ia_info = tk.Label(f_ia, text="Relanzamientos IA: 2", bg="white", font=("Arial", 9)); ia_info.pack()
        d_ia_frame = tk.Frame(f_ia, bg="white"); d_ia_frame.pack(pady=10)
        ia_labels, ia_vars = [], [tk.BooleanVar() for _ in range(5)]
        for i in range(5):
            f_dice = tk.Frame(d_ia_frame, bg="white", padx=10); f_dice.pack(side=tk.LEFT)
            l = tk.Label(f_dice, bg="white"); l.pack(); ia_labels.append(l)
            cb = tk.Checkbutton(f_dice, variable=ia_vars[i], bg="white", takefocus=0); cb.pack()
            cb.bind("<Button-1>", lambda e: "break")
        dados_ia, intentos_ia = tirar_varios_dados(5, 6), 2

        def motor_ia():
            nonlocal intentos_ia
            if nivel_ia == "Fácil": ind = ia_facil(dados_ia)
            elif nivel_ia == "Normal": ind = ia_media(dados_ia)
            else: ind = ia_inteligente(dados_ia)
            if ind and intentos_ia > 0:
                lbl_status.config(text="LA IA MARCA DADOS PARA RELANZAR...")
                mask = [False]*5
                for v in ia_vars: v.set(False)
                for i in ind: ia_vars[i].set(True); mask[i] = True
                root.update()
                def ejecutar():
                    nonlocal intentos_ia
                    for i in ind: dados_ia[i] = tirar_dado(6)
                    intentos_ia -= 1; ia_info.config(text=f"Relanzamientos IA: {intentos_ia}")
                    for v in ia_vars: v.set(False)
                    animar_dados(ia_labels, 15, dados_ia, lambda: root.after(1000, motor_ia), seleccionados=mask)
                root.after(1500, ejecutar)
            else:
                lbl_status.config(text="LA IA SE HA PLANTADO")
                root.after(1500, lambda: mostrar_resultado_final(root, estado["dados"], dados_ia, f"IA {nivel_ia}"))
        animar_dados(ia_labels, 20, dados_ia, lambda: root.after(1000, motor_ia))

    def ejecutar_relanzamiento():
        if estado["intentos"] > 0:
            ind = [i for i, v in enumerate(selecciones) if v.get()]
            if not ind: return
            mask = [s.get() for s in selecciones]
            for i in ind: estado["dados"][i] = tirar_dado(6); selecciones[i].set(False)
            estado["intentos"] -= 1; info_intentos.config(text=f"Relanzamientos restantes: {estado['intentos']}")
            btn_relanzar.config(state="disabled"); btn_plantarse.config(state="disabled")
            animar_dados(labels, 15, estado["dados"], habilitar_botones, seleccionados=mask)
            if estado["intentos"] == 0: root.after(1200, preparar_interfaz_ia)

    def habilitar_botones():
        if estado["intentos"] > 0:
            btn_relanzar.config(state="normal", command=ejecutar_relanzamiento)
            btn_plantarse.config(state="normal", command=preparar_interfaz_ia)
        else: btn_relanzar.config(text="SIN INTENTOS", state="disabled")
    animar_dados(labels, 15, estado["dados"], habilitar_botones)

def mostrar_niveles_ia(root):
    for widget in root.winfo_children(): widget.destroy()
    tk.Label(root, text="SELECCIONA DIFICULTAD", font=("Helvetica", 18, "bold")).pack(pady=40)
    for n in ["Fácil", "Normal", "IA Inteligente"]:
        tk.Button(root, text=n, width=30, font=("Arial", 13, "bold"), bg="#2c3e50", fg="white", pady=18, command=lambda x=n: comenzar_partida_ia(root, x), cursor="hand2").pack(pady=10)
    tk.Button(root, text="ATRÁS", command=lambda: abrir_poker(root), fg="#c0392b", font=("Arial", 12, "bold"), bd=0, cursor="hand2", pady=20).pack()

def abrir_poker(root):
    for widget in root.winfo_children(): widget.destroy()
    load_assets()
    tk.Label(root, text="PÓKER DE DADOS", font=("Helvetica", 28, "bold"), fg="#2c3e50").pack(pady=50)
    tk.Button(root, text="JUGAR VS IA", width=30, font=("Arial", 13, "bold"), bg="#2c3e50", fg="white", pady=18, command=lambda: mostrar_niveles_ia(root), cursor="hand2").pack(pady=10)
    tk.Button(root, text="JUGADOR VS JUGADOR", width=30, font=("Arial", 13, "bold"), bg="#2c3e50", fg="white", pady=18, command=lambda: comenzar_pvp(root), cursor="hand2").pack(pady=10)
    tk.Button(root, text="SALIR AL MENÚ", font=("Arial", 11), command=lambda: volver_al_inicio(root), fg="#7f8c8d", bd=0, cursor="hand2", pady=20).pack()