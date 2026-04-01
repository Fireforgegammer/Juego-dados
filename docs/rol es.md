# 📄 Documentación: `rol.py`

> Módulo del **modo D&D** (Dungeons & Dragons). Permite lanzar dados de rol de distintos tipos y muestra los resultados.

🌐 [English version](rol_en.md) · [← Volver al índice](README.md)

---

## ¿Qué hace este archivo?

Simula las tiradas de dados típicas de los juegos de rol de mesa como Dungeons & Dragons. A diferencia del póker (que siempre usa 5 dados de 6 caras), aquí el jugador puede elegir **qué tipo de dado** quiere usar y **cuántos** quiere lanzar.

---

## Tipos de dados disponibles

En los juegos de rol se usan dados con distinto número de caras. Se nombran con una "d" seguida del número de caras:

| Dado | Caras | Uso típico |
|------|-------|------------|
| `d4` | 4 | Daño de daga |
| `d6` | 6 | Dado estándar |
| `d8` | 8 | Daño de espada corta |
| `d10` | 10 | Daño de espada larga |
| `d12` | 12 | Daño de hacha de guerra |
| `d20` | 20 | Chequeos de habilidad y ataques |

---

## Funciones

---

### `tirar_rol(cantidad, caras)`

Lanza varios dados del mismo tipo y devuelve los resultados individuales y el total.

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `cantidad` | `int` | Cuántos dados se lanzan |
| `caras` | `int` | Número de caras de cada dado |

**Devuelve:** una tupla con `(lista_de_tiradas, total)`

```python
tirar_rol(3, 6)   →  ([4, 2, 6], 12)   # Tres dados de 6: resultados y suma
tirar_rol(1, 20)  →  ([17], 17)         # Un dado de 20
tirar_rol(2, 8)   →  ([5, 3], 8)        # Dos dados de 8
```

> 💡 Una **tupla** es como una lista, pero sus valores no cambian. Aquí devolvemos dos cosas a la vez: la lista de tiradas individuales y su suma.

---

### `jugar_rol()`

Punto de entrada del modo D&D. Guía al jugador para elegir el tipo de dado y la cantidad, realiza la tirada y muestra el resultado.

**No recibe parámetros.**  
**No devuelve nada** (muestra el resultado directamente en pantalla).

**Flujo de la función:**
1. Muestra los dados disponibles
2. El jugador elige cuántas caras tiene el dado
3. El jugador elige cuántos dados lanzar
4. Se llama a `tirar_rol()` con esos valores
5. Se muestran los resultados individuales y el total

---

## Diagrama de flujo

```
┌──────────────────────────────┐
│         jugar_rol()          │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  Muestra los dados posibles  │
│  d4, d6, d8, d10, d12, d20  │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  ¿Cuántas caras? (4/6/8...) │
│  El jugador escribe un número│
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  ¿Cuántos dados lanzar?      │
│  El jugador escribe un número│
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      tirar_rol(cantidad,     │
│               caras)         │
│  ← usa tirar_varios_dados()  │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  Muestra cada tirada         │
│  Dado 1: [4]                 │
│  Dado 2: [2]                 │
│  Dado 3: [6]                 │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  Muestra el total: 12        │
└──────────────────────────────┘
```

---

## Ejemplo de sesión completa

```
¿Qué dado quieres usar?
  d4 | d6 | d8 | d10 | d12 | d20
Elige número de caras: 20
¿Cuántos dados? 1

🎲 Lanzando 1d20...
  Dado 1: [17]

Total: 17
```

---

## Dependencias

| Módulo | Uso |
|--------|-----|
| `core.dados` | Usa `tirar_varios_dados()` para lanzar los dados |

---

## Notas

- El modo D&D está diseñado para ser **flexible**: no importa qué dado o cuántos quieras tirar.
- La función `tirar_rol` delega el lanzamiento en `dados.py`, siguiendo el principio de que cada módulo hace solo su trabajo.
- *(En desarrollo)* Se prevé añadir modificadores de tirada (sumar o restar un valor fijo al resultado).