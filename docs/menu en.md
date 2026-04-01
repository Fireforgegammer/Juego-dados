# 📄 Documentation: `menu.py`

> **Visual interface** module. Responsible exclusively for displaying the program's main menu on screen.

🌐 [Versión en español](menu_es.md) · [← Back to index](README.md)

---

## What does this file do?

Contains a single function whose only job is to print the main menu. It doesn't process input or make decisions — it just shows the user what options are available.

---

## Functions

---

### `mostrar_menu()`

Prints the main menu of the dice simulator to the console.

**No parameters. No return value.**

**Output:**
```
========================================
🎲 DICE LAUNCHER
========================================
1. Poker dice
2. D&D
3. Exit
```

---

## Dependencies

None. This module is completely self-contained and imports nothing.

---

## Flow diagram

```
┌──────────────────────────────┐
│       mostrar_menu()         │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  Print separator line        │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  Print title                 │
│  🎲 DICE LAUNCHER            │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  Print options:              │
│  1. Poker dice               │
│  2. D&D                      │
│  3. Exit                     │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  Done (returns nothing)      │
└──────────────────────────────┘
```

---

## Notes

- Its design follows the **single responsibility principle**: it only does one thing (show the menu).
- To add a new menu option, just add a `print()` line here and register the logic in `acciones.py`.
- The menu is displayed every time the main loop calls it, normally before asking the user for input.