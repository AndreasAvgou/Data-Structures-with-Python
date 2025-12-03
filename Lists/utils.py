# Filename: utils.py
import os

def clear_screen():
    """ Clears the console screen (Windows/Linux) """
    # 'cls' for Windows, 'clear' for Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_for_input():
    """ Pauses execution until Enter is pressed """
    input("\n\n Press Enter to continue. \n")

def get_number():
    """ Reads a positive integer from the keyboard """
    n = -1
    while n <= 0:
        clear_screen()
        try:
            s = input("Enter a number ( >0 ): ")
            n = int(s)
        except ValueError:
            pass # Ignore non-integer inputs and ask again
    return n