# 📄 Documentation: `utils.py`

> Module of **text helper functions**. Contains tools for measuring and formatting text in the console, especially when colours or special styles are used.

🌐 [Versión en español](utils_es.md) · [← Back to index](README.md)

---

## What does this file do?

When coloured text is displayed in the terminal, Python includes invisible characters called **ANSI codes** that activate those colours. The problem is those characters count towards the string length even though they're not visible.

`utils.py` solves that: it measures text as if those characters weren't there, and lets you align text blocks correctly even when they contain colours.

> 💡 **Visual example of the problem:**  
> `"\033[31mHello\033[0m"` shows as `Hello` in red, but Python thinks it has 16 characters instead of 5. `utils.py` knows it's only 5.

---

## Functions

---

### `largo_real(texto)`

Measures the **visible** length of a text, ignoring ANSI colour codes.

| Parameter | Type | Description |
|-----------|------|-------------|
| `texto` | `str` | The text to measure, may contain colours |

**Returns:** an integer with the number of visible characters.

```python
largo_real("Hello")               →  5
largo_real("\033[31mHello\033[0m") →  5   # Also 5, even with colour codes
largo_real("1:[🎲]")              →  6
```

---

### `formatear_bloque(texto, ancho)`

Pads a text with spaces until it reaches the specified width. Useful for aligning columns in the console.

| Parameter | Type | Description |
|-----------|------|-------------|
| `texto` | `str` | The text to format |
| `ancho` | `int` | The desired total width in characters |

**Returns:** the original text plus the spaces needed to reach `ancho`.

```python
formatear_bloque("Hello", 10)   →  "Hello     "   # 5 spaces added
formatear_bloque("Player", 10)  →  "Player    "   # 4 spaces added
```

---

## Flow diagram

```
┌──────────────────────────────────┐
│       largo_real(texto)          │
└──────────────────┬───────────────┘
                   │
                   ▼
┌──────────────────────────────────┐
│  Find and remove all ANSI codes  │
│  from the text                   │
│  (those starting with \x1B[)     │
└──────────────────┬───────────────┘
                   │
                   ▼
┌──────────────────────────────────┐
│  Count the remaining characters  │
│  (the visible ones)              │
└──────────────────┬───────────────┘
                   │
                   ▼
┌──────────────────────────────────┐
│  Return that number              │
└──────────────────────────────────┘


┌──────────────────────────────────┐
│   formatear_bloque(texto, ancho) │
└──────────────────┬───────────────┘
                   │
                   ▼
┌──────────────────────────────────┐
│  Call largo_real(texto)          │
│  to find out how wide it is      │
└──────────────────┬───────────────┘
                   │
                   ▼
┌──────────────────────────────────┐
│  Calculate spaces needed:        │
│  padding = ancho - largo_real    │
└──────────────────┬───────────────┘
                   │
                   ▼
┌──────────────────────────────────┐
│  Return text + spaces            │
└──────────────────────────────────┘
```

---

## Dependencies

| Library | Used for |
|---------|----------|
| `re` (Python standard) | Detects and removes ANSI codes using regular expressions |