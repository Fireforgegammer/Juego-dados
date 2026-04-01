# 📄 Documentación: `menu.py`

> Módulo de **interfaz visual**. Se encarga exclusivamente de mostrar el menú principal del programa en pantalla.

🌐 [English version](menu_en.md) · [← Volver al índice](README.md)

---

## ¿Qué hace este archivo?

Contiene una única función cuya única responsabilidad es imprimir el menú principal. No procesa entradas ni toma decisiones: solo muestra al usuario qué opciones tiene disponibles.

---

## Funciones

---

### `mostrar_menu()`

Imprime en consola el menú principal del simulador de dados.

**No recibe parámetros.**  
**No devuelve nada.**

**Salida en pantalla:**
```
========================================
🎲 LANZADOR DE DADOS
========================================
1. Poker de dados
2. D&D
3. Salir
```

---

## Dependencias

Ninguna. Este módulo es completamente autónomo y no importa nada.

---

## Diagrama de flujo

```
┌──────────────────────────────┐
│       mostrar_menu()         │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  Imprime línea separadora    │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  Imprime título              │
│  🎲 LANZADOR DE DADOS        │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  Imprime las opciones:       │
│  1. Poker de dados           │
│  2. D&D                      │
│  3. Salir                    │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  Fin (no devuelve nada)      │
└──────────────────────────────┘
```

---

## Notas

- Su diseño sigue el principio de **responsabilidad única**: solo hace una cosa (mostrar el menú).
- Para añadir una nueva opción al menú, solo hay que agregar una línea `print()` aquí y registrar la lógica en `acciones.py`.
- El menú se muestra cada vez que el bucle principal lo llama, normalmente antes de pedir la opción al usuario.