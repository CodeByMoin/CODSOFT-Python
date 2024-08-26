# Task - 4

# User Input: Prompt the user to choose rock, paper, or scissors.

# Computer Selection: Generate a random choice (rock, paper, or scissors) for the computer.

# Game Logic: Determine the winner based on the user's choice and the computer's choice.
# Rock beats scissors, scissors beat paper, and paper beats rock.

# Display Result: Show the user's choice and the computer's choice.
# Display the result, whether the user wins, loses, or it's a tie.

# Score Tracking (Optional): Keep track of the user's and computer's scores for multiple rounds.

# Play Again: Ask the user if they want to play another round.

# User Interface: Design a user-friendly interface with clear instructions and feedback.


import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.user_score = 0
        self.computer_score = 0

        self.root = root
        self.root.title("Rock, Paper, Scissors")
        self.root.geometry("400x400")
        self.root.configure(bg="#282C34")

        # Title Label
        self.title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Helvetica", 24, "bold"), bg="#61AFEF", fg="#282C34")
        self.title_label.pack(pady=20)

        # Button Frame
        self.button_frame = tk.Frame(root, bg="#282C34")
        self.button_frame.pack(pady=20)

        self.rock_button = tk.Button(self.button_frame, bg="#98C379", fg="#282C34", text="Rock", font=("Helvetica", 14, "bold"), command=lambda: self.play('Rock'))
        self.rock_button.grid(row=0, column=0, padx=10)

        self.paper_button = tk.Button(self.button_frame, bg="#E5C07B", fg="#282C34", text="Paper", font=("Helvetica", 14, "bold"), command=lambda: self.play('Paper'))
        self.paper_button.grid(row=0, column=1, padx=10)

        self.scissors_button = tk.Button(self.button_frame, bg="#E06C75", fg="#282C34", text="Scissors", font=("Helvetica", 14, "bold"), command=lambda: self.play('Scissors'))
        self.scissors_button.grid(row=0, column=2, padx=10)

        # Result Label
        self.result_label = tk.Label(root, text="", font=("Helvetica", 18), bg="#282C34", fg="white")
        self.result_label.pack(pady=20)

        # Score Label
        self.score_label = tk.Label(root, text=f"Score: You {self.user_score} - {self.computer_score} Computer", font=("Helvetica", 18), bg="#282C34", fg="white")
        self.score_label.pack(pady=20)

        # Reset Button
        self.reset_button = tk.Button(root, bg="#61AFEF", fg="#282C34", text="Reset Game", font=("Helvetica", 16, "bold"), command=self.reset_game)
        self.reset_button.pack(pady=10)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
             (user_choice == 'Scissors' and computer_choice == 'Paper') or \
             (user_choice == 'Paper' and computer_choice == 'Rock'):
            return "You win!"
        else:
            return "You lose!"

    def play(self, user_choice):
        computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
        result = self.determine_winner(user_choice, computer_choice)

        self.result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
        self.update_scores(result)

    def update_scores(self, result):
        if result == "You win!":
            self.user_score += 1
        elif result == "You lose!":
            self.computer_score += 1
        self.score_label.config(text=f"Score: You {self.user_score} - {self.computer_score} Computer")

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text=f"Score: You {self.user_score} - {self.computer_score} Computer")
        self.result_label.config(text="")
    

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
