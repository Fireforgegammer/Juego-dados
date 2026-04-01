# 📄 Documentation: `dados.py`

> The base module of the simulator. Responsible for **rolling virtual dice** randomly.

🌐 [Versión en español](dados_es.md) · [← Back to index](README.md)

---

## What does this file do?

It's the most fundamental building block of the project. It simulates rolling dice just like you would with physical ones: it generates random numbers within a range defined by the number of sides on the die.

---

## Functions

---

### `tirar_dado(caras=6)`

Rolls **a single die** and returns the result.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `caras`   | `int` | `6`   | Number of sides on the die |

**Returns:** a random integer between `1` and `caras` (both included).

```python
result = tirar_dado()      # 6-sided die → can give 1, 2, 3, 4, 5 or 6
result = tirar_dado(20)    # 20-sided die (typical in D&D)
```

---

### `tirar_varios_dados(cantidad=5, caras=6)`

Rolls **several dice at once** and returns all results in a list.

| Parameter  | Type  | Default | Description |
|------------|-------|---------|-------------|
| `cantidad` | `int` | `5`     | How many dice to roll |
| `caras`    | `int` | `6`     | Number of sides on each die |

**Returns:** a list of integers. Each element is one die result.

```python
results = tirar_varios_dados()        # [3, 1, 6, 4, 2]
results = tirar_varios_dados(3, 10)   # Three 10-sided dice → [7, 2, 9]
```

---

## Dependencies

| Library | Used for |
|---------|----------|
| `random` (Python standard) | Generating random numbers |

---

## Flow diagram

```
┌─────────────────────────────────┐
│     tirar_dado(caras=6)         │
└─────────────────┬───────────────┘
                  │
                  ▼
┌─────────────────────────────────┐
│  Generate random number         │
│  between 1 and caras (included) │
└─────────────────┬───────────────┘
                  │
                  ▼
┌─────────────────────────────────┐
│  Return the number              │
└─────────────────────────────────┘


┌─────────────────────────────────┐
│  tirar_varios_dados(            │
│    cantidad=5, caras=6)         │
└─────────────────┬───────────────┘
                  │
                  ▼
┌─────────────────────────────────┐
│  Repeat `cantidad` times:       │
│    → call tirar_dado(caras)     │
└─────────────────┬───────────────┘
                  │
                  ▼
┌─────────────────────────────────┐
│  Return list with all results   │
│  E.g. [3, 1, 6, 4, 2]          │
└─────────────────────────────────┘
```

---

## Notes

- This module has **no game logic**. It only knows how to roll dice.
- It is used by `poker.py` and `rol.py` to get dice for each turn.
- The default `caras=6` makes it ready to use with no extra configuration.