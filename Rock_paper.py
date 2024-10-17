import random
import tkinter as tk

# Main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("450x600")
root.config(bg="#ffffff")

# Global variables for score
player_score = 0
computer_score = 0

# Game logic
def play(player_choice):
    global player_score, computer_score
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)
    
    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        player_score += 1
        result = f"You Win! {player_choice} beats {computer_choice}."
    else:
        computer_score += 1
        result = f"You Lose! {computer_choice} beats {player_choice}."
    
    # Update the result and score
    result_label.config(text=result)
    score_label.config(text=f"Player: {player_score}  Computer: {computer_score}")

# Function to exit the game
def exit_game():
    root.quit()


title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 28, "bold"), bg="#ffffff", fg="#333")
title_label.pack(pady=30)

result_label = tk.Label(root, text="Make your choice!", font=("Arial", 20), bg="#ffffff", fg="#333")
result_label.pack(pady=30)

score_label = tk.Label(root, text="Player: 0  Computer: 0", font=("Arial", 16), bg="#ffffff", fg="#333")
score_label.pack(pady=30)

# Button styling
button_style = {
    'font': ("Arial", 18),
    'width': 20,
    'fg': "black",  # Dark text color
    'bd': 0,
    'padx': 10,
    'pady': 10,
}

# Rock Button
rock_btn = tk.Button(root, text="Rock", command=lambda: play('Rock'), bg="#ff4757", activebackground="#ff6b81", **button_style)
rock_btn.pack(pady=10)

# Paper Button
paper_btn = tk.Button(root, text="Paper", command=lambda: play('Paper'), bg="#1e90ff", activebackground="#63a4ff", **button_style)
paper_btn.pack(pady=10)

# Scissors Button
scissors_btn = tk.Button(root, text="Scissors", command=lambda: play('Scissors'), bg="#2ed573", activebackground="#5be79b", **button_style)
scissors_btn.pack(pady=10)

# Exit Button
exit_btn = tk.Button(root, text="Exit", command=exit_game, bg="#ff6348", activebackground="#ff7f7f", **button_style)
exit_btn.pack(pady=30)

# Start the game loop
root.mainloop()
