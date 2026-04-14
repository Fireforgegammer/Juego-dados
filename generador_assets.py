import os
from PIL import Image, ImageDraw

def generar_dados_ui(ruta_destino="ui/assets"):
    if not os.path.exists(ruta_destino):
        os.makedirs(ruta_destino)
    size = 512
    for valor in range(1, 7):
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        pad = size // 8
        rect = [pad, pad, size - pad, size - pad]
        draw.rounded_rectangle(rect, radius=size//6, fill=(190, 20, 20, 230), outline=(255, 100, 100, 250), width=4)
        c = size // 2
        p1, p2 = pad * 2.5, size - pad * 2.5
        r = size // 18
        posiciones = {
            1: [(c, c)], 2: [(p1, p1), (p2, p2)], 3: [(p1, p1), (c, c), (p2, p2)],
            4: [(p1, p1), (p2, p1), (p1, p2), (p2, p2)],
            5: [(p1, p1), (p2, p1), (c, c), (p1, p2), (p2, p2)],
            6: [(p1, p1), (p2, p1), (p1, c), (p2, c), (p1, p2), (p2, p2)]
        }
        for (x, y) in posiciones[valor]:
            draw.ellipse([x - r, y - r, x + r, y + r], fill=(255, 255, 255, 255))
        nombre_final = os.path.join(ruta_destino, f"dado_{valor}.png")
        img.save(nombre_final)

def generar_dados_rol(ruta_destino="ui/assets"):
    if not os.path.exists(ruta_destino):
        os.makedirs(ruta_destino)
    size = 512
    config_rol = [
        (4, "#e74c3c"), (6, "#3498db"), (8, "#2ecc71"),
        (10, "#f1c40f"), (12, "#9b59b6"), (20, "#e67e22"), (100, "#1abc9c")
    ]
    for caras, color in config_rol:
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        pad = size // 8
        rect = [pad, pad, size - pad, size - pad]
        draw.rounded_rectangle(rect, radius=size//4, fill=color, outline="black", width=12)
        nombre_final = os.path.join(ruta_destino, f"rol_d{caras}.png")
        img.save(nombre_final)

if __name__ == "__main__":
    generar_dados_ui()
    generar_dados_rol()