import tkinter as tk
import random

# ---------- Settings ----------
EMOJI = {"Rock": "✊", "Paper": "✋", "Scissors": "✌️"}
BEATS = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}

BG, CARD, TEXT = "#1e1e2e", "#2a2a3d", "#f5f5f5"
GREEN, RED, YELLOW, BLUE = "#4ade80", "#f87171", "#facc15", "#60a5fa"
EMOJI_FONT = ("Segoe UI Emoji", 46)

scores = {"you": 0, "comp": 0}


# ---------- Game logic ----------
def play(user):
    comp = random.choice(list(EMOJI))

    if user == comp:
        text, color = "It's a Tie!", YELLOW
    elif BEATS[user] == comp:
        text, color = "You Win! 🎉", GREEN
        scores["you"] += 1
    else:
        text, color = "Computer Wins!", RED
        scores["comp"] += 1

    you_emoji.config(text=EMOJI[user])
    comp_emoji.config(text=EMOJI[comp])
    result.config(text=text, fg=color)
    you_score.config(text=scores["you"])
    comp_score.config(text=scores["comp"])


def reset():
    scores["you"] = scores["comp"] = 0
    you_emoji.config(text="❔")
    comp_emoji.config(text="❔")
    result.config(text="Choose your move!", fg=TEXT)
    you_score.config(text=0)
    comp_score.config(text=0)


def hover(widget, on):
    widget.config(bg=BLUE if on else CARD)


# ---------- Window ----------
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("420x520")
root.configure(bg=BG)
root.resizable(False, False)

tk.Label(root, text="Rock  Paper  Scissors", font=("Arial", 20, "bold"),
         bg=BG, fg=TEXT).pack(pady=(18, 10))

# Scoreboard
board = tk.Frame(root, bg=BG)
board.pack(pady=5)
for name, key in (("YOU", "you"), ("COMPUTER", "comp")):
    card = tk.Frame(board, bg=CARD, padx=25, pady=8)
    card.pack(side="left", padx=10)
    tk.Label(card, text=name, font=("Arial", 10, "bold"), bg=CARD, fg="#aaaaaa").pack()
    lbl = tk.Label(card, text="0", font=("Arial", 24, "bold"), bg=CARD, fg=TEXT)
    lbl.pack()
    if key == "you":
        you_score = lbl
    else:
        comp_score = lbl

# Arena (shows both moves)
arena = tk.Frame(root, bg=BG)
arena.pack(pady=20)
you_emoji = tk.Label(arena, text="❔", font=EMOJI_FONT, bg=CARD, width=3, pady=10)
you_emoji.pack(side="left", padx=10)
tk.Label(arena, text="VS", font=("Arial", 14, "bold"), bg=BG, fg="#888888").pack(side="left")
comp_emoji = tk.Label(arena, text="❔", font=EMOJI_FONT, bg=CARD, width=3, pady=10)
comp_emoji.pack(side="left", padx=10)

result = tk.Label(root, text="Choose your move!", font=("Arial", 18, "bold"),
                  bg=BG, fg=TEXT)
result.pack(pady=5)

# Move buttons
buttons = tk.Frame(root, bg=BG)
buttons.pack(pady=20)
for move, emoji in EMOJI.items():
    b = tk.Button(buttons, text=f"{emoji}\n{move}", font=("Segoe UI Emoji", 14),
                  width=7, bg=CARD, fg=TEXT, activebackground=BLUE,
                  relief="flat", cursor="hand2", command=lambda m=move: play(m))
    b.pack(side="left", padx=8)
    b.bind("<Enter>", lambda e, w=b: hover(w, True))
    b.bind("<Leave>", lambda e, w=b: hover(w, False))

tk.Button(root, text="Reset Game", font=("Arial", 11, "bold"), bg=RED, fg="white",
          relief="flat", padx=15, pady=4, cursor="hand2", command=reset).pack(pady=10)

root.mainloop()