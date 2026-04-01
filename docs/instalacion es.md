# 🛠️ Guía de instalación y uso

> Cómo instalar y ejecutar el **Simulador de Dados** paso a paso, pensado para personas que nunca han programado.

🌐 [English version](installation_en.md) · [← Volver al índice](README.md)

---

## ¿Qué necesitas antes de empezar?

Solo necesitas tener instalado **Python**. Nada más.

### 1. Comprueba si ya tienes Python

Abre una terminal (en Windows: `cmd` o `PowerShell`; en Mac/Linux: `Terminal`) y escribe:

```bash
python --version
```

Si ves algo como `Python 3.10.0` o superior, ¡ya lo tienes! Salta al paso 3.

Si ves un error, pasa al paso 2.

---

### 2. Instala Python

Visita [python.org/downloads](https://python.org/downloads) y descarga la versión más reciente.

> ⚠️ Durante la instalación en Windows, marca la casilla **"Add Python to PATH"**. Es importante.

---

### 3. Descarga el proyecto

#### Opción A — Con Git (recomendado)

```bash
git clone <url-del-repositorio>
cd JUEGO-DADOS
```

#### Opción B — Sin Git

1. Ve a la página del repositorio
2. Haz clic en el botón verde **"Code"**
3. Elige **"Download ZIP"**
4. Descomprime el archivo en tu carpeta preferida

---

### 4. Ejecuta el programa

Abre la terminal dentro de la carpeta del proyecto y escribe:

```bash
python main.py
```

Deberías ver el menú principal:

```
========================================
🎲 LANZADOR DE DADOS
========================================
1. Poker de dados
2. D&D
3. Salir
```

¡Ya está funcionando! 🎉

---

## ¿Cómo se juega?

### Menú principal

Cuando veas el menú, escribe el número de la opción que quieras y pulsa `Enter`.

```
1  →  Jugar al Póker de Dados
2  →  Modo D&D (lanzar dados de rol)
3  →  Salir del programa
```

### Póker de Dados

1. Elige si jugar **contra la IA** o **contra otro jugador**
2. Se lanzan 5 dados automáticamente
3. Puedes elegir qué dados relanzar (hasta 2 veces)
4. Al final se comparan las jugadas y se anuncia el ganador

**Para elegir qué dados relanzar**, escribe los números separados por espacios:

```
¿Qué dados quieres relanzar? (ej: 1 3 5): 2 4
```

Eso relanzaría el dado 2 y el dado 4.

### Modo D&D

Elige el tipo de dado y cuántos quieres lanzar. El programa muestra los resultados y el total.

---

## Diagrama de flujo del inicio

```
┌──────────────────────────┐
│   Abres la terminal      │
└──────────────┬───────────┘
               │
               ▼
┌──────────────────────────┐
│   python main.py         │
└──────────────┬───────────┘
               │
               ▼
┌──────────────────────────┐
│   Se muestra el menú     │
│   mostrar_menu()         │
└──────────────┬───────────┘
               │
               ▼
┌──────────────────────────┐
│   Escribes un número     │
│   y pulsas Enter         │
└──────────────┬───────────┘
               │
        ┌──────┴──────┐
        │             │
      1 ó 2           3
        │             │
        ▼             ▼
  Empieza el      El programa
  juego           se cierra
```

---

## Preguntas frecuentes

**¿El programa no arranca?**  
Asegúrate de estar dentro de la carpeta correcta antes de ejecutar `python main.py`. Usa `cd JUEGO-DADOS` para entrar.

**¿Veo un error con `python`?**  
Prueba con `python3 main.py` en su lugar. En Mac y Linux es habitual que se llame `python3`.

**¿Puedo cambiar el número de caras de los dados?**  
Sí, desde el modo D&D puedes elegir dados de 4, 6, 8, 10, 12 o 20 caras.

---

## Dependencias

Este proyecto **no necesita instalar librerías externas**. Usa únicamente módulos que ya vienen con Python:

| Librería | Para qué se usa |
|----------|-----------------|
| `random` | Generar números aleatorios (tirar los dados) |
| `re`     | Procesar texto con patrones (en `utils.py`) |