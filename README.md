# 🎲 Juego-Dados
**Simulador profesional de tiradas de dados con modos Póker y D&D**  
**Professional dice roll simulator with Poker and D&D modes**

---

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.7+-blue?logo=python&logoColor=white&style=for-the-badge)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)](https://github.com/Fireforgegammer/Juego-dados)
[![Repository](https://img.shields.io/badge/Repository-GitHub-black?logo=github&style=for-the-badge)](https://github.com/Fireforgegammer/Juego-dados)

</div>

---

## 📚 Tabla de Contenidos / Table of Contents

### 🇪🇸 Español
- [Descripción](#-descripción)
- [Características](#-características)
- [Requisitos](#-requisitos)
- [Instalación y Uso](#-instalación-y-uso)
- [Módulos y API](#-módulos-y-api)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Ejemplos de Uso](#-ejemplos-de-uso)
- [Documentación Completa](#-documentación-completa-es)
- [Autor y Licencia](#-autor-y-licencia)

### 🇬🇧 English
- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation & Usage](#installation--usage)
- [Modules & API](#modules--api)
- [Project Structure](#project-structure)
- [Usage Examples](#usage-examples)
- [Full Documentation](#-full-documentation-en)
- [Author & License](#author--license)

---

# DOCUMENTACIÓN EN ESPAÑOL

## 📖 Descripción

**Juego-Dados** es un simulador de tiradas de dados profesional y educativo, escrito en Python, que proporciona dos modos principales:

- **🃏 Póker de Dados**: Juego completo de Póker de Dados con mano de 5 dados
- **⚔️ D&D**: Sistema de tiradas de rol estilo Dungeons & Dragons (d4, d6, d8, d10, d12, d20, d100)

Ideal para desarrolladores que desean aprender programación modular, gestión de menús interactivos y visualización en consola.

---

## ✨ Características

| Característica | Descripción |
|---|---|
| 🎲 **Múltiples dados** | Soporta dados de 4, 6, 8, 10, 12, 20 y 100 caras |
| 🎮 **Interfaz intuitiva** | Menú interactivo y fácil de usar en consola |
| 📊 **Visualización avanzada** | Representación gráfica de dados en consola |
| 🎯 **Póker de Dados** | Juego completo con manos, puntuaciones y evaluación |
| 🧮 **Sistema D&D** | Multitirada con gestión de cesta y cálculo automático |
| 🔧 **Código modular** | Arquitectura limpia y reutilizable |
| 📝 **Totalmente documentado** | Documentación bilingüe completa |
| 🧪 **Preparado para tests** | Estructura de directorio lista para pruebas unitarias |

---

## 🔧 Requisitos

- **Python**: 3.7 o superior
- **SO**: Windows, macOS, Linux
- **Dependencias**: Ninguna (solo librerías estándar de Python)

---

## ⚡ Instalación y Uso

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/Fireforgegammer/Juego-dados.git
cd Juego-dados
```

### 2️⃣ Ejecutar el programa

```bash
python main.py
```

### 3️⃣ Opciones del menú

```
====================================
LANZADOR DE DADOS
====================================
1. Poker de dados
2. D&D
3. Salir
```

---

## 📦 Módulos y API

### Núcleo (`core/`)

| Módulo | Función Principal | Documentación |
|--------|-------------------|---|
| **dados.py** | Lanzamiento básico de dados | [📄 dados_es.md](docs/dados_es.md) |
| **poker.py** | Lógica completa del Póker de Dados | [📄 poker_es.md](docs/poker_es.md) |
| **rol.py** | Sistema de tiradas D&D | [📄 rol_es.md](docs/rol_es.md) |
| **utils.py** | Funciones de utilidad y formato | [📄 utils_es.md](docs/utils_es.md) |
| **visuals.py** | Visualización gráfica en consola | [📄 visuals_es.md](docs/visuals_es.md) |

### Interfaz de Usuario (`ui/`)

| Módulo | Función Principal | Documentación |
|--------|-------------------|---|
| **menu.py** | Menús del sistema | [📄 menu_es.md](docs/menu_es.md) |
| **acciones.py** | Enrutador de opciones | [📄 acciones_es.md](docs/acciones_es.md) |

---

## 📁 Estructura del Proyecto

```
Juego-dados/
├── 📄 main.py                 # Punto de entrada principal
├── 📄 README.md               # Este archivo
├── 📄 LICENSE                 # Licencia MIT
│
├── 📂 core/                   # Módulos principales
│   ├── __pycache__/
│   ├── dados.py              # 🎲 Tiradas básicas
│   ├── poker.py              # 🃏 Lógica Póker Dados
│   ├── rol.py                # ⚔️  Sistema D&D
│   ├── utils.py              # 🔧 Utilidades
│   └── visuals.py            # 🎨 Visualización
│
├── 📂 ui/                     # Interfaz de usuario
│   ├── __pycache__/
│   ├── menu.py               # 📋 Menús
│   └── acciones.py           # 🔀 Enrutador
│
├── 📂 docs/                   # Documentación completa
│   ├── *_es.md               # Documentación en español
│   ├── *_en.md               # Documentación en inglés
│   └── nomenclature_es.md    # Convenciones de código
│
└── 📂 tests/                  # Pruebas unitarias (preparado)
```

---

## 💡 Ejemplos de Uso

### Ejemplo 1: Tirada básica de d20

```python
from core.dados import tirar_dado

# Una tirada de d20
resultado = tirar_dado(caras=20)
print(f"Resultado: {resultado}")  # Output: Resultado: 15
```

### Ejemplo 2: Múltiples dados

```python
from core.dados import tirar_varios_dados

# Tirada de 5d6 (Póker de Dados)
dados = tirar_varios_dados(cantidad=5, caras=6)
print(f"Dados: {dados}")  # Output: Dados: [3, 6, 2, 5, 4]
```

### Ejemplo 3: Tirada con suma

```python
from core.dados import tirar_rol

# Tirada 4d6 con suma
datos, suma = tirar_rol(cantidad=4, caras=6)
print(f"Tiradas: {datos}, Total: {suma}")  # Output: Tiradas: [4, 5, 3, 2], Total: 14
```

---

## 📖 Documentación Completa (ES)

Accede a la documentación detallada de cada módulo:

| Documento | Contenido |
|-----------|----------|
| [dados_es.md](docs/dados_es.md) | Función `tirar_dado()`, `tirar_varios_dados()`, `tirar_rol()` |
| [poker_es.md](docs/poker_es.md) | Lógica de Póker de Dados, manos, puntuaciones |
| [rol_es.md](docs/rol_es.md) | Sistema D&D, multitirada, cesta de dados |
| [utils_es.md](docs/utils_es.md) | Funciones de utilidad y formato |
| [visuals_es.md](docs/visuals_es.md) | Visualización gráfica, representación ASCII |
| [menu_es.md](docs/menu_es.md) | Menús del sistema |
| [acciones_es.md](docs/acciones_es.md) | Enrutador de opciones |
| [instalacion_es.md](docs/instalacion_es.md) | Guía de instalación |
| [nomenclatura_es.md](docs/nomenclatura_es.md) | Convenciones de código |

---

---

# ENGLISH DOCUMENTATION

## 📖 Description

**Juego-Dados** is a professional and educational dice roll simulator written in Python, providing two main modes:

- **🃏 Poker Dice**: Full Poker Dice game with 5-dice hand
- **⚔️ D&D**: Dungeons & Dragons style roll system (d4, d6, d8, d10, d12, d20, d100)

Ideal for developers who want to learn modular programming, interactive menu management, and console visualization.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎲 **Multiple dice** | Supports d4, d6, d8, d10, d12, d20, and d100 |
| 🎮 **Intuitive interface** | Interactive and easy-to-use console menu |
| 📊 **Advanced visualization** | Graphical dice representation in console |
| 🎯 **Poker Dice** | Full game with hands, scores, and evaluation |
| 🧮 **D&D System** | Multi-roll with basket management and auto-calculation |
| 🔧 **Modular code** | Clean and reusable architecture |
| 📝 **Fully documented** | Complete bilingual documentation |
| 🧪 **Test-ready** | Directory structure ready for unit tests |

---

## 🔧 Requirements

- **Python**: 3.7 or higher
- **OS**: Windows, macOS, Linux
- **Dependencies**: None (only Python standard library)

---

## ⚡ Installation & Usage

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Fireforgegammer/Juego-dados.git
cd Juego-dados
```

### 2️⃣ Run the program

```bash
python main.py
```

### 3️⃣ Menu options

```
====================================
DICE LAUNCHER
====================================
1. Poker Dice
2. D&D
3. Exit
```

---

## 📦 Modules & API

### Core (`core/`)

| Module | Main Function | Documentation |
|--------|---------------|---|
| **dados.py** | Basic dice rolls | [📄 dados_en.md](docs/dados_en.md) |
| **poker.py** | Complete Poker Dice logic | [📄 poker_en.md](docs/poker_en.md) |
| **rol.py** | D&D roll system | [📄 rol_en.md](docs/rol_en.md) |
| **utils.py** | Utility and formatting functions | [📄 utils_en.md](docs/utils_en.md) |
| **visuals.py** | Console graphical visualization | [📄 visuals_en.md](docs/visuals_en.md) |

### User Interface (`ui/`)

| Module | Main Function | Documentation |
|--------|---------------|---|
| **menu.py** | System menus | [📄 menu_en.md](docs/menu_en.md) |
| **acciones.py** | Option router | [📄 acciones_en.md](docs/acciones_en.md) |

---

## 📁 Project Structure

```
Juego-dados/
├── 📄 main.py                 # Main entry point
├── 📄 README.md               # This file
├── 📄 LICENSE                 # MIT License
│
├── 📂 core/                   # Core modules
│   ├── __pycache__/
│   ├── dados.py              # 🎲 Basic rolls
│   ├── poker.py              # 🃏 Poker Dice logic
│   ├── rol.py                # ⚔️  D&D system
│   ├── utils.py              # 🔧 Utilities
│   └── visuals.py            # 🎨 Visualization
│
├── 📂 ui/                     # User interface
│   ├── __pycache__/
│   ├── menu.py               # 📋 Menus
│   └── acciones.py           # 🔀 Router
│
├── 📂 docs/                   # Complete documentation
│   ├── *_es.md               # Spanish documentation
│   ├── *_en.md               # English documentation
│   └── nomenclature_en.md    # Code conventions
│
└── 📂 tests/                  # Unit tests (ready)
```

---

## 💡 Usage Examples

### Example 1: Basic d20 roll

```python
from core.dados import tirar_dado

# Single d20 roll
resultado = tirar_dado(caras=20)
print(f"Result: {resultado}")  # Output: Result: 15
```

### Example 2: Multiple dice

```python
from core.dados import tirar_varios_dados

# 5d6 roll (Poker Dice)
dados = tirar_varios_dados(cantidad=5, caras=6)
print(f"Dice: {dados}")  # Output: Dice: [3, 6, 2, 5, 4]
```

### Example 3: Roll with sum

```python
from core.dados import tirar_rol

# 4d6 roll with sum
datos, suma = tirar_rol(cantidad=4, caras=6)
print(f"Rolls: {datos}, Total: {suma}")  # Output: Rolls: [4, 5, 3, 2], Total: 14
```

---

## 📖 Full Documentation (EN)

Access detailed documentation for each module:

| Document | Content |
|----------|---------|
| [dados_en.md](docs/dados_en.md) | `tirar_dado()`, `tirar_varios_dados()`, `tirar_rol()` |
| [poker_en.md](docs/poker_en.md) | Poker Dice logic, hands, scores |
| [rol_en.md](docs/rol_en.md) | D&D system, multi-roll, dice basket |
| [utils_en.md](docs/utils_en.md) | Utility and formatting functions |
| [visuals_en.md](docs/visuals_en.md) | Graphical visualization, ASCII representation |
| [menu_en.md](docs/menu_en.md) | System menus |
| [acciones_en.md](docs/acciones_en.md) | Action router |
| [installation_en.md](docs/installation_en.md) | Installation guide |
| [nomenclature_en.md](docs/nomenclature_en.md) | Code conventions |

---

## 👨‍💻 Autor y Licencia

<div align="center">

**Creado por:** [Fireforgegammer](https://github.com/Fireforgegammer)

[![GitHub Profile](https://img.shields.io/badge/GitHub-Fireforgegammer-black?logo=github&style=for-the-badge)](https://github.com/Fireforgegammer)
[![Repository](https://img.shields.io/badge/Repository-Juego--dados-blue?logo=github&style=for-the-badge)](https://github.com/Fireforgegammer/Juego-dados)

**Licencia:** [MIT License](LICENSE) © 2026 Fireforgegammer

---

**Contribuciones:** Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request en el repositorio.

</div>