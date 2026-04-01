# 📚 Naming Conventions

> Style guide for the **Dice Simulator** project: how things are named, why, and what conventions are followed. Written for people with no prior programming experience.

🌐 [Versión en español](nomenclatura_es.md) · [← Back to index](README.md)

---

## 📖 Glossary

| Term | Plain meaning |
|------|---------------|
| **Module** | A `.py` file. Each module does one specific thing. |
| **Function** | A named block of code that performs a task. You call it by writing its name followed by `()`. |
| **Parameter** | A value you give a function so it knows how to work. E.g. how many sides the die has. |
| **Default value** | The value the function uses if you don't specify one. E.g. `faces=6` uses 6 if you say nothing. |
| **Returns** | What the function gives you back when it's done. Like the result on a calculator. |
| **List** | An ordered collection of values. E.g. `[3, 1, 6, 4, 2]` — five dice results. |
| **Dictionary** | Key-value pairs. E.g. `{3: 2, 5: 3}` means "3 appeared twice, 5 appeared three times". |
| **Index** | The position of an element in a list. Starts at 0. Die 1 → index 0. |
| **Boolean** | A value that can only be `True` or `False`. |
| **Import** | Using code from another module. Like borrowing a tool. |
| **AI** | Artificial Intelligence. In this project, the virtual opponent. |
| **Tuple** | Like a list, but its values cannot change. E.g. `("Full House", 6)`. |
| **String** | A text value. E.g. `"easy"`, `"Player"`. |

---

## 🔤 How functions are named

Functions follow the **`verb_noun`** pattern in Spanish with underscores (`snake_case`):

```
tirar_dado         →  roll  +  die
mostrar_menu       →  show  +  menu
evaluar_jugada     →  evaluate  +  hand
```

> 💡 **Why this way?** Because reading `tirar_dado()` (roll die) is almost like reading plain language. You know exactly what it does without needing an explanation.

### Full function table

| Function | Verb | Object | What it does |
|----------|------|--------|--------------|
| `tirar_dado` | roll | die | Rolls a single die |
| `tirar_varios_dados` | roll | several dice | Rolls multiple dice |
| `contar_valores` | count | values | Counts how many times each number appears |
| `es_escalera` | is | straight | Checks if dice form a straight |
| `evaluar_jugada` | evaluate | hand | Identifies the poker combination |
| `mostrar_dados` | show | dice | Prints the dice to screen |
| `leer_indices` | read | indices | Gets which dice the user wants to re-roll |
| `relanzar_dados` | re-roll | dice | Re-rolls the chosen dice |
| `jugar_turno` | play | turn | Manages the full human player turn |
| `turno_ia` | turn | ai | Manages the AI opponent's turn |
| `modo_vs_ia` | mode | vs ai | Player vs AI match |
| `modo_vs_jugador` | mode | vs player | Two human players match |
| `jugar_poker` | play | poker | Starts the full poker game |
| `jugar_rol` | play | rpg | Starts D&D mode |
| `mostrar_menu` | show | menu | Draws the main menu |
| `ejecutar_opcion` | execute | option | Runs the action for the chosen option |
| `largo_real` | real | length | Measures text ignoring colour codes |
| `formatear_bloque` | format | block | Pads text with spaces to a fixed width |

---

## 🔤 How variables are named

Variables also use `snake_case` with Spanish names. They aim to be **short but descriptive**:

| Variable | Type | Example | Meaning |
|----------|------|---------|---------|
| `dados` | List | `[3, 1, 6, 4, 2]` | The 5 current dice |
| `caras` | Integer | `6` | Number of sides on the die |
| `cantidad` | Integer | `5` | How many dice to roll |
| `conteo` | Dictionary | `{3: 2, 6: 1}` | How many times each number appeared |
| `repeticiones` | List | `[3, 2]` | Frequencies sorted highest to lowest |
| `indices` | List | `[0, 2, 4]` | Positions of dice to re-roll (0-based) |
| `intentos` | Integer | `2` | Re-rolls remaining |
| `nivel` | String | `"facil"` | AI difficulty level |
| `jugada` | String | `"Full"` | Name of the combination achieved |
| `pts` | Integer | `6` | Score for the hand |
| `pj` | Integer | `5` | Human player's points |
| `pi` | Integer | `7` | AI's points |
| `opcion` | String | `"1"` | Option chosen from the menu |
| `buenos` | List | `[3, 5]` | Values the AI decides to keep |
| `objetivo` | Integer | `4` | Value the AI tries to maximise |
| `ancho` | Integer | `20` | Width in characters of a visual block |
| `relleno` | Integer | `8` | Extra spaces to reach the target width |

---

## 📐 Code conventions

### Comments in Spanish
All code is commented in Spanish to stay consistent with variable and function names.

### Clear default values
When a function has a default value, it's the most common use case:

```python
def tirar_dado(caras=6):                      # A normal die has 6 sides
def tirar_varios_dados(cantidad=5, caras=6):  # Poker uses 5 six-sided dice
```

### Single responsibility principle
Each module does **one thing only**:

| Module | Its single responsibility |
|--------|--------------------------|
| `dados.py` | Roll dice |
| `poker.py` | Poker game logic |
| `utils.py` | Text helper tools |
| `visuals.py` | Display things on screen |
| `menu.py` | Draw the menu |
| `acciones.py` | Connect menu to games |

---

## 📦 Module dependency diagram

```
main.py
   │
   ├── ui/menu.py          (depends on nothing)
   └── ui/acciones.py
          ├── core/poker.py
          │      ├── core/dados.py
          │      │      └── random  ← Python built-in
          │      └── random
          ├── core/rol.py
          │      └── core/dados.py
          └── core/visuals.py
                 └── core/utils.py
                        └── re  ← Python built-in
```

> **General rule:** modules at the bottom (`dados.py`, `utils.py`) don't know anyone. Modules at the top (`acciones.py`, `main.py`) coordinate everything. Never the other way around.

---

## 🔄 Visual dependency diagram

```
     main.py
        │
   ┌────┴────┐
menu.py   acciones.py
              │
         ┌────┴────┐
      poker.py   rol.py
         │          │
         └────┬─────┘
           dados.py
              │
           random

visuals.py → utils.py → re
```