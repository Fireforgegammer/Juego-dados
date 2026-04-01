# 📄 Documentación: `utils.py`

> Módulo de **funciones auxiliares de texto**. Contiene herramientas para medir y formatear texto en consola, especialmente cuando se usan colores o estilos especiales.

🌐 [English version](utils_en.md) · [← Volver al índice](README.md)

---

## ¿Qué hace este archivo?

Cuando se muestra texto con colores en la terminal, Python incluye unos caracteres invisibles llamados **códigos ANSI** que activan esos colores. El problema es que esos caracteres cuentan como longitud aunque no se vean.

`utils.py` soluciona eso: mide el texto como si no tuviese esos caracteres, y permite alinear bloques de texto correctamente aunque contengan colores.

> 💡 **Ejemplo visual del problema:**  
> `"\033[31mHola\033[0m"` se ve como `Hola` en rojo, pero Python cree que tiene 15 caracteres en vez de 4. `utils.py` sabe que son solo 4.

---

## Funciones

---

### `largo_real(texto)`

Mide la longitud **visible** de un texto, ignorando los códigos de color ANSI.

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `texto` | `str` | El texto a medir, puede contener colores |

**Devuelve:** un entero con el número de caracteres visibles.

```python
largo_real("Hola")              →  4
largo_real("\033[31mHola\033[0m")  →  4   # También 4, aunque haya colores
largo_real("1:[🎲]")            →  6
```

---

### `formatear_bloque(texto, ancho)`

Rellena un texto con espacios hasta que alcanza el ancho indicado. Útil para alinear columnas en la consola.

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `texto` | `str` | El texto a formatear |
| `ancho` | `int` | El ancho total deseado en caracteres |

**Devuelve:** el texto original más los espacios necesarios para llegar a `ancho`.

```python
formatear_bloque("Hola", 10)     →  "Hola      "   # 6 espacios añadidos
formatear_bloque("Jugador", 10)  →  "Jugador   "   # 3 espacios añadidos
```

> 💡 Esto permite poner dos bloques de texto uno al lado del otro y que queden perfectamente alineados, como columnas.

---

## Diagrama de flujo

```
┌──────────────────────────────────┐
│       largo_real(texto)          │
└──────────────────┬───────────────┘
                   │
                   ▼
┌──────────────────────────────────┐
│  Busca y elimina todos los       │
│  códigos ANSI del texto          │
│  (los que empiezan por \x1B[)    │
└──────────────────┬───────────────┘
                   │
                   ▼
┌──────────────────────────────────┐
│  Cuenta los caracteres que       │
│  quedan (los visibles)           │
└──────────────────┬───────────────┘
                   │
                   ▼
┌──────────────────────────────────┐
│  Devuelve ese número             │
└──────────────────────────────────┘


┌──────────────────────────────────┐
│   formatear_bloque(texto, ancho) │
└──────────────────┬───────────────┘
                   │
                   ▼
┌──────────────────────────────────┐
│  Llama a largo_real(texto)       │
│  para saber cuánto ocupa         │
└──────────────────┬───────────────┘
                   │
                   ▼
┌──────────────────────────────────┐
│  Calcula cuántos espacios faltan │
│  relleno = ancho - largo_real    │
└──────────────────┬───────────────┘
                   │
                   ▼
┌──────────────────────────────────┐
│  Devuelve texto + espacios       │
└──────────────────────────────────┘
```

---

## ¿Cuándo se usa esto en el proyecto?

Se usa principalmente en `visuals.py` cuando se quieren mostrar los dados o resultados alineados en columnas. Sin estas funciones, los colores harían que los textos se desalinearan.

**Sin `utils.py`** (desalineado):
```
Jugador  🎲[3] [1] [6]    Full   → 6 pts
IA             🎲[4] [4] [4] [2] [2]  Full   → 6 pts
```

**Con `utils.py`** (alineado):
```
Jugador   🎲 [3] [1] [6] [4] [2]   Full   → 6 pts
IA        🎲 [4] [4] [4] [2] [2]   Full   → 6 pts
```

---

## Dependencias

| Librería | Uso |
|----------|-----|
| `re` (Python estándar) | Detecta y elimina los códigos ANSI mediante expresiones regulares |