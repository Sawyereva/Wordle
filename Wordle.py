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
        random_number = random.randint(0, len(FIVE_LETTER_WORDS) - 1)
        randWord = FIVE_LETTER_WORDS[random_number]
        for i in range(N_COLS):
            j = 0
            gw.set_square_letter(j,i,randWord[i])



        gw.show_message("You have to implement this method.")


    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()
