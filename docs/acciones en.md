# 📄 Documentation: `acciones.py`

> **Option router** module. Connects the main menu options to the corresponding game modules.

🌐 [Versión en español](acciones_es.md) · [← Back to index](README.md)

---

## What does this file do?

Acts as the middleman between what the user chooses in the menu and what actually runs. It receives the selected option and calls the appropriate game function. It also controls when the program should close.

---

## Functions

---

### `ejecutar_opcion(opcion)`

Receives the option chosen by the user and triggers the corresponding action.

| Parameter | Type  | Description |
|-----------|-------|-------------|
| `opcion`  | `str` | The key pressed by the user (`"1"`, `"2"` or `"3"`) |

**Returns:** `True` if the program should keep running, `False` if it should close.

---

#### Behaviour by option:

| Option | Action | Returns |
|--------|--------|---------|
| `"1"`  | Calls `jugar_poker()` | `True` |
| `"2"`  | Calls `jugar_rol()` *(in development)* | `True` |
| `"3"`  | Shows exit message and closes | `False` |
| Other  | Shows error message, returns to menu | `True` |

```python
keep_going = ejecutar_opcion("1")  # Starts poker, returns True
keep_going = ejecutar_opcion("3")  # Closes program, returns False
```

---

## Flow diagram

```
┌──────────────────────────────┐
│    ejecutar_opcion(opcion)   │
└──────────────┬───────────────┘
               │
       ┌───────┼──────────┬────────────┐
    op="1"  op="2"     op="3"       other
       │       │           │            │
       ▼       ▼           ▼            ▼
┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
│jugar_    │ │jugar_    │ │"Exiting" │ │"Invalid  │
│poker()   │ │rol()     │ │          │ │option"   │
└────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘
     │            │            │             │
     ▼            ▼            ▼             ▼
  True          True         False         True
(continues)  (continues)   (closes)    (continues)
```

---

## Dependencies

| Module | Used for |
|--------|----------|
| `core.poker` | Imports `jugar_poker()` |
| `core.rol`   | Imports `jugar_rol()` *(pending)* |

---

## Notes

- This module **does not manage the main loop**: it only executes one option per call.
- The loop control is decided by the returned value (`True`/`False`).
- Adding new game modes is as simple as adding a new `elif` and importing the corresponding module.