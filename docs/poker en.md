# 📄 Documentation: `poker.py`

> Main module of the **Poker Dice** game. Contains all the logic: hand evaluation, player turns, AI behaviour, and game modes.

🌐 [Versión en español](poker_es.md) · [← Back to index](README.md)

---

## What does this file do?

Implements the full Poker Dice game. A player rolls 5 dice, can re-roll whichever they choose up to 2 times, and at the end the combination is evaluated. Supports player vs AI mode (with three difficulty levels) and two-player mode.

---

## Scoring table

| Hand         | Points | Description |
|--------------|--------|-------------|
| Nothing      | 1      | No combination |
| Straight     | 2      | 5 consecutive dice (e.g. 1-2-3-4-5) |
| Pair         | 3      | Two matching dice |
| Two pair     | 4      | Two different pairs |
| Three of a kind | 5   | Three matching dice |
| Full house   | 6      | Three of a kind + Pair |
| Four of a kind | 7    | Four matching dice |
| Five of a kind | 8    | All five dice matching |

---

## Functions

---

### `contar_valores(dados)`

Counts how many times each number appears in the dice.

**Input:** list of 5 integers  
**Returns:** dictionary `{value: count}`

```python
contar_valores([3, 3, 5, 5, 3])  →  {3: 3, 5: 2}
```

---

### `es_escalera(dados)`

Checks whether the dice form a straight (5 consecutive numbers).

**Input:** list of 5 integers  
**Returns:** `True` or `False`

```python
es_escalera([1, 2, 3, 4, 5])  →  True
es_escalera([1, 1, 3, 4, 5])  →  False
```

---

### `evaluar_jugada(dados)`

Analyses the dice and determines which poker hand they form.

**Input:** list of 5 integers  
**Returns:** tuple `("Hand name", points)`

```python
evaluar_jugada([4, 4, 4, 2, 2])  →  ("Full", 6)
evaluar_jugada([6, 6, 6, 6, 1])  →  ("Poker", 7)
```

---

### `mostrar_dados(dados)`

Prints the dice to screen with their numbered positions.

```
1:[3]  2:[3]  3:[5]  4:[1]  5:[6]
```

---

### `leer_indices()`

Asks the player which dice they want to re-roll and validates the input.

**Returns:** list of indices (0-based) of dice to re-roll.  
**Validations:** only accepts numbers 1–5, no duplicates. Returns empty list if player types nothing.

---

### `relanzar_dados(dados, indices)`

Re-rolls only the dice at the specified positions.

**Input:** current dice list + list of positions to re-roll  
**Returns:** new list with selected dice replaced

---

## AI Functions

---

### `ia_facil()`

The **easy** AI picks dice to re-roll at random. No strategy whatsoever.

---

### `ia_media(dados)`

The **medium** AI keeps dice that already form pairs or better, and re-rolls the rest.

---

### `ia_inteligente(dados)`

The **smart** AI finds the most repeated value and keeps all dice showing that value, re-rolling the rest. This is the optimal strategy.

---

## Turn Functions

---

### `jugar_turno(nombre="Jugador")`

Manages a full human player turn: rolls, displays, allows re-rolls (up to 2), evaluates.

**Returns:** score achieved (integer)

---

### `turno_ia(nivel)`

Manages the AI turn based on its level (`"facil"`, `"medio"`, `"inteligente"`).

**Returns:** score achieved (integer)

---

### `modo_vs_ia()`

Runs a full match against the AI: asks difficulty, runs both turns, compares and announces winner.

---

### `modo_vs_jugador()`

Runs a match between two human players and determines the winner.

---

### `jugar_poker()`

Entry point of the game. Shows the mode menu and calls the appropriate function.

---

## Flow diagrams

### General game flow

```
┌──────────────────────────────┐
│        jugar_poker()         │
│  Menu: 1=vs AI / 2=vs Human │
└──────────┬───────────────────┘
           │
     ┌─────┴──────┐
     │            │
  op="1"       op="2"
     │            │
     ▼            ▼
┌──────────┐  ┌─────────────┐
│modo_vs_  │  │modo_vs_     │
│ia()      │  │jugador()    │
└────┬─────┘  └──────┬──────┘
     │               │
     ▼               ▼
┌──────────────────────────────┐
│       jugar_turno()          │
│  (human player turn)         │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│   tirar_varios_dados(5, 6)   │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       mostrar_dados()        │
└──────────────┬───────────────┘
               │
       ┌───────┴────────┐
    Re-roll?       attempts=0
       │ YES           │ NO
       ▼               │
┌─────────────┐        │
│leer_indices()│       │
└──────┬──────┘        │
       ▼               │
┌──────────────┐       │
│relanzar_     │       │
│dados()       │       │
└──────┬───────┘       │
       └───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      evaluar_jugada()        │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  Result: hand + points       │
└──────────────────────────────┘
```

### AI turn flow

```
┌──────────────────────────────┐
│      turno_ia(level)         │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│   tirar_varios_dados(5, 6)   │
└──────────────┬───────────────┘
               │
       ┌───────┼──────────────┐
    "facil"  "medio"   "inteligente"
       │        │              │
       ▼        ▼              ▼
┌──────────┐ ┌──────────┐ ┌──────────────┐
│ia_facil()│ │ia_media()│ │ia_inteligente│
│Full rand │ │Keeps     │ │Maximises     │
│          │ │pairs+    │ │most repeated │
└─────┬────┘ └────┬─────┘ └──────┬───────┘
      └───────────┴──────────────┘
                  │
                  ▼
      ┌───────────────────────┐
      │   relanzar_dados()    │
      │   (up to 2 attempts)  │
      └───────────┬───────────┘
                  │
                  ▼
      ┌───────────────────────┐
      │   evaluar_jugada()    │
      └───────────────────────┘
```

### Hand evaluation flow

```
evaluar_jugada(dados)
        │
        ▼
contar_valores(dados)
→ How many times does each number appear?
        │
        ▼
Sort frequencies highest to lowest
        │
   ┌────┴──────────────────────────────┐
   │  What's the pattern?              │
   └────┬──────────────────────────────┘
        │
        ├─ [5]        → Five of a kind  (8 pts)
        ├─ [4, 1]     → Four of a kind  (7 pts)
        ├─ [3, 2]     → Full house      (6 pts)
        ├─ [3, 1, 1]  → Three of a kind (5 pts)
        ├─ [2, 2, 1]  → Two pair        (4 pts)
        ├─ [2, 1,1,1] → Pair            (3 pts)
        ├─ es_escalera() = True → Straight (2 pts)
        └─ None of the above → Nothing  (1 pt)
```

---

## Dependencies

| Module | Used for |
|--------|----------|
| `random` | Needed for the easy AI |
| `core.dados` | To roll dice (`tirar_dado`, `tirar_varios_dados`) |