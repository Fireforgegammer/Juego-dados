# 📄 Documentation: `rol.py`

> Module for **D&D mode** (Dungeons & Dragons). Allows rolling different types of RPG dice and displays the results.

🌐 [Versión en español](rol_es.md) · [← Back to index](README.md)

---

## What does this file do?

Simulates the dice rolls typical in tabletop RPGs like Dungeons & Dragons. Unlike poker (which always uses 5 six-sided dice), here the player can choose **what type of die** and **how many** to roll.

---

## Available dice types

RPG games use dice with different numbers of sides. They're named with a "d" followed by the number of sides:

| Die | Sides | Typical use |
|-----|-------|-------------|
| `d4` | 4 | Dagger damage |
| `d6` | 6 | Standard die |
| `d8` | 8 | Short sword damage |
| `d10` | 10 | Long sword damage |
| `d12` | 12 | War axe damage |
| `d20` | 20 | Skill checks and attacks |

---

## Functions

---

### `tirar_rol(cantidad, caras)`

Rolls several dice of the same type and returns individual results and the total.

| Parameter | Type | Description |
|-----------|------|-------------|
| `cantidad` | `int` | How many dice to roll |
| `caras` | `int` | Number of sides on each die |

**Returns:** a tuple with `(list_of_rolls, total)`

```python
tirar_rol(3, 6)   →  ([4, 2, 6], 12)   # Three d6: results and sum
tirar_rol(1, 20)  →  ([17], 17)         # One d20
tirar_rol(2, 8)   →  ([5, 3], 8)        # Two d8
```

---

### `jugar_rol()`

Entry point for D&D mode. Guides the player through choosing the die type and count, rolls, and displays results.

**No parameters. No return value** (prints results directly).

---

## Flow diagram

```
┌──────────────────────────────┐
│         jugar_rol()          │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  Show available dice         │
│  d4, d6, d8, d10, d12, d20  │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  How many sides? (4/6/8...)  │
│  Player types a number       │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  How many dice to roll?      │
│  Player types a number       │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      tirar_rol(cantidad,     │
│               caras)         │
│  ← uses tirar_varios_dados() │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  Shows each roll             │
│  Die 1: [4]                  │
│  Die 2: [2]                  │
│  Die 3: [6]                  │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  Shows total: 12             │
└──────────────────────────────┘
```

---

## Dependencies

| Module | Used for |
|--------|----------|
| `core.dados` | Uses `tirar_varios_dados()` to roll the dice |