# File: Wordle.py
# i think i did some stuff
"""
Picks a random word and puts it in the top row. Milestone 1 complete!
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, MISSING_COLOR, PRESENT_COLOR, UNKNOWN_COLOR

def wordle():

    # Choose a random word from the provided list
    selected_word = random.choice(FIVE_LETTER_WORDS)

        
    def enter_action(s):
        if s.lower() in FIVE_LETTER_WORDS:
            if s.lower() == selected_word:
                gw.show_message("Congrats")
                gw.set_current_row(6)
            else:
                for i in range(5):
                    check = 0
                    for j in range(5):
                        if(s.lower()[i] == selected_word[j]):
                            gw.set_square_color(gw.get_current_row(), i, PRESENT_COLOR)
                            check += 1
                    if check == 0:
                        gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR)        
                    if(s.lower()[i] == selected_word[i]):
                        gw.set_square_color(gw.get_current_row(), i, CORRECT_COLOR)
                gw.set_current_row(gw.get_current_row() + 1)
        else:
            gw.show_message("Not in word list")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)


    # Display the selected word in the first row
    for col in range(N_COLS):
        gw.set_square_letter(0, col, selected_word[col])

# Startup code

if __name__ == "__main__":
    wordle()