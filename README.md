# Wordle-AI-Solver 🧩🤖

An **AI-powered Wordle solver** developed in Python with a **graphical user interface (GUI)**, optimizing word-guessing algorithms using knowledge-based techniques to improve accuracy, speed, and minimize guesses.

---

## Description
This project implements an **AI-powered Wordle solver** with a **GUI** using Python. The solver leverages an advanced algorithm to enhance word-guessing accuracy and speed while minimizing the number of guesses required. The project uses knowledge-based decision-making to improve future guesses based on past attempts, making it more efficient. Features include:
- **Word-guessing algorithms**: Optimized to improve accuracy and speed.
- **Knowledge-based decision-making**: Refines future guesses based on previous feedback.
- **Graphical User Interface (GUI)**: Interactive interface built using **Tkinter** for a user-friendly experience.
- **Data structures and optimization techniques**: Minimize the number of guesses by refining knowledge after each attempt.

This project is a personal initiative to demonstrate the integration of algorithms, optimization, and UI design in Python.

---

## Features
- **AI-Driven Solver**: Solves Wordle puzzles by making efficient guesses.
- **GUI Interface**: Built with **Tkinter**, providing a visual representation of the game.
- **Knowledge-Based Approach**: Learns from each guess to refine subsequent attempts.
- **Optimized Word Guessing**: Reduces unnecessary guesses through data structures and optimization techniques.
- **Word Database**: Uses a dictionary of valid five-letter words for the solver to guess.

---

## How It Works
1. **Game Setup**: The solver randomly selects a target word from a pre-defined dictionary of five-letter words.
2. **Make a Guess**: The solver makes a guess and receives feedback (correct letters, wrong letters, and letter positions).
3. **Refine Knowledge**: Based on the feedback, the solver updates its knowledge and adjusts future guesses.
4. **Minimize Guesses**: The solver continually narrows down potential solutions, making the process more efficient and reducing the number of guesses.
5. **GUI Update**: The results of each guess are displayed visually on the GUI, showing which letters are correctly placed, mispositioned, or not in the word.
