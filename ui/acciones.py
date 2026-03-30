from core.poker import jugar_poker
from core.rol import jugar_rol

def ejecutar_opcion(opcion):
    if opcion == "1":
        # Simplemente llamamos a la función. 
        # Ella ya se encarga de sus propios menús internos.
        jugar_poker()
        return True

    elif opcion == "2":
        jugar_rol()
        return True

    elif opcion == "3":
        print("👋 Saliendo...")
        return False
        
    else:
        print("❌ Opción no válida")
        return True