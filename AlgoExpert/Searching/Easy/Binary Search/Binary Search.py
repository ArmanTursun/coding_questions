# Easy

# Write a function that takes in a sorted array of integers as well as a target integer. The function
# should use the Binary Search algorithm to determine if the target integer is contained in the array
# and should return its index if it is. otherwise -1.

# Sample Input
# [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
# target = 33

# Sample Output
# 3

# iteration
def binarySearch(array, target):
    # Write your code here.

    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# recurssive
def binarySearch(array, target):
    # Write your code here.
    left = 0
    right = len(array) - 1
    return helper (left, right, array, target)

def helper(left, right, array, target):
    if left > right:
        return -1
    mid = (left + right) // 2
    if array[mid] == target:
        return mid
    if array[mid] < target:
        return helper(mid + 1, right, array, target)
    else:
        return helper(left, mid - 1, array, target)
