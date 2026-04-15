import sys
import os

sys.stdout.reconfigure(encoding="utf-8")

ruta_raiz = os.path.dirname(os.path.abspath(__file__))
if ruta_raiz not in sys.path:
    sys.path.insert(0, ruta_raiz)

try:
    from ui.menu import mostrar_menu
    from ui.acciones_terminal import ejecutar_opcion_terminal
except ImportError as e:
    print(f"Error: {e}")
    sys.exit(1)

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()
        if not ejecutar_opcion_terminal(opcion):
            break

if __name__ == "__main__":
    main()