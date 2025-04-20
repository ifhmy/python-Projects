import tkinter as tk
import random

# Function to determine the winner
def play_game(user_choice):
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    pc_choice = random.choice(['r', 'p', 's'])

    user_choice_text.set(f"You chose: {choices[user_choice]}")
    pc_choice_text.set(f"PC chose: {choices[pc_choice]}")

    if user_choice == pc_choice:
        result_text.set("🤝 It's a tie!")
    elif (user_choice == 'r' and pc_choice == 's') or \
         (user_choice == 'p' and pc_choice == 'r') or \
         (user_choice == 's' and pc_choice == 'p'):
        result_text.set("🎉 You win!")
    else:
        result_text.set("💥 You lose! PC wins.")

# Create main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.configure(bg="#1e1e2f")
root.geometry("500x500")

# Variables
user_choice_text = tk.StringVar()
pc_choice_text = tk.StringVar()
result_text = tk.StringVar()

# Title
tk.Label(root, text="Rock, Paper, Scissors!", font=("Arial", 20, "bold"), bg="#1e1e2f", fg="white").pack(pady=20)

# Display choices
tk.Label(root, textvariable=user_choice_text, font=("Arial", 12), bg="#1e1e2f", fg="#ccc").pack()
tk.Label(root, textvariable=pc_choice_text, font=("Arial", 12), bg="#1e1e2f", fg="#ccc").pack()
tk.Label(root, textvariable=result_text, font=("Arial", 16, "bold"), bg="#1e1e2f", fg="#ffd700").pack(pady=20)

# Buttons with text (no images)
button_frame = tk.Frame(root, bg="#1e1e2f")
button_frame.pack(pady=20)

tk.Button(button_frame, text="Rock", width=10, height=2, command=lambda: play_game('r'), bg="#1e1e2f", fg="white", font=("Arial", 12), bd=0).grid(row=0, column=0, padx=20)
tk.Button(button_frame, text="Paper", width=10, height=2, command=lambda: play_game('p'), bg="#1e1e2f", fg="white", font=("Arial", 12), bd=0).grid(row=0, column=1, padx=20)
tk.Button(button_frame, text="Scissors", width=10, height=2, command=lambda: play_game('s'), bg="#1e1e2f", fg="white", font=("Arial", 12), bd=0).grid(row=0, column=2, padx=20)

# Start GUI
root.mainloop()
