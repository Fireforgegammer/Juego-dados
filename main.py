import tkinter as tk
from poker_gui import abrir_poker

def abrir_dnd():
    from tkinter import messagebox
    messagebox.showinfo("D&D", "Aquí irá el submenú de D&D")

def mostrar_menu(root):
    for widget in root.winfo_children():
        widget.destroy()

    titulo = tk.Label(root, text="🎲 LANZADOR DE DADOS", font=("Arial", 16))
    titulo.pack(pady=20)

    btn_poker = tk.Button(root, text="Póker de Dados", width=20, command=lambda: abrir_poker(root))
    btn_poker.pack(pady=5)

    btn_dnd = tk.Button(root, text="D&D", width=20, command=abrir_dnd)
    btn_dnd.pack(pady=5)

    btn_salir = tk.Button(root, text="Salir", width=20, command=root.quit)
    btn_salir.pack(pady=5)

root = tk.Tk()
root.title("🎲 Lanzador de Dados")
root.geometry("400x300")

mostrar_menu(root)

root.mainloop()