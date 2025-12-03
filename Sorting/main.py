# Filename: main.py
from array import array
from utils import clear_screen, wait_for_input
from handlers import (
    show_array, handle_bubble_sort, handle_insertion_sort,
    handle_selection_sort, handle_shell_sort, handle_quick_sort
)

def show_menu():
    """ Displays the option menu """
    valid_choices = ["1", "2", "3", "4", "5", "6", "7"]
    ans = "0"

    while ans not in valid_choices:
        clear_screen()
        print("*** SORTING ALGORITHMS MENU ***")
        print("1. Show Array")
        print("2. BubbleSort")
        print("3. Straight Insertion Sort")
        print("4. Straight Selection Sort")
        print("5. Shell Sort")
        print("6. QuickSort")
        print("7. Exit")
        ans = input("Your choice: ")

    return ans

def main():
    # Initialization
    my_array = array('i', [30, 2, 17, 19, 24, 16, 8, 7, 10, 15, 21, 13, 16, 12, 1, 9, 26, 27, 14, 20])
    
    ans = show_menu()
    while ans != "7":
        if ans == "1":
            show_array(my_array)
        elif ans == "2":
            handle_bubble_sort(my_array)
        elif ans == "3":
            handle_insertion_sort(my_array)
        elif ans == "4":
            handle_selection_sort(my_array)
        elif ans == "5":
            handle_shell_sort(my_array)
        elif ans == "6":
            handle_quick_sort(my_array)
            
        ans = show_menu()

    print("\n\nEnd of program")
    wait_for_input()

if __name__ == "__main__":
    main()