#!/usr/bin/env python
# coding: utf-8

"""
D6
Randomly shows a different six sided die face each time enter is pressed

HOW TO RUN:
    Double click script
"""

import random

__author__ = 'Pedro HC David, https://github.com/Kronopt'
__credits__ = ['Pedro HC David']
__version__ = '0.1'
__date__ = '14:27h, 15/06/2016'
__status__ = 'Finished'


def d6():
    """
    Prints a different six sided die face each time
    Allows the user to leave the script by typing 'q', 'quit' or 'exit'
    """

    print "Press enter to throw dice"

    user_wants_to_continue = True
    while user_wants_to_continue:
        keyboard_input = raw_input()

        # Quit script prompt
        if keyboard_input.lower() in ('q', 'quit', 'exit'):
            are_you_sure = raw_input("Leave D6 (y/n)? ")
            
            if are_you_sure.lower() in ('', 'y', 'yes'):
                user_wants_to_continue = False
                continue

        else:
            dice = random.randint(1, 6)
            s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = s9 = ' '

            if dice == 1:
                s5 = 'O'
            elif dice == 2:
                s1 = s9 = 'O'
            elif dice == 3:
                s1 = s5 = s9 = 'O'
            elif dice == 4:
                s1 = s3 = s7 = s9 = 'O'
            elif dice == 5:
                s1 = s3 = s5 = s7 = s9 = 'O'
            else:
                s1 = s3 = s4 = s6 = s7 = s9 = 'O'

            print '-------------'
            print '| %s | %s | %s |' % (s1, s2, s3)
            print '-------------'
            print '| %s | %s | %s |' % (s4, s5, s6)
            print '-------------'
            print '| %s | %s | %s |' % (s7, s8, s9)
            print '-------------'

if __name__ == "__main__":
    d6()
