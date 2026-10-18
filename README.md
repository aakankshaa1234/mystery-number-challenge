# 🎮 Mystery Number Challenge

A beginner-friendly number guessing game built with Python. The computer chooses a secret number, and you try to guess it before you run out of attempts.

## ✨ Features

- Random secret number between 1 and 100
- Five attempts per round
- Helpful **too high** and **too low** hints
- Input validation for letters, decimals, and numbers outside the allowed range
- Option to play multiple rounds
- No third-party packages required

## 🧰 Requirements

- Python 3.8 or newer
- A terminal, Command Prompt, or an editor such as Visual Studio Code

## ▶️ How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python game.py
   ```

   If `python` does not work on Windows, try:

   ```bash
   py game.py
   ```

4. Follow the prompts and enter a whole number from 1 to 100.

## 🕹️ How to Play

1. The computer chooses a secret number.
2. Enter a guess between 1 and 100.
3. Follow the hints:
   - **Too low** means try a higher number.
   - **Too high** means try a lower number.
   - **Correct** means you found the secret number!
4. You have five valid guesses per round.
5. Choose whether to play another round.

Invalid entries do not use up an attempt.

## 📁 Project Structure

```text
mystery-number-challenge/
├── game.py
├── README.md
├── .gitignore
└── LICENSE
```

## 🧠 Python Concepts Practised

- Variables and constants
- `random.randint()`
- `input()` and `print()`
- `int()` and `try` / `except`
- `if` / `elif` / `else` logic
- `while` and `for` loops
- Functions and return values

## 💡 Ideas for Future Improvements

- Add easy, medium, and hard difficulty levels
- Keep track of a best score
- Let the player choose the number range
- Add automated tests
- Create a graphical interface

## 📜 License

This project is available under the MIT License. See [LICENSE](LICENSE).

---

Made as a learning project. Have fun guessing! 🎉
