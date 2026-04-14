import tkinter as tk
from PIL import Image, ImageTk
import os
from core.dados import tirar_rol

IMAGENES_ORIGINALES = {}
COLORES_DADOS = {
    4: "#e74c3c", 6: "#3498db", 8: "#2ecc71",
    10: "#f1c40f", 12: "#9b59b6", 20: "#e67e22", 100: "#1abc9c"
}

def cargar_assets_rol():
    global IMAGENES_ORIGINALES
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    assets_path = os.path.join(project_root, "ui", "assets")
    for t in COLORES_DADOS.keys():
        img_path = os.path.join(assets_path, f"rol_d{t}.png")
        if os.path.exists(img_path):
            try:
                IMAGENES_ORIGINALES[t] = Image.open(img_path).convert("RGBA")
            except:
                pass

class RolGUI:
    def __init__(self, root, volver_callback):
        self.root = root
        self.volver_al_menu = volver_callback
        self.cesta = {}
        self.referencias_img = []
        self.dados_disponibles = [
            ("d4", 4), ("d6", 6), ("d8", 8), 
            ("d10", 10), ("d12", 12), ("d20", 20), ("d100", 100)
        ]
        cargar_assets_rol()

    def limpiar_pantalla(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def iniciar_interfaz(self):
        self.limpiar_pantalla()
        tk.Label(self.root, text="MESA DE ROL", font=("Helvetica", 22, "bold"), fg="#2c3e50").pack(pady=10)
        
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=5)
        for nombre, caras in self.dados_disponibles:
            color = COLORES_DADOS.get(caras, "#34495e")
            tk.Button(frame_botones, text=nombre.upper(), font=("Arial", 10, "bold"), 
                      width=7, bg=color, fg="white", pady=6, relief="flat",
                      command=lambda c=caras: self.agregar_a_cesta(c), cursor="hand2").pack(side=tk.LEFT, padx=3)
        
        self.lbl_cesta = tk.Label(self.root, text="Cesta vacía", font=("Arial", 11, "italic"), fg="#e67e22")
        self.lbl_cesta.pack(pady=5)
        
        container = tk.Frame(self.root, bg="#ecf0f1")
        container.pack(fill="both", expand=True, padx=15, pady=5)
        
        self.canvas = tk.Canvas(container, bg="#ecf0f1", highlightthickness=0)
        self.scrollbar = tk.Scrollbar(container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#ecf0f1")
        
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas_win = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.itemconfig(self.canvas_win, width=e.width))
        
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        btm = tk.Frame(self.root)
        btm.pack(pady=15)
        tk.Button(btm, text="LANZAR DADOS", font=("Arial", 13, "bold"), bg="#27ae60", fg="white", 
                  width=18, pady=10, command=self.lanzar_cesta, cursor="hand2").pack(side=tk.LEFT, padx=10)
        tk.Button(btm, text="LIMPIAR", font=("Arial", 11), bg="#c0392b", fg="white",
                  width=10, pady=10, command=self.limpiar_cesta, cursor="hand2").pack(side=tk.LEFT, padx=10)
        tk.Button(self.root, text="VOLVER AL MENÚ", command=self.volver_al_menu, 
                  fg="#7f8c8d", font=("Arial", 10), bd=0, cursor="hand2").pack(pady=5)

    def agregar_a_cesta(self, caras):
        self.cesta[caras] = self.cesta.get(caras, 0) + 1
        self.actualizar_resumen()

    def limpiar_cesta(self):
        self.cesta = {}
        self.referencias_img = []
        for w in self.scrollable_frame.winfo_children(): w.destroy()
        self.actualizar_resumen()

    def actualizar_resumen(self):
        if not self.cesta: self.lbl_cesta.config(text="Cesta vacía")
        else:
            txt = " + ".join([f"{cant}d{caras}" for caras, cant in sorted(self.cesta.items())])
            self.lbl_cesta.config(text=f"Preparado: {txt}")

    def lanzar_cesta(self):
        if not self.cesta: return
        for w in self.scrollable_frame.winfo_children(): w.destroy()
        self.referencias_img = []
        
        self.scrollable_frame.update_idletasks()
        ancho_m = self.canvas.winfo_width() - 30
        total_dados = sum(self.cesta.values())
        
        if total_dados <= 2: size_dado = 160
        elif total_dados <= 6: size_dado = 120
        elif total_dados <= 15: size_dado = 90
        elif total_dados <= 30: size_dado = 75
        else: size_dado = 60

        cols = max(1, ancho_m // (size_dado + 15))
        col, row = 0, 0

        for caras, cantidad in sorted(self.cesta.items()):
            res, _ = tirar_rol(cantidad, caras)
            for val in res:
                if caras in IMAGENES_ORIGINALES:
                    img_scaled = IMAGENES_ORIGINALES[caras].resize((size_dado, size_dado), Image.Resampling.LANCZOS)
                    tk_img = ImageTk.PhotoImage(img_scaled)
                    self.referencias_img.append(tk_img)
                    
                    font_size = max(12, int(size_dado / 3.2))
                    lbl = tk.Label(self.scrollable_frame, image=tk_img, 
                                   text=str(val), compound="center",
                                   font=("Helvetica", font_size, "bold"), fg="white", bg="#ecf0f1")
                    lbl.grid(row=row, column=col, padx=8, pady=8)
                
                col += 1
                if col >= cols:
                    col = 0
                    row += 1
        
        self.cesta = {}
        self.actualizar_resumen()

def abrir_rol(root, volver_callback):
    juego = RolGUI(root, volver_callback)
    juego.iniciar_interfaz()