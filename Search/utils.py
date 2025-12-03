# Filename: utils.py
import os

def clear_screen():
    """ Clears the console screen (Windows/Linux/Mac) """
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_for_input():
    """ Pauses execution until Enter is pressed """
    input("\n\n Press Enter to continue. \n\n")