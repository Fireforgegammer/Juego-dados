from core.dados import tirar_rol

def obtener_resumen_cesta(cesta):
    if not cesta:
        return "Cesta vacía"
    return ", ".join([f"{cant}d{caras}" for caras, cant in sorted(cesta.items())])

def calcular_lanzamiento_completo(cesta):
    resultados_detallados = {}
    total_general = 0
    for caras, cantidad in cesta.items():
        caras_int = int(caras)
        resultados, subtotal = tirar_rol(cantidad, caras_int)
        resultados_detallados[caras_int] = {
            "lista": resultados,
            "subtotal": subtotal
        }
        total_general += subtotal
    return resultados_detallados, total_general