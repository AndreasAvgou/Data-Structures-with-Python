# Filename: search.py

def show_minimum(arr):
    print("\n--- Minimum Value ---")
    if len(arr) == 0:
        print("Array is empty.")
        return

    min_val = arr[0]
    min_pos = 0
    
    for i in range(len(arr)):
        if min_val > arr[i]:
            min_val = arr[i]
            min_pos = i
            
    print("Minimum value: %d at position %d" % (min_val, min_pos))