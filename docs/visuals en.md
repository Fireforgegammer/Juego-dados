# 📄 Documentation: `visuals.py`

> **Console visualisation** module. Responsible for drawing dice, results, and comparisons in a clear and attractive way in the terminal.

🌐 [Versión en español](visuals_es.md) · [← Back to index](README.md)

---

## What does this file do?

Transforms dice numbers into something visually pleasant in the console. Instead of just seeing `[3, 1, 6, 4, 2]`, the player sees the dice drawn, with colours, aligned and easy to read.

It works together with `utils.py` to ensure text stays correctly aligned even when colours are used.

---

## Functions

---

### `mostrar_dados_visual(dados, nombre)`

Displays a player's dice on screen with their name and values shown visually.

| Parameter | Type | Description |
|-----------|------|-------------|
| `dados` | List | The 5 dice to display, e.g. `[3, 1, 6, 4, 2]` |
| `nombre` | `str` | The player's or AI's name |

**Returns nothing.** Prints to screen only.

**Example output:**
```
Player    🎲  1:[3]  2:[1]  3:[6]  4:[4]  5:[2]
```

---

### `mostrar_resultado(jugada, puntos, nombre)`

Shows the final hand achieved by a player along with their score.

| Parameter | Type | Description |
|-----------|------|-------------|
| `jugada` | `str` | Name of the combination, e.g. `"Full"` |
| `puntos` | `int` | Score achieved, e.g. `6` |
| `nombre` | `str` | The player's name |

**Example output:**
```
Player    →  Full House  (6 pts)
```

---

### `mostrar_comparativa(nombre1, pts1, nombre2, pts2)`

Shows a comparison table between two players' results and announces the winner.

**Example output:**
```
========================================
  Player      →  Full House   (6 pts)
  AI          →  Three oak    (5 pts)
----------------------------------------
  🏆 Player wins!
========================================
```

---

## Flow diagram

```
┌──────────────────────────────────────┐
│  mostrar_dados_visual(dados, nombre) │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  Format name with                    │
│  formatear_bloque() ← utils.py       │
│  (so all names are the same width)   │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  For each die in the list:           │
│    display   N:[value]               │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  Print the full line                 │
│  "Player 🎲 1:[3] 2:[1] ..."         │
└──────────────────────────────────────┘


┌──────────────────────────────────────┐
│  mostrar_comparativa(n1,p1,n2,p2)   │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  Show player 1 result                │
│  Show player 2 result                │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│   pts1 > pts2?  pts1 < pts2?         │
│   pts1 == pts2?                      │
└──────────────────┬───────────────────┘
                   │
        ┌──────────┼──────────┐
      p1 wins    draw       p2 wins
        │          │           │
        ▼          ▼           ▼
 "🏆 name1    "🤝 Draw!"   "🏆 name2
   wins!"                   wins!"
```

---

## Dependencies

| Module | Used for |
|--------|----------|
| `core.utils` | Uses `largo_real()` and `formatear_bloque()` to align text correctly |

---

## Notes

- This module **never makes game decisions**: it only displays information.
- Separating visuals from logic makes it easy to change the game's look without touching how it works.
- If a graphical interface were ever added, only this module would need replacing.