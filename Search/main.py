# Filename: main.py
from array import array
from utils import clear_screen, wait_for_input
from handlers import show_array, handle_seq_search, handle_bin_search

def show_menu():
    valid_choices = ["1", "2", "3", "4"]
    ans = 0
    while ans not in valid_choices:
        clear_screen()
        print("*** SEARCH & SORT MENU ***")
        print("1. Show Array")
        print("2. Sequential Search")
        print("3. Binary Search (with QuickSort)")
        print("4. Exit")
        ans = input("Your choice: ")
    return ans

def main():
    # Initialize the array
    my_array = array('i', [30, 2, 17, 19, 24, 16, 8, 7, 10, 15, 21, 13, 16, 12, 1, 9, 26, 27, 14, 20])
    
    ans = show_menu()
    while ans != "4":
        if ans == "1":
            show_array(my_array)
        elif ans == "2":
            handle_seq_search(my_array)
        elif ans == "3":
            handle_bin_search(my_array)
        
        # Show menu again after operation
        ans = show_menu()
        
    print("\n\nEnd of program")
    wait_for_input()

if __name__ == "__main__":
    main()