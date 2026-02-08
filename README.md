# 🎮 World of Games

**A collection of classic console games built in Python.** This project demonstrates the use of modular programming, game logic, file handling (I/O), and error management in Python.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)

## 📋 Table of Contents
- [About the Project](#about-the-project)
- [The Games](#the-games)
- [Key Features & Skills](#key-features--skills)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)

---

## 🧐 About the Project
"World of Games" is a Python-based application that serves as a central hub for multiple mini-games. The project was designed with a **modular architecture**, meaning each game is a standalone module managed by a central controller (`main.py`).

The project also includes a **scoring system** that persists data, saving the user's score to a local file even after the program is closed.

---

## 🕹️ The Games

### 1. Memory Game (`memory_game.py`)
A challenge that tests your memory and speed.
* **Logic:** Generates a random sequence of numbers, displays them for a few seconds, and then clears the screen.
* **Challenge:** The user must recall the sequence exactly.
* **Smart Feedback:** If the user fails, the game indicates exactly how many numbers were guessed correctly in the right position.

### 2. Guess Game (`guess_game.py`)
A classic "High/Low" guessing game.
* **Logic:** The computer selects a random number within a range based on the chosen difficulty level.
* **Challenge:** The user must guess the number. The game provides hints ("Too high", "Too low") to guide the user.

### 3. Math quiz (`math_game.py`)
Answer math qustions and get score


---

## 🚀 Key Features & Skills Demonstrated

* **Modular Design:** Separation of concerns by splitting the project into a main controller and separate game modules.
* **File I/O & Persistence:** Implementation of `score.py` to read and write scores to a text file (`Scores.txt`), ensuring data is saved between sessions.
* **Error Handling:** Robust use of `try...except` blocks to prevent crashes from invalid user inputs.
* **Data Structures:** Extensive use of Lists for managing game sequences and loops (`for`/`while`) for game flow.
* **Standard Libraries:** Usage of Python's built-in libraries: `random`, `time`, `os`.
* **Clean Code:** Written with readability and maintainability in mind.

---

## 📂 Project Structure

```text
World_Of_Games/
│
├── main.py             # The entry point / Game Manager
├── memory_game.py      # Logic for the Memory Game
├── guess_game.py       # Logic for the Guess Game
├── math_game.py         # Logic for Math game ├── score.py            # Handles reading/writing scores to a file
└── Scores.txt          # Stores the user's total score
