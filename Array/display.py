# Filename: display.py

def print_array(arr):
    print("\n--- Array Contents ---")
    for i in range(len(arr)):
        print("a[%d]=%d" % (i, arr[i]))