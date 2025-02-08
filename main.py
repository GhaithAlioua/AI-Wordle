# Import necessary libraries
import tkinter as tk
import random

# Load a comprehensive dictionary of five-letter words
with open('words.txt', 'r') as file:
    # Create a list of words from the file, stripping whitespace and converting to lowercase
    words_file = [x.lower().strip() for x in file.readlines()]

# Function to compare each letter in the guess to the word
def result(word,guess):
    res = []
    for guessed_char, word_char in zip(guess, word):
        if guessed_char == word_char:
            res.append("G")  # Correct guess
        elif guessed_char in word:
            res.append("Y")  # Letter is in the word but in the wrong place
        else:
            res.append("N")  # Letter is not in the word
    return res

# Function to modify the knowledge about the word based on the guess
def modifyKnowledge(chosen,guess,knowledge):
    if not knowledge:
        # Initialize knowledge
        knowledge = [set("abcdefghijklmnopqrstuvwxyz") for _ in guess], set()
    letters, must = knowledge
    results = result(chosen,guess)
    for index, res in enumerate(results):
        if res == "G":
            # If the guess is correct, update the knowledge
            letters[index] = {guess[index]}
            must.add(guess[index])
        elif res == "Y":
            # If the letter is in the word but in the wrong place, update the knowledge
            letters[index].discard(guess[index])
            must.add(guess[index])
        elif res == "N":
            # If the letter is not in the word, update the knowledge
            for letter_set in letters:
                letter_set.discard(guess[index])
    return knowledge, results

# Function to modify the remaining possible words based on the guess
def modifyRemaining(chosen,guess,knowledge):
    remaining=[]
    knowledge,results=modifyKnowledge(chosen,guess,knowledge)
    letters, must = knowledge
    for word in words_file:
        # If the word matches the knowledge, add it to the remaining words
        if all(w in letter_set for w, letter_set in zip(word, letters)) and must.issubset(word):
            remaining.append(word)
    return remaining,knowledge,results

# Function to reset the game
def reset_game():
    for row in range(6):
        for column in range(5):
            labels[row][column].config(text="", bg="#121213")
    play()

# Function to play the game
def play():
    # Declare global variables
    global word
    global guess_counters

    # Select a random word from the list of words
    guess=random.choice(words_file)

    # Select a random word to be guessed
    word=random.choice(words_file)

    # Display the word to be guessed
    word_label.config(text=f"Word: {word}")

    # Initialize variables
    results=[]
    tries=1
    triedWords=[]
    knowledge=None
    working=True

    # Define the function to make a guess
    def make_guess():
        # Declare variables as nonlocal so they can be modified inside this function
        nonlocal guess, results, tries, triedWords, knowledge, working

        # Modify the remaining possible words based on the guess
        guesslist,knowledge,results = modifyRemaining(word,guess,knowledge)

        # Update the GUI based on the results of the guess
        for i in range(5):
            if results[i] == "G":
                color = "green"
            elif results[i] == "Y":
                color = "yellow"
            else:
                color = "grey"
            labels[tries-1][i].config(text=guess[i], bg=color)

        # If the guess is correct, update the win counter and guess counter
        if(results==["G","G","G","G","G"]):
            working=False
            win_counter[0] += 1
            win_label.config(text=f"Wins: {win_counter[0]}")
            guess_counters[tries - 1] += 1
        else:
            # If the guess is not correct, select a new guess from the remaining words
            guess=random.choice(guesslist)
            while guess in triedWords:
                guesslist.remove(guess)
                guess=random.choice(guesslist)
            triedWords.append(guess)
            tries+=1

            # If the number of tries exceeds 6, update the loss counter
            if tries > 6:
                loss_counter[0] += 1
                loss_label.config(text=f"Losses: {loss_counter[0]}")
            else:
                # If the number of tries does not exceed 6, make another guess after 1 second
                root.after(1000, make_guess)

    # Start making guesses
    make_guess()

# Function to show stats
def show_stats():
    total_games = win_counter[0] + loss_counter[0]
    if total_games == 0:
        print("No games played yet.")
        return
    print(f"Total games played: {total_games}")
    efficiency_percentage = win_counter[0] / total_games * 100
    print(f"Efficiency: {efficiency_percentage}%")
    print()
    for i, counter in enumerate(guess_counters):
        print(f"Attempt {i + 1}: {counter} times")

# Initialize counters
guess_counters = [0, 0, 0, 0, 0, 0]
root = tk.Tk()
root.title("Game")
root.geometry("600x600")
root.configure(bg='#121213')

# Initialize GUI elements
boxes = [[tk.Frame(root, bg='#3a3a3c') for _ in range(5)] for _ in range(6)]
labels = [[tk.Label(boxes[row][column], bg='#121213') for column in range(5)] for row in range(6)]
box_size = 60
gap_size = 10
start_x = (600 - (5 * box_size + 4 * gap_size)) / 2
start_y = (600 - (6 * box_size + 5 * gap_size)) / 2
for row in range(6):
    for column in range(5):
        boxes[row][column].place(x=start_x + column * (box_size + gap_size), y=start_y + row * (box_size + gap_size), width=box_size, height=box_size)
        labels[row][column].place(x=1, y=1, width=box_size-2, height=box_size-2)
win_counter = [0]
loss_counter = [0]
win_label = tk.Label(root, text=f"Wins: {win_counter[0]}", bg='#121213', fg='white', font=("Helvetica", 16), padx=10, pady=10)
win_label.place(x=150, y=540)
loss_label = tk.Label(root, text=f"Losses: {loss_counter[0]}", bg='#121213', fg='white', font=("Helvetica", 16), padx=10, pady=10)
loss_label.place(x=350, y=540)
retry_button = tk.Button(root, text="Retry", command=reset_game, bg='#3a3a3c', fg='white', font=("Helvetica", 12), padx=10, pady=10)
retry_button_width = 80
padding = 20
retry_button.place(x=600 - retry_button_width - padding, y=20, width=retry_button_width)
stats_button = tk.Button(root, text="Stats", command=show_stats, bg='#3a3a3c', fg='white', font=("Helvetica", 12), padx=10, pady=10)
stats_button_width = 80
padding = 20
stats_button.place(x=600 - stats_button_width - padding, y=75, width=stats_button_width)
word_label = tk.Label(root, bg='#121213', fg='white', font=("Helvetica", 16), padx=10, pady=10)
word_label_width = 200
word_label.place(x=(600 - word_label_width) / 2, y=20, width=word_label_width)

# Start the game
play()
root.mainloop()