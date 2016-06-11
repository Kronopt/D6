#!/usr/bin/env python
# coding: utf-8

'''
D6
Randomly shows a different six sided die face each time enter is pressed

HOW TO RUN
    Double click script
'''

import random

__author__ = 'Pedro HC David, https://github.com/Kronopt'
__credits__ = ['Pedro HC David']
__version__ = '0.1'
__date__ = '01:44h, 09/06/2016'
__status__ = 'Finished'

def d6():
    '''
    Prints a different six sided die face each time
    Allows the user to leave the script by typing 'q', 'quit' or 'exit'
    '''

    print "Press enter to throw dice"

    continueD6 = True
    while continueD6:
        keyboardInput = raw_input()

        # Quit script prompt
        if keyboardInput.lower() in ('q', 'quit', 'exit'):
            areYouSure = raw_input("Leave D6 (y/n)? ")
            
            if areYouSure.lower() in ('', 'y', 'yes'):
                continueD6 = False
                continue

        else:
            dice = random.randint(1,6)

            S1 = S2 = S3 = S4 = S5 = S6 = S7 = S8 = S9 = ' '

            if dice == 1:
                S5 = 'O'
            elif dice == 2:
                S1 = S9 = 'O'
            elif dice == 3:
                S1 = S5 = S9 = 'O'
            elif dice == 4:
                S1 = S3 = S7 = S9 = 'O'
            elif dice == 5:
                S1 = S3 = S5 = S7 = S9 = 'O'
            else:
                S1 = S3 = S4 = S6 = S7 = S9 = 'O'

            print '-------------'
            print '| %s | %s | %s |' %(S1, S2, S3)
            print '-------------'
            print '| %s | %s | %s |' %(S4, S5, S6)
            print '-------------'
            print '| %s | %s | %s |' %(S7, S8, S9)
            print '-------------'

if __name__ == "__main__":
    d6()
