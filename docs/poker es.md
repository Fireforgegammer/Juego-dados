# 📄 Documentación: `poker.py`

> Módulo principal del juego **Póker de Dados**. Contiene toda la lógica: evaluación de jugadas, turnos del jugador, comportamiento de la IA y modos de juego.

🌐 [English version](poker_en.md) · [← Volver al índice](README.md)

---

## ¿Qué hace este archivo?

Implementa el juego completo de póker con dados. Un jugador lanza 5 dados, puede relanzar los que quiera hasta 2 veces, y al final se evalúa qué combinación ha conseguido. Soporta modo jugador contra IA (con tres niveles de dificultad) y modo dos jugadores.

---

## Tabla de puntuaciones

| Jugada       | Puntos | Descripción |
|--------------|--------|-------------|
| Nada         | 1      | Sin combinación |
| Escalera     | 2      | 5 dados consecutivos (ej: 1-2-3-4-5) |
| Pareja       | 3      | Dos dados iguales |
| Doble pareja | 4      | Dos pares distintos |
| Trío         | 5      | Tres dados iguales |
| Full         | 6      | Trío + Pareja |
| Póker        | 7      | Cuatro dados iguales |
| Re-poker     | 8      | Los cinco dados iguales |

---

## Funciones

---

### `contar_valores(dados)`

Cuenta cuántas veces aparece cada número en los dados.

**Entrada:** lista de 5 enteros  
**Devuelve:** diccionario `{valor: cantidad}`

```python
contar_valores([3, 3, 5, 5, 3])  →  {3: 3, 5: 2}
```

---

### `es_escalera(dados)`

Comprueba si los dados forman una escalera (5 números consecutivos).

**Entrada:** lista de 5 enteros  
**Devuelve:** `True` o `False`

```python
es_escalera([1, 2, 3, 4, 5])  →  True
es_escalera([1, 1, 3, 4, 5])  →  False
```

---

### `evaluar_jugada(dados)`

Analiza los dados y determina qué jugada de póker forman.

**Entrada:** lista de 5 enteros  
**Devuelve:** tupla `("Nombre jugada", puntos)`

```python
evaluar_jugada([4, 4, 4, 2, 2])  →  ("Full", 6)
evaluar_jugada([6, 6, 6, 6, 1])  →  ("Poker", 7)
```

---

### `mostrar_dados(dados)`

Imprime los dados en pantalla con su posición numerada.

```
1:[3]  2:[3]  3:[5]  4:[1]  5:[6]
```

---

### `leer_indices()`

Pide al usuario qué dados quiere relanzar y valida la entrada.

**Devuelve:** lista de índices (base 0) de los dados a relanzar.  
**Validaciones:** solo acepta números del 1 al 5, sin repetidos. Devuelve lista vacía si el usuario no escribe nada.

---

### `relanzar_dados(dados, indices)`

Relanza únicamente los dados en las posiciones indicadas.

**Entrada:** lista de dados actual + lista de posiciones  
**Devuelve:** nueva lista con los dados seleccionados renovados

---

## Funciones de IA

---

### `ia_facil()`

Elige dados al azar para relanzar. No tiene ninguna estrategia.

---

### `ia_media(dados)`

Conserva los dados que ya forman parejas o mejores combinaciones, relanza el resto.

---

### `ia_inteligente(dados)`

Busca el valor que más se repite y conserva todos los dados con ese valor. Es la estrategia óptima.

---

## Funciones de turno

---

### `jugar_turno(nombre="Jugador")`

Gestiona el turno completo de un jugador humano: lanza, muestra, permite relanzar (hasta 2 veces), evalúa.

**Devuelve:** puntuación obtenida (entero)

---

### `turno_ia(nivel)`

Gestiona el turno de la IA según su nivel (`"facil"`, `"medio"`, `"inteligente"`).

**Devuelve:** puntuación obtenida (entero)

---

### `modo_vs_ia()`

Ejecuta una partida completa contra la IA: pide nivel, ejecuta ambos turnos, compara y anuncia ganador.

---

### `modo_vs_jugador()`

Ejecuta una partida entre dos jugadores humanos y determina el ganador.

---

### `jugar_poker()`

Punto de entrada del juego. Muestra el menú de modos y llama a la función correspondiente.

---

## Diagramas de flujo

### Flujo general del juego

```
┌──────────────────────────────┐
│        jugar_poker()         │
│  Menú: 1=vs IA / 2=vs Human │
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
│  (turno del jugador humano)  │
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
    ¿Relanzar?      intentos=0
       │ SÍ            │ NO
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
│  Resultado: jugada + puntos  │
└──────────────────────────────┘
```

### Flujo del turno de la IA

```
┌──────────────────────────────┐
│      turno_ia(nivel)         │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│   tirar_varios_dados(5, 6)   │
└──────────────┬───────────────┘
               │
       ┌───────┼───────────┐
    "facil"  "medio"  "inteligente"
       │        │           │
       ▼        ▼           ▼
┌──────────┐ ┌──────────┐ ┌──────────────┐
│ia_facil()│ │ia_media()│ │ia_inteligente│
│Azar total│ │Guarda    │ │Maximiza el   │
│          │ │parejas   │ │valor más     │
│          │ │          │ │repetido      │
└─────┬────┘ └────┬─────┘ └──────┬───────┘
      └───────────┴──────────────┘
                  │
                  ▼
      ┌───────────────────────┐
      │   relanzar_dados()    │
      │   (hasta 2 intentos)  │
      └───────────┬───────────┘
                  │
                  ▼
      ┌───────────────────────┐
      │   evaluar_jugada()    │
      └───────────────────────┘
```

### Flujo de evaluación de jugada

```
evaluar_jugada(dados)
        │
        ▼
contar_valores(dados)
→ ¿Cuántas veces sale cada número?
        │
        ▼
Ordenar repeticiones de mayor a menor
        │
   ┌────┴──────────────────────────────┐
   │  ¿Cuál es el patrón?              │
   └────┬──────────────────────────────┘
        │
        ├─ [5]        → Re-poker  (8 pts)
        ├─ [4, 1]     → Póker     (7 pts)
        ├─ [3, 2]     → Full      (6 pts)
        ├─ [3, 1, 1]  → Trío      (5 pts)
        ├─ [2, 2, 1]  → Doble par (4 pts)
        ├─ [2, 1,1,1] → Pareja    (3 pts)
        ├─ es_escalera() = True → Escalera (2 pts)
        └─ Ninguno anterior  → Nada (1 pt)
```

---

## Dependencias

| Módulo | Uso |
|--------|-----|
| `random` | Necesario para la IA fácil |
| `core.dados` | Para lanzar los dados (`tirar_dado`, `tirar_varios_dados`) |