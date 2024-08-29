import random
import tkinter as tk

# create the window
window = tk.Tk()
window.title("Card Draw")

# create a canvas to draw the card on
canvas = tk.Canvas(window, width=200, height=200)
canvas.pack()

# define a function to draw a card
def draw_card():
    # create a rectangle for the card
    card_rect = canvas.create_rectangle(0, 0, 200, 200, fill="#FFFFFF")
    # create a text object for the card value
    card_value = canvas.create_text(100, 50, text="Choose", font=("Helvetica", 36, "bold"))
    # choose a random card value
    card_value = random.choice(["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"])
    # create a text object for the card value
    card_text = canvas.create_text(100, 100, text=card_value, font=("Helvetica", 36, "bold"))

# create a button to draw a card
draw_button = tk.Button(window, text="Draw Card", command=draw_card)
draw_button.pack()

# start the main loop to keep the window open
window.mainloop()