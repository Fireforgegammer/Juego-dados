# 📚 Nomenclaturas y Diagramas de Flujo

> Guía general del proyecto **Simulador de Dados** pensada para personas sin experiencia en programación. Aquí encontrarás qué significa cada término, cómo se llaman las cosas y cómo funciona todo visualmente.

---

## 🗂️ Estructura del proyecto

```
simulador-dados/
│
├── core/                  ← Carpeta con toda la lógica del juego
│   ├── dados.py           ← Lanza los dados
│   ├── poker.py           ← Juego de Póker de Dados
│   └── acciones.py        ← Conecta el menú con los juegos
│
├── menu.py                ← Muestra el menú principal
└── docs/                  ← Esta carpeta de documentación
```

---

## 📖 Glosario de términos

| Término | Significado sencillo |
|---------|----------------------|
| **Módulo** | Un archivo `.py`. Cada módulo hace una cosa concreta. |
| **Función** | Un bloque de código con nombre que hace una tarea. Se llama escribiendo su nombre seguido de `()`. |
| **Parámetro** | Un valor que le das a una función para que sepa cómo trabajar. Ej: cuántas caras tiene el dado. |
| **Valor por defecto** | El valor que usa la función si no le dices nada. Ej: `caras=6` usa 6 si no especificas. |
| **Devuelve** | Lo que te da back la función cuando termina. Como el resultado de una calculadora. |
| **Lista** | Una colección de valores en orden. Ej: `[3, 1, 6, 4, 2]` son 5 dados. |
| **Diccionario** | Pares de clave-valor. Ej: `{3: 2, 5: 3}` significa "el 3 salió 2 veces, el 5 salió 3 veces". |
| **Índice** | La posición de un elemento en una lista. Empieza en 0. Dado 1 → índice 0. |
| **Booleano** | Un valor que solo puede ser `True` (verdadero) o `False` (falso). |
| **Importar** | Usar código de otro módulo. Como pedir prestada una herramienta. |
| **IA** | Inteligencia Artificial. En este proyecto, el oponente virtual del jugador. |

---

## 🔤 Nomenclatura de funciones

Las funciones siguen el patrón `verbo_sustantivo` en español con guiones bajos:

| Función | Verbo | Objeto | ¿Qué hace? |
|---------|-------|--------|------------|
| `tirar_dado` | tirar | dado | Lanza un dado |
| `tirar_varios_dados` | tirar | varios dados | Lanza múltiples dados |
| `contar_valores` | contar | valores | Cuenta repeticiones |
| `es_escalera` | es | escalera | Comprueba si es escalera |
| `evaluar_jugada` | evaluar | jugada | Identifica la combinación |
| `mostrar_dados` | mostrar | dados | Imprime los dados |
| `leer_indices` | leer | índices | Recoge entrada del usuario |
| `relanzar_dados` | relanzar | dados | Vuelve a tirar los elegidos |
| `jugar_turno` | jugar | turno | Gestiona el turno humano |
| `turno_ia` | turno | ia | Gestiona el turno de la IA |
| `modo_vs_ia` | modo | vs ia | Partida contra IA |
| `modo_vs_jugador` | modo | vs jugador | Partida entre dos personas |
| `jugar_poker` | jugar | poker | Inicia el juego completo |
| `mostrar_menu` | mostrar | menú | Dibuja el menú |
| `ejecutar_opcion` | ejecutar | opción | Lanza la acción elegida |

---

## 🔤 Nomenclatura de variables

| Variable | Tipo | Ejemplo | Significa |
|----------|------|---------|-----------|
| `dados` | Lista | `[3, 1, 6, 4, 2]` | Los 5 dados actuales |
| `caras` | Entero | `6` | Número de caras del dado |
| `cantidad` | Entero | `5` | Cuántos dados lanzar |
| `conteo` | Diccionario | `{3: 2, 6: 1}` | Veces que sale cada número |
| `repeticiones` | Lista | `[3, 2]` | Frecuencias ordenadas |
| `indices` | Lista | `[0, 2, 4]` | Posiciones de dados a relanzar |
| `intentos` | Entero | `2` | Relanzamientos que quedan |
| `nivel` | Texto | `"facil"` | Dificultad de la IA |
| `jugada` | Texto | `"Full"` | Nombre de la combinación |
| `pts` | Entero | `6` | Puntuación de la jugada |
| `pj` | Entero | `5` | Puntos del jugador |
| `pi` | Entero | `7` | Puntos de la IA |
| `opcion` | Texto | `"1"` | Opción elegida en el menú |
| `buenos` | Lista | `[3, 5]` | Valores a conservar (IA media) |
| `objetivo` | Entero | `4` | Valor a maximizar (IA inteligente) |

---

## 🔄 Diagrama de flujo general del programa

```
┌─────────────────────────────┐
│       Inicia el programa    │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      mostrar_menu()         │  ← menu.py
│  1. Póker  2. D&D  3. Salir │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│   El usuario elige opción   │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│    ejecutar_opcion(opcion)  │  ← acciones.py
└──────┬──────────────┬───────┘
       │              │
    opción 1       opción 3
       │              │
       ▼              ▼
┌──────────┐    ┌──────────┐
│jugar_    │    │  Salir   │
│poker()   │    │ del prog.│
└──────────┘    └──────────┘
       │
       ▼
  (ver diagrama de póker)
```

---

## 🎲 Diagrama de flujo: Juego de Póker

```
┌──────────────────────────────┐
│        jugar_poker()         │
│  Menú: 1=vs IA / 2=vs Human │
└──────────┬───────────────────┘
           │
     ┌─────┴─────┐
     │           │
  vs IA      vs Jugador
     │           │
     ▼           ▼
┌─────────┐ ┌──────────┐
│modo_vs_ │ │modo_vs_  │
│ia()     │ │jugador() │
└────┬────┘ └────┬─────┘
     │           │
     ▼           ▼
┌──────────────────────────────┐
│       jugar_turno()          │
│  (Turno del jugador humano)  │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│   tirar_varios_dados(5, 6)   │  ← dados.py
│   Lanza 5 dados              │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       mostrar_dados()        │
│   1:[3] 2:[1] 3:[6] 4:[4] 5:[2] │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│   ¿Quiere relanzar?          │
│   (quedan hasta 2 intentos)  │
└──────┬───────────────┬───────┘
       │ SÍ            │ NO
       ▼               │
┌─────────────┐        │
│leer_indices()│       │
│¿Qué dados?  │        │
└──────┬──────┘        │
       │               │
       ▼               │
┌─────────────────┐    │
│relanzar_dados() │    │
│Nuevos dados     │    │
└──────┬──────────┘    │
       │               │
       └───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      evaluar_jugada()        │
│  ¿Qué combinación es?        │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  Resultado: jugada + puntos  │
└──────────────────────────────┘
```

---

## 🤖 Diagrama de flujo: Turno de la IA

```
┌──────────────────────────────┐
│        turno_ia(nivel)       │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│   tirar_varios_dados(5, 6)   │
└──────────────┬───────────────┘
               │
       ┌───────┴────────┐
    "facil"           "medio"       "inteligente"
       │                │                │
       ▼                ▼                ▼
┌───────────┐  ┌──────────────┐  ┌──────────────┐
│ ia_facil()│  │  ia_media()  │  │ia_inteligente│
│Azar total │  │Guarda parejas│  │Maximiza el   │
│           │  │o mejor       │  │valor más     │
│           │  │              │  │repetido      │
└─────┬─────┘  └──────┬───────┘  └──────┬───────┘
      │               │                  │
      └───────────────┴──────────────────┘
                      │
                      ▼
         ┌────────────────────────┐
         │   relanzar_dados()     │
         │   (hasta 2 intentos)   │
         └────────────┬───────────┘
                      │
                      ▼
         ┌────────────────────────┐
         │    evaluar_jugada()    │
         └────────────────────────┘
```

---

## 🏆 Diagrama de flujo: Evaluación de jugada

```
evaluar_jugada(dados)
        │
        ▼
contar_valores(dados)
→ ¿Cuántas veces sale cada número?
        │
        ▼
Ordenar las repeticiones de mayor a menor
        │
   ┌────┴──────────────────────────────┐
   │  ¿Cuál es el patrón?              │
   └────┬──────────────────────────────┘
        │
        ├─ [5]       → Re-poker  (8 pts)
        ├─ [4, 1]    → Póker     (7 pts)
        ├─ [3, 2]    → Full      (6 pts)
        ├─ [3, 1, 1] → Trío      (5 pts)
        ├─ [2, 2, 1] → Doble par (4 pts)
        ├─ [2,1,1,1] → Pareja    (3 pts)
        ├─ es_escalera() = True → Escalera (2 pts)
        └─ Ninguno anterior → Nada (1 pt)
```

---

## 📦 Diagrama de dependencias entre módulos

```
menu.py
   │  (solo muestra texto, no depende de nada)

acciones.py
   ├── importa → core.poker  (jugar_poker)
   └── importa → core.rol    (jugar_rol)  [en desarrollo]

poker.py
   ├── importa → core.dados  (tirar_varios_dados, tirar_dado)
   └── importa → random      (para la IA fácil)

dados.py
   └── importa → random      (para generar números aleatorios)
```

> **Regla general:** cada módulo solo conoce a los módulos que están "por debajo" de él. `dados.py` es la base y no depende de nadie. `menu.py` es la capa visual y tampoco depende de nadie. `acciones.py` es el intermediario que une menú y juegos.