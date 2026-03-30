from core.dados import tirar_dado

def jugar_rol():
    print("\n🧙 Tirada de rol (d20)...")
    resultado = tirar_dado(20)
    print("Resultado:", resultado)