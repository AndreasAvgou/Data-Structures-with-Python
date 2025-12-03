# Filename: sorting.py

def quick_sort(arr, bottom, top):
    """
    Recursive implementation of QuickSort.
    Sorts the array in-place.
    """
    i = bottom
    j = top
    k = (bottom + top) // 2
    pivot = arr[k]
    
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            # Swap elements
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1

    if bottom < j:
        quick_sort(arr, bottom, j)
    if i < top:
        quick_sort(arr, i, top)