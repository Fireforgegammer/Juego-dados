# 📄 Documentación: `acciones.py`

> Módulo **enrutador de opciones**. Conecta las opciones del menú principal con los módulos de juego correspondientes.

---

## ¿Qué hace este archivo?

Actúa como intermediario entre lo que el usuario elige en el menú y lo que realmente se ejecuta. Recibe la opción seleccionada y llama a la función de juego adecuada. También controla cuándo debe cerrarse el programa.

---

## Funciones

---

### `ejecutar_opcion(opcion)`

Recibe la opción elegida por el usuario y lanza la acción correspondiente.

| Parámetro | Tipo  | Descripción |
|-----------|-------|-------------|
| `opcion`  | `str` | La tecla pulsada por el usuario (`"1"`, `"2"` o `"3"`) |

**Devuelve:** `True` si el programa debe seguir ejecutándose, `False` si debe cerrarse.

---

#### Comportamiento según la opción:

| Opción | Acción | Devuelve |
|--------|--------|----------|
| `"1"`  | Llama a `jugar_poker()` — inicia el juego de Póker de Dados | `True` |
| `"2"`  | Llama a `jugar_rol()` — inicia el modo D&D *(en desarrollo)* | `True` |
| `"3"`  | Muestra mensaje de salida y cierra el programa | `False` |
| Otro   | Muestra mensaje de error y vuelve al menú | `True` |

---

**Ejemplo de uso:**
```python
continuar = ejecutar_opcion("1")  # Lanza el póker, devuelve True
continuar = ejecutar_opcion("3")  # Cierra el programa, devuelve False
```

---

## Diagrama de flujo

```
┌──────────────────────────────┐
│    ejecutar_opcion(opcion)   │
└──────────────┬───────────────┘
               │
       ┌───────┼──────────┬────────────┐
    op="1"  op="2"     op="3"       otro
       │       │           │            │
       ▼       ▼           ▼            ▼
┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
│jugar_    │ │jugar_    │ │"Saliendo"│ │"Opción   │
│poker()   │ │rol()     │ │          │ │no válida"│
└────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘
     │            │            │             │
     ▼            ▼            ▼             ▼
  True          True         False         True
  (continúa)  (continúa)  (cierra)     (continúa)
```

---

## Dependencias

| Módulo | Uso |
|--------|-----|
| `core.poker` | Importa `jugar_poker()` para el modo póker |
| `core.rol`   | Importa `jugar_rol()` para el modo D&D *(pendiente de implementar)* |

---

## Notas

- Este módulo **no gestiona el bucle principal** del programa; solo ejecuta una opción por llamada.
- El control del bucle (seguir mostrando el menú o no) lo decide el valor devuelto (`True`/`False`).
- Añadir nuevos modos de juego es tan sencillo como agregar un nuevo `elif` aquí e importar el módulo correspondiente.