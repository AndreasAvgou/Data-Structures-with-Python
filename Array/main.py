# Filename: main.py
from array import array


from retrieve import get_value_at_pos
from inputs import fill_array
from display import print_array
from stats import show_sum_and_average
from search import show_minimum
from counting import count_negatives

def main():
    # 1. Initialization
    # We create the array here in the main file
    my_array = array('i', [2, 5, -1, 8, 0, -4, -9, 12, 3, -2])
    
    # 2. Function Calls
    # We pass 'my_array' to each function imported from the other files
    get_value_at_pos(my_array)      # From retrieve.py
    fill_array(my_array)            # From inputs.py
    print_array(my_array)           # From display.py
    show_sum_and_average(my_array)  # From stats.py
    show_minimum(my_array)          # From search.py
    count_negatives(my_array)       # From counting.py

if __name__ == "__main__":
    main()