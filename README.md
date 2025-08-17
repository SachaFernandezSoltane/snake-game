# 🐍 Snake Game in Python

---

A simple Snake game built with Python and Pygame. Navigate the snake with Arrow keys ⬆️⬇️⬅️➡️, eat 🍎 apples, avoid walls and yourself, and try to fill the grid to win! 🏆

---

## ✨ Features

* Classic Snake gameplay 🐍
* Grid-based movement 🔲
* Apple spawning at random positions 🍏
* Snake grows when eating apples ➕
* Game over when hitting walls or itself ❌
* Victory condition when the snake fills the entire grid 🏅
* Start and restart functionality 🔄

---

## ⚡ Installation

1. Clone the repository:

```bash
git clone https://github.com/SachaFernandezSoltane/snake-game.git
cd snake-game
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
```

3. Install dependencies:

```bash
pip -r requirements.txt
```

4. Run the game:

```bash
python main.py
```

Make sure you have the `Graphics` folder with `apple.png` 🍎.

---

## 🎮 Controls

| Key         | Action        |
| ----------- | ------------- |
| Up Arrow    | Move Up ⬆️    |
| Down Arrow  | Move Down ⬇️  |
| Left Arrow  | Move Left ⬅️  |
| Right Arrow | Move Right ➡️ |

---

## 🔍 How It Works

* The game is grid-based with a `cell_size` for each block 🟩.
* The snake moves one cell at a time 🐍.
* Collisions:

  * Self collision → Game Over ❌
  * Wall collision → Game Over ❌
  * Apple collision → Snake grows ➕
* Victory occurs when the snake fills the entire grid 🏆.

---

## 📂 Project Structure

```
snake-game/
├─ src/
│  ├─ snake.py
│  ├─ apple.py
│  ├─ game.py
├─ Graphics/
│  ├─ apple.png 🍎
├─ main.py
├─ requirements.txt
├─ LICENCE
├─ .gitignore
├─ README.md
```

---
## 📜 License

This project is open-source and available under the MIT License.