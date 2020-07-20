# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):

    while start <= end:
        mid = (start + end) // 2

        if target == arr[mid]:
            return mid

        if target < arr[mid]:
            end = mid - 1

        if target > arr[mid]:
            start = mid + 1

    return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass