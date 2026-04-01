# 🛠️ Installation & Usage Guide

> How to install and run the **Dice Simulator** step by step — written for people with no programming experience.

🌐 [Versión en español](instalacion_es.md) · [← Back to index](README.md)

---

## What do you need before starting?

Just **Python** installed on your computer. Nothing else.

### 1. Check if you already have Python

Open a terminal (on Windows: `cmd` or `PowerShell`; on Mac/Linux: `Terminal`) and type:

```bash
python --version
```

If you see something like `Python 3.10.0` or higher, you already have it! Skip to step 3.

If you see an error, move to step 2.

---

### 2. Install Python

Go to [python.org/downloads](https://python.org/downloads) and download the latest version.

> ⚠️ On Windows, during installation, make sure to check **"Add Python to PATH"**. This is important.

---

### 3. Download the project

#### Option A — With Git (recommended)

```bash
git clone <repository-url>
cd JUEGO-DADOS
```

#### Option B — Without Git

1. Go to the repository page
2. Click the green **"Code"** button
3. Choose **"Download ZIP"**
4. Unzip the file to your preferred folder

---

### 4. Run the program

Open the terminal inside the project folder and type:

```bash
python main.py
```

You should see the main menu:

```
========================================
🎲 DICE LAUNCHER
========================================
1. Poker dice
2. D&D
3. Exit
```

It's working! 🎉

---

## How to play?

### Main menu

When the menu appears, type the number of the option you want and press `Enter`.

```
1  →  Play Poker Dice
2  →  D&D mode (roll dice)
3  →  Exit the program
```

### Poker Dice

1. Choose whether to play **against the AI** or **against another player**
2. 5 dice are rolled automatically
3. You can choose which dice to re-roll (up to 2 times)
4. At the end, hands are compared and the winner is announced

**To choose which dice to re-roll**, type the numbers separated by spaces:

```
Which dice do you want to re-roll? (e.g. 1 3 5): 2 4
```

That would re-roll dice 2 and dice 4.

### D&D Mode

Choose the type of dice and how many you want to roll. The program shows individual results and the total.

---

## Startup flow diagram

```
┌──────────────────────────┐
│   Open the terminal      │
└──────────────┬───────────┘
               │
               ▼
┌──────────────────────────┐
│   python main.py         │
└──────────────┬───────────┘
               │
               ▼
┌──────────────────────────┐
│   Menu is displayed      │
│   mostrar_menu()         │
└──────────────┬───────────┘
               │
               ▼
┌──────────────────────────┐
│   You type a number      │
│   and press Enter        │
└──────────────┬───────────┘
               │
        ┌──────┴──────┐
        │             │
      1 or 2          3
        │             │
        ▼             ▼
  Game starts     Program
                  closes
```

---

## Frequently asked questions

**The program won't start?**  
Make sure you're inside the correct folder before running `python main.py`. Use `cd JUEGO-DADOS` to navigate there.

**I see an error with `python`?**  
Try `python3 main.py` instead. On Mac and Linux it's common to use `python3`.

**Can I change the number of sides on the dice?**  
Yes, from D&D mode you can choose dice with 4, 6, 8, 10, 12 or 20 sides.

---

## Dependencies

This project **does not need any external libraries**. It uses only modules that come with Python:

| Library | What it's used for |
|---------|-------------------|
| `random` | Generate random numbers (rolling dice) |
| `re`     | Process text with patterns (in `utils.py`) |