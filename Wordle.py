# File: Wordle.py
# i think i did some stuff
"""
Picks a random word and puts it in the top row. Milestone 1 complete!
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    
    def enter_action(s):
        if s.lower() in FIVE_LETTER_WORDS:
            gw.show_message("Good Job")
        else:
            gw.show_message("Not in word list")


    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

     # Choose a random word from the provided list
    selected_word = random.choice(FIVE_LETTER_WORDS)

    # Display the selected word in the first row
    for col in range(N_COLS):
        gw.set_square_letter(0, col, selected_word[col])

# Startup code

if __name__ == "__main__":
    wordle()
