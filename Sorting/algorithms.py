# Filename: algorithms.py

def bubble_sort(arr):
    """ Bubble Sort Implementation """
    last = 1
    t = 1
    size_a = len(arr)
    while t > 0:
        t = 0
        for j in range(size_a - 1, last - 1, -1):
            if arr[j - 1] > arr[j]:
                # Swap
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                t = j
        last = t

def insertion_sort(arr):
    """ Insertion Sort Implementation """
    size_a = len(arr)
    for j in range(1, size_a):
        i = j - 1
        t = arr[j]
        while i >= 0:
            if t >= arr[i]:
                break
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = t

def get_min_index(arr, start):
    """ Helper for Selection Sort: Finds index of min element """
    min_val = arr[start]
    min_index = start
    i = start + 1
    while i < len(arr):
        if min_val > arr[i]:
            min_val = arr[i]
            min_index = i
        i += 1
    return min_index

def selection_sort(arr):
    """ Selection Sort Implementation """
    i = 0
    while i < len(arr):
        min_idx = get_min_index(arr, i)
        # Swap
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
        i += 1

def shell_sort(arr):
    """ Shell Sort Implementation """
    # Create gaps (powers of 2)
    h = [2**i for i in range(20)] 

    size_a = len(arr)
    # Iterate backwards through the gaps
    for s in range(19, -1, -1):
        gap = h[s]
        for j in range(gap, size_a, 1):
            i = j - gap
            temp = arr[j]
            while (i >= 0) and (temp < arr[i]):
                arr[i + gap] = arr[i]
                i = i - gap
            arr[i + gap] = temp

def quick_sort(arr, bottom, top):
    """ QuickSort Recursive Implementation """
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
            # Swap
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    if bottom < j:
        quick_sort(arr, bottom, j)
    if i < top:
        quick_sort(arr, i, top)