import tkinter as tk
from core.poker_gui import abrir_poker
from rol.rol_gui import abrir_rol

def limpiar_pantalla(root):
    for widget in root.winfo_children():
        widget.destroy()

def mostrar_menu(root):
    limpiar_pantalla(root)
    
    root.title("Multi-Juegos de Dados")
    root.geometry("800x600")
    root.configure(bg="#f0f0f0")

    tk.Label(
        root, 
        text="CENTRAL DE JUEGOS", 
        font=("Helvetica", 32, "bold"), 
        bg="#f0f0f0", 
        fg="#2c3e50"
    ).pack(pady=60)

    btn_frame = tk.Frame(root, bg="#f0f0f0")
    btn_frame.pack(expand=True)

    tk.Button(
        btn_frame, 
        text="PÓKER DE DADOS", 
        width=25, 
        font=("Arial", 14, "bold"), 
        bg="#2980b9", 
        fg="white", 
        pady=20, 
        cursor="hand2",
        command=lambda: abrir_poker(root)
    ).pack(pady=15)

    tk.Button(
        btn_frame, 
        text="LANZADOR ROL (D&D)", 
        width=25, 
        font=("Arial", 14, "bold"), 
        bg="#c0392b", 
        fg="white", 
        pady=20, 
        cursor="hand2",
        command=lambda: abrir_rol(root, lambda: mostrar_menu(root))
    ).pack(pady=15)

    tk.Button(
        root, 
        text="SALIR", 
        font=("Arial", 12), 
        bg="#f0f0f0", 
        fg="#7f8c8d", 
        bd=0, 
        cursor="hand2",
        command=root.quit
    ).pack(pady=40)

if __name__ == "__main__":
    root = tk.Tk()
    mostrar_menu(root)
    root.mainloop()