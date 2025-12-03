# Filename: searching.py

def sequential_search(target, arr):
    """
    Linear search implementation.
    Returns: (found_status (0/1), index)
    """
    index = -1
    found = 0
    i = 0
    
    while i < len(arr) and found == 0:
        if target == arr[i]:
            index = i
            found = 1
        i += 1
        
    return found, index

def binary_search(target, sorted_arr):
    """
    Binary search implementation.
    Requires a sorted array.
    Returns: (found_status (0/1), index)
    Note: If not found, 'index' indicates the insertion point.
    """
    found = 0
    index = -1
    left = 0
    right = len(sorted_arr) - 1
    mid = 0
    
    while left <= right and found == 0:
        mid = (left + right) // 2
        
        if target == sorted_arr[mid]:
            index = mid
            found = 1
        elif target < sorted_arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    # Logic to return insertion point if not found
    if found == 0:
        if right < 0: # Case: Insert at beginning
             index = 0
        elif target > sorted_arr[mid]:
            index = mid + 1
        else:
            index = mid
    
    return found, index