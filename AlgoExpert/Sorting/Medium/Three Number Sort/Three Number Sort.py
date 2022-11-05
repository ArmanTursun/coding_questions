# Medium

# You're given an array of integers and another array of three distinct integers. The first array is guaranteed to
# only contain integers that are in the second array, and the second array array represents a desired order for the
# integers in the first array. For example, a second array of [x, y, z] represents a desired order of [x, x, ..., x,
# y, y, ..., z, z, ..., z] in the first array.

# Write a function that sorts the first array according to the desired order in the second array.

# The function should perform this in place, and it shouldn't use any auxiliary space.
# Note that the desired order won't necessarily be ascending or descending and that the first array won't necessarily
# contain all three integers found in the second array - it might only contain one or two.

# Sample Input
# array = [1, 0, 0, -1, -1, 0, 1, 1]
# order = [0, 1, -1]

# Sample Output
# [0, 0, 0, 1, 1, 1, -1, -1]

def threeNumberSort(array, order):
    # Write your code here.
    idx = 0
    for i in range(len(order) - 1):
        curValue = order[i]
        for j in range(idx, len(array)):
            if array[j] == curValue:
                swap(array, j, idx)
                idx += 1
    return array

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

## T = O(n); S = O(1)
## n is the length of array, O(2n) = O(n)



def threeNumberSort(array, order):
    # Write your code here.
    firstIdx, secondIdx, thirdIdx = 0, 0, len(array) - 1
    while secondIdx <= thirdIdx:
        value = array[secondIdx]
        if value == order[0]:
            swap(array, secondIdx, firstIdx)
            firstIdx += 1
            secondIdx += 1
        elif value == order[1]:
            secondIdx += 1
        else:
            swap(array, secondIdx, thirdIdx)
            thirdIdx -= 1
    return array

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
