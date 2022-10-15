# Medium

# Write a function that takes in two non-empty arrays of integers, finds the pair of numbers
# (one from each array) whose absolute difference is closest to zero, and returns an array
# containing these two numbers, with the number from the first array in the first position.

# Sample Input
# arrayOne = [-1, 5, 10, 20, 28, 3]
# arrayTwo = [26, 134, 135, 15, 17]

# Sample Output
# [28, 26]

def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    i = j = 0
    minDiff = float("inf")
    result = [arrayOne[0], arrayTwo[0]]

    while i < len(arrayOne) and j < len(arrayTwo):
        if abs(arrayOne[i] - arrayTwo[j]) < minDiff:
            minDiff = abs(arrayOne[i] - arrayTwo[j])
            result = [arrayOne[i], arrayTwo[j]]
        if arrayOne[i] < arrayTwo[j]:
            i += 1
        else:
            j += 1
    return result

# T = O(nlog(n) + mlog(m)); S = O(1)
