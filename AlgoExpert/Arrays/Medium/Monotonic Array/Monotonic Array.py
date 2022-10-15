# Medium

# Write a function that takes in an array of integers and returns a boolean representing whether
# the array is monotonic.

# An array is said to be monotonic if its elements, from left to right, are entirely non-increasing
# or entirely non-decreasing.

# Note that empty arrays and arrays of one element are monotonic.

# Sample Input
# array = [-1, -5, -10, -1100, -1100, -1100, -1101, -1102, -9001]

# Sample Output
# True

def isMonotonic(array):
    # Write your code here.
    if not array or len(array) == 1:
        return True

    increase = True if array[0] < array[-1] else False
    if increase:
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                return False
    else:
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                return False
    return True

## Simpler code
##################
##################

def isMonotonic(array):
    # Write your code here.
    increase = decrease = True

    for i in range(len(array) - 1):
        if array[i] < array[i + 1]:
            decrease = False
        if array[i] > array[i + 1]:
            increase = False

    return increase or decrease

## T = O(n); S = O(1)