from core.dados import tirar_rol
from ui.menu import mostrar_menu_rol

def jugar_rol():
    dados_disponibles = {
        "1": 4, "2": 6, "3": 8, 
        "4": 10, "5": 12, "6": 20, "7": 100
    }
    cesta = {}

    mostrar_menu_rol()
    while True:
        if cesta:
            resumen = ", ".join([f"{cant}d{caras}" for caras, cant in cesta.items()])
            print(f"\nDados seleccionados: {resumen}")
        
        opcion = input("\nAñade (1-7), Lanza (L), Limpia (C), Vuelve (8): ").strip().upper()

        if opcion == "8":
            break
        
        elif opcion == "L":
            if not cesta:
                print("⚠️ Cesta vacía.")
                continue
            
            print("\n" + "="*30)
            print("🎲 RESULTADOS INDIVIDUALES")
            print("="*30)
            
            for caras, cantidad in cesta.items():
                resultados, _ = tirar_rol(cantidad, int(caras))
                print(f"d{caras} ({cantidad} dados): {resultados}")
            
            input("\nPresiona Enter para continuar...")
            cesta = {}
            mostrar_menu_rol()

        elif opcion == "C":
            cesta = {}
            print("Cesta vaciada.")

        elif opcion in dados_disponibles:
            caras = dados_disponibles[opcion]
            try:
                cantidad = int(input(f"¿Cuántos d{caras} quieres añadir?: "))
                if cantidad > 0:
                    cesta[str(caras)] = cesta.get(str(caras), 0) + cantidad
            except ValueError:
                print("❌ Error: Número inválido.")
        else:
            print("❌ Opción no válida.")