# WordGame

A lightweight, offline, command-line word game. You are given a random English word and
have to extract as many meaningful words as you can from its letters. Every valid word
scores one point.

## Features

- Random word generation (5–10 letters) using `wonderwords`.
- Dictionary-based validation with `pyspellchecker` (words must be real English words).
- Letter-checking: a submitted word can only use letters that appear in the generated
  word, and no letter more times than it appears there.
- Duplicate-submission protection: the same word cannot be scored twice in a round.
- Simple menu with three options: **Score Board**, **Start Game**, and **Exit**.
- Score board that displays saved players and their scores.
- Local persistence of player data in `players_db.dat` using Python `pickle`.
- Fully offline after dependencies are installed; no account or network required.

## Who is it suitable for?

- **Word-game enthusiasts** who enjoy anagram and letter-puzzle style challenges.
- **Students and language learners** who want to practice English spelling and vocabulary
  in a low-pressure, self-paced way.
- **Beginner Python developers** looking at a small, readable project that demonstrates
  modules, classes, the standard library `Counter` and `pickle`, and third-party packages.
- **Anyone who wants a quick brain teaser** in the terminal — no GUI, browser, or
  internet connection needed.

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`:
  - `wonderwords`
  - `pyspellchecker`

## Installation

```powershell
# Clone the repository and change into it
git clone https://github.com/Srinadhch07/wordgame-cli-based-offline-game.git
cd wordgame

# Create and activate a virtual environment (Windows / PowerShell)
python -m venv .venv
.\.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

The included `zvenv.ps1` script can be used to activate the virtual environment,
and `zstart.ps1` runs the game.

## Usage

Start the game from the project directory:

```powershell
python main.py
```

You will see the main menu:

```
================== menu ========================
1. Score Board
2. Start Game
3.Exit
Choose option:
```

- **1 – Score Board:** shows the names and scores of recorded players.
- **2 – Start Game:** prints the rules, asks for your name, generates a word, and starts
  the round.
- **3 – Exit:** closes the application.

### Playing a round

1. The generated word is displayed between banners, for example:

   ```
   ================ LISTEN ================
   ```

2. Build words using only the letters of that word (each letter can be used only as many
   times as it appears in the generated word). Examples for `LISTEN`: `listen`, `silent`,
   `enlist`, `tile`, `net`.
3. Enter words one at a time when asked `Enter an english word:`. A valid, new word scores
   one point and shows `✔️`; an invalid, misspelled, reused, or impossible word shows `❌`.
4. To finish, answer `N` (or `n`) to `Do you have word in mind [Y|N] default [Y]:`.
   Pressing Enter keeps the round going. Your final score is printed.
5. Reanswer the menu to view the score board or play again.

## Project structure

| File | Purpose |
| --- | --- |
| `main.py` | Game logic, input handling, and menu interface. |
| `score_dbms.py` | `DbManager` class for reading/writing player data with pickle. |
| `requirements.txt` | Third-party Python dependencies. |
| `zvenv.ps1` | Helper to activate the virtual environment. |
| `zstart.ps1` | Helper to launch the game. |
| `players_db.dat` | Local data file created at runtime to store scores. |
| `LICENSE` | MIT License. |

## License

Distributed under the MIT License. See `LICENSE` for details.
