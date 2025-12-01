# Filename: retrieve.py

def get_value_at_pos(arr):
    N = len(arr)
    pos = -1
    print("\n--- Retrieve Value by Index ---")
    
    # Loop until the user provides a valid index
    while pos < 0 or pos > N-1:
        try:
            p = input(f"Give array position (0-{N-1}): ")
            pos = int(p)
            if pos < 0 or pos > N-1:
                print(f"Position must be between 0 and {N-1}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
            
    print("a[%d]=%d" % (pos, arr[pos]))