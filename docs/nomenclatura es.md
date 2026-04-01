# 📚 Nomenclatura y Convenciones

> Guía de estilo del proyecto **Simulador de Dados**: cómo se nombran las cosas, por qué, y qué convenciones se siguen. Pensada para personas sin experiencia previa en programación.

🌐 [English version](nomenclature_en.md) · [← Volver al índice](README.md)

---

## 📖 Glosario de términos

| Término | Significado sencillo |
|---------|----------------------|
| **Módulo** | Un archivo `.py`. Cada módulo hace una cosa concreta. |
| **Función** | Un bloque de código con nombre que hace una tarea. Se llama escribiendo su nombre seguido de `()`. |
| **Parámetro** | Un valor que le das a una función para que sepa cómo trabajar. Ej: cuántas caras tiene el dado. |
| **Valor por defecto** | El valor que usa la función si no le dices nada. Ej: `caras=6` usa 6 si no especificas. |
| **Devuelve** | Lo que te da la función cuando termina. Como el resultado de una calculadora. |
| **Lista** | Una colección de valores en orden. Ej: `[3, 1, 6, 4, 2]` son 5 dados. |
| **Diccionario** | Pares de clave-valor. Ej: `{3: 2, 5: 3}` significa "el 3 salió 2 veces, el 5 salió 3 veces". |
| **Índice** | La posición de un elemento en una lista. Empieza en 0. Dado 1 → índice 0. |
| **Booleano** | Un valor que solo puede ser `True` (verdadero) o `False` (falso). |
| **Importar** | Usar código de otro módulo. Como pedir prestada una herramienta. |
| **IA** | Inteligencia Artificial. En este proyecto, el oponente virtual del jugador. |
| **Tupla** | Como una lista, pero sus valores no pueden cambiar. Ej: `("Full", 6)`. |
| **String** | Una cadena de texto. Ej: `"facil"`, `"Jugador"`. |

---

## 🔤 Cómo se nombran las funciones

Las funciones siguen el patrón **`verbo_sustantivo`** en español con guiones bajos (`snake_case`):

```
tirar_dado         →  tirar  +  dado
mostrar_menu       →  mostrar  +  menú
evaluar_jugada     →  evaluar  +  jugada
```

> 💡 **¿Por qué así?** Porque leer `tirar_dado()` es casi como leer español normal. Sabes exactamente lo que hace sin necesitar explicación.

### Tabla completa de funciones

| Función | Verbo | Objeto | ¿Qué hace? |
|---------|-------|--------|------------|
| `tirar_dado` | tirar | dado | Lanza un dado |
| `tirar_varios_dados` | tirar | varios dados | Lanza múltiples dados |
| `contar_valores` | contar | valores | Cuenta repeticiones de cada número |
| `es_escalera` | es | escalera | Comprueba si los dados forman escalera |
| `evaluar_jugada` | evaluar | jugada | Identifica la combinación de póker |
| `mostrar_dados` | mostrar | dados | Imprime los dados en pantalla |
| `leer_indices` | leer | índices | Recoge qué dados quiere relanzar el usuario |
| `relanzar_dados` | relanzar | dados | Vuelve a tirar los dados elegidos |
| `jugar_turno` | jugar | turno | Gestiona el turno completo del jugador humano |
| `turno_ia` | turno | ia | Gestiona el turno del oponente virtual |
| `modo_vs_ia` | modo | vs ia | Partida jugador contra IA |
| `modo_vs_jugador` | modo | vs jugador | Partida entre dos jugadores humanos |
| `jugar_poker` | jugar | poker | Inicia el juego de póker completo |
| `jugar_rol` | jugar | rol | Inicia el modo D&D |
| `mostrar_menu` | mostrar | menú | Dibuja el menú principal |
| `ejecutar_opcion` | ejecutar | opción | Lanza la acción según la opción elegida |
| `largo_real` | largo | real | Mide el texto ignorando caracteres de color |
| `formatear_bloque` | formatear | bloque | Rellena texto con espacios hasta un ancho fijo |

---

## 🔤 Cómo se nombran las variables

Las variables también usan `snake_case` y nombres en español. Se intenta que sean **cortas pero descriptivas**:

| Variable | Tipo | Ejemplo | Significa |
|----------|------|---------|-----------|
| `dados` | Lista | `[3, 1, 6, 4, 2]` | Los 5 dados actuales |
| `caras` | Entero | `6` | Número de caras del dado |
| `cantidad` | Entero | `5` | Cuántos dados se lanzan |
| `conteo` | Diccionario | `{3: 2, 6: 1}` | Veces que aparece cada número |
| `repeticiones` | Lista | `[3, 2]` | Frecuencias ordenadas de mayor a menor |
| `indices` | Lista | `[0, 2, 4]` | Posiciones de dados a relanzar (base 0) |
| `intentos` | Entero | `2` | Relanzamientos que le quedan al jugador |
| `nivel` | Texto | `"facil"` | Dificultad de la IA |
| `jugada` | Texto | `"Full"` | Nombre de la combinación conseguida |
| `pts` | Entero | `6` | Puntuación de la jugada |
| `pj` | Entero | `5` | Puntos del jugador humano |
| `pi` | Entero | `7` | Puntos de la IA |
| `opcion` | Texto | `"1"` | Opción elegida en el menú |
| `buenos` | Lista | `[3, 5]` | Valores que la IA decide conservar |
| `objetivo` | Entero | `4` | Valor que la IA intenta maximizar |
| `ancho` | Entero | `20` | Ancho en caracteres de un bloque visual |
| `relleno` | Entero | `8` | Espacios adicionales para completar el ancho |

---

## 📐 Convenciones de código

### Comentarios en español
Todo el código está comentado en español para mantener consistencia con los nombres de variables y funciones.

### Valores por defecto claros
Cuando una función tiene un valor por defecto, ese valor es el más común:

```python
def tirar_dado(caras=6):       # Un dado normal tiene 6 caras
def tirar_varios_dados(cantidad=5, caras=6):  # El póker usa 5 dados de 6
```

### Principio de responsabilidad única
Cada módulo hace **una sola cosa**:

| Módulo | Su única responsabilidad |
|--------|--------------------------|
| `dados.py` | Lanzar dados |
| `poker.py` | Lógica del juego de póker |
| `utils.py` | Herramientas de texto |
| `visuals.py` | Mostrar cosas en pantalla |
| `menu.py` | Dibujar el menú |
| `acciones.py` | Conectar menú con juegos |

---

## 📦 Dependencias entre módulos

```
main.py
   │
   ├── ui/menu.py          (no depende de nadie)
   └── ui/acciones.py
          ├── core/poker.py
          │      ├── core/dados.py
          │      │      └── random  ← librería de Python
          │      └── random
          ├── core/rol.py
          │      └── core/dados.py
          └── core/visuals.py
                 └── core/utils.py
                        └── re  ← librería de Python
```

> **Regla general:** los módulos de la parte inferior (`dados.py`, `utils.py`) no conocen a nadie. Los módulos superiores (`acciones.py`, `main.py`) son los que coordinan. Nunca al revés.

---

## 🔄 Diagrama de dependencias visual

```
     main.py
        │
   ┌────┴────┐
menu.py   acciones.py
              │
         ┌────┴────┐
      poker.py   rol.py
         │          │
         └────┬─────┘
           dados.py
              │
           random

visuals.py → utils.py → re
```