# K-Script Programming Language (v1.0.0)

**K-Script** is a custom, interpreted programming language designed for minimalism and readability. It features a declarative `Command: Data` syntax, making it a lightweight tool for procedural programming.

---

## 🚀 Features
- **Dynamic Typing:** No need to declare `int` or `string`. The interpreter infers types automatically.
- **Custom Syntax:** Uses a unique `Command: Data` structure (e.g., `print:'Hello'`).
- **Math Engine:** Full support for arithmetic operations respecting **PEMDAS**.
- **Control Flow:** Robust `if` logic and `loop` iteration.
- **Modular Functions:** Define reusable code blocks with `def:` and execute them with `run:`.
- **Pure Python:** Built on a recursive descent interpreter engine with no external dependencies.

---

## 🛠️ Installation & Usage

### Prerequisites
- Python 3.x

### 1. Installation
Clone the repository to your local machine:
```bash
git clone https://github.com/Karthik-Siraparapu-1/K-Script.git
cd K-Script
```

### 2. Running a Script
Use the Python engine to execute a K-Script file:

```bash
python src/kscript.py examples/calc.ks
```

## 📝 Syntax Guide

### Variables & I/O
```text
name = 'K-Script'
version = 1.0

print:'Welcome to'
print:name
```

### Logic & Loops
**Note:** Code blocks must be indented by **4 spaces**.

```text
count = 1

loop: count < 5 do:
    print:count
    
    if: count = 3 do:
        print:'Halfway there!'
        
    count = count + 1
```

### Functions
```text
def: greet_user do:
    print:'Hello from a function!'

run: greet_user



