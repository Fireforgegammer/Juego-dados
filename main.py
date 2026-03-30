import sys
import os

# Añadir carpeta raíz al path para que Python encuentre ui/ y core/
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ui.menu import mostrar_menu
from ui.acciones import ejecutar_opcion

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()
        continuar = ejecutar_opcion(opcion)
        if not continuar:
            break

if __name__ == "__main__":
    main()