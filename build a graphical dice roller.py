# build a graphical dice roller
import random
import tkinter as tk

# create the window
window = tk.Tk()
window.title("Dice Roller")

# create a label to display the dice result
result_label = tk.Label(window, text="You rolled a ")
result_label.pack()

# define a function to roll the dice and display the result
def roll_dice():
    # roll the dice
    roll = random.randint(1, 6)
    # display the result
    result_label.configure(text=f"You rolled a {roll}")

# create a button to roll the dice
roll_button = tk.Button(window, text="Roll Dice", command=roll_dice)
roll_button.pack()

# start the main loop to keep the window open
window.mainloop()