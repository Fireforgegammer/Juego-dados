from core.dados import tirar_rol
from ui.menu import mostrar_menu_rol
from core.visuals import imprimir_grid, ejecutar_animacion_rol


def jugar_rol():
    dados_disponibles = {"1": 4, "2": 6, "3": 8, "4": 10, "5": 12, "6": 20, "7": 100}
    cesta = {}
    mostrar_menu_rol()

    while True:
        if cesta:
            resumen = ", ".join([f"{cant}d{caras}" for caras, cant in cesta.items()])
            print(f"\nCesta: {resumen}")

        opcion = (
            input("\nAñade (1-7), Lanza (L), Limpia (C), Vuelve (8): ").strip().upper()
        )

        if opcion == "8":
            break
        elif opcion == "C":
            cesta = {}
            print("Cesta vaciada.")
        elif opcion == "L":
            if not cesta:
                continue

            dados_logica = []
            for caras_str, cant in cesta.items():
                for _ in range(cant):
                    dados_logica.append(int(caras_str))

            ejecutar_animacion_rol(dados_logica)

            resultados_finales = []
            for caras_str, cantidad in cesta.items():
                res, _ = tirar_rol(cantidad, int(caras_str))
                for r in res:
                    resultados_finales.append((r, int(caras_str)))

            print("\n" + "─" * 30)
            imprimir_grid(resultados_finales)
            print("─" * 30)

            input("\nPresiona Enter para continuar...")
            cesta = {}
            mostrar_menu_rol()

        elif opcion in dados_disponibles:
            caras = dados_disponibles[opcion]
            try:
                cantidad = int(input(f"¿Cuántos d{caras}?: ") or 0)
                if cantidad > 0:
                    cesta[str(caras)] = cesta.get(str(caras), 0) + cantidad
            except ValueError:
                pass
