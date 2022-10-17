# Medium

# Given an array of integers between 1 and n, inclusive, where n is the length of the array, write a
# function that returns the first integer that appears more than once. If no integer appears more than
# once, your function should return -1.

# Sample Inpout
# array = [2, 1, 5, 2, 3, 3, 4]

# Sample Output
# 2

def firstDuplicateValue(array):
    # Write your code here.
    memo = set()

    for item in array:
        if item in memo:
            return item
        memo.add(item)
    return -1

## T = O(n); T = O(n)

def firstDuplicateValue(array):
    # Write your code here.
    for num in array:
        abs_num = abs(num)
        if array[abs_num - 1] < 0:
            return abs_num
        array[abs_num - 1] *= -1
    return -1

## T = O(n); S = O(1)