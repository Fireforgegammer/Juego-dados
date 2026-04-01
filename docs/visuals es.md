# 📄 Documentación: `visuals.py`

> Módulo de **visualización en consola**. Se encarga de dibujar los dados, resultados y comparativas de forma clara y atractiva en la terminal.

🌐 [English version](visuals_en.md) · [← Volver al índice](README.md)

---

## ¿Qué hace este archivo?

Transforma los números de los dados en algo visualmente agradable en la consola. En vez de ver solo `[3, 1, 6, 4, 2]`, el jugador ve los dados dibujados, con colores, alineados y fáciles de leer.

Trabaja junto con `utils.py` para asegurarse de que el texto quede correctamente alineado incluso cuando se usan colores.

---

## Funciones

---

### `mostrar_dados_visual(dados, nombre)`

Muestra los dados de un jugador en pantalla con su nombre y los valores representados visualmente.

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `dados` | Lista | Los 5 dados a mostrar, ej: `[3, 1, 6, 4, 2]` |
| `nombre` | `str` | El nombre del jugador o de la IA |

**No devuelve nada.** Solo imprime en pantalla.

**Ejemplo de salida:**
```
Jugador   🎲  1:[3]  2:[1]  3:[6]  4:[4]  5:[2]
```

---

### `mostrar_resultado(jugada, puntos, nombre)`

Muestra la jugada final conseguida por un jugador junto con su puntuación.

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `jugada` | `str` | Nombre de la combinación, ej: `"Full"` |
| `puntos` | `int` | Puntuación obtenida, ej: `6` |
| `nombre` | `str` | El nombre del jugador |

**Ejemplo de salida:**
```
Jugador   →  Full  (6 pts)
```

---

### `mostrar_comparativa(nombre1, pts1, nombre2, pts2)`

Muestra una tabla comparativa entre los resultados de dos jugadores y anuncia el ganador.

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `nombre1` | `str` | Nombre del primer jugador |
| `pts1` | `int` | Puntuación del primer jugador |
| `nombre2` | `str` | Nombre del segundo jugador |
| `pts2` | `int` | Puntuación del segundo jugador |

**Ejemplo de salida:**
```
========================================
  Jugador     →  Full       (6 pts)
  IA          →  Trío       (5 pts)
----------------------------------------
  🏆 ¡Gana Jugador!
========================================
```

---

## Diagrama de flujo

```
┌──────────────────────────────────────┐
│   mostrar_dados_visual(dados, nombre)│
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  Formatea el nombre con              │
│  formatear_bloque() ← utils.py       │
│  (para que todos queden igual ancho) │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  Para cada dado de la lista:         │
│    muestra   N:[valor]               │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  Imprime la línea completa           │
│  "Jugador  🎲  1:[3] 2:[1] ..."      │
└──────────────────────────────────────┘


┌──────────────────────────────────────┐
│  mostrar_comparativa(n1,p1,n2,p2)   │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  Muestra resultado de jugador 1      │
│  Muestra resultado de jugador 2      │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│   ¿pts1 > pts2?  ¿pts1 < pts2?       │
│   ¿pts1 == pts2?                     │
└──────────────────┬───────────────────┘
                   │
        ┌──────────┼──────────┐
      gana 1    empate      gana 2
        │          │           │
        ▼          ▼           ▼
 "🏆 ¡Gana    "🤝 Empate"  "🏆 ¡Gana
  nombre1!"                 nombre2!"
```

---

## Dependencias

| Módulo | Uso |
|--------|-----|
| `core.utils` | Usa `largo_real()` y `formatear_bloque()` para alinear el texto correctamente |

---

## Notas

- Este módulo **nunca toma decisiones de juego**: solo muestra información.
- Separar la visualización del resto de la lógica hace que sea fácil cambiar el aspecto del juego sin tocar cómo funciona.
- Si en el futuro se quisiera hacer una versión con interfaz gráfica, solo habría que reemplazar este módulo.