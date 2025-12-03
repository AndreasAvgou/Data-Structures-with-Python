# Filename: handlers.py
from utils import clear_screen, wait_for_input
from searching import sequential_search, binary_search
from sorting import quick_sort

def show_array(arr):
    print("\n\nCurrent Array:")
    print(arr)
    wait_for_input()

def handle_seq_search(arr):
    clear_screen()
    try:
        s = input("Enter a number to search (Sequential): ")
        n = int(s)
    except ValueError:
        print("Invalid input.")
        wait_for_input()
        return

    print("\n\nArray:")
    print(arr)
    
    # Call the algorithm
    found, index = sequential_search(n, arr)
    
    print("\n\n")
    if found:
        print("Found @ position %d!" % (index + 1))
    else:
        print("Not found")
    wait_for_input()

def handle_bin_search(arr):
    clear_screen()
    
    # Create a copy to sort, so we don't mess up the original for the menu
    temp_arr = arr[:]
    size_a = len(temp_arr)
    
    # Sort the copy using QuickSort
    quick_sort(temp_arr, 0, size_a - 1)
    
    try:
        s = input("Enter a number to search (Binary): ")
        n = int(s)
    except ValueError:
        print("Invalid input.")
        wait_for_input()
        return

    # Call the algorithm
    found, index = binary_search(n, temp_arr)
    
    print("\n\n")
    print("Initial Array (Unsorted):")
    print(arr)
    print("\nSorted Array (Used for Binary Search):")
    print(temp_arr)
    print("\n\n")
    
    if found:
        print("Found @ position %d!" % (index + 1))
    else:
        print("Not Found! It should be inserted @ position %d" % (index + 1))
    wait_for_input()