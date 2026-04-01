import tkinter as tk
from tkinter import messagebox

def iniciar_vs_ia():
    messagebox.showinfo("Jugador vs IA", "Aquí se jugará contra la IA")

def iniciar_vs_jugador():
    messagebox.showinfo("Jugador vs Jugador", "Aquí se jugará jugador vs jugador")

def abrir_poker(root):
    for widget in root.winfo_children():
        widget.destroy()

    titulo = tk.Label(root, text="🎲 POKER DE DADOS", font=("Arial", 16))
    titulo.pack(pady=20)

    btn_vs_ia = tk.Button(root, text="Jugador vs IA", width=20, command=iniciar_vs_ia)
    btn_vs_ia.pack(pady=5)

    btn_vs_jugador = tk.Button(root, text="Jugador vs Jugador", width=20, command=iniciar_vs_jugador)
    btn_vs_jugador.pack(pady=5)

    btn_volver = tk.Button(root, text="Volver al menú", width=20, command=lambda: volver_menu(root))
    btn_volver.pack(pady=5)

def volver_menu(root):
    from main import mostrar_menu
    mostrar_menu(root)