import tkinter as tk
import random

# ---------- Game Data ----------
number = random.randint(1, 100)
tries = 0

# ---------- Functions ----------
def check_guess():
    global tries
    try:
        guess = int(entry.get())
    except ValueError:
        result.config(text="Please enter a valid number!", fg="red")
        return

    tries += 1
    tries_label.config(text=f"Tries: {tries}")

    if guess < number:
        result.config(text="Too low! Try higher.", fg="orange")
    elif guess > number:
        result.config(text="Too high! Try lower.", fg="orange")
    else:
        result.config(text=f"Correct! You got it in {tries} tries!", fg="green")
        guess_btn.config(state="disabled")

    entry.delete(0, tk.END)

def new_game():
    global number, tries
    number = random.randint(1, 100)
    tries = 0
    tries_label.config(text="Tries: 0")
    result.config(text="", fg="black")
    guess_btn.config(state="normal")
    entry.delete(0, tk.END)

# ---------- Window ----------
root = tk.Tk()
root.title("Guess the Number")
root.geometry("300x250")
root.resizable(False, False)

tk.Label(root, text="Guess the Number", font=("Arial", 16, "bold")).pack(pady=10)
tk.Label(root, text="I'm thinking of a number between 1 and 100").pack()

entry = tk.Entry(root, font=("Arial", 14), justify="center", width=10)
entry.pack(pady=10)
entry.bind("<Return>", lambda event: check_guess())

guess_btn = tk.Button(root, text="Guess", width=10, command=check_guess)
guess_btn.pack()

result = tk.Label(root, text="", font=("Arial", 11))
result.pack(pady=8)

tries_label = tk.Label(root, text="Tries: 0")
tries_label.pack()

tk.Button(root, text="New Game", width=10, command=new_game).pack(pady=8)

root.mainloop()