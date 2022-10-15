# Medium

# You're given an array of integers and an integer. Write a function that moves all instances
# of that integer in the array to the end of the array and returns the array.

# The function should perform this in place and doesn't need to maintain the order of the other integers.

# Sample Input
# array = [2, 1, 2, 2, 2, 3, 4, 2]
# toMove = 2

# Sample Output
# [1, 3, 4, 2, 2, 2, 2, 2]

def moveElementToEnd(array, toMove):
    # Write your code here.
    left = 0
    right = len(array) - 1
    while left < right:
        if array[left] == toMove:
            array[left], array[right] = array[right], array[left]
            right -= 1
        else:
            left += 1

    return array

## T = O(n); S = O(1)
