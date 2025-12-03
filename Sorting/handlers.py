# Filename: handlers.py
from utils import clear_screen, wait_for_input
from algorithms import (
    bubble_sort, insertion_sort, selection_sort, 
    shell_sort, quick_sort
)

def show_array(arr):
    print("\n\n Current Array:")
    print(arr)
    wait_for_input()

def _run_sort_demo(arr, sort_func, method_name, is_quicksort=False):
    """ 
    Generic helper to handle the UI flow: 
    Copy -> Sort -> Print Results 
    """
    clear_screen()
    new_arr = arr[:] # Create a copy
    
    print(f"--- Running {method_name} ---")
    
    # Run the algorithm
    if is_quicksort:
        sort_func(new_arr, 0, len(new_arr) - 1)
    else:
        sort_func(new_arr)
        
    print("\nInitial Array:")
    print(arr)
    print("\nSorted Array:")
    print(new_arr)
    wait_for_input()

# --- Wrapper Functions ---

def handle_bubble_sort(arr):
    _run_sort_demo(arr, bubble_sort, "Bubble Sort")

def handle_insertion_sort(arr):
    _run_sort_demo(arr, insertion_sort, "Insertion Sort")

def handle_selection_sort(arr):
    _run_sort_demo(arr, selection_sort, "Selection Sort")

def handle_shell_sort(arr):
    _run_sort_demo(arr, shell_sort, "Shell Sort")

def handle_quick_sort(arr):
    # Special flag because QuickSort needs extra arguments
    _run_sort_demo(arr, quick_sort, "QuickSort", is_quicksort=True)