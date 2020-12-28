# This is my attempt at a simple hangman game with the little knowledge I've learned so far. Although I've failed
# at just this simple task. I will still complete this and perfect the logic. At this point (12-27-20),
# the program can replace the letters displayed to terminal but it is buggy and gets caught. It also for
# some reason doesn't break out of the loop to display results after getting the word right. The counter implementation is also 
# shit because it doesn't take away from the guesses every time.

import random
import sys

intro = """###################
###################
## Welcome to #####
## Hangman made ###
## by Chris Kade ##
###################
###################
"""

def listtostring(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


play = True
# store bank of possible words
while play == True:
    # initiate game prompt
    print(intro)
    print("If you would like to start a game, type the letter y. If you would like to quit, type the letter q.")
    a = input()
    if a == 'y':
        bank = ['fin','blank','bananna']
        word = random.randint(0, 1)
        word = bank[word]
        guesses = 5
        fin = list('_ _ _')
        blank = list('_ _ _ _ _')
        bananna = list('_ _ _ _ _ _ _')
        if word == 'fin':
            while fin != 'f i n' or guesses > 0:
                guess = input(f'You have {guesses} left.\n'+ listtostring(fin) + '\nPick a letter: ')
                guesses -= 1
                if guess == 'f':
                    fin[0] = 'f'

                elif guess == 'i':
                    fin[2] = 'i'
                    
                elif guess == 'n':
                    fin[4] = 'n'
                    
                elif fin == 'f i n':
                    print(f'You correctly got the word fin in {guesses}!!! Great job.')
                    play = False
                
        if word == 'blank':
            while blank != 'b l a n k' or guesses > 0:
                guess = input(f'You have {guesses} left.\n'+ listtostring(blank)+ '\nPick a letter: ')
                guesses -= 1
                if guess == 'b':
                    blank[0] = 'b'
                    
                elif guess == 'l':
                    blank[2] = 'l'
                    
                elif guess == 'a':
                    blank[4] = 'a'
                    
                elif guess == 'n':
                    blank[6] = 'n'
                 
                elif guess == 'k':
                    blank[8] = 'k'
                
                elif blank == 'b l a n k':
                    print(f'You correctly guessed the word blank in {guesses} guesses. Great job.')
                    play = False
            print(f'You correctly guessed the word blank in {guesses} guesses. Great job.')
                

    else:
        sys.exit()




