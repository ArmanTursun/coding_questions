# Medium

# Write a function that takes in an array of positive integers and returns the maximum sum of non-adjacent elements in
# the array. If the input array is empty, the function should return 0.

# Sample Input
# array = [75, 105, 120, 75, 90, 135]

# Sample Output
# 330

def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if not array:
        return 0
    if len(array) == 1:
        return array[0]

    curMax = array
    for i in range(len(curMax)):
        if i == 0:
            continue
        if i == 1:
            curMax[i] = max(curMax[i], curMax[i - 1])
            continue
        curMax[i] = max(curMax[i-1], curMax[i-2] + curMax[i])
    return curMax[-1]

## T = O(n), S = O(n)



def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if not array:
        return 0
    if len(array) == 1:
        return array[0]

    exMax = max(array[1], array[0])
    exexMax = array[0]
    for i in range(2, len(array)):
        temp = exMax
        exMax = max(exexMax + array[i], exMax)
        exexMax = temp
    return exMax

## T = O(n); S = O(1)