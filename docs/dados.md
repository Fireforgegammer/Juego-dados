# 📄 Documentación: `dados.py`

> Módulo base del simulador. Se encarga de **lanzar dados virtuales** de forma aleatoria.

---

## ¿Qué hace este archivo?

Es el bloque más fundamental del proyecto. Simula el lanzamiento de dados igual que lo harías con dados físicos: genera números al azar dentro de un rango definido por el número de caras del dado.

---

## Funciones

---

### `tirar_dado(caras=6)`

Lanza **un único dado** y devuelve el resultado.

| Parámetro | Tipo | Por defecto | Descripción |
|-----------|------|-------------|-------------|
| `caras`   | `int` | `6`        | Número de caras del dado |

**Devuelve:** un número entero aleatorio entre `1` y `caras` (ambos incluidos).

**Ejemplo de uso:**
```python
resultado = tirar_dado()      # Dado de 6 caras → puede dar 1, 2, 3, 4, 5 o 6
resultado = tirar_dado(20)    # Dado de 20 caras (típico de D&D)
```

---

### `tirar_varios_dados(cantidad=5, caras=6)`

Lanza **varios dados a la vez** y devuelve todos los resultados en una lista.

| Parámetro  | Tipo  | Por defecto | Descripción |
|------------|-------|-------------|-------------|
| `cantidad` | `int` | `5`         | Cuántos dados se lanzan |
| `caras`    | `int` | `6`         | Número de caras de cada dado |

**Devuelve:** una lista de enteros. Cada elemento es el resultado de un dado.

**Ejemplo de uso:**
```python
resultados = tirar_varios_dados()        # [3, 1, 6, 4, 2]
resultados = tirar_varios_dados(3, 10)   # Tres dados de 10 caras → [7, 2, 9]
```

---

## Dependencias

| Librería | Uso |
|----------|-----|
| `random` (Python estándar) | Genera los números aleatorios |

---

## Diagrama de flujo

```
┌─────────────────────────────────┐
│     tirar_dado(caras=6)         │
└─────────────────┬───────────────┘
                  │
                  ▼
┌─────────────────────────────────┐
│  Genera número aleatorio        │
│  entre 1 y caras (incluidos)    │
└─────────────────┬───────────────┘
                  │
                  ▼
┌─────────────────────────────────┐
│  Devuelve el número             │
└─────────────────────────────────┘


┌─────────────────────────────────┐
│  tirar_varios_dados(            │
│    cantidad=5, caras=6)         │
└─────────────────┬───────────────┘
                  │
                  ▼
┌─────────────────────────────────┐
│  Repite `cantidad` veces:       │
│    → llama a tirar_dado(caras)  │
└─────────────────┬───────────────┘
                  │
                  ▼
┌─────────────────────────────────┐
│  Devuelve lista con todos       │
│  los resultados                 │
│  Ej: [3, 1, 6, 4, 2]           │
└─────────────────────────────────┘
```

---

## Notas

- Este módulo **no tiene lógica de juego**. Solo sabe tirar dados.
- Es utilizado por `poker.py` para obtener los dados de cada turno.
- El valor por defecto de `caras=6` lo hace listo para usar sin configuración adicional.