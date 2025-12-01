# Filename: counting.py

def count_negatives(arr):
    print("\n--- Count Negatives ---")
    count_neg = 0
    
    for i in range(len(arr)):
        if arr[i] < 0:
            count_neg += 1
            
    print("Count of negatives: %d" % (count_neg))