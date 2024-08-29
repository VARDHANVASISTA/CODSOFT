import random
import tkinter as tk
from tkinter import messagebox

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to update the game based on the user's choice
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(user_choice, computer_choice)

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1
    
    score_label.config(text=f"Scores -> You: {user_score}, Computer: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Make your move!")
    score_label.config(text=f"Scores -> You: {user_score}, Computer: {computer_score}")

# Function to handle exit
def exit_game():
    if messagebox.askyesno("Quit", "Do you really want to quit?"):
        root.destroy()

user_score = 0
computer_score = 0

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Create labels and buttons
title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Helvetica", 16))
title_label.pack(pady=10)

result_label = tk.Label(root, text="Make your move!", font=("Helvetica", 14))
result_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("rock"))
rock_button.grid(row=0, column=0, padx=5, pady=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("paper"))
paper_button.grid(row=0, column=1, padx=5, pady=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("scissors"))
scissors_button.grid(row=0, column=2, padx=5, pady=5)

score_label = tk.Label(root, text=f"Scores -> You: {user_score}, Computer: {computer_score}", font=("Helvetica", 12))
score_label.pack(pady=10)

reset_button = tk.Button(root, text="Reset", width=10, command=reset_game)
reset_button.pack(side=tk.LEFT, padx=10, pady=10)

exit_button = tk.Button(root, text="Exit", width=10, command=exit_game)
exit_button.pack(side=tk.RIGHT, padx=10, pady=10)

root.mainloop()
