def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    l = 0
    r = len(arr) -1
    while l <= r:
        mid = (l+r)//2
        if target < arr[mid]:
            r = mid - 1
        elif target > arr[mid]:
            l = mid + 1
        else:
            return mid

    return -1  # not found
