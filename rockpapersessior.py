import tkinter as tk
import random

CHOICES = ["Rock", "Paper", "Scissors"]
BEATS = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}

user_score = 0
comp_score = 0


def play(user):
    global user_score, comp_score
    comp = random.choice(CHOICES)

    if user == comp:
        result = "It's a Tie!"
    elif BEATS[user] == comp:
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        comp_score += 1

    choice_label.config(text=f"You: {user}   |   Computer: {comp}")
    result_label.config(text=result)
    score_label.config(text=f"Score  You: {user_score}  -  Computer: {comp_score}")


def reset():
    global user_score, comp_score
    user_score = comp_score = 0
    choice_label.config(text="Make your choice!")
    result_label.config(text="")
    score_label.config(text="Score  You: 0  -  Computer: 0")


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("380x300")
root.resizable(False, False)

tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold")).pack(pady=10)

choice_label = tk.Label(root, text="Make your choice!", font=("Arial", 12))
choice_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), fg="blue")
result_label.pack(pady=5)

score_label = tk.Label(root, text="Score  You: 0  -  Computer: 0", font=("Arial", 12))
score_label.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=15)
for c in CHOICES:
    tk.Button(frame, text=c, width=9, font=("Arial", 11),
              command=lambda x=c: play(x)).pack(side="left", padx=5)

tk.Button(root, text="Reset", command=reset).pack()

root.mainloop()