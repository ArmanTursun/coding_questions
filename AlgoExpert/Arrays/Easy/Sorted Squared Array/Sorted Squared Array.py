# Write a function that takes in a non-empty array of intergers that are
# sorted in ascending order and returns a new array of the same length
# with the squares of the original integers also sorted in ascending order.

# Sample Input
# array = [1, 2, 3, 5, 6, 8, 9]

# Sample Output
# [1, 4, 9, 25, 36, 64, 81]

def sortedSquaredArray(array):
    # Write your code here.
    #new_array = sorted([x**2 for x in array])
    #return new_array
    new_array = [x**2 for x in array]
    new_array.sort()
    return new_array

## T = O(nlog(n)); S = O(n)

def sortedSquaredArray(array):
    # Write your code here.
    result = [0 for _ in array]
    left = 0
    right = len(array) - 1
    idx = len(array) - 1

    while idx >= 0:
        if abs(array[left]) < abs(array[right]):
            result[idx] = array[right] ** 2
            right -= 1
        else:
            result[idx] = array[left] ** 2
            left += 1
        idx -= 1

    return result

## T = O(n); S = O(n)
