# Filename: inputs.py

def fill_array(arr):
    print("\n--- Input New Values ---")
    print("Give new values for the array:")
    
    for i in range(len(arr)):
        while True:
            try:
                # Prompt user for each index
                val = input("a[%d]=" % (i))
                arr[i] = int(val)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")