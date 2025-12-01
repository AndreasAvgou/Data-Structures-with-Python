# Filename: stats.py

def show_sum_and_average(arr):
    print("\n--- Sum and Average ---")
    total_sum = 0
    N = len(arr)
    
    for i in range(N):
        total_sum = total_sum + arr[i]

    print("Sum of all elements: %d" % (total_sum))
    
    if N > 0:
        ave = total_sum / N
        print("Average value: %.2f" % (ave))
    else:
        print("Array is empty, cannot calculate average.")