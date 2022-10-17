# Medium
# LC 238. Product of Array Except Self

# Write a function that takes in a non-empty array of integers and returns an array of the same
# length, where each element in the output array is equal to the product of every other number
# in the input array. In other words, the value at output[i] is equal to the product of every
# number in the input array other than input[i].
# Note that you're expected to solve this problem without using division.

# Sample Input
# array = [5, 1, 4, 2]

# Sample Output
# [8, 40, 10, 20]

def arrayOfProducts(array):
    # Write your code here.
    result = [1 for _ in array]

    for i in range(len(array)):
        for j in range(len(array)):
            if i != j:
                result[i] *= array[j]
    return result

## T = O(n ^ 2); S = O(n)


# Better method
def arrayOfProducts(array):
    # Write your code here.
    left = [None for _ in array]
    right = [None for _ in array]
    result = [None for _ in array]
    for i in range(len(array)):
        left[i] = array[i] * left[i - 1] if i > 0 else array[i]
    for j in range(len(array) - 1, -1, -1):
        right[j] = array[j] * right[j + 1] if j < len(array) - 1 else array[j]
    for k in range(len(array)):
        if k == 0:
            result[0] = right[k + 1]
        elif k == len(array) - 1:
            result[k] = left[k - 1]
        else:
            result[k] = left[k - 1] * right[k + 1]
    return result
## T = O(n); S = O(n)

## solution with less space consumption
def arrayOfProducts(array):
    # Write your code here.
    result = [1 for _ in array]

    left_sub = 1
    for i in range(len(array)):
        result[i] *= left_sub
        left_sub *= array[i]

    right_sub = 1
    for j in range(len(array) - 1, -1, -1):
        result[j] *= right_sub
        right_sub *= array[j]

    return result